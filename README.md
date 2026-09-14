# MKT_VISA & Bank Hub

> Sistema centralizado de activos visuales multi-banco, matriz de decisión semántica, ensamblador de piezas de email marketing y exportador automático a ZIP sin montaje manual de imágenes.

Desarrollado por **Israel Torres** para centralizar la producción de campañas de medios de pago, tarjetas de crédito y piezas directivas (Banco de Chile, Visa Consulting & Analytics, Scotiabank, Santander, Itaú y Artefact).

---

## 🌟 Características Principales

1. **Biblioteca Centralizada de Activos**:
   - **Banco de Chile**: 30 íconos 3D de alta definición en PNG transparente (`01_tarjeta.png` a `30_traslado_aeropuerto.png`), 10 íconos Travel Club originales, logotipos vectoriales y arte de plásticos de tarjetas.
   - **Visa Consulting & Analytics**: Logotipos oficiales en positivo y negativo, junto con el catálogo Nova Icons System (333 íconos vectoriales).
   - **Scotiabank, Santander, Itaú & Artefact**: Logotipos oficiales y recursos de co-branding modular.
   - **Buscador Inteligente**: Filtrado instantáneo en tiempo real por banco, categoría, rubro de consumo o concepto comercial.
   - **Herramientas de Copia Rápida**: Snippets de tag HTML `<img>`, rutas relativas para código local y descarga directa.

2. **Matriz de Decisión de Íconos (BCH Icon Decision Matrix)**:
   - Basada en el documento oficial `BCH_Icon_Decision_Matrix_v1.md`.
   - Árbol de decisión interactivo: selecciona el concepto o rubro de gasto (supermercado, delivery, cuotas, salón VIP, cashback) y la interfaz destaca el ícono exacto y su justificación semántica para el brief.

3. **Armador de Piezas de Email Marketing (Builder Studio)**:
   - Ensambla correos comerciales responsivos y modulares en minutos.
   - Plantillas preconfiguradas basadas en piezas reales de producción (Bienvenida & Activación, Inactividad Temprana M1-M3, Travel Ecosistema, Cross-Border Internacional).
   - Selector visual de íconos, banners y tarjetas.
   - Previsualización dual instantánea: **Desktop (700px)** y **Mobile (375px)**.
   - Editor de código HTML en vivo con opción de copia al portapapeles.

4. **Motor de Exportación a ZIP Automatizado**:
   - **Solución al montaje manual**: Analiza todas las etiquetas `<img>` de la pieza armada o de cualquier HTML pegado.
   - Descarga y empaqueta automáticamente todas las imágenes en una carpeta `images/` dentro del ZIP.
   - Reescribe los atributos `src` en el `index.html` para que apunten a las rutas relativas locales (`images/nombre.png`).
   - Genera un archivo `.zip` listo para abrir localmente sin internet o para importar en plataformas de Email Marketing (Salesforce Marketing Cloud, Braze, Mailchimp).

---

## 📁 Estructura del Repositorio

```text
MKT_VISA/
├── index.html                   # Portal web principal y estudio interactivo
├── vercel.json                  # Configuración de despliegue, CORS y headers para Vercel
├── package.json                 # Metadatos del proyecto y scripts
├── README.md                    # Documentación técnica
├── tokens/
│   └── theme.css                # Sistema de diseño, tokens cromáticos y efectos glass
├── public/
│   └── assets/
│       ├── bch/                 # Activos Banco de Chile (30 íconos 3D, logos, banners, tarjetas)
│       │   ├── icons/           # 01_tarjeta.png ... 30_traslado_aeropuerto.png
│       │   ├── travel/          # Íconos Travel Club originals
│       │   ├── logos/           # Logotipos Banco de Chile
│       │   ├── banners/         # Hero banners de campaña
│       │   ├── cards/           # Arte de plásticos (Infinite, etc.)
│       │   └── BCH_Icon_Decision_Matrix_v1.md # Matriz de decisión en Markdown
│       ├── visa/                # Activos Visa (Logos, Nova Icons, catálogo)
│       ├── scotiabank/          # Activos Scotiabank
│       ├── santander/           # Activos Santander
│       ├── itau/                # Activos Itaú
│       └── artefact/            # Logos Artefact co-branding
└── src/
    ├── data/
    │   ├── assets_manifest.json # Base de datos indexada con metadatos
    │   └── assets_data.js       # Runtime data embebido para carga instantánea
    ├── builder/
    │   ├── templates.js         # Plantillas HTML preconfiguradas
    │   └── builder.js           # Controlador del editor visual y previsualización
    ├── exporter/
    │   └── zip_exporter.js      # Motor JSZip para empaquetado de HTML + imágenes
    └── vendor/
        └── jszip.min.js         # Librería JSZip compilada para navegador
```

---

## 🚀 Despliegue en Vercel

Este proyecto es 100% estático y no depende de ningún framework pesado ni base de datos en servidor.

Para desplegarlo en Vercel:
1. Haz push a tu repositorio en GitHub:
   ```bash
   git add .
   git commit -m "feat: Initial release of MKT_VISA Asset Hub and Email Builder"
   git push origin main
   ```
2. Conecta el repositorio en [Vercel](https://vercel.com).
3. Vercel detectará automáticamente el archivo `index.html` y desplegará la plataforma en segundos con soporte HTTPS, CDN global y compresión inmutable configurada en `vercel.json`.
