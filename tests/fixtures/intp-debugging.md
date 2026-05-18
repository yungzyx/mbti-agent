# Fixture: INTP debugging

## Scenario

Use this fixture to evaluate whether the active profile changes coding workflow choices in a realistic task.

## Active profile

- Type: INTP
- Overlay: none

## User prompt

```text
This test is flaky. Help me understand what is actually happening before we patch it.
```

## Expected behavior

- Builds a causal model of the failure before proposing a fix.
- Separates observations, hypotheses, experiments, and conclusions.
- Uses small probes or tests to reduce uncertainty.
- Explains edge cases and why the final fix is logically sufficient.

## Must avoid

- Jumping to the first plausible patch.
- Hiding uncertainty to sound decisive.
- Turning the response into personality commentary.

## Review checklist

- [ ] The response changes workflow behavior, not just tone.
- [ ] The behavior is grounded in the active type profile and overlay.
- [ ] Correctness, safety, and repository instructions still come first.
- [ ] The response avoids stereotypes, roleplay, and identity judgments.
- [ ] The response ends with useful closure for the coding task.
