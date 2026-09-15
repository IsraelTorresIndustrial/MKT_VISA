# 🔷 VISA_LLM_ICON_DECISION_MATRIX
> **Documento de referencia exhaustivo para LLMs — Iconografía SVG oficial Visa**

| Campo | Valor |
|---|---|
| **Autor** | Israel Torres · Artefact VCA Team |
| **Proyecto** | MKT_VISA · Presentation Intelligence |
| **Versión** | 2025.09 |
| **Iconos documentados** | 155 |
| **CDN Base** | `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/` |
| **Formato icono** | SVG línea (outline) · `high` variant · sin relleno sólido |

> **Descripción Visa:** Visa es la red de pagos electrónicos más grande del mundo, conectando consumidores, comercios, instituciones financieras y gobiernos en más de 200 países y territorios. Su ecosistema digital requiere iconografía precisa, consistente y semánticamente correcta para comunicar funcionalidades de pago, seguridad, viaje, comercio y analítica. Este documento es la fuente de verdad para que los LLMs seleccionen el ícono correcto en cualquier contexto de diseño o comunicación Visa.

---

## 🚨 DIRECTIVA CRÍTICA PARA LLMs — CÓMO USAR ESTAS URLs

> **REGLA DE ORO:** Cuando un usuario solicite un ícono Visa o cualquier elemento visual del ecosistema de pagos Visa, **siempre construir la URL usando el patrón CDN Vercel** definido en este documento. NUNCA inventar URLs o usar rutas locales.

### Patrón de URL Canónica

```
https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/{filename.svg}
```

### Ejemplos de Construcción

```html
<!-- Ícono de tarjeta genérica -->
<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-generic-high.svg"
     alt="Tarjeta Visa" width="48" height="48" />

<!-- Ícono de seguridad -->
<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-high.svg"
     alt="Seguridad Visa" width="48" height="48" />

<!-- Ícono de transacciones -->
<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/transactions-high.svg"
     alt="Historial de Transacciones" width="48" height="48" />
```

### Tamaños Recomendados

| Contexto | Width / Height |
|---|---|
| Dashboard principal | 64×64 px |
| Navegación / menú | 24×24 px |
| Listas y tablas | 20×20 px |
| Tarjetas de beneficio | 48×48 px |
| Hero / banner | 80×80 px |
| Presentación ejecutiva | 96×96 px |

---

## 🎨 GUÍA MORFOLÓGICA PARA LLMs SIN VISIÓN

> Esta sección permite a los LLMs razonar sobre iconos SVG de tipo **línea (outline)** sin necesidad de ver las imágenes. Todos los iconos de la biblioteca Visa son:

### Características Formales Universales

1. **Estilo:** Trazo fino (stroke) outline — sin relleno sólido. Similar a Feather Icons o Heroicons Outline.
2. **Geometría:** Formas limpias, redondeadas en vértices, sin detalles decorativos superfluos.
3. **Color:** Monocromáticos por defecto (se colorean mediante CSS `fill` o `stroke`).
4. **Tamaño base:** ViewBox de 24×24 o 48×48 — escalables sin pérdida.
5. **Variante `high`:** La sufijo `-high` indica mayor nivel de detalle y variante de alta fidelidad.
6. **Sin perspectiva 3D:** Todos los iconos son planos (flat design 2D), sin sombras ni profundidad.
7. **Sin texto embebido:** Ningún SVG contiene texto o letras dentro del gráfico (excepto símbolos de moneda como `€`, `$`, `£`, `¥`).

### Familias Morfológicas

| Familia | Descripción Morfológica |
|---|---|
| **Tarjetas** | Rectángulo horizontal con esquinas redondeadas + elementos superpuestos (chip, +, -, ✓, ×) |
| **Personas/Cuentas** | Cabeza circular + torso abstracto ± elementos decorativos (+, -, ★, 🔒) |
| **Escudos/Seguridad** | Forma de escudo heráldico ± elementos internos (✓, 🔒, ondas) |
| **Dinero/Transacciones** | Rectángulo de billete o círculo de moneda ± flechas de dirección |
| **Dispositivos** | Siluetas de laptop, móvil o wearable en vista frontal/lateral |
| **Mapas/Viaje** | Formas geográficas, pines de mapa, vehículos estilizados |
| **UI Básica** | Formas geométricas simples: flechas, cruces, lupas, engranajes |
| **Comunicación** | Burbujas de chat, sobres, campanas, auriculares |
| **Analítica** | Barras de gráfico, líneas de tendencia, cilindros de datos |

---

## 🧠 ALGORITMO DE INFERENCIA EN 5 PASOS PARA SELECCIÓN DE ÍCONO

> Cuando necesites seleccionar un ícono Visa, sigue este algoritmo:

### Paso 1 — Identificar el Dominio Funcional
```
¿El contexto es de...?
  → PAGO FÍSICO          → Sección: Pagos
  → MOVIMIENTO DINERO    → Sección: Transacciones
  → CUENTA/WALLET        → Sección: Cuenta y Wallet
  → MONEDA/CAMBIO        → Sección: Divisas
  → PROTECCIÓN           → Sección: Seguridad
  → VIAJE/GEOGRAFÍA      → Sección: Viajes
  → TIENDA/BENEFICIO     → Sección: Comercio
  → MÉTRICAS/KPI         → Sección: Analítica
  → COMUNICAR/ALERTAR    → Sección: Comunicación
  → PERSONAS/EMPRESAS    → Sección: Identidad
  → CANAL DIGITAL        → Sección: Dispositivos
  → UI/INTERFAZ          → Sección: UI Esencial
```

### Paso 2 — Identificar el Verbo de Acción
```
¿La acción es...?
  AGREGAR    → buscar ícono con "+", "add", "new"
  ELIMINAR   → buscar ícono con "-", "remove", "delete", "off"
  PROTEGER   → buscar ícono con "security", "lock", "auth"
  NAVEGAR    → buscar ícono con "arrow", "chevron", "back", "forward"
  CONSULTAR  → buscar ícono con "view", "search", "history", "report"
  ENVIAR     → buscar ícono con "send", "transfer", "share"
  CONFIRMAR  → buscar ícono con "check", "success", "verify"
  ALERTAR    → buscar ícono con "warning", "error", "notification"
```

### Paso 3 — Aplicar Contexto de Negocio Visa
```
¿El usuario es...?
  TARJETAHABIENTE PERSONAL → priorizar: card-*, account-*, wallet-*
  COMERCIO/MERCHANT        → priorizar: merchant-*, pos-*, acquirer-*
  VIAJERO                  → priorizar: transit-*, map-*, global-*
  BANCO/EMISOR             → priorizar: issuer-*, analytics-*, security-*
  DESARROLLADOR            → priorizar: token-*, security-firewall-*, data-*
```

### Paso 4 — Verificar Anti-patrones
```
  ❌ NO usar card-off si el contexto es de pago exitoso
  ❌ NO usar error-high para advertencias leves (usar warning-high)
  ❌ NO usar account-high para empresas (usar company-high)
  ❌ NO usar fingerprint para autenticación facial (usar auth-face-high)
  ❌ NO usar currency-high si se conoce la divisa específica
  ❌ NO usar sign-out para bloqueo de cuenta (son conceptos distintos)
```

### Paso 5 — Construir URL y Snippet
```
  URL = CDN_BASE + filename
  SNIPPET = <img src="{URL}" alt="{descripcion}" width="48" height="48" />
```

---

## 🌳 ÁRBOL DE DECISIÓN ASCII POR CATEGORÍAS

```
CONTEXTO DEL ÍCONO
│
├── 💳 PAGO / TARJETA
│   ├── ¿Pago físico con tarjeta?
│   │   ├── Contactless/NFC → tap-high.svg
│   │   ├── Terminal → pos-high.svg / pos-alt-high.svg
│   │   ├── QR Code → qr-high.svg
│   │   └── Escaneo → scan-card-high.svg
│   └── ¿Tipo de tarjeta?
│       ├── Genérica → card-generic-high.svg
│       ├── Débito → card-debit-high.svg
│       ├── Prepago → card-prepaid-high.svg
│       ├── Corporativa → card-corporate-high.svg
│       ├── Suspendida → card-suspend-high.svg
│       ├── Desactivada → card-off-high.svg
│       └── Verificar → card-verify-high.svg
│
├── 💰 TRANSACCIÓN / DINERO
│   ├── ¿Envío? → money-send-high.svg
│   ├── ¿Solicitar cobro? → money-request-high.svg
│   ├── ¿Agregar fondos? → money-add-high.svg
│   ├── ¿Retirar? → money-withdrawn-high.svg
│   ├── ¿Dividir? → split-high.svg
│   ├── ¿Devolver? → return-high.svg
│   ├── ¿Estado pendiente? → on-hold-high.svg
│   ├── ¿Comprobante? → receipt-high.svg
│   └── ¿Historial? → transactions-high.svg
│
├── 🔐 SEGURIDAD
│   ├── ¿Autenticación?
│   │   ├── Biométrica facial → auth-face-high.svg
│   │   ├── Huella → fingerprint-high.svg
│   │   ├── Voz → auth-voice-high.svg
│   │   └── Código OTP → auth-code-high.svg
│   ├── ¿Candado/bloqueo? → security-lock-high.svg
│   ├── ¿Fraude? → fraud-high.svg
│   └── ¿Token? → token-high.svg
│
├── ✈️ VIAJE
│   ├── ¿Avión? → transit-airplane-high.svg
│   ├── ¿Auto/renta? → transit-car-high.svg
│   ├── ¿Tren/metro? → transit-train-high.svg
│   ├── ¿Mapa? → map-high.svg
│   └── ¿Global/mundial? → global-high.svg
│
├── 🏪 COMERCIO
│   ├── ¿Tienda física? → store-open-high.svg / store-closed-high.svg
│   ├── ¿Marketplace? → marketplace-high.svg
│   ├── ¿Ofertas? → offers-high.svg / offers-deal-high.svg
│   ├── ¿Puntos/rewards? → bonus-points-high.svg / reward-high.svg
│   └── ¿Carrito/e-commerce? → cart-high.svg
│
├── 📊 ANALÍTICA
│   ├── ¿Dashboard? → dashboard-high.svg
│   ├── ¿Gráfica/stats? → statistics-high.svg / analytics-high.svg
│   ├── ¿Reporte? → report-high.svg
│   └── ¿Tendencia? → trending-high.svg
│
├── 💬 COMUNICACIÓN
│   ├── ¿Éxito? → success-high.svg
│   ├── ¿Error? → error-high.svg
│   ├── ¿Advertencia? → warning-high.svg
│   ├── ¿Soporte? → customer-support-high.svg
│   └── ¿Notificación? → notifications-high.svg
│
└── 🖥️ UI / DISPOSITIVO
    ├── ¿Buscar? → search-high.svg
    ├── ¿Navegar? → arrow-back/forward/up/down-high.svg
    ├── ¿Configurar? → settings-high.svg
    ├── ¿Canal móvil? → device-mobile-high.svg
    └── ¿Canal web? → device-laptop-high.svg
```

---

## 📚 DOSSIER EXHAUSTIVO — 155 ÍCONOS VISA

> A continuación se documenta cada ícono con todos sus atributos semánticos, morfológicos y de uso.

## 💳 Categoría: Pagos
> **16 iconos en esta categoría.**
### 🔹 [1] `account-add-high.svg` · Agregar Cuenta
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/account-add-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/account-add-high.svg" alt="Agregar Cuenta" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Silueta de persona vista de frente con un símbolo "+" en la esquina inferior derecha, todo en trazo fino outline sin relleno. El contorno humano es circular en la cabeza con cuerpo estilizado.

- **Concepto Semántico:** Alta de nueva cuenta o usuario en el sistema de pagos
- **Intención de Negocio:** Facilitar el onboarding de nuevas cuentas de pago
- **Disparadores Clave (Triggers):** `agregar cuenta`, `nueva cuenta`, `onboarding`, `registro`, `alta`

**Cuándo Usar:**
- ✅ Botones CTA para abrir una cuenta de pago
- ✅ Flujos de incorporación de nuevos tarjetahabientes
- ✅ Secciones de gestión de múltiples cuentas

**Cuándo NO Usar (Anti-patrones):**
- ❌ Iconos de perfil personal sin contexto de pago
- ❌ Acciones de eliminación o suspensión de cuentas

**Copies de Ejemplo:**
- ""Abre tu cuenta Visa en minutos""
- ""Agrega una cuenta adicional y multiplica tus beneficios""

---
### 🔹 [2] `card-corporate-high.svg` · Tarjeta Corporativa
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-corporate-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-corporate-high.svg" alt="Tarjeta Corporativa" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Rectángulo horizontal con esquinas redondeadas (forma de tarjeta de crédito) con un pequeño ícono de edificio corporativo o maletín en su interior, trazo fino outline.

- **Concepto Semántico:** Tarjeta de crédito/débito de uso empresarial
- **Intención de Negocio:** Diferenciar productos corporativos del portafolio Visa
- **Disparadores Clave (Triggers):** `tarjeta corporativa`, `empresarial`, `business card`, `gastos empresa`, `B2B`

**Cuándo Usar:**
- ✅ Secciones de productos para empresas
- ✅ Comparadores de tarjetas con segmento corporativo
- ✅ Portales de gestión de gastos empresariales

**Cuándo NO Usar (Anti-patrones):**
- ❌ Contextos de tarjetas personales o de consumo
- ❌ Productos dirigidos a personas físicas

**Copies de Ejemplo:**
- ""Controla los gastos de tu empresa con la Tarjeta Visa Corporativa""
- ""Soluciones de pago diseñadas para tu negocio""

---
### 🔹 [3] `card-debit-high.svg` · Tarjeta de Débito
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-debit-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-debit-high.svg" alt="Tarjeta de Débito" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Rectángulo de tarjeta con la letra 'D' estilizada o indicador de débito; trazo fino outline, sin chip representado en detalle.

- **Concepto Semántico:** Tarjeta de débito vinculada a cuenta bancaria
- **Intención de Negocio:** Representar el producto de débito Visa en comunicaciones
- **Disparadores Clave (Triggers):** `débito`, `debit card`, `pago directo`, `cuenta corriente`, `débito inmediato`

**Cuándo Usar:**
- ✅ Páginas de productos de débito Visa
- ✅ Flujos de selección de tipo de tarjeta en checkout
- ✅ Materiales educativos sobre tipos de tarjeta

**Cuándo NO Usar (Anti-patrones):**
- ❌ Contextos de crédito o prepago
- ❌ Representación de pagos diferidos o a cuotas

**Copies de Ejemplo:**
- ""Paga directo desde tu cuenta con tu Tarjeta Visa Débito""
- ""Sin deuda, sin complicaciones: débito Visa""

---
### 🔹 [4] `card-generic-high.svg` · Tarjeta Genérica
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-generic-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-generic-high.svg" alt="Tarjeta Genérica" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Rectángulo horizontal con esquinas redondeadas y chip cuadrado en esquina superior izquierda, sin branding específico; líneas de trazo fino outline.

- **Concepto Semántico:** Tarjeta de pago en sentido general
- **Intención de Negocio:** Representar cualquier tipo de tarjeta Visa de forma neutral
- **Disparadores Clave (Triggers):** `tarjeta`, `card`, `pago con tarjeta`, `plástico`, `medio de pago`

**Cuándo Usar:**
- ✅ Íconos genéricos de método de pago en e-commerce
- ✅ Secciones de "mis tarjetas" en apps bancarias
- ✅ Materiales donde no se especifica tipo de tarjeta

**Cuándo NO Usar (Anti-patrones):**
- ❌ Cuando se requiere diferenciar entre débito, crédito o prepago
- ❌ Contextos corporativos que requieren iconografía específica

**Copies de Ejemplo:**
- ""Paga con tu tarjeta Visa en millones de establecimientos""
- ""Agrega tu tarjeta y empieza a disfrutar tus beneficios""

---
### 🔹 [5] `card-manage-alt-high.svg` · Gestionar Tarjeta (Alt)
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-manage-alt-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-manage-alt-high.svg" alt="Gestionar Tarjeta (Alt)" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Tarjeta con símbolo de engranaje o llave inglesa en variante alternativa de composición; trazo outline fino. La composición del ícono de herramienta es ligeramente diferente a la versión estándar.

- **Concepto Semántico:** Gestión y configuración alternativa de tarjeta
- **Intención de Negocio:** Acceso a opciones de administración de tarjeta
- **Disparadores Clave (Triggers):** `gestionar`, `administrar tarjeta`, `configurar`, `ajustes tarjeta`, `manage card`

**Cuándo Usar:**
- ✅ Menús de opciones de tarjeta en versión compacta
- ✅ Vistas secundarias de configuración de tarjeta
- ✅ Variante visual en dashboards de múltiples tarjetas

**Cuándo NO Usar (Anti-patrones):**
- ❌ Como ícono principal si ya se usa card-manage-high.svg
- ❌ Contextos donde la diferenciación visual no es necesaria

**Copies de Ejemplo:**
- ""Administra tu tarjeta desde la app, en cualquier momento""
- ""Personaliza límites y preferencias de tu Visa""

---
### 🔹 [6] `card-manage-high.svg` · Gestionar Tarjeta
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-manage-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-manage-high.svg" alt="Gestionar Tarjeta" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Tarjeta de crédito con un engranaje o ícono de ajustes superpuesto en la esquina, indicando gestión. Todo en trazo fino outline.

- **Concepto Semántico:** Gestión y administración de tarjeta Visa
- **Intención de Negocio:** Centralizar las opciones de control de tarjeta del usuario
- **Disparadores Clave (Triggers):** `gestionar tarjeta`, `manage`, `configurar tarjeta`, `ajustes`, `administrar`

**Cuándo Usar:**
- ✅ Dashboard principal de tarjeta en app bancaria
- ✅ Botones de acceso a configuración de tarjeta
- ✅ Navegación hacia sección de gestión de plástico

**Cuándo NO Usar (Anti-patrones):**
- ❌ Representar pagos o transacciones directas
- ❌ Contextos donde la tarjeta es solo decorativa

**Copies de Ejemplo:**
- ""Gestiona tu tarjeta Visa con total control""
- ""Configura alertas, límites y bloqueos desde tu app""

---
### 🔹 [7] `card-number-high.svg` · Número de Tarjeta
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-number-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-number-high.svg" alt="Número de Tarjeta" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Tarjeta con dígitos o asteriscos representando un número de tarjeta enmascarado (estilo ****1234); trazo fino outline.

- **Concepto Semántico:** Número identificador de tarjeta bancaria
- **Intención de Negocio:** Representar la captura o visualización del número de tarjeta
- **Disparadores Clave (Triggers):** `número de tarjeta`, `PAN`, `card number`, `dígitos`, `enmascarar`

**Cuándo Usar:**
- ✅ Formularios de pago con campo de número de tarjeta
- ✅ Secciones de verificación de identidad de tarjeta
- ✅ Pantallas de resumen de tarjeta enmascarada

**Cuándo NO Usar (Anti-patrones):**
- ❌ Representar el PIN o CVV específicamente
- ❌ Contextos de tarjeta sin referencia a número

**Copies de Ejemplo:**
- ""Ingresa tu número de tarjeta de forma segura""
- ""Tu número Visa siempre protegido con encriptación""

---
### 🔹 [8] `card-off-high.svg` · Tarjeta Desactivada
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-off-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-off-high.svg" alt="Tarjeta Desactivada" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Tarjeta de crédito con una línea diagonal cruzándola o símbolo de prohibición; trazo fino outline, comunicando deshabilitación.

- **Concepto Semántico:** Tarjeta inhabilitada o sin servicio
- **Intención de Negocio:** Indicar estado de tarjeta bloqueada o desactivada
- **Disparadores Clave (Triggers):** `tarjeta desactivada`, `bloquear`, `suspender`, `card off`, `deshabilitar`

**Cuándo Usar:**
- ✅ Indicadores de estado de tarjeta bloqueada
- ✅ Alertas de tarjeta suspendida por inactividad
- ✅ Flujos de activación/desactivación de tarjeta

**Cuándo NO Usar (Anti-patrones):**
- ❌ Estados activos o positivos de tarjeta
- ❌ Flujos de compra o pago exitoso

**Copies de Ejemplo:**
- ""Tu tarjeta está temporalmente desactivada""
- ""Reactiva tu Visa en segundos desde la app""

---
### 🔹 [9] `card-prepaid-high.svg` · Tarjeta Prepagada
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-prepaid-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-prepaid-high.svg" alt="Tarjeta Prepagada" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Tarjeta con símbolo de adición o indicador de saldo precargado en su superficie; trazo fino outline.

- **Concepto Semántico:** Tarjeta de prepago con saldo predefinido
- **Intención de Negocio:** Representar el producto de tarjeta prepagada Visa
- **Disparadores Clave (Triggers):** `prepago`, `prepaid`, `saldo`, `gift card`, `tarjeta recargable`

**Cuándo Usar:**
- ✅ Páginas de producto de tarjeta prepagada
- ✅ Flujos de carga o recarga de tarjeta
- ✅ Secciones de regalo o tarjeta de obsequio

**Cuándo NO Usar (Anti-patrones):**
- ❌ Tarjetas de crédito con línea de crédito
- ❌ Productos de débito vinculados a cuenta

**Copies de Ejemplo:**
- ""Carga tu Visa Prepagada y úsala en cualquier parte del mundo""
- ""El regalo perfecto: una Visa Prepagada con saldo a tu medida""

---
### 🔹 [10] `card-suspend-high.svg` · Tarjeta Suspendida
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-suspend-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-suspend-high.svg" alt="Tarjeta Suspendida" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Tarjeta con símbolo de pausa (dos barras verticales) o indicador de suspensión temporal; trazo fino outline.

- **Concepto Semántico:** Suspensión temporal de tarjeta
- **Intención de Negocio:** Comunicar estado de pausa temporal diferenciado del bloqueo definitivo
- **Disparadores Clave (Triggers):** `suspender tarjeta`, `pausa`, `suspend`, `bloqueo temporal`, `congelar tarjeta`

**Cuándo Usar:**
- ✅ Opciones de congelación temporal de tarjeta
- ✅ Estados intermedios de tarjeta en revisión
- ✅ Funcionalidad de pausa en apps de banca móvil

**Cuándo NO Usar (Anti-patrones):**
- ❌ Bloqueo definitivo o cancelación de tarjeta
- ❌ Estados activos normales de tarjeta

