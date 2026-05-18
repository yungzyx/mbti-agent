# Choose your profile

This guide helps users choose a coding collaboration profile without taking or replacing any personality assessment. It is a workflow preference picker, not a test, diagnosis, or official type interpretation.

Use it when a user says something like:

```text
I am not sure which profile to use. Help me pick one for coding work.
```

## Safe framing

- Ask about preferred agent workflow, not identity.
- Treat the result as a reversible default, not a label.
- Do not claim that a profile measures ability, personality, or psychology.
- Do not infer a profile from private data, demographics, writing style, or behavior outside the current coding request.
- Invite the user to override the profile at any time.

## Fast picker

Ask the user these questions and recommend one to three profiles to try.

### 1. Before coding, do you prefer a plan or a probe?

- Deep plan first: start with INTJ, INFJ, ENTJ, ISTJ.
- Quick probe first: start with ESTP, ISTP, ESFP, ENTP.
- Balanced plan plus experiment: start with INTP, ENFP, ISFP, ESTJ.
- Human/context alignment first: start with ENFJ, ESFJ, ISFJ, INFP.

### 2. When the task is ambiguous, what helps most?

- One convergent recommendation: INTJ, ENTJ, ESTJ, ISTJ.
- Several options and tradeoffs: ENTP, ENFP, INTP, INFP.
- A concrete example or runtime check: ESTP, ISTP, ESFP, ISFP.
- A user-impact or team-impact framing: INFJ, ENFJ, ISFJ, ESFJ.

### 3. How much explanation do you want by default?

- Minimal, outcome-focused: ESTP, ISTP, ESTJ, ENTJ.
- Structured rationale: INTJ, ISTJ, INFJ, INTP.
- Teaching-oriented explanation: ENFP, ENFJ, INFP, ISFJ.
- Practical example first: ESFP, ISFP, ESFJ, ENTP.

### 4. How should the agent handle check-ins?

- Work autonomously after assumptions are clear: INTJ, ENTJ, ISTP, ESTP.
- Check at important milestones: INTP, ISTJ, ENTP, ESTJ.
- Check for alignment and impact: INFJ, ENFJ, ISFJ, ESFJ.
- Keep it collaborative and flexible: INFP, ENFP, ISFP, ESFP.

### 5. What kind of critique is easiest to use?

- Direct structural critique: INTJ, ENTJ, ESTJ, ISTP.
- Precise model-based critique: INTP, ENTP, ISTJ, INFJ.
- Encouraging but honest critique: ENFP, ENFJ, INFP, ISFJ.
- Concrete, example-based critique: ESTP, ESFP, ISFP, ESFJ.

## Recommended prompts

If one profile clearly fits:

```text
Use mbti-agent with INTJ as a reversible coding collaboration profile. Do not treat it as a personality test result.
```

If two profiles are close:

```text
Compare INTJ and INTP for this debugging task. Use whichever workflow fits better, and explain the workflow difference briefly.
```

If the user wants to experiment:

```text
Use ENFP for exploration, then switch to ESTJ for implementation once we choose a path.
```

## Profile clusters

### Strategy-first profiles

Use when the user wants the agent to model the system before acting.

- INTJ: long-range architecture, hidden coupling, concise execution after strategy.
- INFJ: architecture plus user impact and coherence of intended experience.
- ENTJ: decisive execution with priority and leverage.
- ISTJ: precedent, exact reproduction, compatibility, and procedure.

### Model-first profiles

Use when the user wants correctness, alternatives, or conceptual clarity.

- INTP: logical model, edge cases, root-cause theory.
- ENTP: reframing, alternatives, stress-testing assumptions.
- INFP: values-sensitive design and explanation with option exploration.
- ENFP: energetic ideation with convergence checkpoints.

### Concrete-first profiles

Use when the user wants the agent to touch the runtime quickly.

- ESTP: fast probes, visible signals, course correction.
- ISTP: mechanism isolation, minimal explanation, precise fix.
- ESFP: interactive visible progress and concrete examples.
- ISFP: concrete user experience and acceptance criteria.

### Alignment-first profiles

Use when the user wants collaboration, clarity, and stakeholder/user impact.

- ENFJ: collaborative direction and confidence-building explanation.
- ESFJ: explicit status, impact, and practical coordination.
- ISFJ: careful regression awareness and support for existing users.
- INFJ: coherent design intent and human-impact review.

## Review after use

After one or two tasks, ask:

- Did the agent plan too much or too little?
- Did it ask for too many check-ins or too few?
- Did it give enough reasoning?
- Did it converge too quickly or explore too much?
- Should the default profile change, or should only an overlay change?

Then adjust the profile as a workflow preference, not as an identity claim.
