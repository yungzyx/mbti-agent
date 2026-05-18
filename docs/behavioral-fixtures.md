# Behavioral fixtures

`mbti-agent` should be judged by observable coding-agent behavior, not by whether the response sounds like a personality type.

Behavioral fixtures are small scenario files under `tests/fixtures/`. They help maintainers and contributors review whether a type profile or overlay changes workflow in a useful, testable way.

## What fixtures test

A good fixture checks at least one workflow dimension:

- planning depth
- autonomy level
- check-in frequency
- explanation depth
- feedback style
- option breadth
- ambiguity handling
- closure style

Fixtures should also make task mode clear: planning, implementation, debugging, refactoring, code review, or explanation.

## Required structure

Each fixture must include:

- `## Scenario`
- `## Active profile`
- `## User prompt`
- `## Expected behavior`
- `## Must avoid`
- `## Review checklist`

The repository validator enforces these sections so fixture quality does not drift.

## How to review a fixture manually

1. Load the skill with the fixture's type and overlay.
2. Give the user prompt to the target agent.
3. Compare the response against `Expected behavior` and `Must avoid`.
4. Check whether the response made concrete workflow choices.
5. Reject changes that only alter tone, use stereotypes, or weaken safety.

## Adding a new fixture

Create one small file in `tests/fixtures/` with a specific scenario. Prefer a realistic coding task over a generic personality prompt.

Good fixture title:

```text
Fixture: ISFJ regression-safety review
```

Weak fixture title:

```text
Fixture: ISFJ personality style
```

Good expected behavior:

```text
- Checks existing conventions before recommending a refactor.
- Preserves user-facing behavior and asks for verification evidence.
```

Weak expected behavior:

```text
- Sounds friendly and detail oriented.
```
