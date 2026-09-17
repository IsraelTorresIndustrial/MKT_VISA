# 🎯 Visa · Guía de Selección de Íconos y URLs CDN para LLMs
> **Propósito:** Proveer al LLM la regla exacta para seleccionar el ícono oficial Visa SVG correspondiente a cada contexto y su URL canónica CDN en producción.

---

## ⚡ 1. DIRECTIVA DE URLs CDN
- **Dominio Base CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/{filename}`
- **Formato de inserción `<img>`**:
  ```html
  <img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/{filename}" alt="Visa Icon" width="40" height="40" border="0" />
  ```
- **Variante obligatoria:** Usar siempre la variante curada `-high.svg`.

---

## 📋 2. CATÁLOGO DE ÍCONOS VISA POR CONTEXTO

### 2.1 Pagos & Tarjetas
- Tarjeta Genérica → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-generic-high.svg`
- Tarjeta Débito → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-debit-high.svg`
- Tarjeta Corporativa → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-corporate-high.svg`
- Pago Sin Contacto / Tap to Pay → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/tap-high.svg`
- Terminal POS → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/pos-high.svg`
- Código QR → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/qr-high.svg`
- Escanear Tarjeta → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/scan-card-high.svg`

### 2.2 Transacciones & Transferencias
- Envío de Dinero → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/money-send-high.svg`
- Transferencia Móvil → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/mobile-transfer-high.svg`
- Solicitud de Dinero → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/money-request-high.svg`
- Comprobante / Recibo → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/receipt-high.svg`
- Devolución / Reembolso → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/return-high.svg`
- Dividir Cuenta (Split) → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/split-high.svg`
- Pago Rápido → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/fast-high.svg`
- Saldo / Balance → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/balance-high.svg`

### 2.3 Seguridad & Autenticación
- Protección / Escudo → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-protection-high.svg`
- Candado Seguridad → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-lock-high.svg`
- Antifraude → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/fraud-high.svg`
- Token de Pago → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/token-high.svg`
- Biometría Huella → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/fingerprint-high.svg`
- Biometría Facial → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/auth-face-high.svg`
- Código OTP / Auth → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/auth-code-high.svg`

### 2.4 Viajes & Internacional
- Cobertura Global → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/global-high.svg`
- Vuelos / Avión → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/transit-airplane-high.svg`
- Check Internacional → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/check-international-high.svg`
- Notificaciones de Viaje → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/travel-notifications-high.svg`
- Ubicación / Mapa → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/map-location-high.svg`

### 2.5 Comercio & Beneficios
- Ofertas & Deals → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/offers-deal-high.svg`
- Recompensa / Reward → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/reward-high.svg`
- Puntos Bonus → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/bonus-points-high.svg`
- Carrito de Compras → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/cart-high.svg`
- Regalo / Gift → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/gift-high.svg`
- Envío / Delivery → `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/shipping-high.svg`

---

## 🤖 3. PROMPT COMPACTO PARA TU HERRAMIENTA LLM (VISA)

```text
Eres el Selector de Iconografía Oficial de Visa SVG.
Tu tarea es asignar el ícono oficial Visa exacto para cada concepto y devolver su URL CDN de producción en Vercel.

REGLAS:
1. SIEMPRE usa URLs absolutas con prefijo https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/{nombre}-high.svg.
2. Inserción: <img src="URL" alt="Nombre" width="40" height="40" border="0" />.
3. Elige el ícono que mejor represente la acción o contexto de negocio.
```