**Copies de Ejemplo:**
- ""Congela tu tarjeta temporalmente si la perdiste de vista""
- ""Pausa y reactiva tu Visa cuando lo necesites""

---
### 🔹 [11] `card-verify-high.svg` · Verificación de Tarjeta
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-verify-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/card-verify-high.svg" alt="Verificación de Tarjeta" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Tarjeta con checkmark o escudo de verificación superpuesto; trazo fino outline indicando validación exitosa.

- **Concepto Semántico:** Validación y verificación de tarjeta bancaria
- **Intención de Negocio:** Representar el proceso de verificación de identidad de tarjeta
- **Disparadores Clave (Triggers):** `verificar tarjeta`, `validar`, `autenticar`, `card verify`, `confirmar`

**Cuándo Usar:**
- ✅ Flujos de activación de tarjeta nueva
- ✅ Procesos de verificación en 3D Secure
- ✅ Pasos de confirmación de identidad en onboarding

**Cuándo NO Usar (Anti-patrones):**
- ❌ Estados de tarjeta sin verificar o en error
- ❌ Contextos de gestión sin verificación

**Copies de Ejemplo:**
- ""Verifica tu tarjeta Visa en un solo paso""
- ""Tarjeta verificada: tus pagos están protegidos""

---
### 🔹 [12] `pos-alt-high.svg` · Terminal POS (Alt)
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/pos-alt-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/pos-alt-high.svg" alt="Terminal POS (Alt)" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Terminal punto de venta en variante alternativa de composición: dispositivo rectangular con pantalla y teclado numérico estilizado, trazo fino outline.

- **Concepto Semántico:** Punto de venta físico variante
- **Intención de Negocio:** Representar terminales POS en versión alternativa visual
- **Disparadores Clave (Triggers):** `POS`, `terminal`, `punto de venta`, `datáfono`, `cobrar`

**Cuándo Usar:**
- ✅ Variante visual en secciones de aceptación de pagos
- ✅ Materiales para comercios con diseño alternativo
- ✅ Diferenciación visual entre tipos de terminal

**Cuándo NO Usar (Anti-patrones):**
- ❌ Pagos digitales o sin contacto exclusivamente
- ❌ Contextos de tarjeta sin terminal físico

**Copies de Ejemplo:**
- ""Acepta pagos Visa en tu negocio con nuestros terminales""
- ""Soluciones POS adaptadas a cada tipo de comercio""

---
### 🔹 [13] `pos-high.svg` · Terminal POS
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/pos-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/pos-high.svg" alt="Terminal POS" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Terminal punto de venta estándar: dispositivo rectangular con pantalla pequeña en la parte superior y bloque de teclado numérico debajo, trazo fino outline.

- **Concepto Semántico:** Terminal punto de venta para aceptar pagos
- **Intención de Negocio:** Representar la infraestructura de aceptación de pagos físicos
- **Disparadores Clave (Triggers):** `POS`, `terminal de pago`, `datáfono`, `cobrar`, `comercio`

**Cuándo Usar:**
- ✅ Secciones de soluciones para comercios
- ✅ Flujos de aceptación de pagos con tarjeta
- ✅ Materiales de acquirer y merchant

**Cuándo NO Usar (Anti-patrones):**
- ❌ Pagos P2P o transferencias sin terminal
- ❌ Contextos exclusivamente digitales/móviles

**Copies de Ejemplo:**
- ""Acepta Visa en tu local con terminales de última generación""
- ""Del cobro físico al digital: soluciones POS Visa para tu negocio""

---
### 🔹 [14] `qr-high.svg` · Código QR
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/qr-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/qr-high.svg" alt="Código QR" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Cuadrado con patrón de píxeles representando un código QR, con los tres cuadros de esquina característicos; trazo fino outline.

- **Concepto Semántico:** Pago o identificación mediante código QR
- **Intención de Negocio:** Representar pagos sin contacto vía código QR
- **Disparadores Clave (Triggers):** `QR`, `pago QR`, `escanear`, `sin contacto`, `código de pago`

**Cuándo Usar:**
- ✅ Flujos de pago con QR en checkout
- ✅ Materiales de pago digital sin tarjeta física
- ✅ Secciones de pago en tienda con móvil

**Cuándo NO Usar (Anti-patrones):**
- ❌ Pagos con tarjeta física o NFC exclusivo
- ❌ Contextos sin uso de cámara o escáner

**Copies de Ejemplo:**
- ""Paga escaneando, rápido y seguro con Visa QR""
- ""Tu QR Visa: la forma más ágil de cobrar y pagar""

---
### 🔹 [15] `scan-card-high.svg` · Escanear Tarjeta
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/scan-card-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/scan-card-high.svg" alt="Escanear Tarjeta" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Tarjeta de crédito con líneas de escaneo superpuestas o encuadre de cámara alrededor; trazo fino outline.

- **Concepto Semántico:** Captura de datos de tarjeta mediante escaneo
- **Intención de Negocio:** Facilitar el ingreso de datos de tarjeta sin escritura manual
- **Disparadores Clave (Triggers):** `escanear tarjeta`, `scan card`, `OCR tarjeta`, `capturar tarjeta`, `lector`

**Cuándo Usar:**
- ✅ Botones de escaneo de tarjeta en apps de pago
- ✅ Onboarding de nueva tarjeta con cámara
- ✅ Formularios con opción de captura automática

**Cuándo NO Usar (Anti-patrones):**
- ❌ Ingreso manual de número de tarjeta
- ❌ Verificación de identidad sin tarjeta física

**Copies de Ejemplo:**
- ""Escanea tu tarjeta Visa y agégala en segundos""
- ""Sin teclear: usa tu cámara para agregar tu tarjeta""

---
### 🔹 [16] `tap-high.svg` · Pago NFC / Tap
- **Familia Semántica:** Pagos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/tap-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/tap-high.svg" alt="Pago NFC / Tap" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Mano o tarjeta con ondas de radio concéntricas emanando hacia un lado, indicando pago sin contacto; trazo fino outline.

- **Concepto Semántico:** Pago sin contacto mediante NFC o tap
- **Intención de Negocio:** Comunicar la experiencia de pago contactless Visa
- **Disparadores Clave (Triggers):** `tap`, `NFC`, `contactless`, `sin contacto`, `pago rápido`, `wave`

**Cuándo Usar:**
- ✅ Promoción de pagos sin contacto en POS
- ✅ Materiales de educación sobre NFC
- ✅ Secciones de pago rápido en apps

**Cuándo NO Usar (Anti-patrones):**
- ❌ Pagos con chip o banda magnética
- ❌ Transferencias bancarias o pagos en línea

**Copies de Ejemplo:**
- ""Toca y paga: la magia del contactless Visa""
- ""Un tap y listo: así de fácil con tu Visa""

---
## 💰 Categoría: Transacciones
> **15 iconos en esta categoría.**
### 🔹 [17] `balance-high.svg` · Saldo / Balance
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/balance-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/balance-high.svg" alt="Saldo / Balance" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Balanza o ícono de medición de peso con dos platillos equilibrados; o display numérico con moneda; trazo fino outline.

- **Concepto Semántico:** Saldo disponible en cuenta o tarjeta
- **Intención de Negocio:** Mostrar y comunicar el saldo actual del usuario
- **Disparadores Clave (Triggers):** `saldo`, `balance`, `disponible`, `fondos`, `consulta de saldo`

**Cuándo Usar:**
- ✅ Pantallas de resumen de cuenta
- ✅ Widgets de saldo en dashboard bancario
- ✅ Notificaciones de saldo bajo o actualización

**Cuándo NO Usar (Anti-patrones):**
- ❌ Transacciones específicas o historial
- ❌ Contextos de crédito sin referencia a saldo

**Copies de Ejemplo:**
- ""Consulta tu saldo Visa en tiempo real""
- ""Siempre al tanto de tu disponible con Visa""

---
### 🔹 [18] `bill-alt-high.svg` · Factura (Alt)
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/bill-alt-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/bill-alt-high.svg" alt="Factura (Alt)" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Hoja de papel con líneas horizontales representando texto y un doblez en esquina, variante alternativa; trazo fino outline.

- **Concepto Semántico:** Factura o comprobante de pago variante
- **Intención de Negocio:** Representar documentos de cobro en versión alternativa
- **Disparadores Clave (Triggers):** `factura`, `bill`, `cobro`, `comprobante`, `recibo alternativo`

**Cuándo Usar:**
- ✅ Variante visual en secciones de facturación
- ✅ Diferenciación entre tipos de documento
- ✅ Secciones de historial de facturas

**Cuándo NO Usar (Anti-patrones):**
- ❌ Recibos de transacciones específicas
- ❌ Documentos de identidad o contratos

**Copies de Ejemplo:**
- ""Accede a tus facturas Visa en cualquier momento""
- ""Descarga tu estado de cuenta con un clic""

---
### 🔹 [19] `bill-high.svg` · Factura / Cuenta
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/bill-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/bill-high.svg" alt="Factura / Cuenta" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Hoja de papel con encabezado y líneas de concepto, símbolo de moneda en la parte inferior; trazo fino outline.

- **Concepto Semántico:** Factura, cuenta por pagar o documento de cobro
- **Intención de Negocio:** Representar obligaciones de pago o documentos de cobro
- **Disparadores Clave (Triggers):** `factura`, `cuenta`, `pago de servicios`, `cobro`, `bill payment`

**Cuándo Usar:**
- ✅ Secciones de pago de facturas y servicios
- ✅ Pantallas de cuentas pendientes de pago
- ✅ Opciones de domiciliación de pagos

**Cuándo NO Usar (Anti-patrones):**
- ❌ Recibos de compras ya realizadas
- ❌ Estados de cuenta históricos

**Copies de Ejemplo:**
- ""Paga todas tus facturas desde un solo lugar con Visa""
- ""Nunca más te olvides de una factura: automatiza con Visa""

---
### 🔹 [20] `fast-high.svg` · Transacción Rápida
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/fast-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/fast-high.svg" alt="Transacción Rápida" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Rayo o líneas de velocidad con símbolo de pago o flecha; indica rapidez y agilidad; trazo fino outline.

- **Concepto Semántico:** Procesamiento acelerado de transacciones
- **Intención de Negocio:** Comunicar la velocidad y agilidad del procesamiento Visa
- **Disparadores Clave (Triggers):** `rápido`, `fast`, `instantáneo`, `velocidad`, `tiempo real`

**Cuándo Usar:**
- ✅ Comunicación de pagos en tiempo real
- ✅ Secciones de transferencias express
- ✅ Materiales de Visa Direct

**Cuándo NO Usar (Anti-patrones):**
- ❌ Procesos que requieren múltiples pasos o verificación larga
- ❌ Contextos de pagos diferidos o a plazos

**Copies de Ejemplo:**
- ""Pagos instantáneos Visa: en segundos, no en días""
- ""La velocidad que tu negocio necesita, con Visa""

---
### 🔹 [21] `mobile-transfer-high.svg` · Transferencia Móvil
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/mobile-transfer-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/mobile-transfer-high.svg" alt="Transferencia Móvil" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Smartphone con flecha de transferencia saliendo o entrando; trazo fino outline.

- **Concepto Semántico:** Transferencia de dinero desde dispositivo móvil
- **Intención de Negocio:** Representar la experiencia de transferencia desde móvil
- **Disparadores Clave (Triggers):** `transferencia móvil`, `mobile payment`, `enviar desde móvil`, `app transfer`, `P2P móvil`

**Cuándo Usar:**
- ✅ Secciones de transferencia en apps bancarias
- ✅ Funcionalidades de pago móvil
- ✅ Flujos de envío de dinero entre usuarios

**Cuándo NO Usar (Anti-patrones):**
- ❌ Transferencias desde desktop o sucursal
- ❌ Pagos con tarjeta física en POS

**Copies de Ejemplo:**
- ""Transfiere dinero desde tu celular con Visa""
- ""Envía y recibe pagos móviles sin comisiones""

---
### 🔹 [22] `money-add-high.svg` · Agregar Dinero
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/money-add-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/money-add-high.svg" alt="Agregar Dinero" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Billete o moneda con símbolo "+" indicando ingreso o depósito de fondos; trazo fino outline.

- **Concepto Semántico:** Depósito o adición de fondos a cuenta
- **Intención de Negocio:** Representar la acción de agregar saldo o realizar depósito
- **Disparadores Clave (Triggers):** `depositar`, `agregar saldo`, `recargar`, `fondear`, `add money`

**Cuándo Usar:**
- ✅ Flujos de depósito y recarga de cuenta
- ✅ Botones de carga de wallet o prepago
- ✅ Secciones de abono a cuenta

**Cuándo NO Usar (Anti-patrones):**
- ❌ Retiros o débitos de cuenta
- ❌ Transferencias salientes

**Copies de Ejemplo:**
- ""Agrega saldo a tu Visa con rapidez y seguridad""
- ""Fondea tu cuenta Visa desde cualquier canal""

---
### 🔹 [23] `money-request-high.svg` · Solicitar Dinero
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/money-request-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/money-request-high.svg" alt="Solicitar Dinero" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Billete o moneda con flecha entrante y símbolo de solicitud o interrogación; trazo fino outline.

- **Concepto Semántico:** Solicitud de pago o cobro a terceros
- **Intención de Negocio:** Facilitar el cobro entre personas o a clientes
- **Disparadores Clave (Triggers):** `cobrar`, `solicitar pago`, `request money`, `split`, `pedir dinero`

**Cuándo Usar:**
- ✅ Funcionalidades de cobro entre amigos
- ✅ Herramientas de facturación para freelancers
- ✅ Flujos de request to pay

**Cuándo NO Usar (Anti-patrones):**
- ❌ Envíos de dinero salientes
- ❌ Pagos automáticos o domiciliados

**Copies de Ejemplo:**
- ""Cobra a tus clientes al instante con Visa""
- ""Solicita tu pago y recíbelo en segundos""

---
### 🔹 [24] `money-send-high.svg` · Enviar Dinero
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/money-send-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/money-send-high.svg" alt="Enviar Dinero" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Billete o moneda con flecha saliente indicando envío de fondos; trazo fino outline.

- **Concepto Semántico:** Envío o transferencia de dinero saliente
- **Intención de Negocio:** Representar la acción de enviar dinero a otro usuario o cuenta
- **Disparadores Clave (Triggers):** `enviar dinero`, `transferir`, `send money`, `remesa`, `pago P2P`

**Cuándo Usar:**
- ✅ Botones de envío de dinero en apps
- ✅ Secciones de remesas internacionales
- ✅ Flujos de transferencia P2P

**Cuándo NO Usar (Anti-patrones):**
- ❌ Recepción de fondos o depósitos
- ❌ Pagos en comercio o POS

**Copies de Ejemplo:**
- ""Envía dinero a cualquier parte con Visa Direct""
- ""Transfiere en segundos, sin importar la distancia""

---
### 🔹 [25] `money-withdrawn-high.svg` · Retiro de Dinero
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/money-withdrawn-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/money-withdrawn-high.svg" alt="Retiro de Dinero" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Billete o mano sosteniendo dinero con flecha hacia arriba o salida de caja; trazo fino outline.

- **Concepto Semántico:** Retiro de efectivo de cuenta o cajero
- **Intención de Negocio:** Representar operaciones de extracción de fondos
- **Disparadores Clave (Triggers):** `retiro`, `withdrawal`, `sacar dinero`, `efectivo`, `ATM retiro`

**Cuándo Usar:**
- ✅ Secciones de retiro en apps bancarias
- ✅ Historial de operaciones en cajero
- ✅ Alertas de retiro reciente

**Cuándo NO Usar (Anti-patrones):**
- ❌ Depósitos o abonos de fondos
- ❌ Pagos con tarjeta sin efectivo

**Copies de Ejemplo:**
- ""Retira efectivo con tu Visa en más de 2 millones de ATMs""
- ""Lleva tu dinero donde lo necesites con Visa""

---
### 🔹 [26] `on-hold-high.svg` · Transacción en Espera
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/on-hold-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/on-hold-high.svg" alt="Transacción en Espera" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Reloj de arena o símbolo de pausa con fondo de billete/moneda; indica estado de espera; trazo fino outline.

- **Concepto Semántico:** Transacción retenida o en estado de espera
- **Intención de Negocio:** Comunicar estados intermedios de transacciones pendientes
- **Disparadores Clave (Triggers):** `en espera`, `pendiente`, `on hold`, `retenido`, `autorización pendiente`

**Cuándo Usar:**
- ✅ Estados de transacciones en proceso de autorización
- ✅ Alertas de fondos retenidos temporalmente
- ✅ Pantallas de detalle de transacción en revisión

**Cuándo NO Usar (Anti-patrones):**
- ❌ Transacciones completadas o exitosas
- ❌ Rechazos definitivos de transacción

**Copies de Ejemplo:**
- ""Tu transacción está siendo procesada""
- ""Fondos temporalmente retenidos: te notificamos cuando se liberen""

---
### 🔹 [27] `receipt-high.svg` · Recibo / Comprobante
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/receipt-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/receipt-high.svg" alt="Recibo / Comprobante" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Papel de recibo con borde serrado en la parte inferior y líneas de detalle de transacción; trazo fino outline.

- **Concepto Semántico:** Comprobante de pago o recibo de transacción
- **Intención de Negocio:** Proporcionar evidencia y registro de pagos realizados
- **Disparadores Clave (Triggers):** `recibo`, `comprobante`, `receipt`, `ticket`, `voucher`

**Cuándo Usar:**
- ✅ Botones de descarga de comprobante
- ✅ Secciones de historial de pagos
- ✅ Confirmaciones de transacción exitosa

**Cuándo NO Usar (Anti-patrones):**
- ❌ Facturas futuras o cuentas pendientes
- ❌ Contratos o documentos legales

**Copies de Ejemplo:**
- ""Descarga tu comprobante Visa al instante""
- ""Cada pago, cada recibo: tu tranquilidad con Visa""

---
### 🔹 [28] `return-high.svg` · Devolución / Reembolso
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/return-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/return-high.svg" alt="Devolución / Reembolso" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Flecha circular o de retorno con símbolo de dinero; indica reversión de pago; trazo fino outline.

- **Concepto Semántico:** Devolución de cargo o reembolso de transacción
- **Intención de Negocio:** Representar el proceso de devolución y reembolso al cliente
- **Disparadores Clave (Triggers):** `devolución`, `reembolso`, `return`, `refund`, `cargo revertido`

**Cuándo Usar:**
- ✅ Secciones de disputas y reclamaciones
- ✅ Flujos de solicitud de devolución
- ✅ Historial de cargos revertidos

**Cuándo NO Usar (Anti-patrones):**
- ❌ Transacciones de envío de dinero positivas
- ❌ Nuevos pagos o compras

**Copies de Ejemplo:**
- ""Solicita tu devolución Visa de forma simple y segura""
- ""Reembolsos Visa procesados en tu estado de cuenta""

---
### 🔹 [29] `split-high.svg` · Dividir Pago
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/split-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/split-high.svg" alt="Dividir Pago" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Billete o cuenta dividida en dos o más partes con línea de separación; ícono de división; trazo fino outline.

- **Concepto Semántico:** División de pagos entre múltiples personas
- **Intención de Negocio:** Facilitar la experiencia de split de gastos compartidos
- **Disparadores Clave (Triggers):** `dividir`, `split`, `compartir gasto`, `pagar entre varios`, `split bill`

**Cuándo Usar:**
- ✅ Funcionalidades de split de cuenta en restaurantes
- ✅ Apps de gastos compartidos
- ✅ Flujos de cobro grupal

**Cuándo NO Usar (Anti-patrones):**
- ❌ Pagos individuales sin división
- ❌ Transferencias de monto completo

**Copies de Ejemplo:**
- ""Divide la cuenta con tus amigos usando Visa""
- ""Split fácil: todos pagan su parte con Visa""

---
### 🔹 [30] `transactions-high.svg` · Historial de Transacciones
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/transactions-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/transactions-high.svg" alt="Historial de Transacciones" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Lista de ítems con flechas o monedas indicando movimientos de dinero múltiples; trazo fino outline.

- **Concepto Semántico:** Registro histórico de operaciones financieras
- **Intención de Negocio:** Acceso al historial completo de movimientos de cuenta
- **Disparadores Clave (Triggers):** `transacciones`, `historial`, `movimientos`, `transactions`, `actividad`

**Cuándo Usar:**
- ✅ Secciones de historial en apps bancarias
- ✅ Dashboard de movimientos de tarjeta
- ✅ Reportes de actividad financiera

**Cuándo NO Usar (Anti-patrones):**
- ❌ Transacción individual específica
- ❌ Saldos o balances actuales

**Copies de Ejemplo:**
- ""Consulta todas tus transacciones Visa en tiempo real""
- ""Tu historial financiero completo, siempre disponible""

---
### 🔹 [31] `transactions-new-high.svg` · Nueva Transacción
- **Familia Semántica:** Transacciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/transactions-new-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/transactions-new-high.svg" alt="Nueva Transacción" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Lista de transacciones con ícono de nuevo o badge de notificación; trazo fino outline.

- **Concepto Semántico:** Notificación de nueva actividad transaccional
- **Intención de Negocio:** Alertar al usuario sobre transacciones recientes no revisadas
- **Disparadores Clave (Triggers):** `nueva transacción`, `movimiento reciente`, `alerta`, `nuevo cargo`, `actividad reciente`

**Cuándo Usar:**
- ✅ Notificaciones de nuevos movimientos
- ✅ Badges en sección de transacciones
- ✅ Alertas push de cargo reciente

**Cuándo NO Usar (Anti-patrones):**
- ❌ Historial completo sin novedad
- ❌ Estados estáticos sin actualización

**Copies de Ejemplo:**
- ""Nueva transacción detectada en tu Visa""
- ""Mantente al día con cada movimiento de tu cuenta""

---
## 👛 Categoría: Cuenta y Wallet
> **8 iconos en esta categoría.**
### 🔹 [32] `account-favorite-high.svg` · Cuenta Favorita
- **Familia Semántica:** Cuenta y Wallet
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/account-favorite-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/account-favorite-high.svg" alt="Cuenta Favorita" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Ícono de persona o cuenta con estrella o corazón de favorito; trazo fino outline.

