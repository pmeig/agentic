#!/usr/bin/env bash
# Render an e2e progress file (state<TAB>index<TAB>total<TAB>title) as one line per test.
# usage: render.sh <progress-file> [--once]   (follows the file until the run ends, or prints once)
set -euo pipefail

file="${1:?progress file}"
once="${2:-}"
green=$'\033[32m'; red=$'\033[31m'; grey=$'\033[90m'; blink=$'\033[5m'; reset=$'\033[0m'

pass=0; fail=0; total=0
declare -A running=()

line() { # state index total title
  case "$1" in
    start) running["$2"]="$4"; total="$3"
           printf '%s%s●%s %s\n' "$grey" "$blink" "$reset" "$4" ;;
    pass)  unset 'running[$2]'; pass=$((pass + 1)); total="$3"
           printf '%s●%s %s\n' "$green" "$reset" "$4" ;;
    fail)  unset 'running[$2]'; fail=$((fail + 1)); total="$3"
           printf '%s●%s %s\n' "$red" "$reset" "$4" ;;
  esac
}

summary() {
  local color="$green"; ((fail > 0)) && color="$red"
  printf '%s●%s %d/%s passed, %d failed\n' "$color" "$reset" "$pass" "$total" "$fail"
}

while true; do
  if [[ -f "$file" ]]; then
    break
  fi
  [[ "$once" == "--once" ]] && { echo "no progress file" >&2; exit 1; }
  sleep 0.5
done

if [[ "$once" == "--once" ]]; then
  while IFS=$'\t' read -r state idx tot title; do line "$state" "$idx" "$tot" "$title"; done < "$file"
  summary
  exit $((fail > 0 ? 1 : 0))
fi

# follow until the file is removed (end of the run)
seen=0
while [[ -f "$file" ]]; do
  count=$(wc -l < "$file")
  if ((count > seen)); then
    while IFS=$'\t' read -r state idx tot title; do line "$state" "$idx" "$tot" "$title"; done < <(sed -n "$((seen + 1)),${count}p" "$file")
    seen=$count
  fi
  sleep 0.3
done
summary
