# Contributing to mbti-agent

Thanks for improving `mbti-agent`. This project is an open-source skill for personality-adaptive coding agents. The most valuable contributions improve how a specific MBTI profile changes real coding workflow behavior.

## Contribution principles

- Improve observable coding behavior, not personality vibes.
- Edit one type profile at a time when possible.
- Ground changes in the type's cognitive function stack.
- Preserve safety, correctness, and explicit user instructions above type preferences.
- Avoid stereotypes, therapeutic claims, and roleplay language.

## What to edit

Common contribution targets:

- `references/{TYPE}.md`: behavior for one MBTI type
- `overlays/*.md`: state modifiers such as stuck or rushed
- `examples/test-cases.md`: prompts that reveal whether behavior actually changes
- `tests/fixtures/*.md`: behavioral fixtures for repeatable profile and overlay review
- `docs/profile-quality-rubric.md`: quality bar for profile changes
- `docs/profile-index.md`: quick comparison table for all profiles
- `docs/cognitive-functions.md`: function-stack rationale
- `docs/evaluation.md`: ways to judge whether a profile is useful

## Editing one type at a time

A focused PR should usually change one file in `references/`. For example:

```text
references/INFP.md
```

When editing a type profile, keep all required sections:

- type name
- function stack
- short summary
- 8 behavior dimensions
- stress signal
- per-task behavior for planning, implementation, debugging, refactoring, code review, and explanation
- best fits
- risks
- override notes

Do not rewrite unrelated types to make the whole system match your preferred style. If a cross-cutting schema change is needed, open an issue first or make a separate PR.

## Justifying profile changes

A good PR explains why the change improves real coding collaboration. Use evidence like:

- "For Ti-dominant users, the previous debugging behavior skipped too quickly to patching; this change adds explicit hypothesis modeling."
- "For Si-dominant users, this refactoring behavior now emphasizes behavior preservation and known-good comparison."
- "For inferior Ne stress, the profile now reduces speculative edge-case expansion and returns to known facts."

Avoid justifications like:

- "INTJs are masterminds, so make it more strategic."
- "ENFPs are chaotic, so they should not finish tasks."
- "This is how my friend behaves."

Personal experience is useful when translated into observable coding behavior.

## Testing expectations

Before opening a PR, run the automated validator:

```bash
python scripts/validate_repo.py
```

The validator checks required files, profile sections, function stacks, overlays, behavioral fixture structure, placeholder leftovers, and obvious secret patterns. GitHub Actions runs the same command on pull requests.

For behavior changes, also run a small manual evaluation with at least two task modes. Use prompts from `examples/test-cases.md`, use an existing fixture in `tests/fixtures/`, or add a new fixture when the change covers a gap.

Minimum for a type-profile change:

1. Planning prompt: does the profile change planning depth, options, and check-ins?
2. Debugging prompt: does the profile change hypothesis style, evidence gathering, and explanation depth?
3. Override prompt: does an explicit user instruction override the type behavior?

If you edit an overlay, test it with at least two different base types. For example, `rushed` should shorten both INTJ and ENFP behavior, but it should not erase their base differences entirely.

## Pull request guidance

Use a focused title:

```text
docs(intp): clarify debugging and closure behavior
docs(overlays): tighten rushed behavior rules
docs(evaluation): add code review test case
```

In the PR body, include:

- files changed
- type or overlay affected
- cognitive-function rationale
- observable coding behavior changed
- prompts used to test the change
- behavioral fixtures added or updated, if applicable
- any known tradeoffs

## Style guide

- Use clear Markdown headings.
- Prefer concrete agent actions over adjectives.
- Say "check in at milestone boundaries" instead of "be collaborative."
- Say "compare two architecture options" instead of "be analytical."
- Keep type files parallel in structure so diffs are easy to review.

## Safety and scope

`mbti-agent` should never claim that MBTI determines ability, identity, or value. It is a user-controlled collaboration preference layer. Users can override or disable it at any time.

## License of contributions

By contributing, you agree that your contribution is licensed under the MIT License.