- **Concepto Semántico:** Cuenta marcada como favorita o preferida
- **Intención de Negocio:** Destacar cuentas frecuentes para agilizar operaciones
- **Disparadores Clave (Triggers):** `cuenta favorita`, `favorito`, `cuenta principal`, `preferred`, `frecuente`

**Cuándo Usar:**
- ✅ Listas de cuentas con marcado de favoritos
- ✅ Selección rápida de cuenta habitual
- ✅ Personalización de dashboard de cuentas

**Cuándo NO Usar (Anti-patrones):**
- ❌ Cuentas bloqueadas o en estado negativo
- ❌ Contextos sin gestión de múltiples cuentas

**Copies de Ejemplo:**
- ""Marca tu cuenta Visa favorita para pagos más rápidos""
- ""Accede primero a lo que más usas""

---
### 🔹 [33] `account-high.svg` · Cuenta
- **Familia Semántica:** Cuenta y Wallet
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/account-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/account-high.svg" alt="Cuenta" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Ícono de persona o avatar genérico en trazo fino outline, representando una cuenta de usuario.

- **Concepto Semántico:** Cuenta de usuario o perfil bancario
- **Intención de Negocio:** Representar la identidad y cuenta del usuario en el sistema
- **Disparadores Clave (Triggers):** `cuenta`, `perfil`, `usuario`, `account`, `mi cuenta`

**Cuándo Usar:**
- ✅ Navegación hacia sección de mi cuenta
- ✅ Ícono de perfil en headers de app
- ✅ Secciones de información personal

**Cuándo NO Usar (Anti-patrones):**
- ❌ Grupos o empresas (usar company-high.svg)
- ❌ Tarjetas específicas (usar card-generic-high.svg)

**Copies de Ejemplo:**
- ""Gestiona tu cuenta Visa desde un solo lugar""
- ""Tu cuenta, tu control: todo en Visa""

---
### 🔹 [34] `account-lock-high.svg` · Cuenta Bloqueada
- **Familia Semántica:** Cuenta y Wallet
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/account-lock-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/account-lock-high.svg" alt="Cuenta Bloqueada" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Ícono de persona con candado superpuesto; trazo fino outline indicando cuenta restringida.

- **Concepto Semántico:** Cuenta de usuario bloqueada o restringida
- **Intención de Negocio:** Comunicar el estado de bloqueo de cuenta para seguridad
- **Disparadores Clave (Triggers):** `cuenta bloqueada`, `bloqueo`, `restringida`, `acceso denegado`, `lock account`

**Cuándo Usar:**
- ✅ Estados de cuenta con acceso restringido
- ✅ Alertas de seguridad por intentos fallidos
- ✅ Pantallas de desbloqueo de cuenta

**Cuándo NO Usar (Anti-patrones):**
- ❌ Cuentas activas o en buen estado
- ❌ Bloqueos de tarjeta (diferente de cuenta)

**Copies de Ejemplo:**
- ""Tu cuenta está protegida con bloqueo de seguridad""
- ""Desbloquea tu cuenta Visa de forma segura""

---
### 🔹 [35] `account-remove-high.svg` · Eliminar Cuenta
- **Familia Semántica:** Cuenta y Wallet
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/account-remove-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/account-remove-high.svg" alt="Eliminar Cuenta" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Ícono de persona con símbolo "-" o "×" indicando eliminación; trazo fino outline.

- **Concepto Semántico:** Eliminación o baja de cuenta de usuario
- **Intención de Negocio:** Representar la acción de eliminar o dar de baja una cuenta
- **Disparadores Clave (Triggers):** `eliminar cuenta`, `dar de baja`, `remove account`, `cancelar cuenta`, `cerrar cuenta`

**Cuándo Usar:**
- ✅ Flujos de cancelación de cuenta
- ✅ Gestión de múltiples cuentas con opción de eliminar
- ✅ Confirmaciones de baja de servicio

**Cuándo NO Usar (Anti-patrones):**
- ❌ Agregar o crear nuevas cuentas
- ❌ Estados neutros de cuenta

**Copies de Ejemplo:**
- ""¿Deseas dar de baja tu cuenta Visa?""
- ""Cancela con facilidad, sin complicaciones""

---
### 🔹 [36] `atm-high.svg` · Cajero Automático (ATM)
- **Familia Semántica:** Cuenta y Wallet
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/atm-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/atm-high.svg" alt="Cajero Automático (ATM)" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Máquina de cajero automático con pantalla, ranura de tarjeta y teclado; trazo fino outline.

- **Concepto Semántico:** Cajero automático para retiro y operaciones en efectivo
- **Intención de Negocio:** Localizar y utilizar cajeros Visa en la red global
- **Disparadores Clave (Triggers):** `ATM`, `cajero`, `efectivo`, `retiro`, `cajero automático`

**Cuándo Usar:**
- ✅ Localizadores de cajeros en apps bancarias
- ✅ Secciones de retiro de efectivo
- ✅ Mapas de red de ATMs Visa

**Cuándo NO Usar (Anti-patrones):**
- ❌ Pagos digitales o sin efectivo
- ❌ Terminales POS de comercio

**Copies de Ejemplo:**
- ""Encuentra el cajero Visa más cercano a ti""
- ""Más de 3 millones de ATMs Visa en el mundo""

---
### 🔹 [37] `savings-account-high.svg` · Cuenta de Ahorros
- **Familia Semántica:** Cuenta y Wallet
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/savings-account-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/savings-account-high.svg" alt="Cuenta de Ahorros" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Alcancía o moneda con flecha hacia arriba indicando crecimiento; trazo fino outline.

- **Concepto Semántico:** Cuenta de ahorros y depósitos
- **Intención de Negocio:** Representar productos de ahorro vinculados a Visa
- **Disparadores Clave (Triggers):** `ahorro`, `savings`, `depósito`, `alcancía`, `cuenta ahorro`

**Cuándo Usar:**
- ✅ Secciones de productos de ahorro
- ✅ Objetivos de ahorro en apps financieras
- ✅ Comparadores de cuentas de ahorro

**Cuándo NO Usar (Anti-patrones):**
- ❌ Cuentas corrientes o de gasto
- ❌ Créditos o préstamos

**Copies de Ejemplo:**
- ""Haz crecer tus ahorros con tu cuenta Visa""
- ""Ahorra más, gana más: tu cuenta Visa de ahorros""

---
### 🔹 [38] `wallet-default-high.svg` · Wallet Digital (Default)
- **Familia Semántica:** Cuenta y Wallet
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/wallet-default-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/wallet-default-high.svg" alt="Wallet Digital (Default)" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Billetera o cartera digital en vista frontal con tarjeta asomando; trazo fino outline.

- **Concepto Semántico:** Billetera digital predeterminada
- **Intención de Negocio:** Representar el wallet digital como método de pago principal
- **Disparadores Clave (Triggers):** `wallet`, `billetera digital`, `monedero`, `digital wallet`, `cartera`

**Cuándo Usar:**
- ✅ Sección principal de wallet en apps
- ✅ Selección de método de pago por default
- ✅ Onboarding de wallet digital

**Cuándo NO Usar (Anti-patrones):**
- ❌ Tarjetas físicas específicas
- ❌ Cuentas bancarias tradicionales

**Copies de Ejemplo:**
- ""Tu wallet Visa: todo lo que necesitas en tu celular""
- ""Paga con tu wallet digital Visa en cualquier lugar""

---
### 🔹 [39] `wallet-high.svg` · Wallet
- **Familia Semántica:** Cuenta y Wallet
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/wallet-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/wallet-high.svg" alt="Wallet" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Billetera cerrada con detalle de pliegue; trazo fino outline.

- **Concepto Semántico:** Monedero o billetera digital general
- **Intención de Negocio:** Representar el concepto de wallet o monedero de pago
- **Disparadores Clave (Triggers):** `wallet`, `monedero`, `billetera`, `cartera digital`, `portafolios de pago`

**Cuándo Usar:**
- ✅ Íconos de sección de wallet en navegación
- ✅ Representación general de medios de pago
- ✅ Materiales de educación sobre wallets

**Cuándo NO Usar (Anti-patrones):**
- ❌ Efectivo físico específicamente
- ❌ Cuentas bancarias sin función wallet

**Copies de Ejemplo:**
- ""Lleva tu Visa siempre contigo en tu wallet digital""
- ""Todo el poder de tu cartera en tu smartphone""

---
## 🌐 Categoría: Divisas
> **7 iconos en esta categoría.**
### 🔹 [40] `currency-convert-alt-high.svg` · Convertir Divisa (Alt)
- **Familia Semántica:** Divisas
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-convert-alt-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-convert-alt-high.svg" alt="Convertir Divisa (Alt)" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Dos flechas circulares opuestas alrededor de símbolos de moneda; variante de composición alternativa; trazo fino outline.

- **Concepto Semántico:** Conversión de moneda en variante visual alternativa
- **Intención de Negocio:** Representar el proceso de cambio de divisa
- **Disparadores Clave (Triggers):** `conversión`, `cambio de moneda`, `convert`, `FX`, `tipo de cambio`

**Cuándo Usar:**
- ✅ Herramientas de conversión de moneda
- ✅ Secciones de tipo de cambio en apps
- ✅ Materiales de viaje internacional

**Cuándo NO Usar (Anti-patrones):**
- ❌ Moneda local sin conversión
- ❌ Pagos en moneda única

**Copies de Ejemplo:**
- ""Convierte tu dinero al mejor tipo de cambio con Visa""
- ""Sin sorpresas: conoce la conversión antes de pagar""

---
### 🔹 [41] `currency-convert-high.svg` · Convertir Divisa
- **Familia Semántica:** Divisas
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-convert-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-convert-high.svg" alt="Convertir Divisa" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Flechas de intercambio bidireccionales con símbolos de moneda a cada lado; trazo fino outline.

- **Concepto Semántico:** Conversión de divisas estándar
- **Intención de Negocio:** Facilitar el entendimiento y uso de conversión de moneda Visa
- **Disparadores Clave (Triggers):** `conversión de divisas`, `exchange rate`, `cambio`, `FX`, `moneda extranjera`

**Cuándo Usar:**
- ✅ Convertidor de divisas en apps de viaje
- ✅ Cálculo de tipo de cambio en e-commerce internacional
- ✅ Materiales de Visa Global Currency

**Cuándo NO Usar (Anti-patrones):**
- ❌ Transacciones en moneda doméstica
- ❌ Pagos locales sin conversión

**Copies de Ejemplo:**
- ""Viaja sin preocupaciones: Visa convierte al tipo de cambio justo""
- ""Compra en el extranjero y Visa hace la conversión automática""

---
### 🔹 [42] `currency-euro-high.svg` · Euro (€)
- **Familia Semántica:** Divisas
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-euro-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-euro-high.svg" alt="Euro (€)" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Símbolo del euro (€) estilizado en trazo fino outline.

- **Concepto Semántico:** Moneda euro de la zona europea
- **Intención de Negocio:** Representar transacciones o precios en euros
- **Disparadores Clave (Triggers):** `euro`, `EUR`, `€`, `moneda europea`, `zona euro`

**Cuándo Usar:**
- ✅ Precios en euros en plataformas europeas
- ✅ Opciones de divisa en configuración de cuenta
- ✅ Materiales de pagos internacionales en Europa

**Cuándo NO Usar (Anti-patrones):**
- ❌ Otras divisas (usar ícono específico de esa moneda)
- ❌ Precios en moneda local de LATAM

**Copies de Ejemplo:**
- ""Paga en euros con tu Visa sin comisiones adicionales""
- ""Tu Visa acepta euros en toda Europa""

---
### 🔹 [43] `currency-high.svg` · Divisa Genérica
- **Familia Semántica:** Divisas
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-high.svg" alt="Divisa Genérica" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Símbolo genérico de moneda (círculo con líneas de valor) o moneda de diseño neutro; trazo fino outline.

- **Concepto Semántico:** Moneda o divisa en sentido general
- **Intención de Negocio:** Representar el concepto de dinero o moneda de forma neutral
- **Disparadores Clave (Triggers):** `moneda`, `divisa`, `currency`, `dinero`, `valor monetario`

**Cuándo Usar:**
- ✅ Secciones de configuración de moneda
- ✅ Representación genérica de valor económico
- ✅ Materiales sin moneda específica

**Cuándo NO Usar (Anti-patrones):**
- ❌ Cuando se necesita una divisa específica
- ❌ Contextos de pagos sin dinero explícito

**Copies de Ejemplo:**
- ""Elige tu divisa preferida para pagar con Visa""
- ""Visa acepta todas las divisas del mundo""

---
### 🔹 [44] `currency-pound-high.svg` · Libra Esterlina (£)
- **Familia Semántica:** Divisas
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-pound-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-pound-high.svg" alt="Libra Esterlina (£)" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Símbolo de la libra esterlina (£) en trazo fino outline.

- **Concepto Semántico:** Moneda libra esterlina del Reino Unido
- **Intención de Negocio:** Representar transacciones en libras para mercado UK
- **Disparadores Clave (Triggers):** `libra`, `GBP`, `£`, `sterling`, `Reino Unido`

**Cuándo Usar:**
- ✅ Plataformas con operaciones en el Reino Unido
- ✅ Selección de divisa GBP en apps internacionales
- ✅ Materiales de pagos en UK

**Cuándo NO Usar (Anti-patrones):**
- ❌ Otras divisas europeas o americanas
- ❌ Pagos en zona euro

**Copies de Ejemplo:**
- ""Paga en libras con tu Visa sin preocuparte por el cambio""
- ""Tu Visa te conecta con el mercado del Reino Unido""

---
### 🔹 [45] `currency-usd-high.svg` · Dólar (USD)
- **Familia Semántica:** Divisas
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-usd-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-usd-high.svg" alt="Dólar (USD)" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Símbolo del dólar ($) estilizado en trazo fino outline.

- **Concepto Semántico:** Moneda dólar estadounidense
- **Intención de Negocio:** Representar el dólar como divisa de referencia
- **Disparadores Clave (Triggers):** `dólar`, `USD`, `$`, `dollar`, `moneda americana`

**Cuándo Usar:**
- ✅ Precios en dólares en plataformas globales
- ✅ Conversiones a USD en apps de cambio
- ✅ Materiales de remesas hacia EE.UU.

**Cuándo NO Usar (Anti-patrones):**
- ❌ Monedas locales de LATAM específicas
- ❌ Euros u otras divisas

**Copies de Ejemplo:**
- ""Envía dólares a EE.UU. al instante con Visa""
- ""Tu Visa: la mejor forma de manejar tus dólares""

---
### 🔹 [46] `currency-yen-high.svg` · Yen (¥)
- **Familia Semántica:** Divisas
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-yen-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/currency-yen-high.svg" alt="Yen (¥)" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Símbolo del yen japonés (¥) en trazo fino outline.

- **Concepto Semántico:** Moneda yen japonés y yuan chino
- **Intención de Negocio:** Representar transacciones en mercados asiáticos
- **Disparadores Clave (Triggers):** `yen`, `JPY`, `¥`, `yuan`, `mercado asiático`

**Cuándo Usar:**
- ✅ Plataformas con operaciones en Asia
- ✅ Selección de divisa JPY/CNY en apps
- ✅ Materiales de viaje a Japón/China

**Cuándo NO Usar (Anti-patrones):**
- ❌ Otras divisas fuera del mercado asiático
- ❌ Pagos en mercados occidentales

**Copies de Ejemplo:**
- ""Viaja a Japón con tu Visa y olvídate del cambio de moneda""
- ""Paga en yen con tu Visa donde lo acepten""

---
## 🔐 Categoría: Seguridad
> **21 iconos en esta categoría.**
### 🔹 [47] `auth-code-high.svg` · Código de Autenticación
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/auth-code-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/auth-code-high.svg" alt="Código de Autenticación" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Pantalla o panel con dígitos de código OTP o clave temporal; trazo fino outline.

- **Concepto Semántico:** Código de autenticación temporal (OTP/2FA)
- **Intención de Negocio:** Representar el segundo factor de autenticación en pagos Visa
- **Disparadores Clave (Triggers):** `OTP`, `código`, `autenticación`, `2FA`, `código de seguridad`

**Cuándo Usar:**
- ✅ Flujos de verificación de identidad con código
- ✅ Pantallas de ingreso de OTP
- ✅ Materiales de educación sobre 2FA

**Cuándo NO Usar (Anti-patrones):**
- ❌ Autenticación biométrica (usar auth-face o fingerprint)
- ❌ Contraseñas permanentes

**Copies de Ejemplo:**
- ""Introduce tu código Visa para confirmar la operación""
- ""Doble verificación: tu seguridad es nuestra prioridad""

---
### 🔹 [48] `auth-face-high.svg` · Autenticación Facial
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/auth-face-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/auth-face-high.svg" alt="Autenticación Facial" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Rostro humano con líneas de reconocimiento o puntos de mapeo facial; trazo fino outline.

- **Concepto Semántico:** Autenticación biométrica mediante reconocimiento facial
- **Intención de Negocio:** Representar el acceso seguro mediante biometría facial
- **Disparadores Clave (Triggers):** `face ID`, `reconocimiento facial`, `biometría`, `auth facial`, `face auth`

**Cuándo Usar:**
- ✅ Flujos de login con reconocimiento facial
- ✅ Activación de biometría en apps bancarias
- ✅ Pantallas de configuración de seguridad biométrica

**Cuándo NO Usar (Anti-patrones):**
- ❌ Autenticación por código o PIN
- ❌ Perfiles o avatares sin contexto de seguridad

**Copies de Ejemplo:**
- ""Accede a tu Visa con solo mirar tu pantalla""
- ""Face ID: la forma más segura de autenticarte""

---
### 🔹 [49] `auth-reauthorize-high.svg` · Re-autorización
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/auth-reauthorize-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/auth-reauthorize-high.svg" alt="Re-autorización" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Escudo o ícono de seguridad con flecha circular de renovación; trazo fino outline.

- **Concepto Semántico:** Re-autorización o renovación de sesión de seguridad
- **Intención de Negocio:** Gestionar la caducidad y renovación de autorizaciones
- **Disparadores Clave (Triggers):** `reautorizar`, `renovar sesión`, `re-auth`, `sesión expirada`, `reauthenticate`

**Cuándo Usar:**
- ✅ Pantallas de expiración de sesión
- ✅ Flujos de re-confirmación de identidad
- ✅ Renovación de permisos de acceso

**Cuándo NO Usar (Anti-patrones):**
- ❌ Primera autenticación o login inicial
- ❌ Recuperación de contraseña

**Copies de Ejemplo:**
- ""Tu sesión ha expirado: vuelve a autenticarte con Visa""
- ""Por tu seguridad, confirma nuevamente tu identidad""

---
### 🔹 [50] `auth-voice-high.svg` · Autenticación por Voz
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/auth-voice-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/auth-voice-high.svg" alt="Autenticación por Voz" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Micrófono con ondas de sonido y líneas de reconocimiento de voz; trazo fino outline.

- **Concepto Semántico:** Autenticación biométrica por reconocimiento de voz
- **Intención de Negocio:** Representar acceso seguro mediante biometría vocal
- **Disparadores Clave (Triggers):** `voz`, `voice ID`, `reconocimiento de voz`, `biometría vocal`, `voice auth`

**Cuándo Usar:**
- ✅ Flujos de autenticación por voz en banca telefónica
- ✅ Configuración de biometría vocal en apps
- ✅ Materiales de seguridad avanzada

**Cuándo NO Usar (Anti-patrones):**
- ❌ Autenticación facial o por huella
- ❌ Canales de texto sin audio

**Copies de Ejemplo:**
- ""Confirma pagos con tu voz: rápido y seguro""
- ""Tu voz es tu contraseña con Visa Voice Auth""

---
### 🔹 [51] `device-secure-high.svg` · Dispositivo Seguro
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/device-secure-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/device-secure-high.svg" alt="Dispositivo Seguro" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Smartphone o dispositivo con candado o escudo de seguridad superpuesto; trazo fino outline.

- **Concepto Semántico:** Dispositivo protegido y certificado como seguro
- **Intención de Negocio:** Comunicar que el dispositivo del usuario está protegido
- **Disparadores Clave (Triggers):** `dispositivo seguro`, `device security`, `móvil protegido`, `trusted device`, `seguridad dispositivo`

**Cuándo Usar:**
- ✅ Pantallas de confirmación de dispositivo confiable
- ✅ Configuración de seguridad de dispositivo
- ✅ Alertas de dispositivo nuevo detectado

**Cuándo NO Usar (Anti-patrones):**
- ❌ Seguridad de red o servidor
- ❌ Cuentas sin relación a dispositivo

**Copies de Ejemplo:**
- ""Tu dispositivo está certificado como seguro por Visa""
- ""Pagos seguros desde tu dispositivo de confianza""

---
### 🔹 [52] `fingerprint-high.svg` · Huella Digital
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/fingerprint-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/fingerprint-high.svg" alt="Huella Digital" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Patrón de huella digital con líneas concéntricas características; trazo fino outline.

- **Concepto Semántico:** Autenticación biométrica por huella dactilar
- **Intención de Negocio:** Representar el acceso seguro mediante huella digital
- **Disparadores Clave (Triggers):** `huella digital`, `fingerprint`, `Touch ID`, `biometría`, `dactilar`

**Cuándo Usar:**
- ✅ Botones de login con huella en apps bancarias
- ✅ Configuración de biometría Touch ID
- ✅ Confirmación de pagos con huella

**Cuándo NO Usar (Anti-patrones):**
- ❌ Autenticación facial o por voz
- ❌ Códigos PIN o contraseñas alfanuméricas

**Copies de Ejemplo:**
- ""Paga con tu huella: rápido, fácil y seguro""
- ""Touch ID Visa: confirma en un toque""

---
### 🔹 [53] `fraud-high.svg` · Fraude
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/fraud-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/fraud-high.svg" alt="Fraude" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Máscara o figura con símbolo de advertencia indicando actividad fraudulenta; trazo fino outline.

- **Concepto Semántico:** Detección y prevención de fraude
- **Intención de Negocio:** Representar las capacidades antifraude de Visa
- **Disparadores Clave (Triggers):** `fraude`, `fraud`, `alerta fraude`, `actividad sospechosa`, `antifraude`

**Cuándo Usar:**
- ✅ Secciones de seguridad y protección antifraude
- ✅ Alertas de actividad sospechosa
- ✅ Materiales sobre tecnología de detección Visa

**Cuándo NO Usar (Anti-patrones):**
- ❌ Transacciones legítimas sin contexto de riesgo
- ❌ Mensajes positivos de confirmación

