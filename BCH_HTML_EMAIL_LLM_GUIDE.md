# 🎯 Banco de Chile · Guía de Selección de Íconos y URLs CDN para LLMs
> **Propósito:** Proveer al LLM la regla exacta para elegir el ícono correcto de Banco de Chile y la URL canónica CDN en producción para insertar en etiquetas `<img>`.

---

## ⚡ 1. DIRECTIVA DE URLs CDN (CERO RUTAS LOCALES)
Al insertar un ícono de Banco de Chile, usa SIEMPRE la URL absoluta de producción:
- **Formato estándar `<img>`**:
  ```html
  <img src="URL_CDN_VERCEL" alt="Nombre del Ícono" width="48" height="48" border="0" style="display:block; margin:0 auto;" />
  ```
- **Dominio Base CDN:** `https://mkt-visa.vercel.app/assets/bch/...`

---

## 🎨 2. REGLA DE ESTILO: ¿CUÁNDO USAR 3D VS 2D?

| Estilo | Cuándo Seleccionarlo | Prefijo de Ruta CDN |
|---|---|---|
| **Ícono 3D** | Tarjeta principal, Hero del correo, beneficio protagonista con volumen. | `https://mkt-visa.vercel.app/assets/bch/icons/{id}.png` |
| **Ícono 2D** | Grillas de 2 o 3 columnas de beneficios, bullets, elementos secundarios. | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/{carpeta}/{id}.png` |

---

## 🧠 3. DIFERENCIAS CRÍTICAS DE CONTEXTO (PARA NO EQUIVOCAR EL ÍCONO)

Aplica siempre la opción más específica:

| Contexto del Beneficio | ❌ NO USAR | ✅ USAR ÍCONO EXACTO | URL CDN 2D Recomendada |
|---|---|---|---|
| **Inteligencia Artificial / Chatbots** | `17_tecnologia.png` | **31_inteligencia_artificial.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/31_inteligencia_artificial.png` |
| **Streaming (Netflix, Spotify, Max)** | `23_pago_recurrente.png` | **32_streaming_suscripciones.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/32_streaming_suscripciones.png` |
| **Cine / Entradas a películas** | `20_entretenimiento.png` | **33_cine.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/33_cine.png` |
| **Conciertos / Recitales / Shows** | `20_entretenimiento.png` | **34_conciertos_musica_en_vivo.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/34_conciertos_musica_en_vivo.png` |
| **Moda / Vestuario / Ropa** | `16_retail_shopping.png` | **35_moda_vestuario.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/35_moda_vestuario.png` |
| **Hogar / Muebles / Decoración** | `16_retail_shopping.png` | **36_hogar.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/36_hogar.png` |
| **Mascotas / Veterinaria / Pet** | `15_farmacia_salud.png` | **37_mascotas.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/37_mascotas.png` |
| **Salud Clínica / Médicos / Consultas** | `15_farmacia_salud.png` | **38_salud_clinica_medico.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/38_salud_clinica_medico.png` |
| **Seguridad / Protección / Antifraude** | `01_tarjeta_visa.png` | **39_seguridad_proteccion.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/39_seguridad_proteccion.png` |
| **App del Banco / Autogestión** | `04_wallet_pago_movil.png` | **40_app_canal_digital.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/40_app_canal_digital.png` |
| **Pagar con Celular / Apple Pay / Billetera** | `40_app_canal_digital.png` | **04_wallet_pago_movil.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/04_wallet_pago_movil.png` |
| **Devolución de Dinero (Cashback)** | `24_descuento.png` | **09_cashback.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/09_cashback.png` |
| **Descuento Directo (% OFF)** | `09_cashback.png` | **24_descuento.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/24_descuento.png` |
| **Pago en Cuotas Sin Interés** | `01_tarjeta_visa.png` | **25_cuotas_sin_interes_csi.png** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/25_cuotas_sin_interes_csi.png` |

---

## 📋 4. CATÁLOGO COMPLETO DE ÍCONOS BANCO DE CHILE & URLs CDN

### 4.1 Medios de Pago & Ciclo de Vida (01–10)
| ID | Concepto | URL CDN 3D (Hero / Destacado) | URL CDN 2D (Grillas / Beneficios) |
|---|---|---|---|
| 01 | Tarjeta Crédito Genérica | `https://mkt-visa.vercel.app/assets/bch/icons/01_tarjeta.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/01_tarjeta_visa.png` |
| 02 | Pago Presencial POS | `https://mkt-visa.vercel.app/assets/bch/icons/02_pago_presencial_pos.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/02_pago_presencial_pos.png` |
| 03 | Ecommerce Nacional | `https://mkt-visa.vercel.app/assets/bch/icons/03_ecommerce.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/03_ecommerce.png` |
| 04 | Wallet & Pago Móvil | `https://mkt-visa.vercel.app/assets/bch/icons/04_wallet_pago_movil.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/04_wallet_pago_movil.png` |
| 05 | Activación de Tarjeta | `https://mkt-visa.vercel.app/assets/bch/icons/05_activacion.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/05_activacion.png` |
| 06 | Primera Compra / Debut | `https://mkt-visa.vercel.app/assets/bch/icons/06_primera_compra.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/06_primera_compra.png` |
| 07 | Reactivación (Inactivos) | `https://mkt-visa.vercel.app/assets/bch/icons/07_reactivacion.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/07_reactivacion.png` |
| 08 | Meta de Transacciones | `https://mkt-visa.vercel.app/assets/bch/icons/08_meta_de_transacciones.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/08_meta_de_transacciones.png` |
| 09 | Cashback / Reembolso | `https://mkt-visa.vercel.app/assets/bch/icons/09_cashback.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/09_cashback.png` |
| 10 | Dólares-Premio (DP) | `https://mkt-visa.vercel.app/assets/bch/icons/10_dolares_premio.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/10_dolares_premio.png` |

