# ✉️ Banco de Chile · Guía Maestra para Generación de Emails HTML con IA & LLMs
> **Versión:** 2.0 (Compatible con Email Maker Engine / Adobe AJO / SFMC / Mailchimp / HTML Headless)  
> **Ámbito:** Banco de Chile · Medios de Pago · Tarjetas de Crédito y Débito · Visa · Travel Club  
> **Objetivo:** Instruir a Modelos de Lenguaje (LLMs) para diseñar, maquetar y seleccionar la iconografía exacta de Banco de Chile en correos electrónicos HTML 100% responsivos y compatibles con Outlook, Gmail, Apple Mail y clientes corporativos.

---

## ⚡ 1. DIRECTIVAS TÉCNICAS MANDATORIAS PARA EMAILS HTML

Cualquier LLM o agente que genere código HTML de correos para Banco de Chile DEBE cumplir estrictamente estas reglas:

### 1.1 Estructura Table-Based Bulletproof (Cero CSS Flexbox/Grid)
- Todo el layout DEBE construirse con tablas HTML: `<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%">`.
- Ancho estándar del contenedor principal: `600px` (o `640px` máx.), centrado con `align="center"` y `style="margin:0 auto; max-width:600px; width:100%;"`.
- Nunca usar `<div>` para estructura de columnas, `flexbox`, `css grid`, ni variables CSS (`var(--...)`). Los clientes como Outlook 2016/2019/365 los destruyen.

### 1.2 Regla de Inserción de Íconos en Email
- **Tamaño estándar para grillas de beneficios**: `width="48" height="48"` (o `width="40" height="40"` en móviles / 3 columnas).
- **Tamaño para Hero / Beneficio Principal**: `width="64" height="64"` o `width="80" height="80"`.
- **Atributos obligatorios en cada `<img>`**:
  ```html
  <img src="https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/11_supermercado.png" 
       alt="Supermercado" 
       width="48" 
       height="48" 
       border="0" 
       style="display:block; border:0; outline:none; text-decoration:none; -ms-interpolation-mode:bicubic; margin:0 auto;" />
  ```
- **CDN Canónica**: NUNCA usar rutas locales ni relativas (`assets/...`, `./icons/...`). SIEMPRE usar URLs absolutas en `https://mkt-visa.vercel.app/assets/bch/...`.

---

## 🎨 2. MATRIZ DE DECISIÓN: ¿CUÁNDO USAR ÍCONOS 3D VS 2D EN EMAILS?

Banco de Chile cuenta con 30 conceptos en versión 3D y 40 conceptos en versión 2D. Aplica este criterio:

| Escenario en el Email | Versión Recomendada | Ruta CDN / Carpeta | Justificación Técnica |
|---|---|---|---|
| **Hero Card / Beneficio Central** | **Ícono 3D** | `https://mkt-visa.vercel.app/assets/bch/icons/...` | Alto impacto visual, volumen y textura premium sobre fondos degradados azules `#002464` o tarjetas destacadas. |
| **Grilla de 2 Columnas de Beneficios** | **Ícono 2D** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/...` | Carga ultra-liviana, claridad visual en pantallas pequeñas y lectura inmediata. |
| **Grilla de 3 Columnas de Rubros** | **Ícono 2D** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/...` | Máxima nitidez a 40x40px sin ruido visual ni artefactos de compresión. |
| **Innovación / Canales / Específicos (31-40)** | **Ícono 2D (Grupo 4)** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/...` | Iconografía específica (IA, Streaming, Cine, Conciertos, Moda, Hogar, Mascotas, Salud, Seguridad, App). |
| **Campaña Travel Club / Vuelos** | **Travel Suite** | `https://mkt-visa.vercel.app/assets/bch/travel/...` | Gráficos oficiales del programa de fidelidad Travel Club. |

---

## 📋 3. CATÁLOGO COMPLETO DE URLs CDN PARA EMAILS