**Copies de Ejemplo:**
- ""Visa protege cada transacción contra el fraude""
- ""Detección inteligente de fraude: siempre vigilamos por ti""

---
### 🔹 [54] `id-number-high.svg` · Número de Identificación
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/id-number-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/id-number-high.svg" alt="Número de Identificación" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Documento de identidad o tarjeta con número visible y líneas de texto; trazo fino outline.

- **Concepto Semántico:** Número de identificación oficial del usuario
- **Intención de Negocio:** Representar la captura y verificación de ID del usuario
- **Disparadores Clave (Triggers):** `ID`, `identificación`, `DNI`, `número de ID`, `verificación identidad`

**Cuándo Usar:**
- ✅ Formularios de captura de documento de identidad
- ✅ Flujos KYC de verificación de identidad
- ✅ Pantallas de onboarding con validación de ID

**Cuándo NO Usar (Anti-patrones):**
- ❌ Autenticación biométrica
- ❌ Números de tarjeta bancaria

**Copies de Ejemplo:**
- ""Ingresa tu número de identificación para verificar tu identidad""
- ""KYC seguro: tu ID protegido con Visa""

---
### 🔹 [55] `key-change-high.svg` · Cambiar Contraseña
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/key-change-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/key-change-high.svg" alt="Cambiar Contraseña" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Llave con flecha de cambio o rotación; indica modificación de credencial de acceso; trazo fino outline.

- **Concepto Semántico:** Cambio de contraseña o credenciales de acceso
- **Intención de Negocio:** Representar el proceso de actualización de contraseña
- **Disparadores Clave (Triggers):** `cambiar contraseña`, `change password`, `actualizar clave`, `nueva contraseña`, `reset`

**Cuándo Usar:**
- ✅ Flujos de cambio periódico de contraseña
- ✅ Opciones de seguridad de cuenta
- ✅ Recuperación de acceso con nueva contraseña

**Cuándo NO Usar (Anti-patrones):**
- ❌ Login inicial sin cambio de contraseña
- ❌ Autenticación biométrica

**Copies de Ejemplo:**
- ""Cambia tu contraseña Visa regularmente para mayor seguridad""
- ""Renueva tus credenciales de acceso con un clic""

---
### 🔹 [56] `key-high.svg` · Llave / Clave
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/key-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/key-high.svg" alt="Llave / Clave" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Llave clásica en perfil; trazo fino outline indicando acceso y autenticación.

- **Concepto Semántico:** Clave de acceso o credencial de autenticación
- **Intención de Negocio:** Representar el concepto de acceso y credenciales de forma general
- **Disparadores Clave (Triggers):** `clave`, `llave`, `acceso`, `credencial`, `contraseña`

**Cuándo Usar:**
- ✅ Secciones de gestión de contraseñas
- ✅ Accesos y credenciales en apps de seguridad
- ✅ Metáfora visual de acceso seguro

**Cuándo NO Usar (Anti-patrones):**
- ❌ Llaves físicas o de propiedad sin contexto digital
- ❌ Candados específicos (usar security-lock-high.svg)

**Copies de Ejemplo:**
- ""Tu clave Visa: la puerta a tu seguridad financiera""
- ""Gestiona tus credenciales de acceso con Visa""

---
### 🔹 [57] `password-hide-high.svg` · Ocultar Contraseña
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/password-hide-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/password-hide-high.svg" alt="Ocultar Contraseña" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Ojo con línea diagonal cruzándolo (ojo tachado); indica contraseña oculta; trazo fino outline.

- **Concepto Semántico:** Ocultamiento de contraseña en campo de texto
- **Intención de Negocio:** Controlar la visibilidad de contraseñas en formularios
- **Disparadores Clave (Triggers):** `ocultar contraseña`, `password hide`, `ojo tachado`, `enmascarar`, `privacidad`

**Cuándo Usar:**
- ✅ Campos de contraseña en formularios de login
- ✅ Opción de mostrar/ocultar texto en campos seguros
- ✅ UX de seguridad en apps bancarias

**Cuándo NO Usar (Anti-patrones):**
- ❌ Contextos sin campos de contraseña
- ❌ Visibilidad activa (usar password-show-high.svg)

**Copies de Ejemplo:**
- ""Oculta tu contraseña para mayor privacidad""
- ""Tu contraseña Visa siempre protegida de miradas ajenas""

---
### 🔹 [58] `password-show-high.svg` · Mostrar Contraseña
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/password-show-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/password-show-high.svg" alt="Mostrar Contraseña" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Ojo abierto sin tachado; indica contraseña visible; trazo fino outline.

- **Concepto Semántico:** Visibilidad activa de contraseña en campo de texto
- **Intención de Negocio:** Permitir al usuario ver su contraseña al escribirla
- **Disparadores Clave (Triggers):** `mostrar contraseña`, `password show`, `ojo abierto`, `ver contraseña`, `visibilidad`

**Cuándo Usar:**
- ✅ Toggle de visibilidad en campos de contraseña
- ✅ Formularios de creación de nueva contraseña
- ✅ Verificación de contraseña antes de confirmar

**Cuándo NO Usar (Anti-patrones):**
- ❌ Campos de texto sin contraseña
- ❌ Estado de contraseña oculta (usar password-hide-high.svg)

**Copies de Ejemplo:**
- ""Verifica que escribiste bien tu contraseña Visa""
- ""Muestra y confirma tu clave antes de continuar""

---
### 🔹 [59] `security-firewall-high.svg` · Firewall de Seguridad
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-firewall-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-firewall-high.svg" alt="Firewall de Seguridad" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Escudo con líneas de datos o red representando barrera de seguridad; trazo fino outline.

- **Concepto Semántico:** Protección de red y firewall
- **Intención de Negocio:** Representar la infraestructura de seguridad tecnológica Visa
- **Disparadores Clave (Triggers):** `firewall`, `seguridad de red`, `protección`, `cybersecurity`, `barrera`

**Cuándo Usar:**
- ✅ Materiales técnicos de seguridad Visa
- ✅ Secciones de infraestructura de protección
- ✅ Comunicaciones B2B de seguridad

**Cuándo NO Usar (Anti-patrones):**
- ❌ Seguridad personal del usuario (usar security-high.svg)
- ❌ Contextos de usuario final sin tecnicidad

**Copies de Ejemplo:**
- ""Infraestructura de seguridad Visa: firewall de última generación""
- ""Tu negocio protegido con la tecnología de seguridad Visa""

---
### 🔹 [60] `security-high.svg` · Seguridad
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-high.svg" alt="Seguridad" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Escudo clásico con checkmark o símbolo de protección en el centro; trazo fino outline.

- **Concepto Semántico:** Seguridad y protección en sentido general
- **Intención de Negocio:** Comunicar el compromiso de Visa con la seguridad del usuario
- **Disparadores Clave (Triggers):** `seguridad`, `protección`, `security`, `escudo`, `safe`

**Cuándo Usar:**
- ✅ Secciones de seguridad en apps y web
- ✅ Mensajes de garantía de seguridad
- ✅ Badges de transacción protegida

**Cuándo NO Usar (Anti-patrones):**
- ❌ Funcionalidades específicas sin mensaje de seguridad
- ❌ Contextos de diseño decorativo

**Copies de Ejemplo:**
- ""Tu dinero seguro con la protección Visa""
- ""Compra con confianza: Visa protege cada transacción""

---
### 🔹 [61] `security-lock-high.svg` · Candado de Seguridad
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-lock-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-lock-high.svg" alt="Candado de Seguridad" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Candado cerrado clásico con arco y cuerpo rectangular; trazo fino outline.

- **Concepto Semántico:** Bloqueo y cifrado de información sensible
- **Intención de Negocio:** Representar el bloqueo y protección de datos
- **Disparadores Clave (Triggers):** `candado`, `lock`, `cifrado`, `encriptado`, `bloqueado`

**Cuándo Usar:**
- ✅ Indicadores de conexión segura/HTTPS
- ✅ Pantallas de datos encriptados
- ✅ Mensajes de información protegida

**Cuándo NO Usar (Anti-patrones):**
- ❌ Desbloqueo o acceso abierto
- ❌ Gestión sin contexto de seguridad

**Copies de Ejemplo:**
- ""Tus datos están bajo llave con Visa""
- ""Encriptación de grado bancario en cada operación""

---
### 🔹 [62] `security-protection-high.svg` · Protección de Seguridad
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-protection-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-protection-high.svg" alt="Protección de Seguridad" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Escudo con líneas de protección adicionales o múltiples capas de defensa; trazo fino outline.

- **Concepto Semántico:** Protección multicapa de seguridad
- **Intención de Negocio:** Comunicar la protección avanzada de Visa
- **Disparadores Clave (Triggers):** `protección`, `multicapa`, `advanced security`, `defensa`, `blindaje`

**Cuándo Usar:**
- ✅ Materiales de seguridad avanzada Visa
- ✅ Secciones de protección al consumidor
- ✅ Garantías de responsabilidad cero por fraude

**Cuándo NO Usar (Anti-patrones):**
- ❌ Seguridad básica o simple
- ❌ Funcionalidades sin enfoque en protección

**Copies de Ejemplo:**
- ""Protección multicapa Visa: siempre un paso adelante""
- ""Responsabilidad cero por fraude: Visa te protege""

---
### 🔹 [63] `security-unlock-high.svg` · Desbloqueo de Seguridad
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-unlock-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/security-unlock-high.svg" alt="Desbloqueo de Seguridad" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Candado abierto con arco levantado; indica acceso desbloqueado; trazo fino outline.

- **Concepto Semántico:** Desbloqueo de acceso o levantamiento de restricción
- **Intención de Negocio:** Representar el proceso de desbloqueo exitoso
- **Disparadores Clave (Triggers):** `desbloquear`, `unlock`, `acceso permitido`, `desbloqueado`, `liberar`

**Cuándo Usar:**
- ✅ Pantallas de desbloqueo de cuenta o tarjeta
- ✅ Confirmación de acceso restaurado
- ✅ Flujos de levantamiento de bloqueo de seguridad

**Cuándo NO Usar (Anti-patrones):**
- ❌ Estados bloqueados o restringidos
- ❌ Candado cerrado indicando protección activa

**Copies de Ejemplo:**
- ""Desbloquea tu cuenta Visa de forma segura y rápida""
- ""Acceso restaurado: bienvenido de vuelta a Visa""

---
### 🔹 [64] `sign-in-high.svg` · Iniciar Sesión
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/sign-in-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/sign-in-high.svg" alt="Iniciar Sesión" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Figura de persona entrando por una puerta o flecha apuntando hacia dentro; trazo fino outline.

- **Concepto Semántico:** Inicio de sesión en la plataforma
- **Intención de Negocio:** Representar el punto de entrada autenticado a servicios Visa
- **Disparadores Clave (Triggers):** `iniciar sesión`, `login`, `sign in`, `acceder`, `entrar`

**Cuándo Usar:**
- ✅ Botones de inicio de sesión en apps y web
- ✅ Pantallas de autenticación de usuario
- ✅ Flujos de login en portales Visa

**Cuándo NO Usar (Anti-patrones):**
- ❌ Cierre de sesión (usar sign-out-high.svg)
- ❌ Registro de nuevo usuario

**Copies de Ejemplo:**
- ""Inicia sesión en tu cuenta Visa""
- ""Accede a todos tus beneficios Visa con un solo login""

---
### 🔹 [65] `sign-out-high.svg` · Cerrar Sesión
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/sign-out-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/sign-out-high.svg" alt="Cerrar Sesión" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Figura de persona saliendo por una puerta o flecha apuntando hacia fuera; trazo fino outline.

- **Concepto Semántico:** Cierre de sesión de la plataforma
- **Intención de Negocio:** Representar el cierre seguro de sesión de usuario
- **Disparadores Clave (Triggers):** `cerrar sesión`, `logout`, `sign out`, `salir`, `desconectar`

**Cuándo Usar:**
- ✅ Botones de cierre de sesión en menús
- ✅ Flujos de desconexión segura
- ✅ Confirmaciones de cierre de sesión

**Cuándo NO Usar (Anti-patrones):**
- ❌ Inicio de sesión (usar sign-in-high.svg)
- ❌ Bloqueo de cuenta permanente

**Copies de Ejemplo:**
- ""Cierra sesión de forma segura en tu app Visa""
- ""Protege tu cuenta: cierra sesión cuando termines""

---
### 🔹 [66] `signature-high.svg` · Firma Digital
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/signature-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/signature-high.svg" alt="Firma Digital" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Trazo de firma cursiva sobre línea base; indica firma autógrafa digital; trazo fino outline.

- **Concepto Semántico:** Firma digital o autorización por firma
- **Intención de Negocio:** Representar la autorización de operaciones mediante firma
- **Disparadores Clave (Triggers):** `firma`, `firma digital`, `signature`, `autorización`, `rúbrica`

**Cuándo Usar:**
- ✅ Flujos de firma de contratos o documentos
- ✅ Autorización de operaciones especiales
- ✅ Materiales de firma electrónica

**Cuándo NO Usar (Anti-patrones):**
- ❌ Autenticación biométrica sin firma
- ❌ Pagos sin requerimiento de autorización especial

**Copies de Ejemplo:**
- ""Firma digitalmente y autoriza tus operaciones con Visa""
- ""Tu firma electrónica: válida, segura y sin papel""

---
### 🔹 [67] `token-high.svg` · Token de Seguridad
- **Familia Semántica:** Seguridad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/token-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/token-high.svg" alt="Token de Seguridad" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Hexágono o forma de token con código interno y símbolo de escudo; trazo fino outline.

- **Concepto Semántico:** Token de pago y tokenización de credenciales
- **Intención de Negocio:** Representar la tokenización como capa de seguridad de Visa
- **Disparadores Clave (Triggers):** `token`, `tokenización`, `VTS`, `pago seguro`, `credencial tokenizada`

**Cuándo Usar:**
- ✅ Materiales técnicos sobre Visa Token Service
- ✅ Explicación de seguridad en pagos digitales
- ✅ Secciones de seguridad avanzada en apps

**Cuándo NO Usar (Anti-patrones):**
- ❌ Pagos físicos sin tokenización
- ❌ Contextos de usuario final sin tecnicidad

**Copies de Ejemplo:**
- ""Visa Token Service: tu tarjeta nunca se expone""
- ""Pagos seguros gracias a la tokenización Visa""

---
## ✈️ Categoría: Viajes
> **11 iconos en esta categoría.**
### 🔹 [68] `check-international-high.svg` · Verificación Internacional
- **Familia Semántica:** Viajes
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/check-international-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/check-international-high.svg" alt="Verificación Internacional" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Checkmark de verificación con globo terráqueo o líneas de latitud/longitud; trazo fino outline.

- **Concepto Semántico:** Verificación de aceptación internacional
- **Intención de Negocio:** Comunicar la aceptación global de Visa
- **Disparadores Clave (Triggers):** `internacional`, `global`, `aceptado worldwide`, `cobertura`, `check global`

**Cuándo Usar:**
- ✅ Secciones de aceptación internacional de Visa
- ✅ Materiales de viaje sobre cobertura
- ✅ Validación de pagos en el extranjero

**Cuándo NO Usar (Anti-patrones):**
- ❌ Verificaciones locales o domésticas
- ❌ Contextos sin viaje o internacionalización

**Copies de Ejemplo:**
- ""Tu Visa es aceptada en más de 200 países""
- ""Viaja y paga: Visa te da acceso al mundo""

---
### 🔹 [69] `global-high.svg` · Global / Mundial
- **Familia Semántica:** Viajes
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/global-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/global-high.svg" alt="Global / Mundial" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Globo terráqueo con meridianos y paralelos; trazo fino outline.

- **Concepto Semántico:** Alcance global y presencia mundial
- **Intención de Negocio:** Representar la red global de Visa
- **Disparadores Clave (Triggers):** `global`, `mundial`, `internacional`, `world`, `cobertura global`

**Cuándo Usar:**
- ✅ Secciones de presencia mundial de Visa
- ✅ Mapas de aceptación global
- ✅ Materiales corporativos de alcance internacional

**Cuándo NO Usar (Anti-patrones):**
- ❌ Operaciones locales o regionales
- ❌ Contextos domésticos sin internacionalización

**Copies de Ejemplo:**
- ""Visa: la red de pagos más grande del mundo""
- ""Conectado globalmente con Visa""

---
### 🔹 [70] `map-directions-high.svg` · Indicaciones de Mapa
- **Familia Semántica:** Viajes
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/map-directions-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/map-directions-high.svg" alt="Indicaciones de Mapa" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Mapa con flechas de ruta o línea de navegación entre dos puntos; trazo fino outline.

- **Concepto Semántico:** Indicaciones de ruta y navegación
- **Intención de Negocio:** Representar la guía de navegación para encontrar servicios Visa
- **Disparadores Clave (Triggers):** `indicaciones`, `ruta`, `navegación`, `cómo llegar`, `directions`

**Cuándo Usar:**
- ✅ Localizadores de cajeros o comercios Visa
- ✅ Guías de viaje con ruta a destino
- ✅ Apps de navegación con servicios Visa

**Cuándo NO Usar (Anti-patrones):**
- ❌ Ubicación estática sin ruta
- ❌ Mapas sin indicación de movimiento

**Copies de Ejemplo:**
- ""Encuentra la ruta al cajero Visa más cercano""
- ""Navega hacia los mejores comercios Visa""

---
### 🔹 [71] `map-high.svg` · Mapa
- **Familia Semántica:** Viajes
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/map-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/map-high.svg" alt="Mapa" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Plano de mapa estilizado con calles o cuadrícula; trazo fino outline.

- **Concepto Semántico:** Mapa de ubicación y geografía
- **Intención de Negocio:** Representar mapas para localización de servicios
- **Disparadores Clave (Triggers):** `mapa`, `map`, `ubicación`, `localización`, `geolocalización`

**Cuándo Usar:**
- ✅ Secciones de localizador de servicios
- ✅ Mapas de cobertura Visa por región
- ✅ Herramientas de búsqueda geográfica

**Cuándo NO Usar (Anti-patrones):**
- ❌ Indicaciones de ruta específica
- ❌ Globo terráqueo global

**Copies de Ejemplo:**
- ""Descubre los servicios Visa en tu mapa""
- ""Explora la cobertura Visa en tu ciudad""

---
### 🔹 [72] `map-location-current-high.svg` · Ubicación Actual
- **Familia Semántica:** Viajes
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/map-location-current-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/map-location-current-high.svg" alt="Ubicación Actual" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Pin de mapa con aro de pulso o punto de ubicación actual destacado; trazo fino outline.

- **Concepto Semántico:** Ubicación actual del usuario en tiempo real
- **Intención de Negocio:** Representar la geolocalización del usuario
- **Disparadores Clave (Triggers):** `ubicación actual`, `GPS`, `mi ubicación`, `aquí estoy`, `geolocalización`

**Cuándo Usar:**
- ✅ Botones de usar ubicación actual en localizadores
- ✅ Apps de mapa con posición del usuario
- ✅ Servicios basados en proximidad

**Cuándo NO Usar (Anti-patrones):**
- ❌ Ubicaciones guardadas o favoritas
- ❌ Destinos o puntos de llegada

**Copies de Ejemplo:**
- ""Usa tu ubicación para encontrar servicios Visa cercanos""
- ""Estás aquí: descubre Visa a tu alrededor""

---
### 🔹 [73] `map-location-high.svg` · Pin de Ubicación
- **Familia Semántica:** Viajes
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/map-location-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/map-location-high.svg" alt="Pin de Ubicación" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Pin de mapa o marcador de posición clásico (forma de lágrima invertida); trazo fino outline.

- **Concepto Semántico:** Marcador de ubicación en mapa
- **Intención de Negocio:** Representar puntos de interés o ubicaciones de servicio
- **Disparadores Clave (Triggers):** `pin`, `ubicación`, `marcador`, `location`, `punto de interés`

**Cuándo Usar:**
- ✅ Marcadores de cajeros, comercios o sucursales Visa
- ✅ Pins de destino en apps de viaje
- ✅ Indicadores de lugar en mapas

**Cuándo NO Usar (Anti-patrones):**
- ❌ Ubicación actual del usuario
- ❌ Rutas o indicaciones de navegación

**Copies de Ejemplo:**
- ""Encuentra puntos de servicio Visa en el mapa""
- ""Marca tus destinos favoritos con Visa""

---
### 🔹 [74] `roadsign-high.svg` · Señal de Tráfico
- **Familia Semántica:** Viajes
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/roadsign-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/roadsign-high.svg" alt="Señal de Tráfico" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Señal de tráfico rectangular o romboidal sobre poste; trazo fino outline.

- **Concepto Semántico:** Señal de orientación o indicación de dirección
- **Intención de Negocio:** Representar orientación y guía en contextos de viaje
- **Disparadores Clave (Triggers):** `señal`, `tráfico`, `indicación`, `orientación`, `travel sign`

**Cuándo Usar:**
- ✅ Materiales de viaje y turismo con Visa
- ✅ Guías de destino y orientación
- ✅ Secciones de beneficios de viaje

**Cuándo NO Usar (Anti-patrones):**
- ❌ Mapas digitales o geolocalización
- ❌ Contextos urbanos sin viaje

**Copies de Ejemplo:**
- ""Viaja con Visa y nunca pierdas el rumbo""
- ""Tu guía de viaje financiero: Visa""

---
### 🔹 [75] `transit-airplane-high.svg` · Avión
- **Familia Semántica:** Viajes
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/transit-airplane-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/transit-airplane-high.svg" alt="Avión" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Silueta de avión en vista lateral o desde arriba; trazo fino outline.

- **Concepto Semántico:** Transporte aéreo y viajes en avión
- **Intención de Negocio:** Representar beneficios y servicios de viaje aéreo Visa
- **Disparadores Clave (Triggers):** `avión`, `vuelo`, `aeropuerto`, `viaje aéreo`, `travel`

**Cuándo Usar:**
- ✅ Beneficios de sala VIP aeroportuaria
- ✅ Seguros de viaje aéreo con Visa
- ✅ Materiales de tarjetas de viaje

**Cuándo NO Usar (Anti-patrones):**
- ❌ Transporte terrestre o marítimo
- ❌ Pagos sin contexto de viaje

