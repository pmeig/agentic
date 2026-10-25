#!/usr/bin/env python3
"""Compare Copilot CLI token usage on two git refs using local OpenTelemetry JSONL."""
import argparse
import datetime
import json
import os
import shlex
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(command, cwd, timeout=None, env=None):
    return subprocess.run(
        command, cwd=cwd, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, timeout=timeout, check=False, env=env
    )


def git(*args):
    result = run(["git", *args], ROOT)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "git failed")
    return result.stdout.strip()


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def decode_otel_value(value):
    if not isinstance(value, dict):
        return value
    for key in ("intValue", "int_value", "doubleValue", "double_value",
                "stringValue", "string_value", "boolValue", "bool_value"):
        if key in value:
            raw = value[key]
            if key in ("intValue", "int_value"):
                try:
                    return int(raw)
                except (TypeError, ValueError):
                    return raw
            if key in ("doubleValue", "double_value"):
                try:
                    return float(raw)
                except (TypeError, ValueError):
                    return raw
            return raw
    if "value" in value:
        return decode_otel_value(value["value"])
    return value


def span_attributes(span):
    attrs = {}
    for item in span.get("attributes", []) if isinstance(span.get("attributes"), list) else []:
        if isinstance(item, dict) and "key" in item:
            attrs[item["key"]] = decode_otel_value(item.get("value"))
    return attrs


def read_otel_usage(path):
    """Sum per-request chat spans only, avoiding parent-agent double counting."""
    if not path.is_file():
        return None
    spans = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            event = json.loads(line)
        except (ValueError, TypeError):
            continue
        for item in walk(event):
            if (isinstance(item.get("name"), str)
                    and isinstance(item.get("attributes"), list)):
                spans.append(item)

    chat_spans = [
        (span, span_attributes(span)) for span in spans
        if span.get("name") == "chat"
    ]

    # Token counts are defined on chat spans (one per model request).
    # Do not sum invoke_agent totals together with child chat spans.
    selected = [
        (span, attrs) for span, attrs in chat_spans
        if any(key in attrs for key in (
            "gen_ai.usage.input_tokens", "gen_ai.usage.output_tokens",
            "gen_ai.usage.cache_read.input_tokens",
            "gen_ai.usage.cache_creation.input_tokens",
        ))
    ]
    if not selected:
        return None

    def total(key):
        values = []
        for _, attrs in selected:
            value = attrs.get(key)
            if isinstance(value, (int, float)):
                values.append(value)
        return sum(values) if values else None

    models = sorted({
        str(attrs.get("gen_ai.response.model") or attrs.get("gen_ai.request.model"))
        for _, attrs in selected
        if attrs.get("gen_ai.response.model") or attrs.get("gen_ai.request.model")
    })
    input_tokens = total("gen_ai.usage.input_tokens")
    output_tokens = total("gen_ai.usage.output_tokens")
    cache_read = total("gen_ai.usage.cache_read.input_tokens")
    cache_creation = total("gen_ai.usage.cache_creation.input_tokens")
    nano_aiu = total("github.copilot.nano_aiu")
    return {
        "source": "opentelemetry_file_exporter",
        "llm_requests_with_usage": len(selected),
        "models": models,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_input_output_tokens": (
            input_tokens + output_tokens
            if input_tokens is not None and output_tokens is not None else None
        ),
        "cache_read_input_tokens": cache_read,
        "cache_creation_input_tokens": cache_creation,
        "nano_aiu": nano_aiu,
        "billing_note": "github.copilot.cost is a model billing multiplier, not money; it is not summed here.",
    }


