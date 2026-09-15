#!/usr/bin/env python3
import os, glob, json, struct, pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_FILE = REPO_ROOT / "src" / "data" / "assets_data.js"
ICONS_2D_DIR = REPO_ROOT / "assets" / "banco_de_chile" / "iconos_bch_2d_30"

def get_png_dimensions_and_size(file_path):
    stat = os.stat(file_path)
    size_bytes = stat.st_size
    size_kb = f"{size_bytes / 1024:.1f} KB"
    with open(file_path, 'rb') as f:
        data = f.read(24)
        if len(data) >= 24 and data.startswith(b'\x89PNG\r\n\x1a\n'):
            w, h = struct.unpack('>II', data[16:24])
            return w, h, size_kb, size_bytes
    return 1254, 1254, size_kb, size_bytes

FAMILY_MAP = {
    "01_medios_pago_ciclo_uso": "Medios de Pago & Ciclo de Uso",
    "02_rubros_consumo": "Rubros de Consumo",
    "03_mecanicas_crossborder_travel": "Mecánicas, Crossborder & Travel"
}

def main():
    # Load existing manifest
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    start = text.find("[")
    end = text.rfind("]")
    data = json.loads(text[start:end+1])

    # Find existing 3D BCH items to copy semantic metadata from
    bch_3d_by_number = {}
    for item in data:
        if item.get("bank") == "Banco de Chile" and item.get("category") == "Íconos 3D":
            filename = item.get("filename", "")
            if "_" in filename:
                num = filename.split("_")[0]
                bch_3d_by_number[num] = item

    # Remove any existing 2D BCH entries to avoid duplication on rerun
    data = [item for item in data if not (item.get("bank") == "Banco de Chile" and item.get("category") == "Íconos 2D")]

    new_2d_items = []
    files_2d = sorted(glob.glob(str(ICONS_2D_DIR / "**" / "*.png"), recursive=True))

    for file_path in files_2d:
        rel_path = pathlib.Path(file_path).relative_to(REPO_ROOT).as_posix()
        filename = os.path.basename(file_path)
        folder = os.path.basename(os.path.dirname(file_path))
        num = filename.split("_")[0] if "_" in filename else ""

        w, h, size_kb, size_bytes = get_png_dimensions_and_size(file_path)
        # CDN rewrite: assets/banco_de_chile/... -> assets/bch/...
        cdn_rel = rel_path.replace("assets/banco_de_chile/", "assets/bch/")
        cdn_url = f"https://mkt-visa.vercel.app/{cdn_rel}"

        ref_3d = bch_3d_by_number.get(num, {})

        title = ref_3d.get("title", filename.replace(".png", "").replace("_", " ").title())
        family = FAMILY_MAP.get(folder, ref_3d.get("family", "Iconografía 2D BCH"))
        concept = f"Versión 2D plana - {ref_3d.get('concept', 'Activo 2D oficial Banco de Chile')}"
        rubro = ref_3d.get("rubro", "General")
        rule = f"{ref_3d.get('rule', 'Usar en piezas gráficas donde se prefiera ilustración 2D.')} (Formato 2D)."
        tags = list(set((ref_3d.get("tags", []) + ["2d", "bch", "icono", "banco de chile"])))

        item = {
            "filename": filename,
            "rel_path": rel_path,
            "cdn_url": cdn_url,
            "bank": "Banco de Chile",
            "format": "PNG",
            "width": w,
            "height": h,
            "size_kb": size_kb,
            "size_bytes": size_bytes,
            "title": title,
            "category": "Íconos 2D",
            "family": family,
            "concept": concept,
            "rubro": rubro,
            "rule": rule,
            "tags": tags,
            "is_featured": False
        }
        new_2d_items.append(item)

    print(f"Generated {len(new_2d_items)} 2D BCH items.")
    data.extend(new_2d_items)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write("window.BANK_ASSETS = ")
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write(";\n")

    print("assets_data.js updated cleanly.")

if __name__ == "__main__":
    main()
