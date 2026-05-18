# Security policy

## Supported scope

This repository contains an agent skill, documentation, examples, validation tooling, and behavioral fixtures. It should not contain credentials, private logs, local machine paths, or personal agent memory.

## Reporting a problem

If you find a security or privacy problem in this repository, open a GitHub issue if it is safe to discuss publicly. If the report contains a secret, token, private path, or personal data, do not paste it into an issue. Contact the repository owner through their public GitHub profile instead.

## Secret hygiene

Do not commit:

- API keys or tokens
- private SSH keys
- `.env` files
- local absolute paths
- personal prompts, chat logs, or memory files
- screenshots containing credentials

The repository validator checks for common secret and local-path patterns, but it is best-effort only. GitHub secret scanning and human review are still important.

## Agent safety

`mbti-agent` must never weaken correctness, safety, repository instructions, or policy compliance. Type profiles adapt workflow behavior; they do not override explicit user instructions or safe engineering practice.
