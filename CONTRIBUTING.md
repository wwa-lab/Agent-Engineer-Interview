# Contributing

Thanks for helping make Agent Engineer Interview more useful and more honest. The project favors concrete engineering judgment over framework promotion or long link lists.

## Before opening a pull request

1. Search for an existing page or issue.
2. Keep filenames in `kebab-case` and use the nearest existing page as a style reference.
3. Write original explanations. Attribute external claims and prefer primary documentation.
4. Check every new internal link and run `python scripts/validate-structure.py`.
5. For code, keep the challenge runnable without paid API credentials and add tests for success and failure paths.

## Adding content

### Interview question

Use [the question template](docs/templates/interview-question-template.md). Include difficulty, type, expected answer time, what the interviewer is evaluating, a concise answer, a deeper discussion, common mistakes, and follow-ups. A good question tests a decision or failure mode, not memorization.

### System design case

Use [the system design template](docs/templates/system-design-template.md). State scale and SLO assumptions, draw the request path, identify data and trust boundaries, and name at least two trade-offs.

### Coding challenge

Use [the coding challenge template](docs/templates/coding-challenge-template.md). Every challenge needs `README.md`, `requirements.txt`, `starter/`, `solution/`, and `tests/`. Tests must work offline with Python 3.11+.

### Interview experience

Anonymized experiences are welcome. Describe the role level, interview format, broad topic, and what you learned. Never include company-confidential prompts, take-home answers, private repository code, interviewer names, candidate names, or personally identifying details. If an experience is governed by an NDA, do not submit it.

### Outdated content

Open an issue using the content request form and include the page, the claim that changed, an authoritative source, and the date checked. Avoid silently replacing a historical note when the timeline itself is useful.

## Quality bar

- Explain constraints and failure modes, not only happy paths.
- Separate facts, recommendations, and personal experience.
- Prefer small runnable examples over pseudo-code that hides important behavior.
- Avoid provider-specific claims unless the scope is explicit.
- Do not hard-code secrets, personal data, or production endpoints.
- Keep examples accessible to an engineer who is learning agents for the first time.

## Pull request checklist

- [ ] The change has a focused title and description.
- [ ] New content follows the relevant template.
- [ ] Internal links resolve.
- [ ] Markdown and structure checks pass.
- [ ] Python tests pass for changed challenges.
- [ ] No confidential, copyrighted, or personally identifying material was added.
- [ ] The PR explains any version-sensitive claim or trade-off.
