# 🦁 Banco Galicia · Matriz de Decisión de Iconografía & Headers para LLMs
> **Versión:** 1.0 (Producción Vercel Edge)  
> **Ámbito:** Banco Galicia · Galicia Seguros · Promociones Permanentes Visa · Pagos de Servicios · Entretenimiento  
> **Objetivo:** Instruir a Modelos de Lenguaje (LLMs) para seleccionar con 100% de precisión los íconos oficiales, headers sin texto y logotipos de Banco Galicia con sus URLs CDN canónicas.

---

## ⚡ 1. DIRECTIVA DE URLs CDN (PRODUCCIÓN VERCEL EDGE)

Todos los activos de Banco Galicia deben referenciarse exclusivamente mediante URLs absolutas con prefijo:
```text
https://mkt-visa.vercel.app/assets/galicia/...
```

- **Headers Sin Texto**: `https://mkt-visa.vercel.app/assets/galicia/headers/{filename}.png`
- **Íconos 3D**: `https://mkt-visa.vercel.app/assets/galicia/icons/{filename}.png`
- **Logotipos**: `https://mkt-visa.vercel.app/assets/galicia/logos/{filename}.png`

---

## 🖼️ 2. CATÁLOGO DE HEADERS SIN TEXTO (BANNERS HERO RETINA)

Banners de cabecera en alta resolución (1100px ancho, optimizados para rendering retina en emails de 550px / 600px).  
**Propósito:** Usar como imagen superior de cabecera limpia, permitiendo superponer o continuar con títulos dinámicos en HTML/AJO.

| Archivo | Dimensiones | URL CDN Canónica | Cuándo Usar |
|---|---|---|---|
| `header_promos_visa_permanentes_07.png` | 1100x504 | `https://mkt-visa.vercel.app/assets/galicia/headers/header_promos_visa_permanentes_07.png` | Campañas de beneficios permanentes Galicia + Visa (formato estándar alto). |
| `header_promos_visa_permanentes_08.png` | 1100x504 | `https://mkt-visa.vercel.app/assets/galicia/headers/header_promos_visa_permanentes_08.png` | Promociones destacadas con acento visual en beneficios recurrentes. |
| `header_promos_visa_permanentes_09.png` | 1100x502 | `https://mkt-visa.vercel.app/assets/galicia/headers/header_promos_visa_permanentes_09.png` | Ofertas especiales y comunicación de descuentos fijos. |
| `header_promos_visa_permanentes_10.png` | 1100x463 | `https://mkt-visa.vercel.app/assets/galicia/headers/header_promos_visa_permanentes_10.png` | Cabecera compacta cuando el correo tiene una grilla extensa de beneficios inferior. |
| `header_promos_visa_permanentes_11.png` | 1100x463 | `https://mkt-visa.vercel.app/assets/galicia/headers/header_promos_visa_permanentes_11.png` | Cabecera compacta con composición naranja/blanca para promociones de ahorro. |
| `header_promos_visa_permanentes_12.png` | 1100x463 | `https://mkt-visa.vercel.app/assets/galicia/headers/header_promos_visa_permanentes_12.png` | Cabecera compacta minimalista para avisos transaccionales o notificaciones. |

---

## 🎨 3. CATÁLOGO DE ÍCONOS BANCO GALICIA POR FAMILIA SEMÁNTICA

### 3.1 Servicios Básicos & Pagos de Cuentas
| Concepto | Archivo | URL CDN Canónica | Cuándo Usar |
|---|---|---|---|
| **Electricidad / Luz** | `luz_lampara.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/luz_lampara.png` | Facturas de Edenor, Edesur, consumo eléctrico, servicios de luz. |
| **Gas Natural** | `gas.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/gas.png` | Facturas de Metrogas, Naturgy, gas natural, garrafas, calefacción. |
| **Agua Corriente** | `canilla.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/canilla.png` | Facturas de AySA, agua potable, expensas, saneamiento. |
| **Energía / Pago Rápido** | `rayo.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/rayo.png` | Débitos automáticos express, pagos flash, energía instantánea. |
| **Internet & Wi-Fi** | `wi_fi.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/wi_fi.png` | Abonos de internet, fibra óptica, Wi-Fi del hogar, conectividad. |
| **Telefonía Móvil** | `celular.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/celular.png` | Recargas de saldo, planes móviles (Personal, Claro, Movistar), banca móvil. |

### 3.2 Galicia Seguros & Coberturas
| Concepto | Archivo | URL CDN Canónica | Cuándo Usar |
|---|---|---|---|
| **Seguro Automotor** | `seguro_auto.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/seguro_auto.png` | Pólizas de auto, asistencia mecánica en ruta, cobertura vehicular. |
| **Seguro de Hogar** | `seguro_hogar.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/seguro_hogar.png` | Pólizas de casa/depto, combinado familiar, cobertura ante robos/incendio. |
| **Seguro de Vida** | `seguro_vida.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/seguro_vida.png` | Pólizas de vida, protección familiar, respaldo económico futuro. |
| **Seguros Integral** | `seguros.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/seguros.png` | Portafolio integral de pólizas y coberturas Galicia Seguros. |
| **Protección / Imprevistos** | `paraguas.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/paraguas.png` | Respaldo ante contingencias, protección financiera, cobertura ante imprevistos. |
| **Primeros Auxilios & Salud** | `primeros_auxilios.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/primeros_auxilios.png` | Cobertura médica, asistencia al viajero, botiquín, emergencias de salud. |

