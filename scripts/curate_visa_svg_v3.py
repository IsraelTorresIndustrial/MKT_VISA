#!/usr/bin/env python3
import pathlib, json, shutil, subprocess, sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
SVG_DIR = REPO_ROOT / "assets" / "visa" / "icons" / "assets" / "visa-icons" / "svg" / "visa"
BACKUP_DIR = REPO_ROOT / "assets" / "visa" / "icons" / "full"
USAGE_REPORT = REPO_ROOT / "usage_report.json"
MANIFEST_SCRIPT = REPO_ROOT / "scripts" / "generate_visa_svg_manifest.py"

# Keywords that indicate likely useful icons
ESSENTIAL_KEYWORDS = [
    "card", "payment", "secure", "travel", "wallet", "add", "remove",
    "check", "close", "alert", "error", "info", "lock", "unlock",
    "gift", "money", "atm", "scan", "barcode", "bank", "visa",
    "logo", "pin", "chip", "cash", "refund", "credit", "debit"
]

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

def is_essential(stem: str) -> bool:
    lowered = stem.lower()
    return any(kw in lowered for kw in ESSENTIAL_KEYWORDS)

def prune_icons(usage, max_keep=120):
    # First filter by essential keywords
    candidates = []
    for path in SVG_DIR.iterdir():
        if not path.is_file() or path.suffix.lower() != ".svg":
            continue
        stem = path.stem  # e.g., account-add-high
        base = stem.rsplit("-", 1)[0] if stem.endswith(("-high", "-low", "-tiny")) else stem
        # Use usage count (fallback to 0) and essential flag
        refs = usage.get(stem, 0) or usage.get(base, 0)
        essential = is_essential(base)
        candidates.append((path, refs, essential))
    # Sort: essential first, then by usage desc
    candidates.sort(key=lambda x: (not x[2], -x[1]))
    kept = []
    for i, (path, refs, essential) in enumerate(candidates):
        if i < max_keep:
            kept.append(path)
        else:
            # Delete extra files
            rel = path.relative_to(REPO_ROOT)
            path.unlink()
            print(f"Removed {rel} (essential={essential}, refs={refs})")
    print(f"Kept {len(kept)} icons (max target {max_keep})")

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
    prune_icons(usage, max_keep=100)  # aim for ~100 icons
    regenerate_manifest()

if __name__ == "__main__":
    main()