### 3.1 Medios de Pago & Ciclo de Uso (01–10)
| ID | Concepto | URL CDN 3D | URL CDN 2D | Regla Semántica |
|---|---|---|---|---|
| 01 | **Tarjeta de Crédito** | `https://mkt-visa.vercel.app/assets/bch/icons/01_tarjeta.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/01_tarjeta_visa.png` | Explicación del portafolio o medio de pago genérico. |
| 02 | **Pago Presencial POS** | `https://mkt-visa.vercel.app/assets/bch/icons/02_pago_presencial_pos.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/02_pago_presencial_pos.png` | Compras en comercio físico con máquina POS. |
| 03 | **Ecommerce Nacional** | `https://mkt-visa.vercel.app/assets/bch/icons/03_ecommerce.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/03_ecommerce.png` | Compras online en comercios locales de Chile. |
| 04 | **Wallet & Pago Móvil** | `https://mkt-visa.vercel.app/assets/bch/icons/04_wallet_pago_movil.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/04_wallet_pago_movil.png` | Pagar con Apple Pay, Google Wallet o Garmin Pay. (Si es entrar a la app usar 40). |
| 05 | **Activación de Tarjeta** | `https://mkt-visa.vercel.app/assets/bch/icons/05_activacion.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/05_activacion.png` | Bienvenida, desbloqueo y encendido de nueva tarjeta. |
| 06 | **Primera Compra** | `https://mkt-visa.vercel.app/assets/bch/icons/06_primera_compra.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/06_primera_compra.png` | Incentivo a realizar la primera compra o debut transaccional. |
| 07 | **Reactivación** | `https://mkt-visa.vercel.app/assets/bch/icons/07_reactivacion.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/07_reactivacion.png` | Campañas de retención para clientes inactivos (M1, M2, M3). |
| 08 | **Meta de Transacciones** | `https://mkt-visa.vercel.app/assets/bch/icons/08_meta_de_transacciones.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/08_meta_de_transacciones.png` | Condición de campaña por N° de compras (ej. 'haz 3 compras'). |
| 09 | **Cashback / Devolución** | `https://mkt-visa.vercel.app/assets/bch/icons/09_cashback.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/09_cashback.png` | Reembolso o abono directo en dinero a la cuenta/tarjeta. |
| 10 | **Dólares-Premio (DP)** | `https://mkt-visa.vercel.app/assets/bch/icons/10_dolares_premio.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/10_dolares_premio.png` | Acumulación o canje en el programa Travel Club. |

### 3.2 Rubros de Consumo (11–20)
| ID | Concepto | URL CDN 3D | URL CDN 2D | Regla Semántica |
|---|---|---|---|---|
| 11 | **Supermercados** | `https://mkt-visa.vercel.app/assets/bch/icons/11_supermercado.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/11_supermercado.png` | Descuentos en Jumbo, Lider, Santa Isabel, Unimarc. |
| 12 | **Gastronomía & Rest.** | `https://mkt-visa.vercel.app/assets/bch/icons/12_gastronomia_restaurantes.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/12_gastronomia_restaurantes.png` | Restaurantes, salidas a comer, sabores, delivery gourmet. |
| 13 | **Cafeterías & Coffee** | `https://mkt-visa.vercel.app/assets/bch/icons/13_cafe_cafeterias.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/13_cafe_cafeterias.png` | Starbucks, Dunkin', Juan Valdez, pastelerías. |
| 14 | **Combustible & Bencina** | `https://mkt-visa.vercel.app/assets/bch/icons/14_combustible.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/14_combustible.png` | Rebaja por litro en Shell, Copec, Petrobras. |
| 15 | **Farmacias & Salud** | `https://mkt-visa.vercel.app/assets/bch/icons/15_farmacia_salud.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/15_farmacia_salud.png` | Medicamentos y farmacias (Cruz Verde, Salcobrand). |
| 16 | **Retail & Shopping** | `https://mkt-visa.vercel.app/assets/bch/icons/16_retail_shopping.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/16_retail_shopping.png` | Tiendas por departamento y centros comerciales. |
| 17 | **Tecnología & Electro** | `https://mkt-visa.vercel.app/assets/bch/icons/17_tecnologia.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/17_tecnologia.png` | Hardware, smartphones, computadores. (Para IA usar 31). |
| 18 | **Delivery & Apps** | `https://mkt-visa.vercel.app/assets/bch/icons/18_delivery.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/18_delivery.png` | PedidosYa, Uber Eats, Rappi. |
| 19 | **Viajes & Turismo** | `https://mkt-visa.vercel.app/assets/bch/icons/19_viajes_turismo.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/19_viajes_turismo.png` | Pasajes aéreos, hoteles y paquetes turísticos. |
| 20 | **Entretenimiento Genérico** | `https://mkt-visa.vercel.app/assets/bch/icons/20_entretenimiento_musica.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/20_entretenimiento_musica.png` | Panoramas amplios. (Para cine usar 33, conciertos usar 34). |

