# Behavior schema

Every type profile must use the same behavior dimensions so contributors can edit one profile without changing the whole repository.

## Required dimensions

| Dimension | Definition | Observable agent behavior |
| --- | --- | --- |
| Planning | Amount of upfront architecture, sequence, and risk analysis | Plan length, assumptions, acceptance criteria, diagrams in prose |
| Autonomy | How independently the agent proceeds | Whether it asks before edits or continues to milestones |
| Check-ins | Frequency and granularity of confirmation | Number and timing of questions or progress updates |
| Explanation | Depth and style of reasoning exposed | Theory, examples, concise rationale, or step-by-step teaching |
| Feedback | Critique style | Direct, diplomatic, structural, encouraging, procedural |
| Options | Breadth of alternatives | One recommendation, shortlist, or many explored options |
| Ambiguity | Treatment of uncertainty | Resolve, explore, test, ground in precedent, or ask |
| Closure | How responses end | Checklist, next step, recommendation, risk summary, recap |

## Required task modes

Each type must describe behavior for:

- planning
- implementation
- debugging
- refactoring
- code review
- explanation

## Profile file checklist

- Type name is clear in the title.
- Function stack lists dominant, auxiliary, tertiary, inferior.
- Short summary explains coding collaboration behavior.
- All 8 dimensions are concrete.
- Stress signal references the inferior function.
- Per-task behavior covers all six task modes.
- Best fits and risks are practical, not stereotyped.
- Override notes explain how direct user instructions supersede the profile.
