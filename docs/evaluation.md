# Evaluation

`mbti-agent` is useful only if it changes real coding behavior. Evaluate profiles by comparing how the same task is handled under different active types and overlays.

## What to measure

- Planning depth: short risk scan vs full architecture plan
- Autonomy: proceeds independently vs checks in frequently
- Explanation depth: concise result vs detailed reasoning
- Feedback style: blunt, diplomatic, procedural, encouraging, structural
- Option breadth: one recommendation vs several alternatives
- Ambiguity handling: resolve, explore, test, or ground in precedent
- Closure: checklist, next step, risk note, recommendation, or recap

## Manual test protocol

1. Choose one task prompt from `examples/test-cases.md`.
2. Run it with two contrasting types, such as INTJ and ENFP or ISTP and ENFJ.
3. Verify that workflow changes, not just word choice.
4. Add one overlay and verify it modifies but does not erase the base type.
5. Test an explicit override, such as "ignore MBTI" or "give me only one option."

## Acceptance criteria

A profile passes if a reviewer can point to specific behavioral differences in the agent's plan, actions, questions, review comments, or final summary. It fails if the only difference is tone.

## Example evaluation pair

Prompt: "Use mbti-agent with INTP. Debug this failing auth test."

Expected behavior: builds a causal model, states hypotheses, inspects logic, explains tradeoffs, closes with a recommendation and caveats.

Prompt: "Use mbti-agent with ESTP. Debug this failing auth test."

Expected behavior: runs direct probes, follows runtime evidence, patches quickly, explains briefly, closes with outcome-first verification.