### 3.3 Mecánicas, Crossborder & Travel (21–30)
| ID | Concepto | URL CDN 3D | URL CDN 2D | Regla Semántica |
|---|---|---|---|---|
| 21 | **Contactless** | `https://mkt-visa.vercel.app/assets/bch/icons/21_contactless.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/21_contactless.png` | Pagar acercando la tarjeta o reloj (NFC). |
| 22 | **Card on File (COF)** | `https://mkt-visa.vercel.app/assets/bch/icons/22_card_on_file_cof.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/22_card_on_file_cof.png` | Inscribir tarjeta en Uber, Spotify, Netflix, Mercado Libre. |
| 23 | **Pago Recurrente / PAT** | `https://mkt-visa.vercel.app/assets/bch/icons/23_pago_recurrente.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/23_pago_recurrente.png` | Pago automático mensual de cuentas (agua, luz, autopistas). |
| 24 | **Descuento / % OFF** | `https://mkt-visa.vercel.app/assets/bch/icons/24_descuento.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/24_descuento.png` | Beneficio expresado en % de rebaja directa. |
| 25 | **Cuotas Sin Interés (CSI)** | `https://mkt-visa.vercel.app/assets/bch/icons/25_cuotas_sin_interes_csi.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/25_cuotas_sin_interes_csi.png` | Financiamiento en 3, 6, 12 o 24 cuotas a tasa 0%. |
| 26 | **Meta de Facturación** | `https://mkt-visa.vercel.app/assets/bch/icons/26_meta_de_facturacion.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/26_meta_de_facturacion.png` | Condición por monto de gasto acumulado (ej. '$200.000'). |
| 27 | **Compra Internacional** | `https://mkt-visa.vercel.app/assets/bch/icons/27_compra_internacional_crossborder.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/27_compra_internacional_crossborder.png` | Compras presenciales en el extranjero. |
| 28 | **Ecommerce Internacional** | `https://mkt-visa.vercel.app/assets/bch/icons/28_ecommerce_internacional.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/28_ecommerce_internacional.png` | Amazon, AliExpress, Shein, eBay o servicios en dólares. |
| 29 | **Salones VIP Pacific** | `https://mkt-visa.vercel.app/assets/bch/icons/29_lounge_salon_vip.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/29_lounge_salon_vip.png` | Acceso a salones VIP Lounge en aeropuertos. |
| 30 | **Traslado Aeropuerto** | `https://mkt-visa.vercel.app/assets/bch/icons/30_traslado_aeropuerto.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/30_traslado_aeropuerto.png` | Transfer / traslado al aeropuerto en planes Travel. |

