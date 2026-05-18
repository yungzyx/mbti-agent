# Install in Codex

```bash
git clone https://github.com/yungzyx/mbti-agent.git
mkdir -p ~/.codex/skills
cp -R mbti-agent ~/.codex/skills/mbti-agent
```

For one project:

```bash
mkdir -p .codex/skills
cp -R /path/to/mbti-agent .codex/skills/mbti-agent
```

Prompt example:

```text
Use the mbti-agent skill. My type is INTP. Help me debug this failing test.
```
