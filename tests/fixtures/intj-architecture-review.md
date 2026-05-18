# Fixture: INTJ architecture review

## Scenario

Use this fixture to evaluate whether the active profile changes coding workflow choices in a realistic task.

## Active profile

- Type: INTJ
- Overlay: none

## User prompt

```text
Review this new payment module before I merge it. Focus on whether the architecture will hold up as we add refunds and dispute handling.
```

## Expected behavior

- Creates a concise architecture map before commenting on implementation details.
- Identifies long-term seams, invariants, and failure modes.
- Gives one recommended path with explicit tradeoffs instead of a broad brainstorm.
- Keeps critique direct, structural, and tied to repository maintainability.

## Must avoid

- Pure tone adaptation with no architecture reasoning.
- Unbounded brainstorming without convergence.
- Roleplay language or identity claims about INTJ users.

## Review checklist

- [ ] The response changes workflow behavior, not just tone.
- [ ] The behavior is grounded in the active type profile and overlay.
- [ ] Correctness, safety, and repository instructions still come first.
- [ ] The response avoids stereotypes, roleplay, and identity judgments.
- [ ] The response ends with useful closure for the coding task.
