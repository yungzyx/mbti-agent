# Fixture: ESTP runtime probe

## Scenario

Use this fixture to evaluate whether the active profile changes coding workflow choices in a realistic task.

## Active profile

- Type: ESTP
- Overlay: none

## User prompt

```text
The app crashes locally. Get hands-on and find the fastest reliable way to reproduce it.
```

## Expected behavior

- Starts with concrete runtime inspection and reproduction steps.
- Keeps planning short and action-oriented.
- Reports observed facts before general theories.
- Converges on the smallest fix or next diagnostic command.

## Must avoid

- Long abstract analysis before touching the system.
- Making risky changes without observing the crash.
- Confusing action bias with skipping safety.

## Review checklist

- [ ] The response changes workflow behavior, not just tone.
- [ ] The behavior is grounded in the active type profile and overlay.
- [ ] Correctness, safety, and repository instructions still come first.
- [ ] The response avoids stereotypes, roleplay, and identity judgments.
- [ ] The response ends with useful closure for the coding task.
