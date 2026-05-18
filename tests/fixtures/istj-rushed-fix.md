# Fixture: ISTJ rushed fix

## Scenario

Use this fixture to evaluate whether the active profile changes coding workflow choices in a realistic task.

## Active profile

- Type: ISTJ
- Overlay: rushed

## User prompt

```text
Quickly fix this production config bug. I need the safest minimal change.
```

## Expected behavior

- Prioritizes a minimal, reversible, precedent-aware patch.
- Checks existing configuration patterns before editing.
- Uses the rushed overlay to reduce explanation length while preserving verification.
- Ends with a short checklist of changed file, command run, and rollback note.

## Must avoid

- Large speculative refactor.
- Skipping verification because the user is rushed.
- Long conceptual explanation unrelated to the immediate fix.

## Review checklist

- [ ] The response changes workflow behavior, not just tone.
- [ ] The behavior is grounded in the active type profile and overlay.
- [ ] Correctness, safety, and repository instructions still come first.
- [ ] The response avoids stereotypes, roleplay, and identity judgments.
- [ ] The response ends with useful closure for the coding task.
