#!/usr/bin/env python3
import os, json, pathlib

# Paths (relative to repository root)
REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
ASSETS_ROOT = REPO_ROOT / "assets" / "visa"
SVG_DIR = ASSETS_ROOT / "icons" / "assets" / "visa-icons" / "svg" / "visa"
MANIFEST_FILE = REPO_ROOT / "src" / "data" / "assets_data.js"

def load_manifest():
    """Load the existing BANK_ASSETS array from assets_data.js.
    Returns the list, plus the prefix and suffix strings so we can write back preserving surrounding code.
    """
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    # Find the start of the JSON array after the assignment
    start_idx = content.find("[")
    end_idx = content.rfind("]")
    if start_idx == -1 or end_idx == -1:
        raise RuntimeError("Could not locate JSON array in assets_data.js")
    prefix = content[:start_idx]
    suffix = content[end_idx+1:]
    array_text = content[start_idx:end_idx+1]
    # Use json.loads after fixing potential trailing commas
    data = json.loads(array_text)
    return data, prefix, suffix

def save_manifest(data, prefix, suffix):
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        f.write(prefix)
        f.write("\nwindow.BANK_ASSETS = ")
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write(suffix)

def make_entry(rel_path: str) -> dict:
    filename = os.path.basename(rel_path)
    # Build CDN URL – Vercel serves from the same path
    cdn_url = f"https://mkt-visa.vercel.app/{rel_path}"
    title = os.path.splitext(filename)[0].replace("_", " ").title()
    return {
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

def main():
    assets, prefix, suffix = load_manifest()
    existing_paths = {item["rel_path"] for item in assets}
    new_entries = []
    for root, _, files in os.walk(SVG_DIR):
        for f in files:
            if f.lower().endswith('.svg'):
                full_path = pathlib.Path(root) / f
                rel_path = str(full_path.relative_to(REPO_ROOT).as_posix())
                if rel_path not in existing_paths:
                    new_entries.append(make_entry(rel_path))
    if new_entries:
        assets.extend(new_entries)
        # Optionally sort alphabetically by filename
        assets.sort(key=lambda x: x["filename"].lower())
        save_manifest(assets, prefix, suffix)
        print(f"Added {len(new_entries)} SVG entries to assets_data.js")
    else:
        print("No new SVG assets to add.")

if __name__ == "__main__":
    main()
