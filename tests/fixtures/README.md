# Behavioral fixtures

Behavioral fixtures are lightweight, reviewable scenarios for checking whether `mbti-agent` changes workflow rather than only changing tone.

Each fixture is a Markdown file with the same required sections:

- `## Scenario`
- `## Active profile`
- `## User prompt`
- `## Expected behavior`
- `## Must avoid`
- `## Review checklist`

The validator checks structure. Human reviewers use the checklist to judge whether a profile or overlay produces useful coding-agent behavior.
