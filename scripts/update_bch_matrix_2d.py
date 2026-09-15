#!/usr/bin/env python3
import pathlib, json

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
MATRIX_FILE = REPO_ROOT / "assets" / "banco_de_chile" / "BCH_LLM_ICON_DECISION_MATRIX.md"
ROOT_MATRIX_FILE = REPO_ROOT / "BCH_LLM_ICON_DECISION_MATRIX.md"
DATA_FILE = REPO_ROOT / "src" / "data" / "assets_data.js"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    text = f.read()

start = text.find("[")
end = text.rfind("]")
data = json.loads(text[start:end+1])

bch_2d = [item for item in data if item.get("bank") == "Banco de Chile" and item.get("category") == "Íconos 2D"]

section_2d = """

---

## 🎨 SUITE DE ÍCONOS 2D OFICIALES BANCO DE CHILE (30 ACTIVOS VECTORIALES/PLANOS)

Para piezas con lenguaje visual plano, ilustraciones 2D, minimalismo gráfico o compresión ultra-ligera, Banco de Chile dispone de la versión 2D oficial correspondiente a los 30 conceptos clave de medios de pago.

### 📐 Estándar Canónico de URLs CDN para Íconos 2D:
```text
https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/{carpeta}/{filename}
```

### 📋 Catálogo Completo de Íconos 2D:

| ID | Concepto / Nombre | Carpeta | Filename | URL CDN Vercel Producción |
|---|---|---|---|---|
"""

for item in sorted(bch_2d, key=lambda x: x["filename"]):
    fn = item["filename"]
    num = fn.split("_")[0] if "_" in fn else "2D"
    title = item["title"]
    rel = item["rel_path"]
    folder = rel.split("/")[-2]
    cdn = item["cdn_url"]
    section_2d += f"| **[{num}]** | {title} | `{folder}` | `{fn}` | `{cdn}` |\n"

section_2d += """
### ⚡ Regla de Selección 2D vs 3D para LLMs y Diseñadores:
- **Usar versión 3D (`assets/bch/icons/...`)**: Cuando el diseño principal use componentes 3D renderizados, degradados con volumen, tarjetas metálicas o piezas hero ricas en textura.
- **Usar versión 2D (`assets/bch/iconos_bch_2d_30/...`)**: Cuando la interfaz o email siga una guía de diseño plana (*Flat Design*), infografías sencillas, badges circulares pequeños (< 32px) o comunicaciones corporativas sobrias.
"""

with open(MATRIX_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Update headcount from 42 to 72
content = content.replace("42 Activos Digitales Oficiales", "72 Activos Digitales Oficiales (42 3D/Travel/Logos + 30 2D)")
content = content.replace("42 activos disponibles", "72 activos disponibles")
content = content.replace("42 activos verificados", "72 activos verificados")

if "SUITE DE ÍCONOS 2D OFICIALES BANCO DE CHILE" not in content:
    content += section_2d

with open(MATRIX_FILE, "w", encoding="utf-8") as f:
    f.write(content)

with open(ROOT_MATRIX_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated BCH decision matrices with 2D icon suite.")