### 3.4 Grupo 4 · Contextos Específicos & Innovación (2D Exclusivo 31–40)
| ID | Concepto | URL CDN 2D | Cuándo Usar en Email |
|---|---|---|---|
| 31 | **Inteligencia Artificial** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/31_inteligencia_artificial.png` | Novedades de IA, chatbots, asistentes inteligentes, recomendaciones AI. |
| 32 | **Streaming & Suscripciones** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/32_streaming_suscripciones.png` | Promociones en Netflix, Spotify, Disney+, Max, YouTube Premium. |
| 33 | **Cine** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/33_cine.png` | Entradas al cine, Cinemark, CineHoyts/Cinépolis, estrenos de cartelera. |
| 34 | **Conciertos & Música en Vivo** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/34_conciertos_musica_en_vivo.png` | Preventas exclusivas de conciertos, festivales (Lollapalooza) y recitales. |
| 35 | **Moda & Vestuario** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/35_moda_vestuario.png` | Descuentos específicos en ropa, vestuario, calzado, fashion retail. |
| 36 | **Hogar & Deco** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/36_hogar.png` | Muebles, decoración, línea blanca, mejoramiento del hogar (Sodimac, Easy). |
| 37 | **Mascotas** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/37_mascotas.png` | Alimento, veterinarias, pet shops y cuidado animal. |
| 38 | **Salud Clínica & Médico** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/38_salud_clinica_medico.png` | Consultas médicas, exámenes, clínicas y centros de salud privados. |
| 39 | **Seguridad & Protección** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/39_seguridad_proteccion.png` | Bloques de compra protegida, seguro antifraude, validación de transacciones. |
| 40 | **App Canal Digital** | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/40_app_canal_digital.png` | Descarga de app Mi Banco, autogestión, consulta de saldo, activación digital. |

### 3.5 Logotipos Institucionales Banco de Chile
- **Logo Wordmark Azul (Header Principal)**:  
  `https://mkt-visa.vercel.app/assets/bch/logos/banco_de_chile.png` (`width="140"` recomendado)
- **Isotipo Estrella Azul (Favicon / Footer / Badge)**:  
  `https://mkt-visa.vercel.app/assets/bch/logos/bch_logo.png` (`width="32"` recomendado)

---

## 🧱 4. COMPONENTES HTML DE EMAIL LISTOS PARA COPIAR (BULLETPROOF)

### Componente A: Header Institucional con Logo
```html
<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#002464;">
  <tr>
    <td align="center" style="padding:24px 20px;">
      <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="max-width:600px; width:100%;">
        <tr>
          <td align="left" valign="middle">
            <img src="https://mkt-visa.vercel.app/assets/bch/logos/banco_de_chile.png" alt="Banco de Chile" width="140" height="auto" border="0" style="display:block; border:0; outline:none; text-decoration:none;" />
          </td>
          <td align="right" valign="middle" style="font-family:'Arial', Helvetica, sans-serif; font-size:12px; color:#FFFFFF; opacity:0.85;">
            Medios de Pago · Visa
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

### Componente B: Grilla de 2 Columnas de Beneficios (Responsiva Table-Based)
```html
<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#F8FAFC; padding:32px 0;">
  <tr>
    <td align="center">
      <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="max-width:600px; width:100%;">
        <tr>
          <!-- Columna 1 -->
          <td width="288" valign="top" style="padding:0 8px 16px 0;">
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#FFFFFF; border:1px solid #E2E8F0; border-radius:12px; padding:20px; text-align:center;">
              <tr>
                <td align="center" style="padding-bottom:12px;">
                  <img src="https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/11_supermercado.png" alt="Supermercados" width="48" height="48" border="0" style="display:block; margin:0 auto;" />
                </td>
              </tr>
              <tr>
                <td align="center" style="font-family:'Arial', Helvetica, sans-serif; font-size:18px; font-weight:bold; color:#002464; padding-bottom:4px;">
                  Hasta 30% OFF
                </td>
              </tr>
              <tr>
                <td align="center" style="font-family:'Arial', Helvetica, sans-serif; font-size:13px; color:#475569; line-height:1.4;">
                  En supermercados adheridos pagando con tus tarjetas Banco de Chile.
                </td>
              </tr>
            </table>
          </td>
          <!-- Columna 2 -->
          <td width="288" valign="top" style="padding:0 0 16px 8px;">
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#FFFFFF; border:1px solid #E2E8F0; border-radius:12px; padding:20px; text-align:center;">
              <tr>
                <td align="center" style="padding-bottom:12px;">
                  <img src="https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/14_combustible.png" alt="Combustible" width="48" height="48" border="0" style="display:block; margin:0 auto;" />
                </td>
              </tr>
              <tr>
                <td align="center" style="font-family:'Arial', Helvetica, sans-serif; font-size:18px; font-weight:bold; color:#002464; padding-bottom:4px;">
                  $100 dcto / litro
                </td>
              </tr>
              <tr>
                <td align="center" style="font-family:'Arial', Helvetica, sans-serif; font-size:13px; color:#475569; line-height:1.4;">
                  Todos los jueves en estaciones de servicio Shell y Copec con Mi Pago.
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