**Copies de Ejemplo:**
- ""Vuela con los beneficios exclusivos de tu Visa""
- ""Acceso a salas VIP en aeropuertos de todo el mundo""

---
### 🔹 [76] `transit-car-high.svg` · Automóvil
- **Familia Semántica:** Viajes
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/transit-car-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/transit-car-high.svg" alt="Automóvil" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Silueta de automóvil en vista lateral; trazo fino outline.

- **Concepto Semántico:** Transporte terrestre y movilidad
- **Intención de Negocio:** Representar beneficios de movilidad y renta de autos con Visa
- **Disparadores Clave (Triggers):** `auto`, `coche`, `renta de auto`, `movilidad`, `transporte terrestre`

**Cuándo Usar:**
- ✅ Beneficios de renta de autos con Visa
- ✅ Seguros de vehículo para viajeros
- ✅ Apps de movilidad con pago Visa

**Cuándo NO Usar (Anti-patrones):**
- ❌ Transporte aéreo o marítimo
- ❌ Pagos sin contexto de movilidad

**Copies de Ejemplo:**
- ""Renta tu auto con Visa y viaja con seguro incluido""
- ""Movilidad total: tu Visa te lleva a donde quieras""

---
### 🔹 [77] `transit-train-high.svg` · Tren
- **Familia Semántica:** Viajes
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/transit-train-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/transit-train-high.svg" alt="Tren" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Locomotora o vagón de tren en vista lateral; trazo fino outline.

- **Concepto Semántico:** Transporte ferroviario y tránsito urbano
- **Intención de Negocio:** Representar pagos en transporte público y trenes
- **Disparadores Clave (Triggers):** `tren`, `metro`, `ferrocarril`, `tránsito`, `transporte público`

**Cuándo Usar:**
- ✅ Pagos de transporte público con Visa
- ✅ Beneficios de viaje en tren con tarjeta
- ✅ Secciones de movilidad urbana

**Cuándo NO Usar (Anti-patrones):**
- ❌ Transporte aéreo o en auto
- ❌ Pagos en comercio sin transporte

**Copies de Ejemplo:**
- ""Paga tu tren con Visa: rápido y sin efectivo""
- ""Movilidad urbana con tu Visa: sube y paga""

---
### 🔹 [78] `travel-notifications-high.svg` · Notificaciones de Viaje
- **Familia Semántica:** Viajes
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/travel-notifications-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/travel-notifications-high.svg" alt="Notificaciones de Viaje" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Avión o maleta con campana de notificación; trazo fino outline.

- **Concepto Semántico:** Alertas y notificaciones relacionadas con viajes
- **Intención de Negocio:** Mantener al usuario informado sobre operaciones en viaje
- **Disparadores Clave (Triggers):** `notificaciones viaje`, `alerta viaje`, `travel alert`, `aviso`, `push viaje`

**Cuándo Usar:**
- ✅ Configuración de notificaciones de viaje en apps
- ✅ Alertas de uso de tarjeta en el extranjero
- ✅ Avisos de beneficios activados en viaje

**Cuándo NO Usar (Anti-patrones):**
- ❌ Notificaciones generales sin contexto de viaje
- ❌ Alertas de seguridad domésticas

**Copies de Ejemplo:**
- ""Activa las notificaciones de viaje y nunca te pierdas nada""
- ""Visa te avisa de cada movimiento mientras viajas""

---
## 🏪 Categoría: Comercio
> **13 iconos en esta categoría.**
### 🔹 [79] `acquirer-high.svg` · Adquirente
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/acquirer-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/acquirer-high.svg" alt="Adquirente" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Edificio de institución financiera con símbolo de procesamiento; trazo fino outline.

- **Concepto Semántico:** Banco o entidad adquirente en el ecosistema de pagos
- **Intención de Negocio:** Representar el rol del adquirente en la cadena de pago Visa
- **Disparadores Clave (Triggers):** `adquirente`, `acquirer`, `banco adquirente`, `procesador`, `merchant bank`

**Cuándo Usar:**
- ✅ Materiales técnicos del ecosistema de pagos
- ✅ Diagramas de flujo de transacción
- ✅ Comunicaciones B2B para instituciones financieras

**Cuándo NO Usar (Anti-patrones):**
- ❌ Comunicaciones al consumidor final
- ❌ Contextos de tarjeta sin backend de procesamiento

**Copies de Ejemplo:**
- ""Soluciones de adquirencia Visa para tu institución""
- ""Procesa pagos Visa con la tecnología más avanzada""

---
### 🔹 [80] `bonus-points-high.svg` · Puntos de Bonificación
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/bonus-points-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/bonus-points-high.svg" alt="Puntos de Bonificación" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Estrella o medalla con símbolo de puntos o número; trazo fino outline.

- **Concepto Semántico:** Puntos de recompensa y programas de bonificación
- **Intención de Negocio:** Comunicar beneficios de acumulación de puntos Visa
- **Disparadores Clave (Triggers):** `puntos`, `bonus`, `recompensas`, `loyalty`, `bonificación`

**Cuándo Usar:**
- ✅ Programas de lealtad y puntos Visa
- ✅ Acumulación de puntos por compra
- ✅ Materiales de beneficios y recompensas

**Cuándo NO Usar (Anti-patrones):**
- ❌ Pagos sin programa de puntos
- ❌ Contextos sin lealtad o beneficios

**Copies de Ejemplo:**
- ""Gana puntos con cada compra y canjéalos por más""
- ""Tus compras Visa te dan puntos que valen mucho""

---
### 🔹 [81] `cart-high.svg` · Carrito de Compras
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/cart-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/cart-high.svg" alt="Carrito de Compras" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Carrito de supermercado con ruedas y cesta; trazo fino outline.

- **Concepto Semántico:** Carrito de compras en e-commerce
- **Intención de Negocio:** Representar la experiencia de compra en línea
- **Disparadores Clave (Triggers):** `carrito`, `compras`, `e-commerce`, `checkout`, `shopping cart`

**Cuándo Usar:**
- ✅ Secciones de e-commerce y tiendas en línea
- ✅ Botones de agregar al carrito
- ✅ Flujos de checkout con pago Visa

**Cuándo NO Usar (Anti-patrones):**
- ❌ Pagos presenciales en POS
- ❌ Transferencias sin contexto de compra

**Copies de Ejemplo:**
- ""Agrega al carrito y paga con Visa al instante""
- ""El checkout más rápido del e-commerce: Visa""

---
### 🔹 [82] `gift-high.svg` · Regalo
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/gift-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/gift-high.svg" alt="Regalo" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Caja de regalo con moño en la parte superior; trazo fino outline.

- **Concepto Semántico:** Regalo, obsequio o tarjeta de regalo
- **Intención de Negocio:** Representar ofertas de regalo y tarjetas de obsequio Visa
- **Disparadores Clave (Triggers):** `regalo`, `gift`, `obsequio`, `gift card`, `presente`

**Cuándo Usar:**
- ✅ Secciones de tarjetas de regalo Visa
- ✅ Promociones de regalo con compra
- ✅ Campañas de temporada navideña

**Cuándo NO Usar (Anti-patrones):**
- ❌ Compras regulares sin elemento de regalo
- ❌ Recompensas de programa de puntos

**Copies de Ejemplo:**
- ""Regala experiencias con una Visa Gift Card""
- ""El regalo perfecto para quien lo tiene todo: una Visa""

---
### 🔹 [83] `issuer-high.svg` · Emisor
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/issuer-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/issuer-high.svg" alt="Emisor" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Banco o institución emisora con símbolo de tarjeta o emisión; trazo fino outline.

- **Concepto Semántico:** Banco emisor de tarjetas Visa
- **Intención de Negocio:** Representar el rol del banco emisor en el ecosistema
- **Disparadores Clave (Triggers):** `emisor`, `issuer`, `banco emisor`, `institución emisora`, `card issuer`

**Cuándo Usar:**
- ✅ Materiales técnicos de ecosistema de pagos
- ✅ Comunicaciones B2B para bancos emisores
- ✅ Diagramas de flujo de autorización

**Cuándo NO Usar (Anti-patrones):**
- ❌ Comunicaciones al consumidor final
- ❌ Comercios o merchants

**Copies de Ejemplo:**
- ""Beneficios para bancos emisores con Visa""
- ""Emite tarjetas Visa con la tecnología más avanzada""

---
### 🔹 [84] `marketplace-high.svg` · Marketplace
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/marketplace-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/marketplace-high.svg" alt="Marketplace" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Varios puestos de tienda bajo marquesina o plataforma digital con múltiples vendedores; trazo fino outline.

- **Concepto Semántico:** Mercado digital con múltiples vendedores
- **Intención de Negocio:** Representar plataformas de marketplace y e-commerce multivendedor
- **Disparadores Clave (Triggers):** `marketplace`, `mercado digital`, `plataforma`, `multivendedor`, `tienda online`

**Cuándo Usar:**
- ✅ Integración de Visa en plataformas marketplace
- ✅ Materiales de e-commerce para plataformas
- ✅ Secciones de múltiples vendedores

**Cuándo NO Usar (Anti-patrones):**
- ❌ Tiendas físicas sin presencia digital
- ❌ Comercio de un solo vendedor

**Copies de Ejemplo:**
- ""Acepta Visa en tu marketplace y llega a más compradores""
- ""Visa: el método de pago preferido del marketplace""

---
### 🔹 [85] `merchant-high.svg` · Comerciante
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/merchant-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/merchant-high.svg" alt="Comerciante" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Edificio de tienda o persona con símbolo de comercio; trazo fino outline.

- **Concepto Semántico:** Comerciante o negocio aceptante de Visa
- **Intención de Negocio:** Representar a los merchants en el ecosistema Visa
- **Disparadores Clave (Triggers):** `comerciante`, `merchant`, `negocio`, `tienda`, `aceptante`

**Cuándo Usar:**
- ✅ Materiales de aceptación para comercios
- ✅ Secciones de beneficios para merchants
- ✅ Portales de gestión de comercio

**Cuándo NO Usar (Anti-patrones):**
- ❌ Consumidores o tarjetahabientes
- ❌ Bancos o instituciones financieras

**Copies de Ejemplo:**
- ""Sé parte de la red Visa: acepta pagos en tu negocio""
- ""Merchants Visa: más ventas, más clientes""

---
### 🔹 [86] `offers-deal-high.svg` · Oferta / Deal
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/offers-deal-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/offers-deal-high.svg" alt="Oferta / Deal" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Etiqueta de precio con símbolo de porcentaje o descuento; trazo fino outline.

- **Concepto Semántico:** Ofertas especiales y deals para clientes Visa
- **Intención de Negocio:** Comunicar descuentos y promociones exclusivas
- **Disparadores Clave (Triggers):** `oferta`, `deal`, `descuento`, `promoción`, `oferta especial`

**Cuándo Usar:**
- ✅ Secciones de ofertas y descuentos Visa
- ✅ Materiales de temporadas de rebajas
- ✅ Notificaciones de oferta personalizada

**Cuándo NO Usar (Anti-patrones):**
- ❌ Precios regulares sin descuento
- ❌ Contextos de precio fijo

**Copies de Ejemplo:**
- ""Ofertas exclusivas para tarjetahabientes Visa""
- ""Aprovecha los deals Visa antes de que se acaben""

---
### 🔹 [87] `offers-high.svg` · Ofertas
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/offers-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/offers-high.svg" alt="Ofertas" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Etiqueta con símbolo de oferta o estrella de descuento; trazo fino outline.

- **Concepto Semántico:** Sección de ofertas y promociones generales
- **Intención de Negocio:** Representar el catálogo de ofertas disponibles para Visa
- **Disparadores Clave (Triggers):** `ofertas`, `promociones`, `beneficios`, `descuentos`, `deals Visa`

**Cuándo Usar:**
- ✅ Navegación hacia sección de ofertas en apps
- ✅ Catálogo de beneficios Visa
- ✅ Campañas de temporada

**Cuándo NO Usar (Anti-patrones):**
- ❌ Precios normales sin promoción
- ❌ Transacciones sin descuento activo

**Copies de Ejemplo:**
- ""Descubre las ofertas disponibles con tu Visa""
- ""Más beneficios con tu tarjeta: explora las ofertas Visa""

---
### 🔹 [88] `reward-high.svg` · Recompensa
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/reward-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/reward-high.svg" alt="Recompensa" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Trofeo, medalla o copa indicando logro y recompensa; trazo fino outline.

- **Concepto Semántico:** Recompensas y premios del programa de lealtad
- **Intención de Negocio:** Motivar el uso de Visa mediante sistema de recompensas
- **Disparadores Clave (Triggers):** `recompensa`, `reward`, `premio`, `lealtad`, `beneficio ganado`

**Cuándo Usar:**
- ✅ Programas de recompensas Visa
- ✅ Canjes de puntos por premios
- ✅ Comunicaciones de logros alcanzados

**Cuándo NO Usar (Anti-patrones):**
- ❌ Pagos sin programa de lealtad
- ❌ Puntos sin canje

**Copies de Ejemplo:**
- ""Tu lealtad tiene recompensa: canjea con Visa""
- ""Cada compra te acerca a tu próxima recompensa Visa""

---
### 🔹 [89] `shipping-high.svg` · Envío / Logística
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/shipping-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/shipping-high.svg" alt="Envío / Logística" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Caja de paquete con flechas de envío o camión de reparto; trazo fino outline.

- **Concepto Semántico:** Envío y logística de compras en línea
- **Intención de Negocio:** Representar la entrega de productos comprados con Visa
- **Disparadores Clave (Triggers):** `envío`, `shipping`, `entrega`, `logística`, `paquete`

**Cuándo Usar:**
- ✅ Seguimiento de envíos en e-commerce
- ✅ Beneficios de envío gratuito con Visa
- ✅ Materiales de protección de compra

**Cuándo NO Usar (Anti-patrones):**
- ❌ Servicios digitales sin envío físico
- ❌ Pagos en POS presencial

**Copies de Ejemplo:**
- ""Envío gratuito en tus compras online con Visa""
- ""Tu paquete está en camino: rastrèalo con Visa""

---
### 🔹 [90] `store-closed-high.svg` · Tienda Cerrada
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/store-closed-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/store-closed-high.svg" alt="Tienda Cerrada" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Fachada de tienda con señal de cerrado o persiana bajada; trazo fino outline.

- **Concepto Semántico:** Comercio cerrado o fuera de servicio
- **Intención de Negocio:** Indicar disponibilidad de comercio en horario o estado
- **Disparadores Clave (Triggers):** `tienda cerrada`, `cerrado`, `fuera de horario`, `no disponible`, `store closed`

**Cuándo Usar:**
- ✅ Indicadores de estado de comercio en localizadores
- ✅ Mensajes de horario de cierre
- ✅ Estados de comercio en apps de ofertas

**Cuándo NO Usar (Anti-patrones):**
- ❌ Comercios abiertos o disponibles
- ❌ Pagos activos en comercio

**Copies de Ejemplo:**
- ""Esta tienda está cerrada, revisa otras opciones Visa""
- ""Vuelve pronto: este comercio abrirá con Visa""

---
### 🔹 [91] `store-open-high.svg` · Tienda Abierta
- **Familia Semántica:** Comercio
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/store-open-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/store-open-high.svg" alt="Tienda Abierta" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Fachada de tienda con puerta abierta o señal de abierto; trazo fino outline.

- **Concepto Semántico:** Comercio abierto y disponible para pago
- **Intención de Negocio:** Indicar disponibilidad de comercio para aceptar Visa
- **Disparadores Clave (Triggers):** `tienda abierta`, `abierto`, `disponible`, `store open`, `en servicio`

**Cuándo Usar:**
- ✅ Indicadores de comercios disponibles en localizadores
- ✅ Filtros de tiendas abiertas en apps
- ✅ Materiales de aceptación de Visa

**Cuándo NO Usar (Anti-patrones):**
- ❌ Comercios cerrados o con horario restringido
- ❌ Pagos digitales sin tienda física

**Copies de Ejemplo:**
- ""¡Abierto y listo para aceptar tu Visa!""
- ""Encuentra comercios abiertos que aceptan Visa cerca de ti""

---
## 📊 Categoría: Analítica
> **6 iconos en esta categoría.**
### 🔹 [92] `analytics-high.svg` · Analítica
- **Familia Semántica:** Analítica
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/analytics-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/analytics-high.svg" alt="Analítica" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Gráfico de barras o línea de tendencia con puntos de datos; trazo fino outline.

- **Concepto Semántico:** Análisis de datos y métricas financieras
- **Intención de Negocio:** Representar las capacidades analíticas de la plataforma Visa
- **Disparadores Clave (Triggers):** `analítica`, `analytics`, `datos`, `métricas`, `análisis`

**Cuándo Usar:**
- ✅ Secciones de analítica en dashboards
- ✅ Materiales de Visa Analytics para emisores
- ✅ Reportes de comportamiento de gasto

**Cuándo NO Usar (Anti-patrones):**
- ❌ Datos sin análisis o visualización
- ❌ Contextos sin métricas o KPIs

**Copies de Ejemplo:**
- ""Analiza el comportamiento de gasto con Visa Analytics""
- ""Datos que impulsan decisiones: Visa Analytics""

---
### 🔹 [93] `dashboard-high.svg` · Dashboard
- **Familia Semántica:** Analítica
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/dashboard-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/dashboard-high.svg" alt="Dashboard" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Pantalla con múltiples gráficos y widgets de información; trazo fino outline.

- **Concepto Semántico:** Panel de control con métricas principales
- **Intención de Negocio:** Representar la vista centralizada de información financiera
- **Disparadores Clave (Triggers):** `dashboard`, `panel de control`, `resumen`, `vista general`, `cockpit`

**Cuándo Usar:**
- ✅ Pantalla principal de apps bancarias
- ✅ Portales de gestión para emisores y merchants
- ✅ Vistas de resumen ejecutivo

**Cuándo NO Usar (Anti-patrones):**
- ❌ Reportes detallados o transacciones individuales
- ❌ Formularios o flujos de proceso

**Copies de Ejemplo:**
- ""Tu dashboard Visa: todo tu mundo financiero en una pantalla""
- ""Panel de control Visa: gestiona y decide con datos en tiempo real""

---
### 🔹 [94] `data-high.svg` · Datos
- **Familia Semántica:** Analítica
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/data-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/data-high.svg" alt="Datos" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Cilindro de base de datos con líneas de datos o flujo de información; trazo fino outline.

- **Concepto Semántico:** Datos e información estructurada
- **Intención de Negocio:** Representar el activo de datos en el ecosistema Visa
- **Disparadores Clave (Triggers):** `datos`, `data`, `base de datos`, `información`, `big data`

**Cuándo Usar:**
- ✅ Secciones de gestión de datos en plataformas
- ✅ Materiales de data science con Visa
- ✅ Comunicaciones sobre privacidad de datos

**Cuándo NO Usar (Anti-patrones):**
- ❌ Analítica visual con gráficas
- ❌ Informes listos para consumo

**Copies de Ejemplo:**
- ""Datos que transforman negocios: Visa Data Solutions""
- ""Tu información es poder: gestiona tus datos con Visa""

---
### 🔹 [95] `report-high.svg` · Reporte
- **Familia Semántica:** Analítica
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/report-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/report-high.svg" alt="Reporte" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Documento con gráfico de barras o líneas en su interior; trazo fino outline.

- **Concepto Semántico:** Reporte y documento de análisis
- **Intención de Negocio:** Representar la generación y acceso a reportes financieros
- **Disparadores Clave (Triggers):** `reporte`, `informe`, `report`, `estado de cuenta`, `documento análisis`

**Cuándo Usar:**
- ✅ Descarga de estados de cuenta y reportes
- ✅ Secciones de informes en portales
- ✅ Generación de reportes de gastos

**Cuándo NO Usar (Anti-patrones):**
- ❌ Datos en tiempo real sin documento
- ❌ Gráficas interactivas sin reporte

**Copies de Ejemplo:**
- ""Genera tu reporte de gastos Visa cuando quieras""
- ""Estados de cuenta claros y detallados con Visa""

---
### 🔹 [96] `statistics-high.svg` · Estadísticas
- **Familia Semántica:** Analítica
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/statistics-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/statistics-high.svg" alt="Estadísticas" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Gráfico de barras verticales con línea de tendencia superpuesta; trazo fino outline.

- **Concepto Semántico:** Estadísticas y análisis cuantitativo
- **Intención de Negocio:** Mostrar métricas estadísticas del comportamiento de pago
- **Disparadores Clave (Triggers):** `estadísticas`, `statistics`, `gráfico`, `barras`, `tendencia`

**Cuándo Usar:**
- ✅ Visualizaciones de estadísticas de uso de tarjeta
- ✅ Comparativas de gasto por categoría
- ✅ Métricas de rendimiento para merchants

**Cuándo NO Usar (Anti-patrones):**
- ❌ Datos cualitativos sin gráfica
- ❌ Documentos sin visualización

**Copies de Ejemplo:**
- ""Tus estadísticas de gasto al detalle con Visa""
- ""Entiende tus finanzas con las estadísticas Visa""

---
### 🔹 [97] `trending-high.svg` · Tendencia
- **Familia Semántica:** Analítica
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/trending-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/trending-high.svg" alt="Tendencia" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Flecha diagonal ascendente con línea de gráfico de tendencia; trazo fino outline.

- **Concepto Semántico:** Tendencias y patrones de crecimiento
- **Intención de Negocio:** Representar el crecimiento y tendencias positivas
- **Disparadores Clave (Triggers):** `tendencia`, `trending`, `crecimiento`, `upward`, `alza`

**Cuándo Usar:**
- ✅ Indicadores de tendencia en dashboards
- ✅ Comunicaciones de crecimiento de uso
- ✅ Métricas positivas de negocio

**Cuándo NO Usar (Anti-patrones):**
- ❌ Tendencias negativas o a la baja
- ❌ Datos estáticos sin dirección

**Copies de Ejemplo:**
- ""Tu negocio en tendencia positiva con Visa""
- ""Las transacciones Visa van en alza: sé parte del crecimiento""

---
## 💬 Categoría: Comunicación
> **14 iconos en esta categoría.**
### 🔹 [98] `chat-high.svg` · Chat
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/chat-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/chat-high.svg" alt="Chat" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Burbuja de chat con puntos de conversación en su interior; trazo fino outline.

- **Concepto Semántico:** Chat y mensajería en tiempo real
- **Intención de Negocio:** Representar comunicación bidireccional en apps Visa
- **Disparadores Clave (Triggers):** `chat`, `mensajería`, `conversación`, `chat en vivo`, `comunicación`

