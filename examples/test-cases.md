# Test cases

Use these prompts to evaluate whether `mbti-agent` changes workflow behavior.

## Planning

Prompt:

```text
Use mbti-agent with INTJ. Plan a refactor that splits a large authentication service into smaller modules.
```

Expected: architecture-first plan, invariants, interfaces, migration risks, low check-in frequency.

Prompt:

```text
Use mbti-agent with ENFP. Plan a refactor that splits a large authentication service into smaller modules.
```

Expected: multiple possible directions, visible momentum, more interactive checkpoints, eventual shortlist.

## Implementation

```text
Use mbti-agent with ESTJ. Implement a small CLI flag and update tests.
```

Expected: checklist, efficient execution order, milestone-style summary.

```text
Use mbti-agent with ISFP. Implement a small CLI flag and update tests.
```

Expected: concrete implementation with attention to user experience, gentle explanation, acceptance checks.

## Debugging

```text
Use mbti-agent with INTP. Debug this intermittent cache invalidation test failure.
```

Expected: hypothesis model, edge cases, logical causality, caveated recommendation.

```text
Use mbti-agent with ESTP. Debug this intermittent cache invalidation test failure.
```

Expected: fast probes, runtime evidence, quick patch attempt, outcome-first closure.

## Refactoring

```text
Use mbti-agent with ISTJ. Refactor this config loader without changing behavior.
```

Expected: precedent, exact behavior preservation, ordered steps, verification checklist.

```text
Use mbti-agent with ENTP. Refactor this config loader without changing behavior.
```

Expected: alternative designs, challenge current assumptions, ranked recommendation before change.

## Code review

```text
Use mbti-agent with ENTJ. Review this PR for production readiness.
```

Expected: direct findings, delivery risk, prioritized fixes, concrete next actions.

```text
Use mbti-agent with ESFJ. Review this PR for production readiness.
```

Expected: warm but clear feedback, team impact, shared understanding, actionable improvements.

## Explanation

```text
Use mbti-agent with ISTP. Explain how this parser works.
```

Expected: concise mechanism-first explanation.

```text
Use mbti-agent with ENFJ. Explain how this parser works.
```

Expected: approachable teaching, examples, comprehension-oriented pacing.

## Overlay tests

```text
Use mbti-agent with ENTP. I'm rushed; choose an approach and implement the smallest safe version.
```

Expected: reduced option breadth, faster convergence, but still a brief rationale.

```text
Use mbti-agent with ISTJ. I'm exploring; compare approaches before deciding.
```

Expected: safe concrete alternatives, including at least one non-precedent option.

```text
Use mbti-agent with INFP. I'm fatigued; keep this simple.
```

Expected: one recommendation, gentle tone, short rationale, no option overload.

## Override test

```text
Use mbti-agent with INTP, but for this response give me only the answer and no tradeoffs.
```

Expected: explicit user override wins; no multi-option analysis.
