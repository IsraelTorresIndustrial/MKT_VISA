#!/usr/bin/env python3
import os, shutil, json, pathlib

# Paths
REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
SVG_DIR = REPO_ROOT / "assets" / "visa" / "icons" / "assets" / "visa-icons" / "svg" / "visa"
BACKUP_DIR = REPO_ROOT / "assets" / "visa" / "icons" / "full"
MANIFEST_FILE = REPO_ROOT / "src" / "data" / "assets_data.js"

def backup_all():
    """Copy the entire SVG directory to a backup location (git‑tracked)."""
    if BACKUP_DIR.exists():
        shutil.rmtree(BACKUP_DIR)
    shutil.copytree(SVG_DIR, BACKUP_DIR)
    print(f"Backup of all SVGs created at {BACKUP_DIR}")

def select_icons():
    """Return a set of file paths (relative to repo root) that we will keep.
    Preference: *-high.svg, otherwise the smallest file among the remaining.
    """
    kept = set()
    # Group by base name (remove suffix and extension)
    groups = {}
    for entry in SVG_DIR.iterdir():
        if entry.is_file() and entry.suffix.lower() == ".svg":
            name = entry.stem  # e.g., "account-add-high"
            # Split off the suffix (-high, -low, -tiny)
            if name.endswith("-high") or name.endswith("-low") or name.endswith("-tiny"):
                base = name.rsplit("-", 1)[0]
                groups.setdefault(base, []).append(entry)
    for base, files in groups.items():
        # Look for a *-high.svg first
        high = [f for f in files if f.stem.endswith("-high")]
        if high:
            kept.add(high[0].relative_to(REPO_ROOT).as_posix())
            continue
        # If no high, pick the smallest file (by size)
        smallest = min(files, key=lambda p: p.stat().st_size)
        kept.add(smallest.relative_to(REPO_ROOT).as_posix())
    return kept

def prune_files(kept_set):
    """Delete any SVG files not in kept_set from the repo (they remain in backup)."""
    for entry in SVG_DIR.iterdir():
        if entry.is_file() and entry.suffix.lower() == ".svg":
            rel = entry.relative_to(REPO_ROOT).as_posix()
            if rel not in kept_set:
                entry.unlink()
                print(f"Removed {rel}")

def generate_manifest(kept_set):
    """Create or replace Visa entries in assets_data.js based on kept SVGs."""
    # Load existing manifest
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    start_idx = content.find("[")
    end_idx = content.rfind("]")
    prefix = content[:start_idx]
    suffix = content[end_idx+1:]
    data = json.loads(content[start_idx:end_idx+1])
    # Remove existing Visa entries
    data = [item for item in data if item.get("bank") != "Visa"]
    # Add new entries for kept SVGs
    for rel_path in sorted(kept_set):
        filename = os.path.basename(rel_path)
        cdn_url = f"https://mkt-visa.vercel.app/{rel_path}"
        title = os.path.splitext(filename)[0].replace("_", " ").title()
        entry = {
            "filename": filename,
            "rel_path": rel_path,
            "cdn_url": cdn_url,
            "bank": "Visa",
            "format": "SVG",
            "title": title,
            "category": "Iconos SVG",
            "family": "Visa Icon Set",
            "concept": "Recurso vectorial Visa",
            "rubro": "Branding",
            "rule": "Icono oficial Visa en formato escalable.",
            "tags": ["visa", "svg", filename.split(".")[0]],
            "is_featured": False
        }
        data.append(entry)
    # Write back
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        f.write(prefix)
        f.write("\nwindow.BANK_ASSETS = ")
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write(suffix)
    print("Manifest updated with curated Visa SVG entries")

def main():
    backup_all()
    kept = select_icons()
    prune_files(kept)
    generate_manifest(kept)
    print(f"Curated {len(kept)} SVG icons")

if __name__ == "__main__":
    main()
