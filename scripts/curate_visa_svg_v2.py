#!/usr/bin/env python3
import pathlib, json, shutil, subprocess, sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
SVG_DIR = REPO_ROOT / "assets" / "visa" / "icons" / "assets" / "visa-icons" / "svg" / "visa"
BACKUP_DIR = REPO_ROOT / "assets" / "visa" / "icons" / "full"
USAGE_REPORT = REPO_ROOT / "usage_report.json"
MANIFEST_SCRIPT = REPO_ROOT / "scripts" / "generate_visa_svg_manifest.py"

def backup_svg_dir():
    if BACKUP_DIR.exists():
        shutil.rmtree(BACKUP_DIR)
    shutil.copytree(SVG_DIR, BACKUP_DIR)
    print(f"Backup created at {BACKUP_DIR}")

def load_usage():
    if not USAGE_REPORT.exists():
        print("Usage report not found", file=sys.stderr)
        sys.exit(1)
    with open(USAGE_REPORT, "r", encoding="utf-8") as f:
        return json.load(f)

def prune_icons(usage, min_refs=2):
    # Keep any icon whose base name appears at least min_refs times.
    kept = []
    total = 0
    for path in SVG_DIR.iterdir():
        if not path.is_file() or path.suffix.lower() != ".svg":
            continue
        total += 1
        stem = path.stem  # e.g., account-add-high
        # Base without suffix
        if stem.endswith("-high") or stem.endswith("-low") or stem.endswith("-tiny"):
            base = stem.rsplit("-", 1)[0]
        else:
            base = stem
        refs = usage.get(stem, 0) or usage.get(base, 0)
        if refs >= min_refs:
            kept.append(path)
        else:
            path.unlink()
            print(f"Removed {path.relative_to(REPO_ROOT)} (refs={refs})")
    print(f"Kept {len(kept)} icons out of {total} total.")

def regenerate_manifest():
    result = subprocess.run(["python3", str(MANIFEST_SCRIPT)], cwd=REPO_ROOT, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Manifest generation failed", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)
    print("Manifest regenerated with curated icons.")

def main():
    backup_svg_dir()
    usage = load_usage()
    prune_icons(usage, min_refs=2)
    regenerate_manifest()

if __name__ == "__main__":
    main()
