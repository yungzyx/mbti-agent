# Profile quality rubric

Use this rubric when editing a type profile, overlay, or behavioral fixture.

## Strong profile changes

A strong change is:

- grounded in the cognitive function stack
- visible in coding workflow behavior
- specific to one or more task modes
- useful to an agent deciding what to do next
- respectful and non-diagnostic
- easy to test with a behavioral fixture

## Weak profile changes

A weak change usually does one of these:

- changes only tone
- describes a personality stereotype
- claims a type always behaves one way
- adds vague adjectives without operational behavior
- makes the agent less correct, less safe, or less direct
- duplicates another type without explaining the difference

## Review questions

Before merging a profile change, ask:

1. What exact agent behavior changes?
2. Which workflow dimension changes?
3. Which task mode is affected?
4. What cognitive-function rationale supports it?
5. What should the agent avoid doing?
6. Which fixture would catch a regression?

## Acceptance standard

The minimum acceptable contribution is not "this sounds like the type." The minimum standard is:

```text
Given this type or overlay, the agent makes a different, useful, observable workflow choice on a coding task.
```
