# 🧠 Banco Galicia · Matriz de Decisión Contextual para IA
> **Autor:** Israel Torres  
> **Proyecto:** MKT_VISA  
> **Ámbito:** Banco Galicia · Medios de Pago · Visa · Éminent · Quiero!  
> **Esquema de Producción:** `https://mkt-visa.vercel.app/assets/galicia/...`  
> **Estado:** **Estructura Semántica Preparada**. Activos visuales en espera de aprobación e incorporación oficial por parte del usuario.

---

## ⚡ DIRECTIVA PARA LLMs: CONVENCIÓN DE URLs PARA BANCO GALICIA

Cuando se incorporen los activos oficiales de Banco Galicia, las URLs de producción seguirán este estándar unificado:

```html
<!-- Convención estándar para Banco Galicia en Vercel CDN -->
<img src="https://mkt-visa.vercel.app/assets/galicia/icons/{filename}.png" alt="{Concepto}" width="64" height="64" />
<img src="https://mkt-visa.vercel.app/assets/galicia/logos/galicia_logo.png" alt="Banco Galicia" height="32" />
<img src="https://mkt-visa.vercel.app/assets/galicia/creatives/{banner_name}.png" alt="Banner Campaña" />
```

---

## 🎯 1. Arquetipos y Ejes de Campaña Previstos para Banco Galicia

| Eje Semántico | Concepto Principal | Triggers Clave en Prompts | Subcarpeta Destino |
|:---|:---|:---|:---|
| **Programa Quiero!** | Canje de puntos, recompensas, catálogo de beneficios | *quiero, puntos quiero, canje, catalogo, ahorro puntos* | `assets/galicia/icons/` |
| **Galicia Éminent** | Segmento preferencial, salones vip, beneficios premium | *eminent, vip, black, signature, atencion preferencial* | `assets/galicia/icons/` |
| **Medios de Pago** | Tarjeta Visa Galicia Débito / Crédito, contactless | *tarjeta galicia, visa debito, visa credito, contactless* | `assets/galicia/icons/` |
| **Pagos Digitales & MODO** | Pagos con QR, billetera digital, app Galicia, transferencias | *modo, qr, app galicia, pago movil, billetera* | `assets/galicia/icons/` |
| **Ahorro & Promociones** | Descuentos en supermercados, combustible, moda, restaurantes | *ahorro galicia, % off, cuotas sin interes, promocion* | `assets/galicia/icons/` |
| **Financiación** | Cuotas con y sin interés en comercios adheridos | *cuotas, financiacion, cuotas fijas, cuotas galicia* | `assets/galicia/icons/` |

---

## 🌳 2. Reglas de Inferencia y Prioridad Semántica

1. **Priorizar Segmento**: Si la campaña es específica de **Éminent**, el estilo y la paleta deben reflejar la identidad premium.
2. **Distinguir Descuento vs Puntos Quiero!**:
   - Descuento inmediato en el resumen/ticket ➔ Icono de Descuento/Ahorro.
   - Acumulación o multiplicador de puntos ➔ Icono Quiero!
3. **Canal de Pago**:
   - Pago con QR / MODO ➔ Icono específico de pago digital.
   - Pago físico con tarjeta física ➔ Icono de tarjeta / POS.

---

## 📋 3. Plantilla de Registro para Nuevos Activos

A medida que el usuario autorice e ingrese los activos de Banco Galicia a las carpetas `assets/galicia/icons/`, `logos/` o `creatives/`, se poblarán en esta tabla:

| ID | Nombre Archivo | Concepto | Cuándo Usar | URL CDN Vercel | Snippet HTML |
|:---|:---|:---|:---|:---|:---|
| *Pendiente* | *Por incorporar* | *Por incorporar* | *Por incorporar* | `https://mkt-visa.vercel.app/assets/galicia/...` | `<img src="..." />` |