### 3.3 Entretenimiento, Salidas, Cine & Espectáculos
| Concepto | Archivo Principal | Variante Alternativa | URL CDN Principal | Cuándo Usar |
|---|---|---|---|---|
| **Cine & Películas** | `cine.png` | `cine_2.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/cine.png` | Entradas al cine, 2x1 en Hoyts, Cinemark, Showcase, estrenos. |
| **Pochoclos & Candy Bar** | `pochoclos.png` | `pochoclos_2.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/pochoclos.png` | Descuentos en combos de candy bar, pochoclos, snacks de cine. |
| **Teatro & Calle Corrientes** | `teatro.png` | — | `https://mkt-visa.vercel.app/assets/galicia/icons/teatro.png` | Obras teatrales, musicales, artes escénicas en Calle Corrientes. |
| **Entradas & Tickets** | `entradas.png` | `entradas_2.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/entradas.png` | Preventas exclusivas Galicia, AllAccess, Ticketek, compra de tickets. |
| **Stand-up & Shows** | `microfono.png` | `microfono_2.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/microfono.png` | Shows de comedia, recitales, música en vivo, festivales. |
| **Auriculares & Streaming Audio** | `auriculares.png` | `auriculares_2.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/auriculares.png` | Suscripciones de música, Spotify, podcasts, audio. |

### 3.4 Identidad Institucional
| Concepto | Archivo | URL CDN Canónica | Cuándo Usar |
|---|---|---|---|
| **Logo Galicia Header** | `logo_galicia_header.png` | `https://mkt-visa.vercel.app/assets/galicia/logos/logo_galicia_header.png` | Cabecera institucional de correos de Banco Galicia (ancho sugerido: `120px` a `150px`). |

---

## 🧠 4. MATRIZ DE DESAMBIGUACIÓN (REGLAS PARA NO EQUIVOCAR EL ÍCONO)

```text
¿El beneficio es de servicios básicos?
├── ¿Electricidad / Edenor / Edesur? → luz_lampara.png
├── ¿Gas natural / Metrogas / Naturgy? → gas.png
├── ¿Agua corriente / AySA? → canilla.png
├── ¿Internet / Wi-Fi del hogar? → wi_fi.png
└── ¿Recarga de celular / abono móvil? → celular.png

¿El beneficio es de seguros o protección?
├── ¿Póliza de auto / auxilio mecánico? → seguro_auto.png
├── ¿Póliza de vivienda / combinado familiar? → seguro_hogar.png
├── ¿Póliza de vida / protección familiar? → seguro_vida.png
├── ¿Asistencia médica / emergencias de salud? → primeros_auxilios.png
├── ¿Respaldo ante imprevistos / contingencias? → paraguas.png
└── ¿Portafolio general de coberturas? → seguros.png

¿El beneficio es de entretenimiento o salidas?
├── ¿Salas de cine / 2x1 películas? → cine.png
├── ¿Snacks / candy bar / combo de cine? → pochoclos.png
├── ¿Obras de teatro / Calle Corrientes? → teatro.png
├── ¿Preventa de tickets / festivales? → entradas.png
├── ¿Shows de comedia / recitales / stand-up? → microfono.png
└── ¿Música / streaming / Spotify? → auriculares.png
```

---

## 🤖 5. PROMPT DE SISTEMA LISTO PARA LLMs (BANCO GALICIA)

```text
Eres el Selector de Iconografía y Recursos Oficiales de Banco Galicia.
Tu misión es asignar a cada beneficio, servicio o mensaje el ícono exacto de Banco Galicia o el header correspondiente, devolviendo su URL CDN de producción en Vercel.

DIRECTIVAS ESTRICTAS:
1. URL CDN OBLIGATORIA: Usa siempre el prefijo https://mkt-visa.vercel.app/assets/galicia/...
2. INSERCIÓN DE ÍCONOS: Devuelve <img src="URL" alt="Nombre" width="48" height="48" border="0" />.
3. INSERCIÓN DE HEADERS: Devuelve <img src="URL" alt="Promociones Galicia Visa" width="550" border="0" style="display:block; width:100%; max-width:550px;" />.
4. ASIGNACIÓN POR RUBRO:
   - Luz / Electricidad → luz_lampara.png
   - Gas → gas.png
   - Agua / AySA → canilla.png
   - Internet / Wi-Fi → wi_fi.png
   - Celular / Recargas → celular.png
   - Seguro Auto → seguro_auto.png
   - Seguro Hogar → seguro_hogar.png
   - Seguro Vida → seguro_vida.png
   - Seguros General → seguros.png
   - Primeros Auxilios / Salud → primeros_auxilios.png
   - Cine → cine.png
   - Candy Bar / Pochoclos → pochoclos.png
   - Teatro → teatro.png
   - Entradas / Tickets → entradas.png
   - Stand-up / Shows → microfono.png
   - Auriculares / Música → auriculares.png
   - Logo Cabecera → logo_galicia_header.png
   - Header Promos Hero → header_promos_visa_permanentes_07.png (o _10 compacto)
```
