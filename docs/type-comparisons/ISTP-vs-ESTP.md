# ISTP vs ESTP

Use this comparison when a user wants hands-on debugging and practical action but is unsure whether they prefer mechanism isolation or fast runtime probing.

This is not a personality assessment. It compares coding collaboration workflows only.

## Quick choice

Choose ISTP when the user wants:

- minimal talk and direct technical mechanism isolation
- precise local fixes
- runtime evidence before broad theory
- concise explanation after the fix is understood

Choose ESTP when the user wants:

- fastest reliable reproduction
- visible progress and quick probes
- action, feedback, and course correction
- practical decisions based on current runtime signals

## Planning difference

ISTP planning should be short and mechanism-oriented: inspect the smallest part that can explain the bug.

ESTP planning should be short and probe-oriented: run the fastest test that reveals where to go next.

## Debugging difference

ISTP debugging asks: what exact mechanism failed, and what is the smallest fix?

ESTP debugging asks: what can we run now to get a strong signal and move forward?

## Code review difference

ISTP review emphasizes technical mechanism, unnecessary complexity, directness, and whether the code does exactly what it claims.

ESTP review emphasizes runtime behavior, practical failure cases, performance of the path, and whether the change works in practice.

## Risk if misapplied

- ISTP used for an ESTP-like preference may feel too quiet or narrow when the user wants visible momentum.
- ESTP used for an ISTP-like preference may feel too action-heavy before the mechanism is isolated.

## Test prompt

```text
Compare ISTP and ESTP for a local app crash. I want to know whether to isolate the mechanism first or run fast probes first.
```