### 4.2 Rubros de Consumo (11–20)
| ID | Concepto | URL CDN 3D (Hero / Destacado) | URL CDN 2D (Grillas / Beneficios) |
|---|---|---|---|
| 11 | Supermercados | `https://mkt-visa.vercel.app/assets/bch/icons/11_supermercado.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/11_supermercado.png` |
| 12 | Gastronomía & Restaurantes | `https://mkt-visa.vercel.app/assets/bch/icons/12_gastronomia_restaurantes.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/12_gastronomia_restaurantes.png` |
| 13 | Cafeterías & Coffee | `https://mkt-visa.vercel.app/assets/bch/icons/13_cafe_cafeterias.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/13_cafe_cafeterias.png` |
| 14 | Combustible & Bencina | `https://mkt-visa.vercel.app/assets/bch/icons/14_combustible.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/14_combustible.png` |
| 15 | Farmacias & Salud | `https://mkt-visa.vercel.app/assets/bch/icons/15_farmacia_salud.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/15_farmacia_salud.png` |
| 16 | Retail & Shopping | `https://mkt-visa.vercel.app/assets/bch/icons/16_retail_shopping.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/16_retail_shopping.png` |
| 17 | Tecnología & Electro | `https://mkt-visa.vercel.app/assets/bch/icons/17_tecnologia.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/17_tecnologia.png` |
| 18 | Delivery & Apps | `https://mkt-visa.vercel.app/assets/bch/icons/18_delivery.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/18_delivery.png` |
| 19 | Viajes & Turismo | `https://mkt-visa.vercel.app/assets/bch/icons/19_viajes_turismo.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/19_viajes_turismo.png` |
| 20 | Entretenimiento Genérico | `https://mkt-visa.vercel.app/assets/bch/icons/20_entretenimiento_musica.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/20_entretenimiento_musica.png` |

### 4.3 Mecánicas & Crossborder (21–30)
| ID | Concepto | URL CDN 3D (Hero / Destacado) | URL CDN 2D (Grillas / Beneficios) |
|---|---|---|---|
| 21 | Contactless (NFC) | `https://mkt-visa.vercel.app/assets/bch/icons/21_contactless.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/21_contactless.png` |
| 22 | Card on File (Inscribir Apps) | `https://mkt-visa.vercel.app/assets/bch/icons/22_card_on_file_cof.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/22_card_on_file_cof.png` |
| 23 | Pago Recurrente / PAT | `https://mkt-visa.vercel.app/assets/bch/icons/23_pago_recurrente.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/23_pago_recurrente.png` |
| 24 | Descuento / % OFF | `https://mkt-visa.vercel.app/assets/bch/icons/24_descuento.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/24_descuento.png` |
| 25 | Cuotas Sin Interés (CSI) | `https://mkt-visa.vercel.app/assets/bch/icons/25_cuotas_sin_interes_csi.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/25_cuotas_sin_interes_csi.png` |
| 26 | Meta de Facturación | `https://mkt-visa.vercel.app/assets/bch/icons/26_meta_de_facturacion.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/26_meta_de_facturacion.png` |
| 27 | Compra Internacional Presencial | `https://mkt-visa.vercel.app/assets/bch/icons/27_compra_internacional_crossborder.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/27_compra_internacional_crossborder.png` |
| 28 | Ecommerce Internacional | `https://mkt-visa.vercel.app/assets/bch/icons/28_ecommerce_internacional.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/28_ecommerce_internacional.png` |
| 29 | Salones VIP Airport | `https://mkt-visa.vercel.app/assets/bch/icons/29_lounge_salon_vip.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/29_lounge_salon_vip.png` |
| 30 | Traslado al Aeropuerto | `https://mkt-visa.vercel.app/assets/bch/icons/30_traslado_aeropuerto.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/30_traslado_aeropuerto.png` |

