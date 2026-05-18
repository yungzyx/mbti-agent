#!/usr/bin/env python3
"""Validate the mbti-agent skill repository.

This script is intentionally dependency-free so contributors can run it with a
stock Python 3 interpreter and GitHub Actions can run it without package setup.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TYPES = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP",
]

OVERLAYS = ["stuck", "rushed", "learning", "exploring", "fatigued"]

REQUIRED_ROOT_FILES = [
    "SKILL.md",
    "MBTI_AGENT_SKILL.md",
    "README.md",
    "CONTRIBUTING.md",
    "LICENSE.md",
    ".gitignore",
]

REQUIRED_DOCS = [
    "docs/behavior-schema.md",
    "docs/behavioral-fixtures.md",
    "docs/cognitive-functions.md",
    "docs/evaluation.md",
    "docs/profile-index.md",
    "docs/profile-quality-rubric.md",
    "docs/roadmap.md",
    "docs/install/claude-code.md",
    "docs/install/codex.md",
    "docs/install/hermes-agent.md",
    "docs/install/openclaw.md",
]

REQUIRED_EXAMPLES = [
    "examples/prompt-examples.md",
    "examples/test-cases.md",
]

REQUIRED_TRUST_FILES = [
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
]

MIN_BEHAVIORAL_FIXTURES = 6

TYPE_REQUIRED_SECTIONS = [
    "## Function stack",
    "## Short summary",
    "## 8 behavior dimensions",
    "## Stress signal",
    "## Per-task behavior",
    "### Planning",
    "### Implementation",
    "### Debugging",
    "### Refactoring",
    "### Code review",
    "### Explanation",
    "## Best fits",
    "## Risks",
    "## Override notes",
]

OVERLAY_REQUIRED_SECTIONS = [
    "## When it activates",
    "## Behavior dimensions modified",
    "## How it combines with the base type",
    "## Examples of behavior changes",
]

FIXTURE_REQUIRED_SECTIONS = [
    "## Scenario",
    "## Active profile",
    "## User prompt",
    "## Expected behavior",
    "## Must avoid",
    "## Review checklist",
]

FUNCTIONS = {"Ni", "Ne", "Si", "Se", "Te", "Ti", "Fe", "Fi"}

EXPECTED_STACKS = {
    "INTJ": ("Ni", "Te", "Fi", "Se"),
    "INTP": ("Ti", "Ne", "Si", "Fe"),
    "ENTJ": ("Te", "Ni", "Se", "Fi"),
    "ENTP": ("Ne", "Ti", "Fe", "Si"),
    "INFJ": ("Ni", "Fe", "Ti", "Se"),
    "INFP": ("Fi", "Ne", "Si", "Te"),
    "ENFJ": ("Fe", "Ni", "Se", "Ti"),
    "ENFP": ("Ne", "Fi", "Te", "Si"),
    "ISTJ": ("Si", "Te", "Fi", "Ne"),
    "ISFJ": ("Si", "Fe", "Ti", "Ne"),
    "ESTJ": ("Te", "Si", "Ne", "Fi"),
    "ESFJ": ("Fe", "Si", "Ne", "Ti"),
    "ISTP": ("Ti", "Se", "Ni", "Fe"),
    "ISFP": ("Fi", "Se", "Ni", "Te"),
    "ESTP": ("Se", "Ti", "Fe", "Ni"),
    "ESFP": ("Se", "Fi", "Te", "Ni"),
}

SENSITIVE_PATTERNS = [
    re.compile(r"gho_[A-Za-z0-9_]+"),
    re.compile(r"github_pat_[A-Za-z0-9_]+"),
    re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
    re.compile("/Users/" + "yungbot"),
    re.compile("yungbot" + "@"),
    re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"]?[^\s'\"]+"),
    re.compile(r"(?i)password\s*[:=]\s*['\"]?[^\s'\"]+"),
    re.compile(r"(?i)secret\s*[:=]\s*['\"]?[^\s'\"]+"),
    re.compile(r"(?i)token\s*[:=]\s*['\"]?[^\s'\"]+"),
]

PLACEHOLDER_PATTERNS = [
    re.compile(r"\{\{"),
    re.compile("<" + "owner>"),
    re.compile("your" + "-org"),
    re.compile("PROJECT" + "_NAME"),
    re.compile("TARGET" + "_AGENT"),
    re.compile("LICENSE" + "_TYPE"),
    re.compile("COPYRIGHT" + "_HOLDER"),
    re.compile("SECURITY" + "_CONTACT"),
]

ALLOW_PLACEHOLDER_FILES = {
    ".github/ISSUE_TEMPLATE/type-profile.yml",
    ".github/ISSUE_TEMPLATE/overlay.yml",
    ".github/ISSUE_TEMPLATE/behavior-bug.yml",
    ".github/pull_request_template.md",
}


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_required_files(errors: list[str]) -> None:
    required = list(REQUIRED_ROOT_FILES) + REQUIRED_DOCS + REQUIRED_EXAMPLES + REQUIRED_TRUST_FILES
    required += [f"references/{type_name}.md" for type_name in TYPES]
    required += [f"overlays/{overlay}.md" for overlay in OVERLAYS]
    for file_name in required:
        if not (ROOT / file_name).is_file():
            fail(errors, f"missing required file: {file_name}")


def check_skill_file(errors: list[str]) -> None:
    path = ROOT / "SKILL.md"
    if not path.exists():
        return
    content = text(path)
    if not content.startswith("---\n"):
        fail(errors, "SKILL.md must start with YAML frontmatter")
    if "\n---\n" not in content[4:]:
        fail(errors, "SKILL.md frontmatter must close with ---")
    for needle in ["name: mbti-agent", "description:", "## Runtime instructions", "## Type dispatch", "## Hard rules"]:
        if needle not in content:
            fail(errors, f"SKILL.md missing {needle!r}")


def extract_stack(content: str) -> tuple[str, str, str, str] | None:
    labels = ["Dominant", "Auxiliary", "Tertiary", "Inferior"]
    values: list[str] = []
    for label in labels:
        match = re.search(rf"- {label}:\s*([A-Z][a-z])\b", content)
        if not match:
            return None
        values.append(match.group(1))
    return tuple(values)  # type: ignore[return-value]


def check_type_profiles(errors: list[str]) -> None:
    for type_name in TYPES:
        path = ROOT / "references" / f"{type_name}.md"
        if not path.exists():
            continue
        content = text(path)
        if not content.startswith(f"# {type_name}"):
            fail(errors, f"{rel(path)} title must start with '# {type_name}'")
        for section in TYPE_REQUIRED_SECTIONS:
            if section not in content:
                fail(errors, f"{rel(path)} missing section {section}")
        stack = extract_stack(content)
        if stack != EXPECTED_STACKS[type_name]:
            fail(errors, f"{rel(path)} has stack {stack}, expected {EXPECTED_STACKS[type_name]}")
        if stack and set(stack) - FUNCTIONS:
            fail(errors, f"{rel(path)} contains invalid cognitive function in stack: {stack}")
        dimension_rows = re.findall(r"^\| (Planning|Autonomy|Check-ins|Explanation|Feedback|Options|Ambiguity|Closure) \|", content, re.MULTILINE)
        if sorted(dimension_rows) != sorted(["Planning", "Autonomy", "Check-ins", "Explanation", "Feedback", "Options", "Ambiguity", "Closure"]):
            fail(errors, f"{rel(path)} must include exactly the 8 behavior dimension rows")
        if "roleplay" not in content.lower():
            fail(errors, f"{rel(path)} should explicitly avoid roleplay language")


def check_overlays(errors: list[str]) -> None:
    for overlay in OVERLAYS:
        path = ROOT / "overlays" / f"{overlay}.md"
        if not path.exists():
            continue
        content = text(path)
        if not content.startswith(f"# Overlay: {overlay}"):
            fail(errors, f"{rel(path)} title must start with '# Overlay: {overlay}'")
        for section in OVERLAY_REQUIRED_SECTIONS:
            if section not in content:
                fail(errors, f"{rel(path)} missing section {section}")
        if "base type" not in content.lower():
            fail(errors, f"{rel(path)} must explain how it combines with the base type")




def check_behavioral_fixtures(errors: list[str]) -> None:
    fixture_dir = ROOT / "tests" / "fixtures"
    if not fixture_dir.is_dir():
        fail(errors, "missing behavioral fixture directory: tests/fixtures")
        return

    fixture_files = sorted(path for path in fixture_dir.glob("*.md") if path.name != "README.md")
    if len(fixture_files) < MIN_BEHAVIORAL_FIXTURES:
        fail(errors, f"expected at least {MIN_BEHAVIORAL_FIXTURES} behavioral fixtures, found {len(fixture_files)}")

    for path in fixture_files:
        content = text(path)
        if not content.startswith("# Fixture:"):
            fail(errors, f"{rel(path)} title must start with '# Fixture:'")
        for section in FIXTURE_REQUIRED_SECTIONS:
            if section not in content:
                fail(errors, f"{rel(path)} missing section {section}")
        if "- Type:" not in content:
            fail(errors, f"{rel(path)} must declare '- Type:' under Active profile")
        if "- Overlay:" not in content:
            fail(errors, f"{rel(path)} must declare '- Overlay:' under Active profile")
        if "workflow behavior" not in content.lower():
            fail(errors, f"{rel(path)} should explicitly evaluate workflow behavior")
        if "roleplay" not in content.lower():
            fail(errors, f"{rel(path)} should explicitly reject roleplay language")


def iter_repo_text_files() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.name == ".DS_Store":
            continue
        if path.suffix not in {".md", ".py", ".yml", ".yaml", ""}:
            continue
        paths.append(path)
    return paths


def check_sensitive_content(errors: list[str]) -> None:
    for path in iter_repo_text_files():
        content = text(path)
        for pattern in SENSITIVE_PATTERNS:
            for match in pattern.finditer(content):
                line = content.count("\n", 0, match.start()) + 1
                fail(errors, f"possible sensitive content in {rel(path)}:{line}: {pattern.pattern}")


def check_placeholders(errors: list[str]) -> None:
    for path in iter_repo_text_files():
        if rel(path) in ALLOW_PLACEHOLDER_FILES:
            continue
        content = text(path)
        for pattern in PLACEHOLDER_PATTERNS:
            for match in pattern.finditer(content):
                line = content.count("\n", 0, match.start()) + 1
                fail(errors, f"template placeholder in {rel(path)}:{line}: {pattern.pattern}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_skill_file(errors)
    check_type_profiles(errors)
    check_overlays(errors)
    check_behavioral_fixtures(errors)
    check_sensitive_content(errors)
    check_placeholders(errors)

    if errors:
        print("mbti-agent validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    fixture_count = len([path for path in (ROOT / "tests" / "fixtures").glob("*.md") if path.name != "README.md"])
    print("mbti-agent validation passed")
    print(f"validated {len(TYPES)} type profiles, {len(OVERLAYS)} overlays, {fixture_count} behavioral fixtures, and repository hygiene checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
