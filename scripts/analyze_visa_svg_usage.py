#!/usr/bin/env python3
import pathlib, json, re, os

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
# Path to current SVG directory after previous curation
SVG_DIR = REPO_ROOT / "assets" / "visa" / "icons" / "assets" / "visa-icons" / "svg" / "visa"

# Directories to search for references (source code, HTML, etc.)
SEARCH_DIRS = [REPO_ROOT / "src", REPO_ROOT / "public", REPO_ROOT / "templates", REPO_ROOT]

usage = {}

# Regex to capture paths that reference a Visa SVG file
# Example: assets/visa/icons/assets/visa-icons/svg/visa/account-add-high.svg
pattern = re.compile(r"assets/visa/.+?/svg/visa/([^/]+\.svg)")

for base_dir in SEARCH_DIRS:
    for path in base_dir.rglob("*.*"):
        if path.is_file():
            try:
                text = path.read_text(errors="ignore")
            except Exception:
                continue
            for match in pattern.finditer(text):
                filename = match.group(1)
                stem = pathlib.Path(filename).stem  # e.g., account-add-high
                usage[stem] = usage.get(stem, 0) + 1

# Write report to repo root
report_path = REPO_ROOT / "usage_report.json"
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(usage, f, indent=2, ensure_ascii=False)
print(f"Usage report written to {report_path}")