### 4.4 Grupo 4 · Específicos & Innovación (2D Exclusivo 31–40)
| ID | Concepto | URL CDN 2D | Cuándo Usar |
|---|---|---|---|
| 31 | **Inteligencia Artificial** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/31_inteligencia_artificial.png` | IA, chatbots, automatización, asistentes virtuales. |
| 32 | **Streaming & Suscripciones** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/32_streaming_suscripciones.png` | Netflix, Spotify, Disney+, plataformas digitales. |
| 33 | **Cine** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/33_cine.png` | Entradas al cine, Cinemark, Cinépolis, películas. |
| 34 | **Conciertos & Música en Vivo** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/34_conciertos_musica_en_vivo.png` | Recitales, preventas exclusivas shows, festivales. |
| 35 | **Moda & Vestuario** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/35_moda_vestuario.png` | Ropa, vestuario, calzado, tiendas de moda. |
| 36 | **Hogar & Deco** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/36_hogar.png` | Muebles, casa, decoración, electrohogar, Sodimac. |
| 37 | **Mascotas** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/37_mascotas.png` | Veterinaria, pet shops, comida para mascotas. |
| 38 | **Salud Clínica & Médico** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/38_salud_clinica_medico.png` | Clínicas, médicos, consultas, centros de salud. |
| 39 | **Seguridad & Protección** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/39_seguridad_proteccion.png` | Compra segura, respaldo antifraude, validación. |
| 40 | **App Canal Digital** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/40_app_canal_digital.png` | Descarga de app Mi Banco, autogestión, consulta saldo. |

### 4.5 Logotipos Banco de Chile
- **Logo Azul (Cabecera)**: `https://mkt-visa.vercel.app/assets/bch/logos/banco_de_chile.png`
- **Isotipo Estrella Azul**: `https://mkt-visa.vercel.app/assets/bch/logos/bch_logo.png`

---

## 🤖 5. PROMPT COMPACTO PARA TU HERRAMIENTA LLM

```text
Eres el Selector de Iconografía Oficial de Banco de Chile y Visa.
Tu única función es asociar cada beneficio, rubro o mensaje al ícono exacto y devolver su URL CDN canónica de producción en Vercel.

DIRECTIVAS ESTRICTAS:
1. SIEMPRE usa URLs absolutas de producción con prefijo: https://mkt-visa.vercel.app/assets/bch/...
2. SELECCIÓN 3D VS 2D:
   - Usa versión 3D (https://mkt-visa.vercel.app/assets/bch/icons/{id}.png) para el beneficio principal / Hero.
   - Usa versión 2D (https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/{carpeta}/{id}.png) para grillas de 2 o 3 columnas de beneficios.
3. PREFERENCIA POR ESPECIFICIDAD:
   - IA / Chatbot → 31_inteligencia_artificial.png (NO 17_tecnologia)
   - Streaming → 32_streaming_suscripciones.png (NO 23_pago_recurrente)
   - Cine → 33_cine.png (NO 20_entretenimiento)
   - Conciertos / Shows → 34_conciertos_musica_en_vivo.png (NO 20_entretenimiento)
   - Moda / Ropa → 35_moda_vestuario.png (NO 16_retail)
   - Hogar / Muebles → 36_hogar.png (NO 16_retail)
   - Mascotas → 37_mascotas.png (NO 15_farmacia)
   - Salud Clínica / Médico → 38_salud_clinica_medico.png (NO 15_farmacia)
   - Seguridad / Antifraude → 39_seguridad_proteccion.png (NO 01_tarjeta)
   - App del Banco → 40_app_canal_digital.png (NO 04_wallet)
   - Pagar con celular / Wallet → 04_wallet_pago_movil.png
   - Devolución dinero → 09_cashback.png
   - Descuento % OFF → 24_descuento.png
   - Cuotas sin interés → 25_cuotas_sin_interes_csi.png
4. INSERCIÓN: Devuelve la etiqueta HTML <img src="URL" alt="Nombre" width="48" height="48" border="0" /> con la URL CDN exacta.
```
