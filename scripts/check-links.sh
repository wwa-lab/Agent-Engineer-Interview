#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 - <<'PY'
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

root = Path.cwd().resolve()
pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
errors = []

for markdown_file in sorted(root.rglob("*.md")):
    if ".git" in markdown_file.parts:
        continue
    text = markdown_file.read_text(encoding="utf-8")
    for raw_target in pattern.findall(text):
        target = raw_target.strip().strip("<>").split()[0]
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("#"):
            continue
        relative = Path(unquote(parsed.path))
        destination = (markdown_file.parent / relative).resolve() if not relative.is_absolute() else (root / relative.relative_to("/")).resolve()
        try:
            destination.relative_to(root.resolve())
        except ValueError:
            errors.append(f"{markdown_file.relative_to(root)} -> outside repository: {target}")
            continue
        if not destination.exists():
            errors.append(f"{markdown_file.relative_to(root)} -> missing: {target}")

if errors:
    print("Broken internal links:")
    print("\n".join(errors))
    sys.exit(1)
print("Internal Markdown links: OK")
PY
