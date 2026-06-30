"""Validate that JSON-shaped *.include files actually parse as JSON.

Some boilerplate *.include files (computed-metadata, defaults) are JSON
documents containing [TEXT-MACROS] inside string literals. They must be valid
JSON before macro substitution, otherwise Bikeshed/Spec Generator fails with
"Error loading computed-metadata JSON" and the affected spec cannot build.

This script finds every *.include whose first non-whitespace character is "{"
and validates it as strict JSON.
"""

import json
import sys
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent.parent.parent.parent / "boilerplate-v1"
    failures = []
    checked = 0
    for path in sorted(root.rglob("*.include")):
        text = path.read_text(encoding="utf-8")
        if text.lstrip().startswith("{"):
            checked += 1
            try:
                json.loads(text)
            except json.JSONDecodeError as e:
                failures.append((path.relative_to(root.parent), e))

    print(f"Checked {checked} JSON-shaped *.include files.")
    for path, err in failures:
        print(f"::error file={path}::{err}")
    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
