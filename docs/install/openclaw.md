# Install in OpenClaw

`mbti-agent` is a plain `SKILL.md`-style skill repository, so it can be used with OpenClaw setups that load local agent skills or project instruction directories.

## Install as a local skill

```bash
git clone https://github.com/yungzyx/mbti-agent.git ~/.openclaw/skills/mbti-agent
```

Then restart OpenClaw or reload skills according to your OpenClaw setup.

## Use per project

For a project-local setup, clone or copy the repository into the project's agent skills area if your OpenClaw configuration supports one:

```bash
mkdir -p .openclaw/skills
git clone https://github.com/yungzyx/mbti-agent.git .openclaw/skills/mbti-agent
```

If your OpenClaw setup uses instruction files instead of a skills directory, reference the repository's `SKILL.md` from your project instructions:

```markdown
## Agent skills

Use `mbti-agent` from `.openclaw/skills/mbti-agent/SKILL.md` when I provide an MBTI type or default collaboration style. Load the matching file from `references/` and any relevant state overlay from `overlays/`.
```

## Example prompt

```text
Use mbti-agent with ENTJ as my default style. I am rushed, so give me the shortest safe implementation plan and execute after validation.
```

## Notes

OpenClaw installations may differ in how they discover local skills. The repository is intentionally runtime-light: the important contract is that the agent can read `SKILL.md`, then load the selected `references/{TYPE}.md` file and optional `overlays/{state}.md` file.