def parse_cli_usage(text):
    """Fallback only: parse structured JSON usage fields emitted by some CLI versions."""
    keys = {
        "input_tokens", "output_tokens", "total_tokens", "prompt_tokens",
        "completion_tokens", "cache_read_input_tokens",
        "cache_creation_input_tokens", "total_cost_usd", "cost",
    }
    found = []
    for line in text.splitlines():
        try:
            data = json.loads(line.strip())
        except (ValueError, TypeError):
            continue
        for item in walk(data):
            if keys.intersection(item):
                found.append(item)
    return max(found, key=len) if found else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prompt", default="prompts/token-test-copilot.md")
    parser.add_argument("--base", default="main")
    parser.add_argument("--compare", default="chore/optimisation")
    parser.add_argument("--output-dir", default="token-comparison-results")
    parser.add_argument("--timeout", type=int, default=3600)
    parser.add_argument("--copilot-command", default=os.environ.get("COPILOT_COMMAND", "copilot"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    prompt_path = Path(args.prompt)
    prompt_path = prompt_path if prompt_path.is_absolute() else ROOT / prompt_path
    if not prompt_path.is_file():
        parser.error("Prompt file not found: " + str(prompt_path))

    prompt = prompt_path.read_text(encoding="utf-8")
    output_root = Path(args.output_dir)
    output_root = output_root if output_root.is_absolute() else ROOT / output_root
    output_dir = output_root / ("copilot-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    output_dir.mkdir(parents=True, exist_ok=False)
    records, worktrees = [], []

    try:
        for label, ref in (("base", args.base), ("compare", args.compare)):
            commit = git("rev-parse", "--verify", ref + "^{commit}")
            worktree = output_dir / ("worktree-" + label)
            result = run(["git", "worktree", "add", "--detach", str(worktree), commit], ROOT)
            if result.returncode:
                raise RuntimeError(result.stderr.strip())
            worktrees.append(worktree)
            (worktree / "TOKEN-BENCHMARK-PROMPT.md").write_text(prompt, encoding="utf-8")

            otel_path = (output_dir / (label + ".otel.jsonl")).resolve()
            record = {
                "label": label,
                "ref": ref,
                "commit": commit,
                "started_at": datetime.datetime.now().astimezone().isoformat(),
                "telemetry_file": str(otel_path),
            }

            if args.dry_run:
                record.update(status="dry-run", duration_seconds=0, usage=None)
            else:
                env = os.environ.copy()
                env["COPILOT_OTEL_ENABLED"] = "true"
                env["COPILOT_OTEL_EXPORTER_TYPE"] = "file"
                env["COPILOT_OTEL_FILE_EXPORTER_PATH"] = str(otel_path)
                # Do not collect prompt/response bodies; token counts do not need them.
                env["OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT"] = "false"
                command = shlex.split(args.copilot_command) + ["-p", prompt]
                start = time.monotonic()
                try:
                    result = run(command, worktree, timeout=args.timeout, env=env)
                    record.update(
                        status="completed" if result.returncode == 0 else "failed",
                        return_code=result.returncode,
                        duration_seconds=round(time.monotonic() - start, 2),
                    )
                    (output_dir / (label + ".stdout.log")).write_text(result.stdout, encoding="utf-8")
                    (output_dir / (label + ".stderr.log")).write_text(result.stderr, encoding="utf-8")
                    usage = read_otel_usage(otel_path)
                    if usage is None:
                        usage = parse_cli_usage(result.stdout + "\n" + result.stderr)
                        if usage is not None:
                            usage = {
                                "source": "copilot_cli_structured_output_fallback",
                                "fields": usage,
                                "note": "Fallback metrics are only as complete as the CLI output; verify against OTel when possible.",
                            }
                    record["usage"] = usage
                except subprocess.TimeoutExpired as exc:
                    record.update(
                        status="timeout",
                        duration_seconds=round(time.monotonic() - start, 2),
                        usage=read_otel_usage(otel_path),
                    )
                    stdout = exc.stdout or ""
                    stderr = exc.stderr or ""
                    if isinstance(stdout, bytes):
                        stdout = stdout.decode("utf-8", errors="replace")
                    if isinstance(stderr, bytes):
                        stderr = stderr.decode("utf-8", errors="replace")
                    (output_dir / (label + ".stdout.log")).write_text(stdout, encoding="utf-8")
                    (output_dir / (label + ".stderr.log")).write_text(stderr, encoding="utf-8")

            records.append(record)
            if not args.dry_run and record["status"] != "completed":
                break
    finally:
        for worktree in reversed(worktrees):
            run(["git", "worktree", "remove", "--force", str(worktree)], ROOT)

    report = {
        "tool": "GitHub Copilot CLI",
        "created_at": datetime.datetime.now().astimezone().isoformat(),
        "base_ref": args.base,
        "compare_ref": args.compare,
        "prompt": str(prompt_path),
        "measurement_method": "OpenTelemetry local JSONL export, with structured CLI-output fallback",
        "notes": [
            "Token totals are summed from per-request chat spans to avoid double-counting parent invoke_agent spans.",
            "Cache counters are reported separately and are not added again to input/output totals.",
            "Missing metrics mean unavailable, not zero.",
            "github.copilot.cost is a model billing multiplier, not a monetary amount.",
            "Prompt/response content capture is disabled by this script.",
        ],
        "runs": records,
    }
    (output_dir / "comparison.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("Results:", output_dir)
    for record in records:
        print(
            record["label"], record["ref"], record["status"],
            "duration=", record.get("duration_seconds"),
            "usage=", json.dumps(record.get("usage"), ensure_ascii=False),
        )
    if not args.dry_run and any(record.get("usage") is None for record in records):
        print(
            "No token usage metrics found. Check the .otel.jsonl file and Copilot CLI version; "
            "null does not mean zero.",
            file=sys.stderr,
        )
    return 0 if args.dry_run or all(record["status"] == "completed" for record in records) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, OSError, ValueError) as error:
        print("error:", error, file=sys.stderr)
        raise SystemExit(2)
