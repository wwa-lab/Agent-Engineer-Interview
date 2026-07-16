#!/usr/bin/env python3
"""Validate the repository contract used by contributors and CI."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "README.zh-CN.md", "LICENSE", "CONTRIBUTING.md", "SECURITY.md",
    ".github/workflows/markdown-lint.yml", ".github/workflows/link-check.yml",
    "coding-challenges/README.md", "mock-interviews/README.md",
]
QUESTION_HEADINGS = ["## Interview Question", "## Difficulty", "## Type", "## Follow-up Questions"]
question_files = [
    ROOT / "docs/interview-questions/beginner.md",
    ROOT / "docs/interview-questions/intermediate.md",
    ROOT / "docs/interview-questions/senior.md",
    ROOT / "docs/interview-questions/behavioral.md",
]

missing = [path for path in REQUIRED if not (ROOT / path).exists()]
if missing:
    print("Missing required paths:")
    print("\n".join(missing))
    sys.exit(1)

for challenge in sorted((ROOT / "coding-challenges").glob("[0-9][0-9]-*")):
    for child in ("README.md", "requirements.txt", "starter", "solution", "tests"):
        if not (challenge / child).exists():
            print(f"Missing {challenge.relative_to(ROOT)}/{child}")
            sys.exit(1)

for file in question_files:
    content = file.read_text(encoding="utf-8")
    for heading in QUESTION_HEADINGS:
        if heading not in content:
            print(f"{file.relative_to(ROOT)} is missing heading: {heading}")
            sys.exit(1)

counts = {
    "beginner": len(re.findall(r"^### Q\d+", question_files[0].read_text(encoding="utf-8"), re.MULTILINE)),
    "intermediate": len(re.findall(r"^### Q\d+", question_files[1].read_text(encoding="utf-8"), re.MULTILINE)),
    "senior": len(re.findall(r"^### Q\d+", question_files[2].read_text(encoding="utf-8"), re.MULTILINE)),
    "behavioral": len(re.findall(r"^### Q\d+", question_files[3].read_text(encoding="utf-8"), re.MULTILINE)),
}
minimums = {"beginner": 20, "intermediate": 20, "senior": 15, "behavioral": 10}
for level, minimum in minimums.items():
    if counts[level] < minimum:
        print(f"{level}: found {counts[level]}, need at least {minimum}")
        sys.exit(1)

print("Structure: OK")
print("Question counts:", ", ".join(f"{key}={value}" for key, value in counts.items()))
