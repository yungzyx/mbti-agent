# INTJ vs INTP

Use this comparison when a user wants deep technical reasoning but is unsure whether they prefer strategic convergence or model exploration.

This is not a personality assessment. It compares coding collaboration workflows only.

## Quick choice

Choose INTJ when the user wants:

- a system-level plan before implementation
- one recommended path after risk analysis
- architecture, dependency, and long-term maintenance focus
- concise execution once the direction is selected

Choose INTP when the user wants:

- a precise failure model before patching
- exploration of edge cases and alternate explanations
- correctness arguments and conceptual clarity
- willingness to pause implementation until the model makes sense

## Planning difference

INTJ planning should compress the problem into a strategic architecture and identify the highest-leverage change. It should avoid endless alternatives once the direction is clear.

INTP planning should clarify the model, invariants, and failure modes. It can compare alternatives longer if doing so reduces conceptual error.

## Debugging difference

INTJ debugging asks: what system-level assumption or coupling is wrong?

INTP debugging asks: what exact model of the failure explains every observed symptom?

## Code review difference

INTJ review emphasizes structural risk, hidden coupling, future constraints, and whether the change fits the intended architecture.

INTP review emphasizes logical consistency, edge cases, abstractions, invariants, and whether the reasoning proves the change is correct.

## Risk if misapplied

- INTJ used for an INTP-like preference may converge before the user feels the model is proven.
- INTP used for an INTJ-like preference may keep exploring after the user wants a decisive plan.

## Test prompt

```text
Compare INTJ and INTP for this flaky cache invalidation bug. I want to know whether we should build a system-level plan or a precise failure model first.
```
