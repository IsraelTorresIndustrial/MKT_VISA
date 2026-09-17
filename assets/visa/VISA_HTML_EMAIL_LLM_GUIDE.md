# ✉️ Visa · Guía Maestra para Generación de Emails HTML con IA & LLMs
> **Versión:** 2.0 (Compatible con Email Maker Engine / Adobe AJO / SFMC / Mailchimp / HTML Headless)  
> **Ámbito:** Visa Official Brand Standards · Medios de Pago · Co-Branding Bancario · Cross-Border  
> **Objetivo:** Instruir a Modelos de Lenguaje (LLMs) para diseñar y maquetar correos electrónicos HTML para campañas Visa y co-branded con bancos, utilizando los 158 íconos SVG/PNG oficiales y la paleta de marca Visa 2025.

---

## ⚡ 1. DIRECTIVAS TÉCNICAS MANDATORIAS PARA EMAILS VISA

### 1.1 Soporte de Formatos (SVG vs PNG en Email)
- Los íconos oficiales de Visa en este Hub son archivos SVG vectoriales de alta precisión (variantes `-high.svg`).
- **Clientes modernos** (iOS Mail, Apple Mail, Webmail modernos) soportan SVG nativo vía `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/{name}-high.svg" width="40" height="40">`.
- **Outlook Desktop (Windows)** no renderiza SVG directamente. En campañas masivas que requieran compatibilidad legacy con Outlook 2016/2019, usar atributos explícitos `width` y `height`, o renderizar con fallback.

### 1.2 Paleta Oficial Visa para Emails
- **Visa Navy**: `#021E4C` (Fondos de cabeceras, títulos principales).
- **Visa Classic Blue**: `#1434CB` (Botones primarios, enlaces y acentos).
- **Visa Gold / Amber**: `#FCC015` / `#F7A105` (Badges de beneficios, estrellas, recompensas).
- **Surface Light**: `#F4F6FE` (Fondos de cards de beneficios).

---

## 📋 2. CATÁLOGO DE ÍCONOS VISA POR FAMILIA SEMÁNTICA (CDN URLs)

URL Canónica Base: `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/{filename}`

### 2.1 Pagos & Tarjetas
- Tarjeta Genérica: `.../card-generic-high.svg`
- Tarjeta Débito: `.../card-debit-high.svg`
- Tarjeta Corporativa: `.../card-corporate-high.svg`
- Tarjeta Prepago: `.../card-prepaid-high.svg`
- Contactless / Tap to Pay: `.../tap-high.svg`
- POS Terminal: `.../pos-high.svg`
- Código QR: `.../qr-high.svg`
- Escaneo de Tarjeta: `.../scan-card-high.svg`

### 2.2 Transacciones & Dinero
- Transferencia Móvil: `.../mobile-transfer-high.svg`
- Envío de Dinero: `.../money-send-high.svg`
- Solicitud de Dinero: `.../money-request-high.svg`
- Balance / Saldo: `.../balance-high.svg`
- Recibo / Comprobante: `.../receipt-high.svg`
- Devolución / Reembolso: `.../return-high.svg`
- Dividir Cuenta (Split): `.../split-high.svg`
- Pago Rápido: `.../fast-high.svg`

### 2.3 Seguridad & Autenticación
- Protección / Escudo: `.../security-protection-high.svg`
- Candado de Seguridad: `.../security-lock-high.svg`
- Detección de Fraude: `.../fraud-high.svg`
- Biometría Huella: `.../fingerprint-high.svg`
- Biometría Facial: `.../auth-face-high.svg`
- Código de Autorización: `.../auth-code-high.svg`
- Token de Pago: `.../token-high.svg`
- Dispositivo Seguro: `.../device-secure-high.svg`

### 2.4 Viajes & Cross-Border
- Check Internacional: `.../check-international-high.svg`
- Cobertura Global: `.../global-high.svg`
- Tránsito Avión: `.../transit-airplane-high.svg`
- Notificaciones de Viaje: `.../travel-notifications-high.svg`
- Mapa & Ubicación: `.../map-location-high.svg`

### 2.5 Comercio & Ofertas
- Ofertas & Deals: `.../offers-deal-high.svg`
- Recompensas / Reward: `.../reward-high.svg`
- Puntos Bonus: `.../bonus-points-high.svg`
- Carrito de Compras: `.../cart-high.svg`
- Regalo / Gift: `.../gift-high.svg`
- Tienda Abierta: `.../store-open-high.svg`
- Envíos / Shipping: `.../shipping-high.svg`

---

## 🧱 3. COMPONENTE HTML DE EMAIL VISA CO-BRANDED

```html
<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color:#021E4C; padding:28px 0;">
  <tr>
    <td align="center">
      <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="600" style="max-width:600px; width:100%; padding:0 20px;">
        <tr>
          <td align="center" style="padding-bottom:16px;">
            <img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/tap-high.svg" alt="Visa Tap to Pay" width="64" height="64" border="0" style="display:block; margin:0 auto;" />
          </td>
        </tr>
        <tr>
          <td align="center" style="font-family:'Arial', Helvetica, sans-serif; font-size:24px; font-weight:bold; color:#FFFFFF; padding-bottom:8px;">
            Paga Rápido y Seguro con Visa Sin Contacto
          </td>
        </tr>
        <tr>
          <td align="center" style="font-family:'Arial', Helvetica, sans-serif; font-size:14px; color:#E2E8F0; line-height:1.5; padding-bottom:24px;">
            Acerca tu tarjeta o billetera digital al terminal POS y completa tus compras al instante con la protección global de Visa.
          </td>
        </tr>
        <tr>
          <td align="center">
            <table role="presentation" border="0" cellpadding="0" cellspacing="0">
              <tr>
                <td align="center" bgcolor="#1434CB" style="border-radius:24px;">
                  <a href="#" style="font-family:'Arial', Helvetica, sans-serif; font-size:14px; font-weight:bold; color:#FFFFFF; text-decoration:none; display:inline-block; padding:14px 32px; border-radius:24px;">
                    Ver Comercios Adheridos →
                  </a>
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

---

## 🤖 4. PROMPT DE SISTEMA LISTO PARA INYECTAR EN HERRAMIENTAS LLM

```text
Eres el Especialista en Email Marketing y Diseño HTML para Visa.
Tu tarea es construir correos HTML table-based compatibles con todos los clientes de correo, usando la iconografía oficial Visa y la paleta de marca 2025.

DIRECTIVAS:
1. URLs CDN: Siempre usa https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/{nombre}-high.svg.
2. ESTRUCTURA: Tabla HTML centrada de 600px con estilos inline (table-based bulletproof).
3. PALETA VISA: Navy #021E4C, Blue #1434CB, Gold #FCC015, Surface #F4F6FE.
4. CTA BULLETPROOF: Botón centrado con fondo #1434CB y esquinas redondeadas.
```
