#!/usr/bin/env python3
"""Validate data/skills.yml without third-party dependencies.

The repository intentionally keeps data/skills.yml in a small YAML subset:
top-level list of mappings, scalar values, nested scalar maps, and scalar lists.
This validator parses that subset with the Python standard library only.
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "skills.yml"

CATEGORIES = {
    "workflow",
    "engineering",
    "frontend",
    "mobile",
    "database",
    "content",
    "official-reference",
    "discovery",
}

RECOMMENDATIONS = {
    "highly_recommended",
    "recommended",
    "situational",
    "reference_only",
    "caution",
}

REQUIRED_FIELDS = {
    "id",
    "name",
    "repo_url",
    "category",
    "recommendation",
    "agents",
    "install",
    "best_for",
    "avoid_when",
    "highlights",
    "cautions",
    "evidence",
    "license",
    "last_checked",
}

LIST_FIELDS = {
    "agents",
    "best_for",
    "avoid_when",
    "highlights",
    "cautions",
    "evidence",
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


class ValidationError(Exception):
    pass


def split_key_value(text: str) -> tuple[str, str | None]:
    if ":" not in text:
        raise ValidationError(f"Expected 'key: value', got: {text!r}")
    key, value = text.split(":", 1)
    key = key.strip()
    value = value.strip()
    if not key:
        raise ValidationError(f"Empty key in line: {text!r}")
    return key, value or None


def parse_scalar(value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    if value[0] in {"'", '"'}:
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError) as exc:
            raise ValidationError(f"Invalid quoted scalar: {value!r}") from exc
        if not isinstance(parsed, str):
            raise ValidationError(f"Only string scalars are supported: {value!r}")
        return parsed
    return value


def normalized_lines(path: Path) -> list[tuple[int, str, int]]:
    result: list[tuple[int, str, int]] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if "\t" in raw:
            raise ValidationError(f"Tabs are not allowed at line {line_no}")
        indent = len(raw) - len(raw.lstrip(" "))
        result.append((indent, raw.strip(), line_no))
    return result


def parse_yaml_subset(path: Path) -> list[dict[str, object]]:
    lines = normalized_lines(path)
    items: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    pending_key: str | None = None

    for indent, text, line_no in lines:
        if indent == 0 and text.startswith("- "):
            current = {}
            items.append(current)
            pending_key = None
            key, value = split_key_value(text[2:])
            current[key] = parse_scalar(value) if value is not None else ""
            continue

        if current is None:
            raise ValidationError(f"Expected top-level list item before line {line_no}")

        if indent == 2 and not text.startswith("- "):
            key, value = split_key_value(text)
            pending_key = key
            if value is None:
                current[key] = None
            else:
                current[key] = parse_scalar(value)
            continue

        if indent == 4 and text.startswith("- "):
            if pending_key is None:
                raise ValidationError(f"List item without a parent key at line {line_no}")
            if current[pending_key] is None:
                current[pending_key] = []
            if not isinstance(current[pending_key], list):
                raise ValidationError(f"Mixed container types for {pending_key!r} at line {line_no}")
            current[pending_key].append(parse_scalar(text[2:]))
            continue

        if indent == 4 and not text.startswith("- "):
            if pending_key is None:
                raise ValidationError(f"Nested mapping without a parent key at line {line_no}")
            if current[pending_key] is None:
                current[pending_key] = {}
            if not isinstance(current[pending_key], dict):
                raise ValidationError(f"Mixed container types for {pending_key!r} at line {line_no}")
            key, value = split_key_value(text)
            current[pending_key][key] = parse_scalar(value or "")
            continue

        raise ValidationError(f"Unsupported indentation or structure at line {line_no}: {text!r}")

    if not items:
        raise ValidationError("No skills found")

    return items


def is_https_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def require_nonempty_string(entry_id: str, key: str, value: object) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{entry_id}: {key} must be a non-empty string")


def require_string_list(entry_id: str, key: str, value: object) -> None:
    if not isinstance(value, list) or not value:
        raise ValidationError(f"{entry_id}: {key} must be a non-empty list")
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise ValidationError(f"{entry_id}: {key} contains an empty or non-string item")


def require_install_map(entry_id: str, value: object) -> None:
    if not isinstance(value, dict) or not value:
        raise ValidationError(f"{entry_id}: install must be a non-empty map")
    for key, command in value.items():
        if not isinstance(key, str) or not key.strip():
            raise ValidationError(f"{entry_id}: install has an empty key")
        if not isinstance(command, str) or not command.strip():
            raise ValidationError(f"{entry_id}: install.{key} must be a non-empty string")


def validate(entries: list[dict[str, object]]) -> None:
    seen: set[str] = set()

    for entry in entries:
        missing = REQUIRED_FIELDS - set(entry)
        if missing:
            raw_id = entry.get("id", "<missing id>")
            raise ValidationError(f"{raw_id}: missing fields: {', '.join(sorted(missing))}")

        entry_id = entry["id"]
        require_nonempty_string(str(entry_id), "id", entry_id)
        assert isinstance(entry_id, str)

        if not ID_RE.match(entry_id):
            raise ValidationError(f"{entry_id}: id must be lowercase kebab-case")
        if entry_id in seen:
            raise ValidationError(f"{entry_id}: duplicate id")
        seen.add(entry_id)

        for key in ("name", "repo_url", "category", "recommendation", "license", "last_checked"):
            require_nonempty_string(entry_id, key, entry[key])

        if entry["category"] not in CATEGORIES:
            raise ValidationError(f"{entry_id}: invalid category {entry['category']!r}")
        if entry["recommendation"] not in RECOMMENDATIONS:
            raise ValidationError(f"{entry_id}: invalid recommendation {entry['recommendation']!r}")
        if not is_https_url(entry["repo_url"]):
            raise ValidationError(f"{entry_id}: repo_url must be an https URL")
        if not DATE_RE.match(str(entry["last_checked"])):
            raise ValidationError(f"{entry_id}: last_checked must be YYYY-MM-DD")

        for key in LIST_FIELDS:
            require_string_list(entry_id, key, entry[key])

        require_install_map(entry_id, entry["install"])


def main() -> int:
    try:
        entries = parse_yaml_subset(DATA_FILE)
        validate(entries)
    except (OSError, ValidationError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1

    categories = sorted({str(entry["category"]) for entry in entries})
    print(f"Validated {len(entries)} skills across {len(categories)} categories.")
    print("Categories: " + ", ".join(categories))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
