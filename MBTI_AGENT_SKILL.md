# MBTI Agent Skill — Master Specification

`mbti-agent` is a personality-adaptive coding skill for Claude Code, Codex, and compatible agent runtimes. It changes real workflow behavior based on the user's selected MBTI type.

This file is the human-facing master specification. Runtime behavior starts in `SKILL.md`; detailed type behavior lives in `references/`; temporary state modifiers live in `overlays/`.

## Core promise

The skill adapts:

- planning depth
- autonomy level
- check-in frequency
- explanation depth
- feedback style
- option breadth
- ambiguity handling
- closure style

It applies across planning, implementation, debugging, refactoring, code review, and explanation.

## Design constraints

- Include all 16 MBTI types.
- Ground every type in the cognitive function stack.
- Include inferior-function stress signals.
- Support stuck, rushed, learning, exploring, and fatigued overlays.
- Keep profiles useful for real coding sessions, not personality roleplay.
- Let contributors improve one type file at a time.

## Source-of-truth files

- Runtime entry point: `SKILL.md`
- Behavior schema: `docs/behavior-schema.md`
- Function rationale: `docs/cognitive-functions.md`
- Type profiles: `references/{TYPE}.md`
- State overlays: `overlays/*.md`
- Evaluation prompts: `examples/test-cases.md`

## Type coverage

All 16 profiles are included: INTJ, INTP, ENTJ, ENTP, INFJ, INFP, ENFJ, ENFP, ISTJ, ISFJ, ESTJ, ESFJ, ISTP, ISFP, ESTP, ESFP.

## Contribution standard

A profile change should be justified by observable coding behavior and the relevant cognitive functions. The repository intentionally separates profiles so contributors can improve one type without touching the rest.