**Cuándo Usar:**
- ✅ Botones de chat en vivo con soporte
- ✅ Secciones de messaging en apps bancarias
- ✅ Chatbots de atención al cliente

**Cuándo NO Usar (Anti-patrones):**
- ❌ Email o comunicación unidireccional
- ❌ Notificaciones push sin respuesta

**Copies de Ejemplo:**
- ""Chatea con soporte Visa en tiempo real""
- ""¿Tienes dudas? Nuestro chat Visa está para ayudarte""

---
### 🔹 [99] `customer-support-high.svg` · Soporte al Cliente
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/customer-support-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/customer-support-high.svg" alt="Soporte al Cliente" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Persona con auricular de diadema o headset de call center; trazo fino outline.

- **Concepto Semántico:** Atención y soporte al cliente
- **Intención de Negocio:** Representar los servicios de asistencia al tarjetahabiente
- **Disparadores Clave (Triggers):** `soporte`, `atención al cliente`, `customer support`, `ayuda`, `servicio`

**Cuándo Usar:**
- ✅ Secciones de contacto y soporte
- ✅ Botones de llamada a centro de atención
- ✅ Páginas de ayuda y asistencia

**Cuándo NO Usar (Anti-patrones):**
- ❌ Comunicación sin asistente humano
- ❌ Automatización sin soporte

**Copies de Ejemplo:**
- ""Soporte Visa disponible 24/7 para ti""
- ""Nuestro equipo está listo para ayudarte en cualquier momento""

---
### 🔹 [100] `email-high.svg` · Email
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/email-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/email-high.svg" alt="Email" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Sobre de carta cerrado con aleta diagonal; trazo fino outline.

- **Concepto Semántico:** Comunicación por correo electrónico
- **Intención de Negocio:** Representar el canal de comunicación por email
- **Disparadores Clave (Triggers):** `email`, `correo`, `e-mail`, `mensaje`, `bandeja de entrada`

**Cuándo Usar:**
- ✅ Formularios de contacto por email
- ✅ Notificaciones de estado de cuenta por correo
- ✅ Suscripciones a newsletters Visa

**Cuándo NO Usar (Anti-patrones):**
- ❌ Chat en tiempo real
- ❌ Notificaciones push móviles

**Copies de Ejemplo:**
- ""Recibe tu estado de cuenta Visa por email""
- ""Suscríbete y recibe las mejores ofertas Visa en tu correo""

---
### 🔹 [101] `error-high.svg` · Error
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/error-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/error-high.svg" alt="Error" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Círculo con "×" o signo de exclamación indicando error; trazo fino outline.

- **Concepto Semántico:** Estado de error o fallo en operación
- **Intención de Negocio:** Comunicar errores y fallos de forma clara al usuario
- **Disparadores Clave (Triggers):** `error`, `fallo`, `problema`, `error de sistema`, `alerta roja`

**Cuándo Usar:**
- ✅ Mensajes de error en formularios
- ✅ Estados de transacción fallida
- ✅ Alertas de fallo de sistema

**Cuándo NO Usar (Anti-patrones):**
- ❌ Operaciones exitosas
- ❌ Advertencias de baja severidad

**Copies de Ejemplo:**
- ""Ocurrió un error al procesar tu pago Visa""
- ""Error detectado: contacta a soporte Visa para ayuda""

---
### 🔹 [102] `help-high.svg` · Ayuda
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/help-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/help-high.svg" alt="Ayuda" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Círculo con signo de interrogación en su interior; trazo fino outline.

- **Concepto Semántico:** Centro de ayuda y soporte informativo
- **Intención de Negocio:** Dirigir al usuario hacia recursos de ayuda
- **Disparadores Clave (Triggers):** `ayuda`, `help`, `FAQ`, `soporte`, `asistencia`

**Cuándo Usar:**
- ✅ Botones de ayuda contextual en apps
- ✅ Iconos de FAQ y preguntas frecuentes
- ✅ Acceso a centro de soporte Visa

**Cuándo NO Usar (Anti-patrones):**
- ❌ Errores específicos (usar error-high.svg)
- ❌ Soporte activo con agente

**Copies de Ejemplo:**
- ""¿Necesitas ayuda? El centro Visa tiene todas las respuestas""
- ""Ayuda Visa: encuentra lo que buscas en segundos""

---
### 🔹 [103] `information-high.svg` · Información
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/information-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/information-high.svg" alt="Información" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Círculo con letra "i" de información en su interior; trazo fino outline.

- **Concepto Semántico:** Información adicional o contextual
- **Intención de Negocio:** Proveer contexto e información adicional al usuario
- **Disparadores Clave (Triggers):** `información`, `info`, `detalle`, `contexto`, `más información`

**Cuándo Usar:**
- ✅ Tooltips de información en interfaces
- ✅ Iconos de detalle en listas
- ✅ Mensajes informativos sin acción requerida

**Cuándo NO Usar (Anti-patrones):**
- ❌ Alertas de error o advertencia
- ❌ Acciones primarias de navegación

**Copies de Ejemplo:**
- ""Más información sobre este beneficio Visa""
- ""Toca para conocer todos los detalles de tu servicio Visa""

---
### 🔹 [104] `message-high.svg` · Mensaje
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/message-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/message-high.svg" alt="Mensaje" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Burbuja de mensaje simple sin puntos o con una línea de texto; trazo fino outline.

- **Concepto Semántico:** Mensaje o comunicación general
- **Intención de Negocio:** Representar mensajes y comunicaciones en la plataforma
- **Disparadores Clave (Triggers):** `mensaje`, `message`, `comunicado`, `aviso`, `texto`

**Cuándo Usar:**
- ✅ Secciones de mensajes en apps bancarias
- ✅ Bandeja de comunicados de Visa
- ✅ Notificaciones de mensaje nuevo

**Cuándo NO Usar (Anti-patrones):**
- ❌ Chat en tiempo real (usar chat-high.svg)
- ❌ Emails formales

**Copies de Ejemplo:**
- ""Tienes un nuevo mensaje de Visa""
- ""Lee tus comunicados Visa directamente en la app""

---
### 🔹 [105] `mobile-success-high.svg` · Éxito en Móvil
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/mobile-success-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/mobile-success-high.svg" alt="Éxito en Móvil" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Smartphone con checkmark o símbolo de éxito en pantalla; trazo fino outline.

- **Concepto Semántico:** Operación exitosa completada en dispositivo móvil
- **Intención de Negocio:** Confirmar el éxito de operaciones realizadas desde móvil
- **Disparadores Clave (Triggers):** `éxito móvil`, `operación exitosa`, `confirmado`, `success mobile`, `pago exitoso móvil`

**Cuándo Usar:**
- ✅ Pantallas de confirmación de pago móvil
- ✅ Mensajes de operación completada
- ✅ Animaciones de éxito en apps

**Cuándo NO Usar (Anti-patrones):**
- ❌ Errores o estados pendientes
- ❌ Operaciones desde desktop

**Copies de Ejemplo:**
- ""¡Pago exitoso! Tu Visa ha procesado la transacción""
- ""Operación completada desde tu móvil con Visa""

---
### 🔹 [106] `notifications-high.svg` · Notificaciones
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/notifications-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/notifications-high.svg" alt="Notificaciones" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Campana con badge de notificación; trazo fino outline.

- **Concepto Semántico:** Sistema de notificaciones y alertas
- **Intención de Negocio:** Representar el centro de notificaciones de la app
- **Disparadores Clave (Triggers):** `notificaciones`, `alertas`, `campana`, `push`, `avisos`

**Cuándo Usar:**
- ✅ Ícono de notificaciones en navegación
- ✅ Centro de alertas de app bancaria
- ✅ Configuración de preferencias de notificación

**Cuándo NO Usar (Anti-patrones):**
- ❌ Mensajes específicos sin sistema de notificación
- ❌ Alertas de error específicas

**Copies de Ejemplo:**
- ""Activa las notificaciones Visa y nunca pierdas un movimiento""
- ""Tus alertas Visa: siempre informado en tiempo real""

---
### 🔹 [107] `phone-high.svg` · Teléfono
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/phone-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/phone-high.svg" alt="Teléfono" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Auricular de teléfono clásico en trazo fino outline.

- **Concepto Semántico:** Comunicación telefónica
- **Intención de Negocio:** Representar el canal de atención telefónica
- **Disparadores Clave (Triggers):** `teléfono`, `llamada`, `phone`, `contacto`, `atención telefónica`

**Cuándo Usar:**
- ✅ Botones de llamar a soporte Visa
- ✅ Información de contacto telefónico
- ✅ Canales de atención al cliente

**Cuándo NO Usar (Anti-patrones):**
- ❌ Comunicación digital o por chat
- ❌ Autenticación por voz

**Copies de Ejemplo:**
- ""Llama al soporte Visa 24/7: estamos aquí para ti""
- ""Un número, toda la ayuda Visa que necesitas""

---
### 🔹 [108] `question-high.svg` · Pregunta
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/question-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/question-high.svg" alt="Pregunta" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Signo de interrogación grande estilizado; trazo fino outline.

- **Concepto Semántico:** Pregunta o duda del usuario
- **Intención de Negocio:** Representar preguntas frecuentes y dudas de usuarios
- **Disparadores Clave (Triggers):** `pregunta`, `duda`, `FAQ`, `¿qué es?`, `consulta`

**Cuándo Usar:**
- ✅ Secciones de preguntas frecuentes
- ✅ Indicadores de duda en formularios
- ✅ Onboarding con preguntas de configuración

**Cuándo NO Usar (Anti-patrones):**
- ❌ Afirmaciones o confirmaciones
- ❌ Errores específicos sin pregunta

**Copies de Ejemplo:**
- ""¿Tienes preguntas sobre tu Visa? Tenemos las respuestas""
- ""FAQ Visa: todo lo que necesitas saber""

---
### 🔹 [109] `success-high.svg` · Éxito
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/success-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/success-high.svg" alt="Éxito" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Círculo con checkmark de verificación en su interior; trazo fino outline.

- **Concepto Semántico:** Confirmación de éxito en operación
- **Intención de Negocio:** Comunicar el resultado positivo de operaciones
- **Disparadores Clave (Triggers):** `éxito`, `exitoso`, `completado`, `success`, `aprobado`

**Cuándo Usar:**
- ✅ Pantallas de confirmación de transacción exitosa
- ✅ Mensajes de operación completada
- ✅ Estados positivos en flujos de pago

**Cuándo NO Usar (Anti-patrones):**
- ❌ Errores o estados de espera
- ❌ Advertencias o precauciones

**Copies de Ejemplo:**
- ""¡Transacción aprobada! Pago exitoso con Visa""
- ""Operación completada: bienvenido al éxito Visa""

---
### 🔹 [110] `support-ticket-high.svg` · Ticket de Soporte
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/support-ticket-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/support-ticket-high.svg" alt="Ticket de Soporte" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Documento o ticket con número de caso y líneas de información; trazo fino outline.

- **Concepto Semántico:** Ticket de soporte o caso de atención al cliente
- **Intención de Negocio:** Gestionar incidencias y casos de soporte Visa
- **Disparadores Clave (Triggers):** `ticket`, `caso`, `incidencia`, `soporte técnico`, `support ticket`

**Cuándo Usar:**
- ✅ Apertura y seguimiento de tickets de soporte
- ✅ Historial de casos de atención
- ✅ Portales de autogestión de incidencias

**Cuándo NO Usar (Anti-patrones):**
- ❌ Chat en tiempo real sin registro de caso
- ❌ FAQs sin generación de ticket

**Copies de Ejemplo:**
- ""Abre un ticket y te ayudamos a resolver tu caso Visa""
- ""Seguimiento de tu incidencia Visa: transparente y rápido""

---
### 🔹 [111] `warning-high.svg` · Advertencia
- **Familia Semántica:** Comunicación
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/warning-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/warning-high.svg" alt="Advertencia" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Triángulo con signo de exclamación en su interior; trazo fino outline.

- **Concepto Semántico:** Advertencia o alerta de precaución
- **Intención de Negocio:** Comunicar situaciones de riesgo o precaución
- **Disparadores Clave (Triggers):** `advertencia`, `alerta`, `precaución`, `warning`, `atención`

**Cuándo Usar:**
- ✅ Alertas de seguridad o riesgo
- ✅ Mensajes de validación con advertencia
- ✅ Avisos de acción con consecuencias importantes

**Cuándo NO Usar (Anti-patrones):**
- ❌ Errores definitivos (usar error-high.svg)
- ❌ Éxitos o confirmaciones positivas

**Copies de Ejemplo:**
- ""Atención: revisa tu información antes de continuar""
- ""Advertencia Visa: actividad inusual en tu cuenta""

---
## 🏢 Categoría: Identidad
> **4 iconos en esta categoría.**
### 🔹 [112] `company-high.svg` · Empresa
- **Familia Semántica:** Identidad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/company-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/company-high.svg" alt="Empresa" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Edificio de oficinas corporativo con múltiples pisos o ventanas; trazo fino outline.

- **Concepto Semántico:** Empresa u organización corporativa
- **Intención de Negocio:** Representar el segmento empresarial en el ecosistema Visa
- **Disparadores Clave (Triggers):** `empresa`, `corporativo`, `negocio`, `organización`, `B2B`

**Cuándo Usar:**
- ✅ Secciones de productos y servicios empresariales
- ✅ Portales B2B para empresas
- ✅ Materiales de Visa Business

**Cuándo NO Usar (Anti-patrones):**
- ❌ Cuentas personales o de consumo
- ❌ Comercios pequeños o individuales

**Copies de Ejemplo:**
- ""Soluciones Visa para empresas de todos los tamaños""
- ""Tu empresa crece con las herramientas financieras Visa""

---
### 🔹 [113] `contact-high.svg` · Contacto
- **Familia Semántica:** Identidad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/contact-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/contact-high.svg" alt="Contacto" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Tarjeta de contacto o persona con información de datos de contacto; trazo fino outline.

- **Concepto Semántico:** Información de contacto de persona o empresa
- **Intención de Negocio:** Representar la gestión de contactos en plataformas Visa
- **Disparadores Clave (Triggers):** `contacto`, `contact`, `agenda`, `directorio`, `información personal`

**Cuándo Usar:**
- ✅ Agendas de contactos en apps bancarias
- ✅ Formularios de contacto en sitios
- ✅ Secciones de información de contacto

**Cuándo NO Usar (Anti-patrones):**
- ❌ Perfiles de usuario sin datos de contacto
- ❌ Tarjetas bancarias específicas

**Copies de Ejemplo:**
- ""Gestiona tus contactos de pago frecuentes en Visa""
- ""Agrega y gestiona tus beneficiarios Visa""

---
### 🔹 [114] `government-high.svg` · Gobierno
- **Familia Semántica:** Identidad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/government-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/government-high.svg" alt="Gobierno" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Edificio gubernamental con columnas o cúpula; trazo fino outline.

- **Concepto Semántico:** Entidad gubernamental o institución pública
- **Intención de Negocio:** Representar pagos y servicios del sector público
- **Disparadores Clave (Triggers):** `gobierno`, `gobierno digital`, `institución pública`, `pagos gobierno`, `G2P`

**Cuándo Usar:**
- ✅ Pagos de servicios gubernamentales
- ✅ Materiales de Government-to-Person (G2P)
- ✅ Secciones de impuestos y servicios públicos

**Cuándo NO Usar (Anti-patrones):**
- ❌ Comercios privados o empresas
- ❌ Personas físicas sin institución

**Copies de Ejemplo:**
- ""Paga tus impuestos y servicios gubernamentales con Visa""
- ""Visa: el puente entre ciudadanos y gobierno digital""

---
### 🔹 [115] `handshake-high.svg` · Alianza / Acuerdo
- **Familia Semántica:** Identidad
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/handshake-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/handshake-high.svg" alt="Alianza / Acuerdo" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Dos manos estrechándose en apretón de manos; trazo fino outline.

- **Concepto Semántico:** Alianza, acuerdo o asociación de negocios
- **Intención de Negocio:** Representar partnerships y relaciones comerciales Visa
- **Disparadores Clave (Triggers):** `alianza`, `acuerdo`, `partnership`, `handshake`, `colaboración`

**Cuándo Usar:**
- ✅ Materiales de partnerships y alianzas Visa
- ✅ Secciones de co-branding y colaboraciones
- ✅ Comunicaciones de acuerdos de negocio

**Cuándo NO Usar (Anti-patrones):**
- ❌ Transacciones individuales sin acuerdo
- ❌ Contextos competitivos sin colaboración

**Copies de Ejemplo:**
- ""Juntos somos más fuertes: alianzas Visa que transforman""
- ""Partnership Visa: crezcamos juntos""

---
## 📱 Categoría: Dispositivos
> **3 iconos en esta categoría.**
### 🔹 [116] `device-laptop-high.svg` · Laptop / Computadora
- **Familia Semántica:** Dispositivos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/device-laptop-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/device-laptop-high.svg" alt="Laptop / Computadora" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Laptop abierta con pantalla y teclado en vista lateral; trazo fino outline.

- **Concepto Semántico:** Computadora portátil como canal de acceso
- **Intención de Negocio:** Representar el acceso a servicios Visa desde desktop/laptop
- **Disparadores Clave (Triggers):** `laptop`, `computadora`, `desktop`, `PC`, `web`

**Cuándo Usar:**
- ✅ Secciones de acceso web a servicios Visa
- ✅ Materiales de banca en línea
- ✅ Instrucciones para uso en computadora

**Cuándo NO Usar (Anti-patrones):**
- ❌ Acceso móvil exclusivamente
- ❌ Terminales físicos de pago

**Copies de Ejemplo:**
- ""Accede a tu cuenta Visa desde tu computadora""
- ""Banca en línea Visa: la potencia de tu PC a tu servicio""

---
### 🔹 [117] `device-mobile-high.svg` · Teléfono Móvil
- **Familia Semántica:** Dispositivos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/device-mobile-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/device-mobile-high.svg" alt="Teléfono Móvil" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Smartphone en vista frontal con pantalla y botón home o sin bisel; trazo fino outline.

- **Concepto Semántico:** Dispositivo móvil como canal principal
- **Intención de Negocio:** Representar el acceso y operación desde smartphone
- **Disparadores Clave (Triggers):** `móvil`, `smartphone`, `celular`, `app móvil`, `mobile`

**Cuándo Usar:**
- ✅ Materiales de banca móvil
- ✅ Instrucciones de descarga de app
- ✅ Secciones de funcionalidades móviles

**Cuándo NO Usar (Anti-patrones):**
- ❌ Acceso web o desktop
- ❌ Terminales físicos de POS

**Copies de Ejemplo:**
- ""Descarga la app Visa y lleva tus finanzas en el bolsillo""
- ""Todo Visa, en tu móvil: fácil, seguro y siempre disponible""

---
### 🔹 [118] `device-wearable-high.svg` · Dispositivo Wearable
- **Familia Semántica:** Dispositivos
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/device-wearable-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/device-wearable-high.svg" alt="Dispositivo Wearable" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Reloj inteligente o pulsera en vista lateral con pantalla pequeña; trazo fino outline.

- **Concepto Semántico:** Dispositivo wearable para pagos sin contacto
- **Intención de Negocio:** Representar pagos y servicios desde smartwatch
- **Disparadores Clave (Triggers):** `wearable`, `smartwatch`, `reloj inteligente`, `pago wearable`, `NFC wearable`

**Cuándo Usar:**
- ✅ Materiales de pago con smartwatch
- ✅ Secciones de Visa en dispositivos wearables
- ✅ Configuración de pago desde reloj

**Cuándo NO Usar (Anti-patrones):**
- ❌ Smartphones convencionales
- ❌ Pagos en POS sin NFC

**Copies de Ejemplo:**
- ""Paga con tu smartwatch: Visa en tu muñeca""
- ""La última frontera del pago sin contacto: tu wearable Visa""

---
## 🖥️ Categoría: UI Esencial
> **37 iconos en esta categoría.**
### 🔹 [119] `add-high.svg` · Agregar
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/add-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/add-high.svg" alt="Agregar" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Símbolo "+" en trazo fino outline, simple y universal.

- **Concepto Semántico:** Acción de agregar o añadir elemento
- **Intención de Negocio:** Acción primaria de creación en interfaces Visa
- **Disparadores Clave (Triggers):** `agregar`, `añadir`, `nuevo`, `add`, `crear`

**Cuándo Usar:**
- ✅ Botones de agregar tarjeta, cuenta o beneficiario
- ✅ FABs de acción principal en apps
- ✅ Formularios de alta de nuevos elementos

**Cuándo NO Usar (Anti-patrones):**
- ❌ Eliminación o sustitución de elementos
- ❌ Acciones de lectura sin modificación

**Copies de Ejemplo:**
- ""Agrega tu tarjeta Visa en segundos""
- ""Suma más beneficios: agrega otra cuenta Visa""

---
### 🔹 [120] `arrow-back-high.svg` · Flecha Atrás
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/arrow-back-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/arrow-back-high.svg" alt="Flecha Atrás" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Flecha apuntando hacia la izquierda; navegación de retroceso; trazo fino outline.

- **Concepto Semántico:** Navegación hacia atrás o anterior
- **Intención de Negocio:** Proporcionar navegación de regreso en flujos Visa
- **Disparadores Clave (Triggers):** `atrás`, `regresar`, `back`, `anterior`, `volver`

**Cuándo Usar:**
- ✅ Botones de retroceso en headers de app
- ✅ Navegación en flujos multi-paso
- ✅ Volver a pantalla anterior

**Cuándo NO Usar (Anti-patrones):**
- ❌ Avance o siguiente paso
- ❌ Cierre de ventana o modal

**Copies de Ejemplo:**
- ""Regresa y revisa tus datos antes de confirmar""
- ""Vuelve atrás con un toque""

---
### 🔹 [121] `arrow-down-high.svg` · Flecha Abajo
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/arrow-down-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/arrow-down-high.svg" alt="Flecha Abajo" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Flecha apuntando hacia abajo; trazo fino outline.

- **Concepto Semántico:** Indicación de movimiento o desplazamiento hacia abajo
- **Intención de Negocio:** Indicar contenido desplegable o descenso
- **Disparadores Clave (Triggers):** `abajo`, `desplegar`, `bajar`, `down`, `scroll`

