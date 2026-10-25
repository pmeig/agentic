#!/usr/bin/env python3
"""Summarize token usage from Claude Code JSONL transcripts.

Usage:
  python scripts/claude-token-usage.py
  python scripts/claude-token-usage.py --root ~/.claude/projects --json

This reports observed usage from transcript records, not estimates or billing totals.
It sums message.usage on assistant records and groups each transcript separately so
subagent transcripts can be inspected independently. It never uploads transcript data.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def usage_for(path: Path) -> dict[str, int]:
    totals = {
        "input_tokens": 0,
        "output_tokens": 0,
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "messages_with_usage": 0,
    }
    try:
        with path.open("r", encoding="utf-8") as stream:
            for line in stream:
                try:
                    record: dict[str, Any] = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if record.get("type") != "assistant":
                    continue
                message = record.get("message") or {}
                usage = message.get("usage") or record.get("usage") or {}
                if not isinstance(usage, dict) or not usage:
                    continue
                totals["messages_with_usage"] += 1
                for key in (
                    "input_tokens",
                    "output_tokens",
                    "cache_creation_input_tokens",
                    "cache_read_input_tokens",
                ):
                    value = usage.get(key, 0)
                    if isinstance(value, (int, float)):
                        totals[key] += int(value)
    except (OSError, UnicodeError):
        pass
    return totals


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.home() / ".claude" / "projects",
        help="Claude Code projects/transcripts directory",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    if not args.root.exists():
        parser.error(f"transcript directory does not exist: {args.root}")

    rows = []
    for path in sorted(args.root.rglob("*.jsonl")):
        usage = usage_for(path)
        if usage["messages_with_usage"]:
            try:
                label = str(path.relative_to(args.root))
            except ValueError:
                label = str(path)
            rows.append({"transcript": label, **usage,
                         "total_reported_tokens": usage["input_tokens"] + usage["output_tokens"]})

    if args.json:
        print(json.dumps(rows, indent=2))
        return 0

    if not rows:
        print(f"No usage records found under {args.root}")
        return 0

    headers = ("transcript", "input_tokens", "output_tokens",
               "cache_creation_input_tokens", "cache_read_input_tokens",
               "total_reported_tokens")
    widths = {key: max(len(key), *(len(str(row[key])) for row in rows)) for key in headers}
    print("  ".join(key.ljust(widths[key]) for key in headers))
    print("  ".join("-" * widths[key] for key in headers))
    for row in rows:
        print("  ".join(str(row[key]).ljust(widths[key]) for key in headers))
    grand = {key: sum(row[key] for row in rows) for key in headers[1:]}
    print("  ".join(("-TOTAL-").ljust(widths["transcript"]) if key == "transcript"
                    else str(grand[key]).ljust(widths[key]) for key in headers))
    print("\nNote: input totals include separately reported cache tokens when present; "
          "do not add cache columns again to total_reported_tokens.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
