# Install in Hermes Agent

`mbti-agent` works in Hermes Agent as a local skill repository.

## Install globally

```bash
git clone https://github.com/yungzyx/mbti-agent.git ~/.hermes/skills/mbti-agent
hermes skills list
```

If Hermes is already running, start a new session or use `/reload-skills` followed by `/reset` so the skill index is refreshed.

## Install into a Hermes profile

If you use Hermes profiles, install the skill into the profile-specific skills directory:

```bash
hermes profile show <profile-name>
mkdir -p ~/.hermes/profiles/<profile-name>/skills
git clone https://github.com/yungzyx/mbti-agent.git ~/.hermes/profiles/<profile-name>/skills/mbti-agent
```

## Use it in a session

```text
Use the mbti-agent skill with INTJ as my default coding collaboration style.
```

With an overlay:

```text
Use mbti-agent. My type is INTP and I am stuck on this failing test.
```

## Project-level default

Add this to a project instruction file such as `CLAUDE.md`, `AGENTS.md`, or another file Hermes loads for the project:

```markdown
## Collaboration style

Use the mbti-agent skill with ENFP as my default type profile unless I override it. Apply state overlays such as stuck, rushed, learning, exploring, or fatigued when I mention those states.
```

## Verify

Ask Hermes:

```text
Load mbti-agent with ISTJ. Review this change for regression risk and give me the safest next step.
```

A good response should emphasize precedent, minimal safe changes, verification, and a concise closure checklist.