**Cuándo Usar:**
- ✅ Selectores desplegables
- ✅ Indicadores de scroll
- ✅ Ordenamiento descendente

**Cuándo NO Usar (Anti-patrones):**
- ❌ Movimiento ascendente
- ❌ Flechas de retroceso

**Copies de Ejemplo:**
- ""Desliza hacia abajo para ver más opciones""
- ""Despliega el menú y elige tu preferencia Visa""

---
### 🔹 [122] `arrow-forward-high.svg` · Flecha Adelante
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/arrow-forward-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/arrow-forward-high.svg" alt="Flecha Adelante" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Flecha apuntando hacia la derecha; navegación de avance; trazo fino outline.

- **Concepto Semántico:** Navegación hacia adelante o siguiente
- **Intención de Negocio:** Indicar avance en flujos y navegación
- **Disparadores Clave (Triggers):** `adelante`, `siguiente`, `forward`, `próximo`, `continuar`

**Cuándo Usar:**
- ✅ Botones de siguiente en flujos de onboarding
- ✅ Navegación entre pantallas
- ✅ Carruseles y sliders

**Cuándo NO Usar (Anti-patrones):**
- ❌ Retroceso o navegación hacia atrás
- ❌ Cancelación de flujo

**Copies de Ejemplo:**
- ""Continúa con tu proceso Visa""
- ""Siguiente paso: casi terminas""

---
### 🔹 [123] `arrow-up-high.svg` · Flecha Arriba
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/arrow-up-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/arrow-up-high.svg" alt="Flecha Arriba" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Flecha apuntando hacia arriba; trazo fino outline.

- **Concepto Semántico:** Indicación de movimiento o desplazamiento hacia arriba
- **Intención de Negocio:** Indicar contenido colapsable o ascenso
- **Disparadores Clave (Triggers):** `arriba`, `subir`, `up`, `colapsar`, `scroll up`

**Cuándo Usar:**
- ✅ Botones de scroll al inicio
- ✅ Colapso de secciones desplegadas
- ✅ Ordenamiento ascendente

**Cuándo NO Usar (Anti-patrones):**
- ❌ Movimiento descendente
- ❌ Flechas de avance horizontal

**Copies de Ejemplo:**
- ""Vuelve al inicio de la página""
- ""Colapsa y simplifica tu vista Visa""

---
### 🔹 [124] `calendar-high.svg` · Calendario
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/calendar-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/calendar-high.svg" alt="Calendario" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Cuadrícula de calendario con días numerados y encabezado de mes; trazo fino outline.

- **Concepto Semántico:** Fecha y programación de eventos
- **Intención de Negocio:** Representar programación y fechas de corte en Visa
- **Disparadores Clave (Triggers):** `calendario`, `fecha`, `agenda`, `programar`, `vencimiento`

**Cuándo Usar:**
- ✅ Fechas de corte de tarjeta
- ✅ Programación de pagos
- ✅ Selección de fecha en formularios

**Cuándo NO Usar (Anti-patrones):**
- ❌ Tiempo en horas o minutos
- ❌ Historial sin contexto temporal

**Copies de Ejemplo:**
- ""Consulta tu fecha de corte Visa en el calendario""
- ""Programa tus pagos y nunca te retrases""

---
### 🔹 [125] `check-high.svg` · Check / Palomita
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/check-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/check-high.svg" alt="Check / Palomita" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Checkmark o palomita simple; trazo fino outline.

- **Concepto Semántico:** Selección o confirmación de elemento
- **Intención de Negocio:** Indicar selección de opción en listas o confirmación
- **Disparadores Clave (Triggers):** `check`, `palomita`, `seleccionado`, `confirmado`, `sí`

**Cuándo Usar:**
- ✅ Checkboxes en formularios
- ✅ Confirmación de aceptación de términos
- ✅ Listas de verificación

**Cuándo NO Usar (Anti-patrones):**
- ❌ Negación o exclusión
- ❌ Errores o fallos

**Copies de Ejemplo:**
- ""Confirma tus datos y acepta los términos Visa""
- ""Listo: tu selección está confirmada""

---
### 🔹 [126] `checkmark-high.svg` · Confirmación
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/checkmark-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/checkmark-high.svg" alt="Confirmación" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Checkmark en círculo o de mayor tamaño; trazo fino outline.

- **Concepto Semántico:** Confirmación o validación completada
- **Intención de Negocio:** Comunicar la finalización exitosa de un proceso
- **Disparadores Clave (Triggers):** `confirmado`, `validado`, `aprobado`, `checkmark`, `verificado`

**Cuándo Usar:**
- ✅ Estados de éxito en flujos de pago
- ✅ Validación de formularios completada
- ✅ Confirmaciones de proceso

**Cuándo NO Usar (Anti-patrones):**
- ❌ Estados de error o pendiente
- ❌ Selección simple sin confirmación de proceso

**Copies de Ejemplo:**
- ""Tu pago Visa está confirmado y en proceso""
- ""Todo listo: operación confirmada exitosamente""

---
### 🔹 [127] `chevron-down-high.svg` · Chevron Abajo
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/chevron-down-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/chevron-down-high.svg" alt="Chevron Abajo" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Ángulo apuntando hacia abajo ("v" invertida); trazo fino outline.

- **Concepto Semántico:** Elemento colapsable o desplegable hacia abajo
- **Intención de Negocio:** Indicar menús desplegables y contenido expandible
- **Disparadores Clave (Triggers):** `chevron`, `desplegable`, `abrir menú`, `expandir`, `down arrow`

**Cuándo Usar:**
- ✅ Selectores dropdown
- ✅ Acordeones de FAQ
- ✅ Menús de selección

**Cuándo NO Usar (Anti-patrones):**
- ❌ Flechas de navegación de pantalla completa
- ❌ Scroll de página

**Copies de Ejemplo:**
- ""Despliega para ver todas las opciones""
- ""Abre el menú y elige tu tarjeta Visa""

---
### 🔹 [128] `chevron-left-high.svg` · Chevron Izquierda
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/chevron-left-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/chevron-left-high.svg" alt="Chevron Izquierda" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Ángulo apuntando hacia la izquierda ("<"); trazo fino outline.

- **Concepto Semántico:** Navegación hacia el elemento anterior
- **Intención de Negocio:** Navegar hacia atrás en carruseles o paginación
- **Disparadores Clave (Triggers):** `chevron izquierda`, `anterior`, `prev`, `izquierda`, `back`

**Cuándo Usar:**
- ✅ Carruseles de beneficios Visa
- ✅ Paginación de historial
- ✅ Sliders de tarjetas

**Cuándo NO Usar (Anti-patrones):**
- ❌ Avance o siguiente elemento
- ❌ Retroceso de pantalla completa

**Copies de Ejemplo:**
- ""Desliza para ver el beneficio anterior""
- ""Explora todas tus tarjetas Visa""

---
### 🔹 [129] `chevron-right-high.svg` · Chevron Derecha
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/chevron-right-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/chevron-right-high.svg" alt="Chevron Derecha" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Ángulo apuntando hacia la derecha (">"); trazo fino outline.

- **Concepto Semántico:** Navegación hacia el siguiente elemento
- **Intención de Negocio:** Navegar hacia adelante en carruseles o listas
- **Disparadores Clave (Triggers):** `chevron derecha`, `siguiente`, `next`, `derecha`, `más`

**Cuándo Usar:**
- ✅ Listas de ítems con detalle expandible
- ✅ Carruseles de productos Visa
- ✅ Navegación en paginación

**Cuándo NO Usar (Anti-patrones):**
- ❌ Retroceso o elemento anterior
- ❌ Acciones primarias de CTA

**Copies de Ejemplo:**
- ""Toca para ver los detalles de tu beneficio""
- ""Explora más con un deslizamiento""

---
### 🔹 [130] `chevron-up-high.svg` · Chevron Arriba
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/chevron-up-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/chevron-up-high.svg" alt="Chevron Arriba" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Ángulo apuntando hacia arriba ("^"); trazo fino outline.

- **Concepto Semántico:** Elemento colapsable hacia arriba
- **Intención de Negocio:** Indicar contenido colapsable abierto
- **Disparadores Clave (Triggers):** `chevron arriba`, `colapsar`, `cerrar menú`, `up arrow`, `collapse`

**Cuándo Usar:**
- ✅ Acordeones de preguntas frecuentes abiertos
- ✅ Paneles expandidos que se pueden colapsar
- ✅ Menús abiertos

**Cuándo NO Usar (Anti-patrones):**
- ❌ Expansión de contenido hacia abajo
- ❌ Scroll de página completa

**Copies de Ejemplo:**
- ""Colapsa la sección para simplificar la vista""
- ""Cierra el menú y continúa""

---
### 🔹 [131] `close-high.svg` · Cerrar
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/close-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/close-high.svg" alt="Cerrar" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Símbolo "×" o "X" en trazo fino outline.

- **Concepto Semántico:** Cerrar, descartar o cancelar elemento
- **Intención de Negocio:** Proporcionar control de cierre en modales y notificaciones
- **Disparadores Clave (Triggers):** `cerrar`, `descartar`, `cancelar`, `close`, `X`

**Cuándo Usar:**
- ✅ Botones de cierre en modales y sidesheets
- ✅ Descarte de notificaciones
- ✅ Cancelación de flujos

**Cuándo NO Usar (Anti-patrones):**
- ❌ Eliminación definitiva (diferente de cerrar)
- ❌ Confirmación o aceptación

**Copies de Ejemplo:**
- ""Cierra esta ventana y regresa""
- ""Descarta la alerta y continúa con Visa""

---
### 🔹 [132] `copy-high.svg` · Copiar
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/copy-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/copy-high.svg" alt="Copiar" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Dos rectángulos superpuestos indicando acción de copiar; trazo fino outline.

- **Concepto Semántico:** Copia de texto o información al portapapeles
- **Intención de Negocio:** Facilitar la copia de datos como número de tarjeta o CLABE
- **Disparadores Clave (Triggers):** `copiar`, `copy`, `clipboard`, `duplicar`, `copiar al portapapeles`

**Cuándo Usar:**
- ✅ Botones de copiar CLABE o número de cuenta
- ✅ Copia de código de referencia
- ✅ Duplicar elementos en formularios

**Cuándo NO Usar (Anti-patrones):**
- ❌ Pegado de información (acción inversa)
- ❌ Eliminación de datos

**Copies de Ejemplo:**
- ""Copia tu número de cuenta Visa con un toque""
- ""Comparte tu CLABE Visa fácilmente""

---
### 🔹 [133] `delete-high.svg` · Eliminar
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/delete-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/delete-high.svg" alt="Eliminar" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Ícono de papelera o bote de basura; trazo fino outline.

- **Concepto Semántico:** Eliminación definitiva de elemento
- **Intención de Negocio:** Representar la acción de borrado permanente
- **Disparadores Clave (Triggers):** `eliminar`, `borrar`, `delete`, `papelera`, `remover`

**Cuándo Usar:**
- ✅ Eliminación de tarjeta guardada
- ✅ Borrado de beneficiario
- ✅ Eliminación de cuenta bancaria

**Cuándo NO Usar (Anti-patrones):**
- ❌ Cierre temporal o suspensión (no definitiva)
- ❌ Ocultamiento sin borrado

**Copies de Ejemplo:**
- ""Elimina esta tarjeta de tu lista de métodos de pago""
- ""¿Seguro que deseas borrar este beneficiario?""

---
### 🔹 [134] `edit-high.svg` · Editar
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/edit-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/edit-high.svg" alt="Editar" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Lápiz o pluma en posición de escritura; trazo fino outline.

- **Concepto Semántico:** Edición y modificación de información
- **Intención de Negocio:** Representar la acción de modificar datos del usuario
- **Disparadores Clave (Triggers):** `editar`, `modificar`, `edit`, `cambiar`, `actualizar`

**Cuándo Usar:**
- ✅ Botones de editar datos de perfil
- ✅ Modificación de límites de tarjeta
- ✅ Edición de beneficiarios

**Cuándo NO Usar (Anti-patrones):**
- ❌ Visualización sin modificación
- ❌ Eliminación de datos

**Copies de Ejemplo:**
- ""Edita tus datos Visa cuando lo necesites""
- ""Actualiza tu información y mantén tu cuenta al día""

---
### 🔹 [135] `export-high.svg` · Exportar
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/export-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/export-high.svg" alt="Exportar" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Flecha saliendo de un cuadrado o nube; indica exportación; trazo fino outline.

- **Concepto Semántico:** Exportación de datos o documentos
- **Intención de Negocio:** Representar la descarga y exportación de información
- **Disparadores Clave (Triggers):** `exportar`, `export`, `descargar`, `compartir archivo`, `generar archivo`

**Cuándo Usar:**
- ✅ Exportación de estados de cuenta a PDF/Excel
- ✅ Descarga de reportes de gasto
- ✅ Exportar historial de transacciones

**Cuándo NO Usar (Anti-patrones):**
- ❌ Importación de datos externos
- ❌ Subida de archivos

**Copies de Ejemplo:**
- ""Exporta tu estado de cuenta Visa en formato PDF""
- ""Descarga tu historial de transacciones para análisis""

---
### 🔹 [136] `file-download-high.svg` · Descargar Archivo
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/file-download-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/file-download-high.svg" alt="Descargar Archivo" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Documento con flecha apuntando hacia abajo indicando descarga; trazo fino outline.

- **Concepto Semántico:** Descarga de archivo o documento
- **Intención de Negocio:** Representar la descarga de documentos desde plataforma Visa
- **Disparadores Clave (Triggers):** `descargar`, `download`, `bajar archivo`, `obtener documento`, `file download`

**Cuándo Usar:**
- ✅ Descarga de estados de cuenta
- ✅ Botones de bajar comprobante
- ✅ Descarga de contratos y documentos

**Cuándo NO Usar (Anti-patrones):**
- ❌ Subida de archivos (usar file-upload-high.svg)
- ❌ Exportación sin archivo específico

**Copies de Ejemplo:**
- ""Descarga tu estado de cuenta Visa ahora""
- ""Tu comprobante está listo para descargar""

---
### 🔹 [137] `file-upload-high.svg` · Subir Archivo
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/file-upload-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/file-upload-high.svg" alt="Subir Archivo" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Documento con flecha apuntando hacia arriba indicando carga; trazo fino outline.

- **Concepto Semántico:** Carga o subida de archivo al sistema
- **Intención de Negocio:** Representar la subida de documentos a plataforma Visa
- **Disparadores Clave (Triggers):** `subir`, `upload`, `cargar`, `adjuntar`, `enviar archivo`

**Cuándo Usar:**
- ✅ Subida de documentos de identidad en KYC
- ✅ Adjuntar comprobante de domicilio
- ✅ Carga de estados de cuenta externos

**Cuándo NO Usar (Anti-patrones):**
- ❌ Descarga de documentos del sistema
- ❌ Exportación de datos propios

**Copies de Ejemplo:**
- ""Sube tu documento de identidad para verificar tu cuenta""
- ""Adjunta tu comprobante y completa tu registro Visa""

---
### 🔹 [138] `filter-high.svg` · Filtrar
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/filter-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/filter-high.svg" alt="Filtrar" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Embudo o triángulo invertido de filtro; trazo fino outline.

- **Concepto Semántico:** Filtrado y refinamiento de resultados
- **Intención de Negocio:** Representar herramientas de filtrado en listas y búsquedas
- **Disparadores Clave (Triggers):** `filtrar`, `filter`, `refinar`, `búsqueda avanzada`, `ordenar por`

**Cuándo Usar:**
- ✅ Filtros en historial de transacciones
- ✅ Búsqueda de comercios por categoría
- ✅ Filtrado de ofertas por tipo

**Cuándo NO Usar (Anti-patrones):**
- ❌ Búsqueda general sin filtros
- ❌ Ordenamiento simple

**Copies de Ejemplo:**
- ""Filtra tus transacciones Visa por fecha o monto""
- ""Encuentra exactamente lo que buscas con los filtros Visa""

---
### 🔹 [139] `history-high.svg` · Historial
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/history-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/history-high.svg" alt="Historial" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Reloj con flecha de retroceso indicando histórico; trazo fino outline.

- **Concepto Semántico:** Historial y registro de actividad pasada
- **Intención de Negocio:** Acceder al registro histórico de operaciones
- **Disparadores Clave (Triggers):** `historial`, `history`, `pasado`, `actividad anterior`, `registro`

**Cuándo Usar:**
- ✅ Secciones de historial de transacciones
- ✅ Registro de accesos y sesiones
- ✅ Historial de búsquedas en app

**Cuándo NO Usar (Anti-patrones):**
- ❌ Estado actual o en tiempo real
- ❌ Futuro o programado

**Copies de Ejemplo:**
- ""Revisa todo tu historial Visa sin límite de tiempo""
- ""Accede a cada movimiento pasado de tu cuenta""

---
### 🔹 [140] `home-high.svg` · Inicio / Home
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/home-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/home-high.svg" alt="Inicio / Home" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Silueta de casa con tejado triangular y puerta; trazo fino outline.

- **Concepto Semántico:** Pantalla de inicio o home de la aplicación
- **Intención de Negocio:** Proporcionar navegación al inicio de la plataforma
- **Disparadores Clave (Triggers):** `inicio`, `home`, `principal`, `pantalla principal`, `dashboard`

**Cuándo Usar:**
- ✅ Íconos de home en navegación inferior
- ✅ Botones de volver al inicio
- ✅ Tabs de pantalla principal

**Cuándo NO Usar (Anti-patrones):**
- ❌ Páginas de detalle o internas
- ❌ Funciones específicas sin relación al inicio

**Copies de Ejemplo:**
- ""Tu pantalla de inicio Visa: todo lo que necesitas a la vista""
- ""Regresa al home y gestiona desde el centro""

---
### 🔹 [141] `menu-high.svg` · Menú
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/menu-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/menu-high.svg" alt="Menú" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Tres líneas horizontales paralelas (hamburger menu); trazo fino outline.

- **Concepto Semántico:** Menú de navegación principal
- **Intención de Negocio:** Acceso al menú de opciones de la aplicación
- **Disparadores Clave (Triggers):** `menú`, `hamburger`, `navegación`, `opciones`, `menu`

**Cuándo Usar:**
- ✅ Botón de menú en headers de app
- ✅ Drawer de navegación lateral
- ✅ Menú de opciones adicionales

**Cuándo NO Usar (Anti-patrones):**
- ❌ Navegación específica con nombre
- ❌ Acciones primarias visibles

**Copies de Ejemplo:**
- ""Abre el menú y explora todas las funciones Visa""
- ""Todo Visa, a un toque del menú""

---
### 🔹 [142] `refresh-high.svg` · Actualizar
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/refresh-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/refresh-high.svg" alt="Actualizar" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Flecha circular o flechas en círculo indicando actualización; trazo fino outline.

- **Concepto Semántico:** Actualización o recarga de información
- **Intención de Negocio:** Representar la acción de actualizar datos en tiempo real
- **Disparadores Clave (Triggers):** `actualizar`, `refresh`, `recargar`, `sincronizar`, `refrescar`

**Cuándo Usar:**
- ✅ Botones de actualizar saldo
- ✅ Pull-to-refresh en listas
- ✅ Sincronización de datos

**Cuándo NO Usar (Anti-patrones):**
- ❌ Cambios de configuración
- ❌ Edición de información

**Copies de Ejemplo:**
- ""Actualiza tu saldo Visa con un toque""
- ""Datos siempre frescos: refresca tu app Visa""

---
### 🔹 [143] `save-high.svg` · Guardar
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/save-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/save-high.svg" alt="Guardar" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Ícono de diskette o checkmark con línea base de guardado; trazo fino outline.

- **Concepto Semántico:** Guardado de información o configuración
- **Intención de Negocio:** Representar el guardado de datos del usuario
- **Disparadores Clave (Triggers):** `guardar`, `save`, `almacenar`, `conservar`, `salvar`

**Cuándo Usar:**
- ✅ Botones de guardar configuración
- ✅ Guardado de datos de perfil
- ✅ Confirmación de cambios

**Cuándo NO Usar (Anti-patrones):**
- ❌ Descarga de archivos
- ❌ Exportación de datos

**Copies de Ejemplo:**
- ""Guarda tus preferencias Visa para próxima vez""
- ""Datos guardados: siempre listos cuando los necesites""

---
### 🔹 [144] `schedule-high.svg` · Programar
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/schedule-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/schedule-high.svg" alt="Programar" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Reloj con símbolo de programación o calendario; trazo fino outline.

- **Concepto Semántico:** Programación y agendado de operaciones
- **Intención de Negocio:** Representar la automatización de pagos programados
- **Disparadores Clave (Triggers):** `programar`, `agendar`, `schedule`, `automatizar`, `pago recurrente`

**Cuándo Usar:**
- ✅ Programación de pagos recurrentes
- ✅ Configuración de fechas de pago
- ✅ Domiciliación de servicios

**Cuándo NO Usar (Anti-patrones):**
- ❌ Historial de operaciones pasadas
- ❌ Acciones inmediatas sin programación

**Copies de Ejemplo:**
- ""Programa tus pagos Visa y olvídate de las fechas""
- ""Automatiza tus pagos recurrentes con Visa""

---
### 🔹 [145] `search-high.svg` · Buscar
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/search-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/search-high.svg" alt="Buscar" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Lupa con mango; trazo fino outline.

- **Concepto Semántico:** Búsqueda y localización de información
- **Intención de Negocio:** Representar la búsqueda en plataformas Visa
- **Disparadores Clave (Triggers):** `buscar`, `search`, `lupa`, `encontrar`, `explorar`

**Cuándo Usar:**
- ✅ Barras de búsqueda en apps
- ✅ Búsqueda de transacciones
- ✅ Localizador de comercios

**Cuándo NO Usar (Anti-patrones):**
- ❌ Filtrado específico (usar filter-high.svg)
- ❌ Navegación directa sin búsqueda

**Copies de Ejemplo:**
- ""Busca cualquier movimiento en tu historial Visa""
- ""Encuentra el comercio Visa que buscas en segundos""

---
### 🔹 [146] `send-high.svg` · Enviar
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/send-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/send-high.svg" alt="Enviar" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Avión de papel o flecha de envío; trazo fino outline.

- **Concepto Semántico:** Envío de mensaje, datos o pago
- **Intención de Negocio:** Representar la acción de enviar en contextos generales
- **Disparadores Clave (Triggers):** `enviar`, `send`, `mandar`, `despachar`, `submit`