### Componente C: Botón CTA Bulletproof (Compatible con Outlook)
```html
<table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center" style="margin:24px auto;">
  <tr>
    <td align="center" bgcolor="#0032A0" style="border-radius:24px;">
      <a href="https://portales.bancochile.cl/beneficios" target="_blank" style="font-family:'Arial', Helvetica, sans-serif; font-size:14px; font-weight:bold; color:#FFFFFF; text-decoration:none; display:inline-block; padding:14px 32px; border-radius:24px; border:1px solid #0032A0;">
        Conoce Todos los Beneficios →
      </a>
    </td>
  </tr>
</table>
```

---

## 🤖 5. PROMPT DE SISTEMA LISTO PARA INYECTAR EN AGENTES & HERRAMIENTAS LLM

```text
Eres el Diseñador Experto de Emails HTML para Banco de Chile y Visa.
Tu misión es generar correos electrónicos en HTML puro, 100% responsivos y table-based, seleccionando con máxima precisión los íconos oficiales de Banco de Chile y aplicando el estándar corporativo.

REGLAS OBLIGATORIAS:
1. ARQUITECTURA HTML: Usa exclusivamente tablas HTML (<table role="presentation">) con ancho máximo de 600px. Cero Flexbox, cero Grid, cero CSS externo.
2. ICONOGRAFÍA CANÓNICA: Utiliza siempre URLs absolutas con prefijo https://mkt-visa.vercel.app/assets/bch/...
3. SELECCIÓN 3D VS 2D:
   - Usa 3D (assets/bch/icons/{id}.png) para el beneficio Hero destacado.
   - Usa 2D (assets/bch/iconos_bch_2d_30/{carpeta}/{id}.png) para grillas de 2 o 3 columnas de beneficios y listas.
4. DIFERENCIAS SEMÁNTICAS CRÍTICAS:
   - Para Inteligencia Artificial: usa 31_inteligencia_artificial.png (NO 17_tecnologia).
   - Para Streaming (Netflix, Spotify): usa 32_streaming_suscripciones.png (NO 23_pago_recurrente).
   - Para Cine: usa 33_cine.png (NO 20_entretenimiento).
   - Para Conciertos/Preventas: usa 34_conciertos_musica_en_vivo.png (NO 20_entretenimiento).
   - Para Moda/Ropa: usa 35_moda_vestuario.png (NO 16_retail).
   - Para Hogar/Muebles: usa 36_hogar.png (NO 16_retail).
   - Para Mascotas/Veterinaria: usa 37_mascotas.png (NO 15_farmacia).
   - Para Salud Clínica/Médica: usa 38_salud_clinica_medico.png (NO 15_farmacia).
   - Para Seguridad/Antifraude: usa 39_seguridad_proteccion.png (NO 01_tarjeta).
   - Para App del Banco/Autogestión: usa 40_app_canal_digital.png (NO 04_wallet).
5. FORMATO DE IMAGEN EN EMAIL: Cada <img> debe incluir width="48" height="48" border="0" style="display:block; margin:0 auto; border:0; outline:none;".
6. PALETA INSTITUCIONAL:
   - Azul Marino Principal: #002464
   - Azul Primario BCH: #0032A0
   - Fondo de Pieza: #F8FAFC
   - Card Background: #FFFFFF (borde #E2E8F0)
   - Texto Principal: #0F172A
   - Texto Secundario: #475569
```
