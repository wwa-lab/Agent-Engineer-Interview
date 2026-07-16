#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
while IFS= read -r -d '' tests_dir; do
  challenge_dir="$(dirname "$tests_dir")"
  echo "==> $(basename "$challenge_dir")"
  (cd "$challenge_dir" && python3 -m unittest discover -s tests -p 'test_*.py' -v)
done < <(find "$root/coding-challenges" -mindepth 2 -maxdepth 2 -type d -name tests -print0)