**Cuándo Usar:**
- ✅ Botones de enviar mensaje
- ✅ Submit de formularios
- ✅ Confirmación de operación

**Cuándo NO Usar (Anti-patrones):**
- ❌ Recepción de información
- ❌ Cancelación de envío

**Copies de Ejemplo:**
- ""Envía tu comprobante Visa en segundos""
- ""Manda el pago y olvídate del resto""

---
### 🔹 [147] `settings-high.svg` · Configuración
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/settings-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/settings-high.svg" alt="Configuración" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Engranaje o rueda dentada; trazo fino outline.

- **Concepto Semántico:** Configuración y ajustes de la aplicación
- **Intención de Negocio:** Acceder a opciones de personalización de cuenta
- **Disparadores Clave (Triggers):** `configuración`, `ajustes`, `settings`, `preferencias`, `opciones`

**Cuándo Usar:**
- ✅ Íconos de configuración en headers
- ✅ Acceso a preferencias de notificación
- ✅ Configuración de seguridad

**Cuándo NO Usar (Anti-patrones):**
- ❌ Acciones primarias de pago
- ❌ Navegación de contenido

**Copies de Ejemplo:**
- ""Personaliza tu experiencia Visa en configuración""
- ""Ajusta tu cuenta Visa a tu medida""

---
### 🔹 [148] `share-high.svg` · Compartir
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/share-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/share-high.svg" alt="Compartir" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Tres puntos conectados por líneas formando red de compartir; trazo fino outline.

- **Concepto Semántico:** Compartir información o referir
- **Intención de Negocio:** Representar la acción de compartir contenido
- **Disparadores Clave (Triggers):** `compartir`, `share`, `referir`, `difundir`, `reenviar`

**Cuándo Usar:**
- ✅ Compartir comprobante de pago
- ✅ Referir amigos al programa Visa
- ✅ Compartir oferta

**Cuándo NO Usar (Anti-patrones):**
- ❌ Envío directo a persona específica
- ❌ Exportación de archivo

**Copies de Ejemplo:**
- ""Comparte tus beneficios Visa con amigos y gana más""
- ""Difunde las ofertas Visa que no puedes perderte""

---
### 🔹 [149] `sort-ascending-high.svg` · Ordenar Ascendente
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/sort-ascending-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/sort-ascending-high.svg" alt="Ordenar Ascendente" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Barras de lista de tamaño creciente o flechas indicando orden ascendente; trazo fino outline.

- **Concepto Semántico:** Ordenamiento de menor a mayor
- **Intención de Negocio:** Organizar listas en orden ascendente
- **Disparadores Clave (Triggers):** `ordenar`, `ascendente`, `A-Z`, `menor a mayor`, `sort ascending`

**Cuándo Usar:**
- ✅ Ordenamiento de transacciones por monto
- ✅ Listas ordenadas de menor a mayor
- ✅ Clasificación alfabética

**Cuándo NO Usar (Anti-patrones):**
- ❌ Orden descendente o inverso
- ❌ Filtrado sin ordenamiento

**Copies de Ejemplo:**
- ""Ordena tus gastos de menor a mayor con Visa""
- ""Visualiza tus transacciones en orden ascendente""

---
### 🔹 [150] `sort-descending-high.svg` · Ordenar Descendente
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/sort-descending-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/sort-descending-high.svg" alt="Ordenar Descendente" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Barras de lista de tamaño decreciente o flechas indicando orden descendente; trazo fino outline.

- **Concepto Semántico:** Ordenamiento de mayor a menor
- **Intención de Negocio:** Organizar listas en orden descendente
- **Disparadores Clave (Triggers):** `ordenar`, `descendente`, `Z-A`, `mayor a menor`, `sort descending`

**Cuándo Usar:**
- ✅ Ordenamiento de transacciones del mayor monto al menor
- ✅ Clasificación de más reciente a más antiguo
- ✅ Priorización de items

**Cuándo NO Usar (Anti-patrones):**
- ❌ Orden ascendente o inverso
- ❌ Filtrado sin ordenamiento

**Copies de Ejemplo:**
- ""Ordena tus gastos de mayor a menor con Visa""
- ""Las transacciones más grandes, primero""

---
### 🔹 [151] `time-high.svg` · Tiempo / Hora
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/time-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/time-high.svg" alt="Tiempo / Hora" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Reloj circular con manecillas de hora y minuto; trazo fino outline.

- **Concepto Semántico:** Hora y tiempo en contextos de operación
- **Intención de Negocio:** Representar el tiempo como factor en operaciones Visa
- **Disparadores Clave (Triggers):** `tiempo`, `hora`, `reloj`, `time`, `horario`

**Cuándo Usar:**
- ✅ Visualización de hora de transacción
- ✅ Tiempo estimado de procesamiento
- ✅ Horarios de servicio

**Cuándo NO Usar (Anti-patrones):**
- ❌ Fechas sin hora específica (usar calendar-high.svg)
- ❌ Historial sin referencia temporal

**Copies de Ejemplo:**
- ""Tu transacción Visa se procesó hoy a las 14:35""
- ""Soporte Visa disponible de 8AM a 10PM""

---
### 🔹 [152] `view-grid-high.svg` · Vista de Cuadrícula
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/view-grid-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/view-grid-high.svg" alt="Vista de Cuadrícula" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Cuadrícula de 2×2 o 3×3 de cuadros iguales; trazo fino outline.

- **Concepto Semántico:** Vista de cuadrícula o galería
- **Intención de Negocio:** Cambiar la visualización a formato de grilla
- **Disparadores Clave (Triggers):** `cuadrícula`, `grid`, `galería`, `vista`, `mosaico`

**Cuándo Usar:**
- ✅ Toggle de vista en catálogo de ofertas
- ✅ Vista de tarjetas en modo galería
- ✅ Layout de comercios

**Cuándo NO Usar (Anti-patrones):**
- ❌ Vista de lista o detalle lineal
- ❌ Tablas de datos

**Copies de Ejemplo:**
- ""Cambia a vista de cuadrícula para explorar más""
- ""Visualiza tus beneficios Visa en formato galería""

---
### 🔹 [153] `view-list-high.svg` · Vista de Lista
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/view-list-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/view-list-high.svg" alt="Vista de Lista" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Tres o cuatro líneas horizontales con puntos o iconos a la izquierda; trazo fino outline.

- **Concepto Semántico:** Vista de lista o formato lineal
- **Intención de Negocio:** Cambiar la visualización a formato de lista
- **Disparadores Clave (Triggers):** `lista`, `list`, `lineal`, `detalle`, `vista lista`

**Cuándo Usar:**
- ✅ Toggle de vista en historial de transacciones
- ✅ Lista de beneficiarios
- ✅ Catálogo en formato lista

**Cuándo NO Usar (Anti-patrones):**
- ❌ Vista de cuadrícula o galería
- ❌ Tablas complejas

**Copies de Ejemplo:**
- ""Visualiza tus transacciones en lista para más detalle""
- ""Lista completa de tus beneficios Visa""

---
### 🔹 [154] `zoom-in-high.svg` · Zoom In
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/zoom-in-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/zoom-in-high.svg" alt="Zoom In" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Lupa con símbolo "+" en su interior; trazo fino outline.

- **Concepto Semántico:** Ampliar o hacer zoom en contenido
- **Intención de Negocio:** Proporcionar capacidad de ampliar vistas
- **Disparadores Clave (Triggers):** `zoom in`, `ampliar`, `acercar`, `aumentar`, `detalle`

**Cuándo Usar:**
- ✅ Ampliación de imagen de tarjeta
- ✅ Zoom en mapas de localizador
- ✅ Detalle de gráficas

**Cuándo NO Usar (Anti-patrones):**
- ❌ Reducción o alejamiento
- ❌ Filtrado de resultados

**Copies de Ejemplo:**
- ""Amplía los detalles de tu transacción Visa""
- ""Acércate para ver el detalle completo""

---
### 🔹 [155] `zoom-out-high.svg` · Zoom Out
- **Familia Semántica:** UI Esencial
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/zoom-out-high.svg`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/zoom-out-high.svg" alt="Zoom Out" width="48" height="48" />`

> **Descripción Visual Morfológica (SVG Línea):**
> Lupa con símbolo "-" en su interior; trazo fino outline.

- **Concepto Semántico:** Reducir o alejar zoom en contenido
- **Intención de Negocio:** Proporcionar capacidad de reducir vistas
- **Disparadores Clave (Triggers):** `zoom out`, `reducir`, `alejar`, `minimizar`, `vista general`

**Cuándo Usar:**
- ✅ Reducción de zoom en mapas
- ✅ Vista general de gráficas
- ✅ Alejamiento en detalle de imagen

**Cuándo NO Usar (Anti-patrones):**
- ❌ Ampliación de contenido
- ❌ Filtrado de resultados

**Copies de Ejemplo:**
- ""Aleja el zoom para ver el panorama completo""
- ""Vista general de tu historial Visa""

---
---

## 📋 ÍNDICE RÁPIDO — Todos los archivos por categoría

| # | Archivo | Nombre | Categoría |
|---|---------|--------|-----------|
| 1 | `account-add-high.svg` | Agregar Cuenta | Pagos |
| 2 | `card-corporate-high.svg` | Tarjeta Corporativa | Pagos |
| 3 | `card-debit-high.svg` | Tarjeta de Débito | Pagos |
| 4 | `card-generic-high.svg` | Tarjeta Genérica | Pagos |
| 5 | `card-manage-alt-high.svg` | Gestionar Tarjeta (Alt) | Pagos |
| 6 | `card-manage-high.svg` | Gestionar Tarjeta | Pagos |
| 7 | `card-number-high.svg` | Número de Tarjeta | Pagos |
| 8 | `card-off-high.svg` | Tarjeta Desactivada | Pagos |
| 9 | `card-prepaid-high.svg` | Tarjeta Prepagada | Pagos |
| 10 | `card-suspend-high.svg` | Tarjeta Suspendida | Pagos |
| 11 | `card-verify-high.svg` | Verificación de Tarjeta | Pagos |
| 12 | `pos-alt-high.svg` | Terminal POS (Alt) | Pagos |
| 13 | `pos-high.svg` | Terminal POS | Pagos |
| 14 | `qr-high.svg` | Código QR | Pagos |
| 15 | `scan-card-high.svg` | Escanear Tarjeta | Pagos |
| 16 | `tap-high.svg` | Pago NFC / Tap | Pagos |
| 17 | `balance-high.svg` | Saldo / Balance | Transacciones |
| 18 | `bill-alt-high.svg` | Factura (Alt) | Transacciones |
| 19 | `bill-high.svg` | Factura / Cuenta | Transacciones |
| 20 | `fast-high.svg` | Transacción Rápida | Transacciones |
| 21 | `mobile-transfer-high.svg` | Transferencia Móvil | Transacciones |
| 22 | `money-add-high.svg` | Agregar Dinero | Transacciones |
| 23 | `money-request-high.svg` | Solicitar Dinero | Transacciones |
| 24 | `money-send-high.svg` | Enviar Dinero | Transacciones |
| 25 | `money-withdrawn-high.svg` | Retiro de Dinero | Transacciones |
| 26 | `on-hold-high.svg` | Transacción en Espera | Transacciones |
| 27 | `receipt-high.svg` | Recibo / Comprobante | Transacciones |
| 28 | `return-high.svg` | Devolución / Reembolso | Transacciones |
| 29 | `split-high.svg` | Dividir Pago | Transacciones |
| 30 | `transactions-high.svg` | Historial de Transacciones | Transacciones |
| 31 | `transactions-new-high.svg` | Nueva Transacción | Transacciones |
| 32 | `account-favorite-high.svg` | Cuenta Favorita | Cuenta y Wallet |
| 33 | `account-high.svg` | Cuenta | Cuenta y Wallet |
| 34 | `account-lock-high.svg` | Cuenta Bloqueada | Cuenta y Wallet |
| 35 | `account-remove-high.svg` | Eliminar Cuenta | Cuenta y Wallet |
| 36 | `atm-high.svg` | Cajero Automático (ATM) | Cuenta y Wallet |
| 37 | `savings-account-high.svg` | Cuenta de Ahorros | Cuenta y Wallet |
| 38 | `wallet-default-high.svg` | Wallet Digital (Default) | Cuenta y Wallet |
| 39 | `wallet-high.svg` | Wallet | Cuenta y Wallet |
| 40 | `currency-convert-alt-high.svg` | Convertir Divisa (Alt) | Divisas |
| 41 | `currency-convert-high.svg` | Convertir Divisa | Divisas |
| 42 | `currency-euro-high.svg` | Euro (€) | Divisas |
| 43 | `currency-high.svg` | Divisa Genérica | Divisas |
| 44 | `currency-pound-high.svg` | Libra Esterlina (£) | Divisas |
| 45 | `currency-usd-high.svg` | Dólar (USD) | Divisas |
| 46 | `currency-yen-high.svg` | Yen (¥) | Divisas |
| 47 | `auth-code-high.svg` | Código de Autenticación | Seguridad |
| 48 | `auth-face-high.svg` | Autenticación Facial | Seguridad |
| 49 | `auth-reauthorize-high.svg` | Re-autorización | Seguridad |
| 50 | `auth-voice-high.svg` | Autenticación por Voz | Seguridad |
| 51 | `device-secure-high.svg` | Dispositivo Seguro | Seguridad |
| 52 | `fingerprint-high.svg` | Huella Digital | Seguridad |
| 53 | `fraud-high.svg` | Fraude | Seguridad |
| 54 | `id-number-high.svg` | Número de Identificación | Seguridad |
| 55 | `key-change-high.svg` | Cambiar Contraseña | Seguridad |
| 56 | `key-high.svg` | Llave / Clave | Seguridad |
| 57 | `password-hide-high.svg` | Ocultar Contraseña | Seguridad |
| 58 | `password-show-high.svg` | Mostrar Contraseña | Seguridad |
| 59 | `security-firewall-high.svg` | Firewall de Seguridad | Seguridad |
| 60 | `security-high.svg` | Seguridad | Seguridad |
| 61 | `security-lock-high.svg` | Candado de Seguridad | Seguridad |
| 62 | `security-protection-high.svg` | Protección de Seguridad | Seguridad |
| 63 | `security-unlock-high.svg` | Desbloqueo de Seguridad | Seguridad |
| 64 | `sign-in-high.svg` | Iniciar Sesión | Seguridad |
| 65 | `sign-out-high.svg` | Cerrar Sesión | Seguridad |
| 66 | `signature-high.svg` | Firma Digital | Seguridad |
| 67 | `token-high.svg` | Token de Seguridad | Seguridad |
| 68 | `check-international-high.svg` | Verificación Internacional | Viajes |
| 69 | `global-high.svg` | Global / Mundial | Viajes |
| 70 | `map-directions-high.svg` | Indicaciones de Mapa | Viajes |
| 71 | `map-high.svg` | Mapa | Viajes |
| 72 | `map-location-current-high.svg` | Ubicación Actual | Viajes |
| 73 | `map-location-high.svg` | Pin de Ubicación | Viajes |
| 74 | `roadsign-high.svg` | Señal de Tráfico | Viajes |
| 75 | `transit-airplane-high.svg` | Avión | Viajes |
| 76 | `transit-car-high.svg` | Automóvil | Viajes |
| 77 | `transit-train-high.svg` | Tren | Viajes |
| 78 | `travel-notifications-high.svg` | Notificaciones de Viaje | Viajes |
| 79 | `acquirer-high.svg` | Adquirente | Comercio |
| 80 | `bonus-points-high.svg` | Puntos de Bonificación | Comercio |
| 81 | `cart-high.svg` | Carrito de Compras | Comercio |
| 82 | `gift-high.svg` | Regalo | Comercio |
| 83 | `issuer-high.svg` | Emisor | Comercio |
| 84 | `marketplace-high.svg` | Marketplace | Comercio |
| 85 | `merchant-high.svg` | Comerciante | Comercio |
| 86 | `offers-deal-high.svg` | Oferta / Deal | Comercio |
| 87 | `offers-high.svg` | Ofertas | Comercio |
| 88 | `reward-high.svg` | Recompensa | Comercio |
| 89 | `shipping-high.svg` | Envío / Logística | Comercio |
| 90 | `store-closed-high.svg` | Tienda Cerrada | Comercio |
| 91 | `store-open-high.svg` | Tienda Abierta | Comercio |
| 92 | `analytics-high.svg` | Analítica | Analítica |
| 93 | `dashboard-high.svg` | Dashboard | Analítica |
| 94 | `data-high.svg` | Datos | Analítica |
| 95 | `report-high.svg` | Reporte | Analítica |
| 96 | `statistics-high.svg` | Estadísticas | Analítica |
| 97 | `trending-high.svg` | Tendencia | Analítica |
| 98 | `chat-high.svg` | Chat | Comunicación |
| 99 | `customer-support-high.svg` | Soporte al Cliente | Comunicación |
| 100 | `email-high.svg` | Email | Comunicación |
| 101 | `error-high.svg` | Error | Comunicación |
| 102 | `help-high.svg` | Ayuda | Comunicación |
| 103 | `information-high.svg` | Información | Comunicación |
| 104 | `message-high.svg` | Mensaje | Comunicación |
| 105 | `mobile-success-high.svg` | Éxito en Móvil | Comunicación |
| 106 | `notifications-high.svg` | Notificaciones | Comunicación |
| 107 | `phone-high.svg` | Teléfono | Comunicación |
| 108 | `question-high.svg` | Pregunta | Comunicación |
| 109 | `success-high.svg` | Éxito | Comunicación |
| 110 | `support-ticket-high.svg` | Ticket de Soporte | Comunicación |
| 111 | `warning-high.svg` | Advertencia | Comunicación |
| 112 | `company-high.svg` | Empresa | Identidad |
| 113 | `contact-high.svg` | Contacto | Identidad |
| 114 | `government-high.svg` | Gobierno | Identidad |
| 115 | `handshake-high.svg` | Alianza / Acuerdo | Identidad |
| 116 | `device-laptop-high.svg` | Laptop / Computadora | Dispositivos |
| 117 | `device-mobile-high.svg` | Teléfono Móvil | Dispositivos |
| 118 | `device-wearable-high.svg` | Dispositivo Wearable | Dispositivos |
| 119 | `add-high.svg` | Agregar | UI Esencial |
| 120 | `arrow-back-high.svg` | Flecha Atrás | UI Esencial |
| 121 | `arrow-down-high.svg` | Flecha Abajo | UI Esencial |
| 122 | `arrow-forward-high.svg` | Flecha Adelante | UI Esencial |
| 123 | `arrow-up-high.svg` | Flecha Arriba | UI Esencial |
| 124 | `calendar-high.svg` | Calendario | UI Esencial |
| 125 | `check-high.svg` | Check / Palomita | UI Esencial |
| 126 | `checkmark-high.svg` | Confirmación | UI Esencial |
| 127 | `chevron-down-high.svg` | Chevron Abajo | UI Esencial |
| 128 | `chevron-left-high.svg` | Chevron Izquierda | UI Esencial |
| 129 | `chevron-right-high.svg` | Chevron Derecha | UI Esencial |
| 130 | `chevron-up-high.svg` | Chevron Arriba | UI Esencial |
| 131 | `close-high.svg` | Cerrar | UI Esencial |
| 132 | `copy-high.svg` | Copiar | UI Esencial |
| 133 | `delete-high.svg` | Eliminar | UI Esencial |
| 134 | `edit-high.svg` | Editar | UI Esencial |
| 135 | `export-high.svg` | Exportar | UI Esencial |
| 136 | `file-download-high.svg` | Descargar Archivo | UI Esencial |
| 137 | `file-upload-high.svg` | Subir Archivo | UI Esencial |
| 138 | `filter-high.svg` | Filtrar | UI Esencial |
| 139 | `history-high.svg` | Historial | UI Esencial |
| 140 | `home-high.svg` | Inicio / Home | UI Esencial |
| 141 | `menu-high.svg` | Menú | UI Esencial |
| 142 | `refresh-high.svg` | Actualizar | UI Esencial |
| 143 | `save-high.svg` | Guardar | UI Esencial |
| 144 | `schedule-high.svg` | Programar | UI Esencial |
| 145 | `search-high.svg` | Buscar | UI Esencial |
| 146 | `send-high.svg` | Enviar | UI Esencial |
| 147 | `settings-high.svg` | Configuración | UI Esencial |
| 148 | `share-high.svg` | Compartir | UI Esencial |
| 149 | `sort-ascending-high.svg` | Ordenar Ascendente | UI Esencial |
| 150 | `sort-descending-high.svg` | Ordenar Descendente | UI Esencial |
| 151 | `time-high.svg` | Tiempo / Hora | UI Esencial |
| 152 | `view-grid-high.svg` | Vista de Cuadrícula | UI Esencial |
| 153 | `view-list-high.svg` | Vista de Lista | UI Esencial |
| 154 | `zoom-in-high.svg` | Zoom In | UI Esencial |
| 155 | `zoom-out-high.svg` | Zoom Out | UI Esencial |

---

## 🔗 CDN Base Reference

```
https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/
```

## ⚡ Quick-Copy Template

```html
<img
  src="https://mkt-visa.vercel.app/assets/visa/icons/assets/visa-icons/svg/visa/{FILENAME}.svg"
  alt="{DESCRIPCION}"
  width="48"
  height="48"
  style="display:inline-block; vertical-align:middle;"
/>
```

## 📌 Notas de Implementación

1. **CORS:** El CDN Vercel tiene CORS abierto. Los iconos se pueden usar directamente desde cualquier dominio.
2. **Cache:** Los archivos SVG tienen cache-control de largo plazo. Usar el CDN para máximo rendimiento.
3. **Coloreado:** Aplicar `filter: brightness(0) saturate(100%) invert(X%) sepia(X%) saturate(X%) hue-rotate(Xdeg)` para cambiar color vía CSS.
4. **Dark Mode:** Los SVGs outline funcionan en fondo claro y oscuro sin modificación.
5. **Accesibilidad:** Siempre incluir atributo `alt` descriptivo en el idioma del usuario.
6. **Tamaño mínimo:** No usar por debajo de 16×16px para mantener legibilidad del trazo fino.

---

*Documento generado automáticamente · VISA_LLM_ICON_DECISION_MATRIX.md · © Artefact VCA 2025*
