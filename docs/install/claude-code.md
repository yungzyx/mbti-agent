# Install in Claude Code

```bash
git clone https://github.com/yungzyx/mbti-agent.git
mkdir -p ~/.claude/skills
cp -R mbti-agent ~/.claude/skills/mbti-agent
```

For one project:

```bash
mkdir -p .claude/skills
cp -R /path/to/mbti-agent .claude/skills/mbti-agent
```

Project default:

```markdown
## Collaboration style

Use the mbti-agent skill with INTJ as my default MBTI type unless I override it.
```
