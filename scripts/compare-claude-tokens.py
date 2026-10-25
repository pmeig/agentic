#!/usr/bin/env python3
"""Run the same Claude Code prompt on two Git branches and compare reported usage."""
from __future__ import annotations
import argparse, json, shutil, subprocess, sys, tempfile
from pathlib import Path
from typing import Any

def run(command: list[str], *, cwd: Path | None = None, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, capture_output=True, timeout=timeout, check=False)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--branches", nargs=2, default=["main", "chore/optimisation"], metavar=("A", "B"))
    parser.add_argument("--prompt-file", type=Path, required=True)
    parser.add_argument("--model", help="optional Claude model name")
    parser.add_argument("--max-turns", type=int, default=20)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--output-dir", type=Path, default=Path("token-comparison-results"))
    args = parser.parse_args()
    prompt_path = args.prompt_file.resolve()
    if not prompt_path.is_file():
        parser.error(f"prompt file not found: {prompt_path}")
    prompt = prompt_path.read_text(encoding="utf-8").strip()
    if not prompt:
        parser.error("prompt file is empty")
    if shutil.which("git") is None or shutil.which("claude") is None:
        parser.error("git and Claude Code CLI (claude) must be installed and available on PATH")
    root_result = run(["git", "rev-parse", "--show-toplevel"])
    if root_result.returncode:
        parser.error("run this script from inside the repository")
    repo = Path(root_result.stdout.strip())
    output_dir = (repo / args.output_dir).resolve() if not args.output_dir.is_absolute() else args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    summary: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="claude-token-ab-") as temp:
        for index, branch in enumerate(args.branches, start=1):
            worktree = Path(temp) / f"variant-{index}"
            add = run(["git", "worktree", "add", "--detach", str(worktree), branch], cwd=repo)
            if add.returncode:
                print(f"Could not create worktree for {branch}:\n{add.stderr}", file=sys.stderr)
                return 2
            command = ["claude", "-p", "--output-format", "json", "--max-turns", str(args.max_turns)]
            if args.model:
                command.extend(["--model", args.model])
            command.append(prompt)
            try:
                result = run(command, cwd=worktree, timeout=args.timeout)
            except subprocess.TimeoutExpired:
                summary.append({"branch": branch, "status": "timeout", "timeout_seconds": args.timeout})
                run(["git", "worktree", "remove", "--force", str(worktree)], cwd=repo)
                continue
            raw_path = output_dir / f"variant-{index}-raw.txt"
            raw_path.write_text(result.stdout + ("\n--- STDERR ---\n" + result.stderr if result.stderr else ""), encoding="utf-8")
            try:
                data = json.loads(result.stdout)
            except json.JSONDecodeError:
                data = {}
            usage = data.get("usage", {}) if isinstance(data, dict) else {}
            row = {
                "branch": branch, "status": "ok" if result.returncode == 0 else "error",
                "exit_code": result.returncode,
                "model": data.get("model", args.model) if isinstance(data, dict) else args.model,
                "session_id": data.get("session_id") if isinstance(data, dict) else None,
                "duration_ms": data.get("duration_ms") if isinstance(data, dict) else None,
                "num_turns": data.get("num_turns") if isinstance(data, dict) else None,
                "total_cost_usd": data.get("total_cost_usd") if isinstance(data, dict) else None,
                "usage": usage, "raw_output_file": str(raw_path),
            }
            summary.append(row)
            (output_dir / f"variant-{index}.json").write_text(json.dumps(row, indent=2), encoding="utf-8")
            remove = run(["git", "worktree", "remove", "--force", str(worktree)], cwd=repo)
            if remove.returncode:
                print(f"Warning: worktree cleanup failed for {branch}: {remove.stderr}", file=sys.stderr)
    report = {"prompt_file": str(prompt_path), "branches": args.branches, "results": summary}
    (output_dir / "comparison.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Results written to: {output_dir}")
    for row in summary:
        print(f"\n{row['branch']}: status={row['status']}")
        for key in ("total_cost_usd", "duration_ms", "num_turns", "usage"):
            print(f"  {key}: {json.dumps(row.get(key), ensure_ascii=False)}")
    if len(summary) == 2:
        a, b = summary
        ca, cb = a.get("total_cost_usd"), b.get("total_cost_usd")
        if isinstance(ca, (int, float)) and isinstance(cb, (int, float)):
            print(f"\nCost delta ({b['branch']} - {a['branch']}): USD {cb-ca:.6f}")
            if ca:
                print(f"Cost delta percent: {(cb-ca)/ca*100:.2f}%")
        ua, ub = a.get("usage", {}), b.get("usage", {})
        for key in sorted(set(ua) | set(ub)):
            if isinstance(ua.get(key), (int, float)) and isinstance(ub.get(key), (int, float)):
                print(f"Usage delta {key} ({b['branch']} - {a['branch']}): {ub[key]-ua[key]}")
    print("\nReview raw output and subagent transcripts; do not assume CLI summary includes every subagent. "
          "Compare identical prompts, model/settings, starting state and output quality.")
    return 0 if all(row.get("status") == "ok" for row in summary) else 1

if __name__ == "__main__":
    raise SystemExit(main())
