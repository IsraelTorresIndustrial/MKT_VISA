# 🧠 Banco de Chile · Matriz de Decisión Contextual & Dossier Exhaustivo para IA
> **Autor:** Israel Torres  
> **Proyecto:** MKT_VISA  
> **Ámbito:** Banco de Chile · Medios de Pago · Visa · Travel Club  
> **Disponibilidad:** **100% Verificado (80 Activos Digitales Oficiales (42 3D/Travel/Logos + 30 2D + 8 2D Grupo 4))** con descripciones morfológicas hiperdetalladas para LLMs con o sin visión, reglas de negocio, intenciones de campaña y URLs públicas directas de producción en Vercel (`https://mkt-visa.vercel.app/assets/bch/...`).

---

## ⚡ DIRECTIVA CRÍTICA PARA LLMs: COMPILACIÓN WEB Y DOM-TO-PPTX (CERO CAÍDAS)
> [!IMPORTANT]
> **¿Por qué los LLMs deben usar siempre las URLs públicas de producción en Vercel (`https://mkt-visa.vercel.app/assets/bch/...`)?**
> 1. **Compilación Nativa DOM-to-PPTX**: Al compilar diapositivas HTML o emails a presentaciones PowerPoint nativas (`.pptx`) o plantillas de marketing, el motor realiza peticiones HTTP directas para descargar cada imagen e incrustarla como objeto binario independiente. Si usas rutas relativas (`assets/...`, `./icons/...`) o rutas locales (`file:///...`), la descarga fallará y la imagen se caerá de la pieza.
> 2. **Disponibilidad Global HTTP/2 200 OK**: El dominio `https://mkt-visa.vercel.app` cuenta con CDN global en el Edge, enrutamiento optimizado y entrega instantánea.
> 3. **Cabeceras CORS Permisivas (`*`)**: Evita bloqueos de seguridad por cross-origin en navegadores, clientes de correo y compiladores headless.
> 4. **Canal Alfa RGBA Preservado**: Los PNGs 3D cuentan con transparencia limpia de 32 bits, adaptándose sobre fondos blancos, oscuros `#002464` o degradados institucionales.

```html
<!-- ✅ CORRECTO: Uso de URL directa de producción en Vercel -->
<img src="https://mkt-visa.vercel.app/assets/bch/icons/06_primera_compra.png" alt="Primera Compra" width="64" height="64" style="display:block; margin:0 auto;" />
<img src="https://mkt-visa.vercel.app/assets/bch/travel/01_bch_icono_ticket_viaje_ncde7f.png" alt="Ticket Travel" width="64" height="64" />
<img src="https://mkt-visa.vercel.app/assets/bch/logos/banco_de_chile.png" alt="Banco de Chile" height="32" />

<!-- ❌ INCORRECTO: Provoca enlaces rotos y caídas en compiladores -->
<img src="assets/banco_de_chile/icons/06_primera_compra.png" /> <!-- Fallará por ruta relativa -->
<img src="/icons/06_primera_compra.png" /> <!-- Fallará sin host -->
```


---

## 👁️ GUÍA MORFOLÓGICA PARA LLMs SIN CAPACIDAD DE VISIÓN
Muchos modelos de lenguaje (o llamadas vía API de texto plano) no pueden procesar imágenes directamente. Para garantizar una selección 100% precisa y libre de alucinaciones, cada activo cuenta con:
1. **Descripción Visual Morfológica**: Objetos 3D exactos, paleta cromática, texturas, brillos y símbolos en relieve.
2. **Concepto Semántico**: Mensaje instantáneo decodificado por el usuario en menos de 2 segundos.
3. **Intención de Negocio & Métrica**: Qué objetivo persigue el banco (Adquisición, Activación M0, Frecuencia M1-M3, Retención, Gasto Crossborder).
4. **Disparadores Clave (Triggers)**: Términos explícitos en el prompt.
5. **Anti-patrones (Cuándo NO Usar)**: Para evitar confusiones típicas entre íconos similares.

---

## 🎯 ALGORITMO DE INFERENCIA EN 5 PASOS PARA AGENTES LLM
Cuando recibas un copy, brief o requerimiento de campaña para Banco de Chile:
1. **Paso 1: Extracción de Entidades y Verbos Rectores**: Detecta si el copy habla de *activar*, *comprar por primera vez*, *recuperar cliente*, *hacer 5 compras*, *gastar $300.000*, *recibir cashback*, *ahorrar %*, *viajar* o comprar en un *rubro específico*.
2. **Paso 2: Aplicación de la Regla de Prioridad Semántica**:
   $$\text{Acción del Cliente} > \text{Mecánica Comercial} > \text{Rubro de Consumo} > \text{Producto / Canal} > \text{Contexto Experiencial}$$
3. **Paso 3: Filtro de Anti-Patrones**: Revisa la sección 'Cuándo NO Usar' del candidato para descartar falsos positivos.
4. **Paso 4: Selección de Ícono Primario y Secundario**: Elige el ícono nuclear y, si la pieza tiene espacio para 2 íconos, selecciona el complementario.
5. **Paso 5: Emisión de JSON Estructurado**: Devuelve la URL absoluta canónica de producción Vercel.

---

## 🌳 ÁRBOL DE DECISIÓN RÁPIDO (ASCII)
```text
¿El mensaje trata sobre el medio de pago o canal?
│
├── Tarjeta genérica (sin canal específico)           ──► 01_tarjeta.png
├── Compra presencial en tienda / POS                 ──► 02_pago_presencial_pos.png
├── Compra online nacional / sitio web                ──► 03_ecommerce.png
├── Billetera digital (Apple Pay, Google Pay, Celular)──► 04_wallet_pago_movil.png
├── Pago sin contacto / Contactless / Tap to pay      ──► 21_contactless.png
├── Guardar tarjeta en apps (Card on File)            ──► 22_card_on_file_cof.png
└── Suscripción o cargo mensual recurrente (PAT)      ──► 23_pago_recurrente.png
│
¿El mensaje trata sobre etapa del cliente o ciclo de vida?
│
├── Desbloqueo / Bienvenida / Habilitar plástico      ──► 05_activacion.png
├── Debut del cliente / Primera transacción           ──► 06_primera_compra.png
└── Cliente inactivo / Dormido / Vuelve a usar        ──► 07_reactivacion.png
│
¿El mensaje trata sobre incentivo, beneficio o financiamiento?
│
├── Reintegro posterior en dinero a la cuenta         ──► 09_cashback.png
├── Acumulación o canje de Dólares-Premio             ──► 10_dolares_premio.png
├── Descuento porcentual directo (30% OFF)            ──► 24_descuento.png
└── Cuotas sin interés (3, 6, 12 cuotas precio contado)──► 25_cuotas_sin_interes_csi.png
│
¿El mensaje trata sobre una meta o desafío?
│
├── Meta por cantidad de compras (ej. haz 5 compras)  ──► 08_meta_de_transacciones.png
└── Meta por monto de gasto (ej. factura $300.000)    ──► 26_meta_de_facturacion.png
│
¿El mensaje trata sobre un rubro de consumo?
│
├── Supermercados y alimentación                      ──► 11_supermercado.png
├── Restaurantes, cenas y salidas gourmet             ──► 12_gastronomia_restaurantes.png
├── Cafeterías y pausas de café                       ──► 13_cafe_cafeterias.png
├── Combustible, bencina y estaciones de servicio     ──► 14_combustible.png
├── Farmacias, salud y bienestar                      ──► 15_farmacia_salud.png
├── Tiendas de retail, vestuario y shopping mall      ──► 16_retail_shopping.png
├── Tecnología, computación, telefonía y electro      ──► 17_tecnologia.png
├── Apps de despacho y comida a domicilio (Delivery)  ──► 18_delivery.png
├── Viajes, turismo y vacaciones (genérico)           ──► 19_viajes_turismo.png
└── Conciertos, cines, espectáculos y entretenimiento ──► 20_entretenimiento_musica.png
│
¿El mensaje trata sobre compras internacionales o beneficios de viaje?
│
├── Compra presencial en el extranjero (crossborder)  ──► 27_compra_internacional_crossborder.png
├── Compra online en tiendas extranjeras (Amazon, etc)──► 28_ecommerce_internacional.png
├── Salones VIP / Lounge en aeropuertos               ──► 29_lounge_salon_vip.png
└── Traslado privado / Transfer al aeropuerto         ──► 30_traslado_aeropuerto.png
```


---

## 📦 DOSSIER EXHAUSTIVO: LOS 30 ÍCONOS 3D OFICIALES BANCO DE CHILE

### 🔹 [01] `01_tarjeta.png` · Tarjeta de Crédito Genérica Institucional
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/01_tarjeta.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/01_tarjeta.png" alt="Tarjeta de Crédito Genérica Institucional" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Tarjeta de crédito física horizontal en perspectiva frontal tridimensional con esquinas redondeadas biseladas. Cuerpo en acabado metálico azul marino brillante corporativo (#002464) con reflejos especulares de luz superior. En la esquina superior izquierda exhibe la marca denominativa 'Banco de Chile' en tipografía gótica oficial blanca. A la izquierda media incorpora un chip EMV plateado con 6 subdivisiones de contacto en relieve metálico. A la derecha se aprecia el símbolo universal de pago contactless compuesto por tres ondas radiales arqueadas blancas. En la esquina inferior derecha resalta el logotipo oficial blanco tridimensional de VISA.

- **Concepto Semántico:** Medio de pago principal, portafolio de tarjetas y presencia institucional del plástico bancario.
- **Intención de Negocio:** Branding de producto, comunicación masiva de portafolio y mención neutra a tarjetas de crédito/débito sin especificar canal ni comportamiento.
- **Métricas Clave:** `Penetración de producto, recordación de marca, top-of-wallet general.`
- **Disparadores Clave (Triggers):** `tarjeta`, `tarjetas`, `tc`, `td`, `tarjeta de credito`, `tarjeta de debito`, `tus tarjetas del chile`, `plastico`, `medio de pago`, `visa banco de chile`, `portafolio tarjetas`

**Cuándo Usar:**
- ✅ Cuando la comunicación presenta genéricamente el uso de tarjetas Banco de Chile sin centrarse en un canal digital o físico específico.
- ✅ Piezas de portafolio donde se invita a conocer la gama de tarjetas del banco.
- ✅ Bloques institucionales que resumen las condiciones generales de un contrato o paquete de cuenta corriente.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar si la compra ocurre en terminal físico de caja (elegir 02_pago_presencial_pos.png).
- ❌ NO usar si la compra es online en sitio web o app (elegir 03_ecommerce.png).
- ❌ NO usar si el mensaje promueve enrolar la tarjeta en Apple Pay o Google Pay (elegir 04_wallet_pago_movil.png).
- ❌ NO usar si se incentiva la activación de un plástico nuevo (elegir 05_activacion.png).

**Copies de Ejemplo:**
- "Paga con tus Tarjetas de Crédito Banco de Chile y accede a un mundo de beneficios exclusivos en todo Chile."
- "Conoce los beneficios que tu Tarjeta Visa tiene preparados para ti durante esta temporada."

---

### 🔹 [02] `02_pago_presencial_pos.png` · Pago Presencial en Terminal POS
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/02_pago_presencial_pos.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/02_pago_presencial_pos.png" alt="Pago Presencial en Terminal POS" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Terminal punto de venta (POS) o máquina Transbank en perspectiva isométrica 3D de tres cuartos. Carcasa ergonómica en color azul marino mate con cantos curvados y textura sólida. Pantalla vertical rectangular iluminada en fondo blanco suave donde destaca el pictograma de pago sin contacto (tres ondas radiales azul oscuro). Teclado numérico físico compuesto por 9 teclas rectangulares grises redondeadas y una fila inferior con tres botones icónicos de acción en relieve: rojo (cancelar), amarillo (borrar) y verde (confirmar/enter). Bisel lateral con ranura de banda magnética y ranura frontal inferior para inserción de tarjeta con chip.

- **Concepto Semántico:** Transacción presencial en punto de venta físico, caja registradora de comercio y uso de terminal electrónico.
- **Intención de Negocio:** Fomentar el uso de la tarjeta en comercios físicos, malls y restaurantes locales.
- **Métricas Clave:** `Facturación presencial, transacciones POS, uso cotidiano en retail físico.`
- **Disparadores Clave (Triggers):** `pos`, `pago presencial`, `tienda fisica`, `en caja`, `terminal de pago`, `maquinita`, `comercio adherido`, `punto de venta`, `comprar en tienda`, `caja registradora`

**Cuándo Usar:**
- ✅ Comunicaciones que instruyen al cliente a solicitar el POS o pagar en caja en comercios físicos.
- ✅ Campañas que premian pagar presencialmente en tiendas físicas o locales de barrio.
- ✅ Instrucciones de digitación de PIN o confirmación de compra en tienda.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para compras electrónicas por internet o ecommerce (elegir 03_ecommerce.png).
- ❌ NO usar si el foco exclusivo es pagar acercando el celular con Apple Pay o Google Wallet (elegir 04_wallet_pago_movil.png).
- ❌ NO usar para compras presenciales en el extranjero (elegir 27_compra_internacional_crossborder.png).

**Copies de Ejemplo:**
- "Pide la maquinita POS en tiendas físicas y paga acercando tu tarjeta Banco de Chile."
- "Acumula oportunidades en tus compras presenciales pagando en comercios adheridos de todo el país."

---

### 🔹 [03] `03_ecommerce.png` · Ecommerce & Compras Online Nacionales
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/03_ecommerce.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/03_ecommerce.png" alt="Ecommerce & Compras Online Nacionales" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Computador portátil (laptop) tridimensional abierto con teclado plateado satinado y trackpad centrado. Carcasa superior y pantalla en azul marino profundo (#002464), en cuyo centro flota un carrito de compras 3D estilizado en blanco puro con ruedas esféricas. En el plano frontal inferior derecho se encuentra apoyada una tarjeta de crédito azul Banco de Chile con chip plateado visible y tipografía institucional, integrando el canal digital con el medio de pago.

- **Concepto Semántico:** Compra por internet en sitios web locales, comercio electrónico chileno, Webpay y carro de compras digital.
- **Intención de Negocio:** Incrementar el volumen de transacciones no presenciales (CNP) domésticas y captura de compras en CyberDays nacionales.
- **Métricas Clave:** `Volumen CNP nacional, tasa de conversión online, ticket promedio ecommerce.`
- **Disparadores Clave (Triggers):** `ecommerce`, `online`, `compras online`, `sitio web`, `webpay`, `carrito`, `tienda digital`, `internet`, `comprar por internet`, `cyber`, `cyberday`, `cybermonday`

**Cuándo Usar:**
- ✅ Campañas promocionales de CyberDay, CyberMonday, Black Friday nacional o eventos de compras online locales.
- ✅ Beneficios aplicables exclusivamente ingresando a la web de un comercio chileno adherido.
- ✅ Fomento del uso de tarjetas de crédito/débito en pasarelas de pago por internet (Webpay, Mercado Pago).

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar si la tienda online está radicada en el extranjero o cobra en dólares como Amazon o AliExpress (elegir 28_ecommerce_internacional.png).
- ❌ NO usar si el mensaje promueve inscribir la tarjeta para cobros mensuales automáticos (elegir 22_card_on_file_cof.png o 23_pago_recurrente.png).

**Copies de Ejemplo:**
- "Aprovecha este CyberDay comprando online con tus tarjetas del Chile y recibe despacho gratis."
- "Compra por internet en comercios asociados y acumula el doble de Dólares-Premio."

---

### 🔹 [04] `04_wallet_pago_movil.png` · Billetera Digital & Pago Móvil (Wallet)
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/04_wallet_pago_movil.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/04_wallet_pago_movil.png" alt="Billetera Digital & Pago Móvil (Wallet)" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Smartphone 3D vertical con chasis azul metálico brillante y pantalla blanca frontal limpia. En el centro de la pantalla sobresale tridimensionalmente un compartimento de billetera virtual (sleeve digital) en azul royal intenso con el símbolo contactless blanco en alto relieve. De dicho compartimento emergen en abanico dos tarjetas de crédito azul marino apiladas, destacando en la frontal un chip EMV plateado con brillo reflectante.

- **Concepto Semántico:** Digitalización de credenciales en smartphones y relojes inteligentes: Apple Pay, Google Wallet, Garmin Pay.
- **Intención de Negocio:** Aumentar la tokenización de tarjetas en billeteras móviles para generar hábito de pago diario ultra rápido y seguro.
- **Métricas Clave:** `Tasa de enrolamiento en Apple Pay / Google Pay, transacciones tokenizadas móviles, retención.`
- **Disparadores Clave (Triggers):** `wallet`, `apple pay`, `google pay`, `billetera digital`, `billetera movil`, `pago movil`, `pagar con el celular`, `pagar con el reloj`, `garmin pay`, `smartwatch`, `enrolar`

**Cuándo Usar:**
- ✅ Comunicaciones que invitan a enrolar la tarjeta en Apple Wallet o Billetera de Google.
- ✅ Beneficios por pagar directamente acercando el teléfono inteligente o reloj en comercios.
- ✅ Campañas de conveniencia y modernización del ecosistema de pago sin tarjeta física.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar si el pago sin contacto es realizado con el plástico físico tradicional (elegir 21_contactless.png).
- ❌ NO usar si solo se pide guardar los datos de la tarjeta en una página web (elegir 22_card_on_file_cof.png).

**Copies de Ejemplo:**
- "Agrega tu tarjeta Banco de Chile a Apple Pay y paga de forma fácil y segura desde tu iPhone."
- "Paga con tu billetera digital Google Pay y acumula el doble de Dólares-Premio en cada compra."

---

### 🔹 [05] `05_activacion.png` · Activación & Desbloqueo de Tarjeta Nueva
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/05_activacion.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/05_activacion.png" alt="Activación & Desbloqueo de Tarjeta Nueva" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Tarjeta de crédito física Banco de Chile Visa horizontal en azul marino metálico con chip plateado. En su ángulo superior derecho se superpone una insignia circular tridimensional verde esmeralda vibrante (#00C853) con bisel curvo brillante. En el interior de la insignia destaca un ticket o visto bueno (checkmark ✔) volumétrico blanco puro en relieve, que simboliza éxito, validación y producto 100% operativo.

- **Concepto Semántico:** Habilitación inicial del producto bancario recién emitido, primer encendido, asignación de PIN de seguridad y onboarding M0.
- **Intención de Negocio:** Romper la barrera de inactividad técnica inicial para convertir cuentas emitidas en cuentas operativas y listas para transaccionar.
- **Métricas Clave:** `Tasa de activación a 30 días, tiempo medio de activación (time-to-first-activation), reducción de plásticos dormidos.`
- **Disparadores Clave (Triggers):** `activacion`, `activar`, `activa`, `habilitar`, `desbloqueo`, `tarjeta nueva`, `clave pin`, `tarjeta lista`, `onboarding`, `primer encendido`, `mi banco`

**Cuándo Usar:**
- ✅ Correos de bienvenida a clientes nuevos que acaban de recibir su plástico por courier o sucursal.
- ✅ Instrucciones de desbloqueo de tarjeta en la App Mi Banco o cajero automático.
- ✅ Campañas con incentivo condicionado a completar la activación dentro del mes de apertura.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar si el cliente ya tiene la tarjeta habilitada y se le pide hacer su debut de compra (elegir 06_primera_compra.png).
- ❌ NO usar si el cliente fue activo en el pasado pero dejó de usar la tarjeta hace meses (elegir 07_reactivacion.png).

**Copies de Ejemplo:**
- "Activa tu nueva Tarjeta de Crédito en la App Mi Banco en menos de 2 minutos."
- "¡Tu tarjeta ya está contigo! Desbloquéala hoy y prepárate para disfrutar sus beneficios."

---

### 🔹 [06] `06_primera_compra.png` · Primera Compra & Debut Transaccional
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/06_primera_compra.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/06_primera_compra.png" alt="Primera Compra & Debut Transaccional" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Tarjeta de crédito física Banco de Chile Visa horizontal en acabado azul corporativo con chip EMV plateado. En la esquina superior derecha se incorpora un medallón circular 3D azul rey brillante (#0047FF) con borde biselado. En el centro del medallón resalta un número '1' tridimensional blanco puro en tipografía sans-serif gruesa con sombra de proyección, representando el primer uso histórico del producto.

- **Concepto Semántico:** Incentivo a realizar la primera transacción comercial con una tarjeta recién entregada (debut del titular).
- **Intención de Negocio:** Vencer la inercia transaccional en el ciclo M0-M1 para convertir un plástico activo en una tarjeta habitualmente utilizada.
- **Métricas Clave:** `Tasa de activación transaccional M1, días hasta la primera compra, facturación inicial.`
- **Disparadores Clave (Triggers):** `primera compra`, `primer uso`, `primera transaccion`, `debut`, `estrena tu tarjeta`, `usa tu tarjeta por primera vez`, `compra inicial`, `estreno`, `debut transaccional`

**Cuándo Usar:**
- ✅ Campañas que ofrecen una recompensa (cashback, descuento o bono de puntos) tras realizar la compra número 1.
- ✅ Mensajes de seguimiento a clientes que activaron su tarjeta pero aún no registran consumos.
- ✅ Desafíos de bienvenida que premian estrenar la tarjeta en comercios seleccionados.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para clientes inactivos de larga data que ya tenían historial previo de gasto (elegir 07_reactivacion.png).
- ❌ NO usar si la comunicación solo explica cómo activar la tarjeta técnicamente (elegir 05_activacion.png).

**Copies de Ejemplo:**
- "Realiza tu primera compra con tu Tarjeta del Chile y recibe $10.000 de abono en tu estado de cuenta."
- "¡Estrena tu Tarjeta de Crédito hoy y gana 20 Dólares-Premio de bienvenida!"

---

### 🔹 [07] `07_reactivacion.png` · Reactivación de Clientes Inactivos (Winback)
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/07_reactivacion.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/07_reactivacion.png" alt="Reactivación de Clientes Inactivos (Winback)" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Tarjeta de crédito Banco de Chile Visa horizontal azul marino con chip plateado. En la esquina superior derecha monta una chapa circular blanca perlada tridimensional con borde biselado. En su interior incorpora dos flechas curvas gruesas en azul cobalto brillante (#0032A0) que forman un anillo continuo de rotación y renovación en sentido horario (icono de reload / sincronización / retorno).

- **Concepto Semántico:** Recuperación de clientes dormidos o en riesgo de fuga en los meses M1 a M3 sin facturación registrada.
- **Intención de Negocio:** Combatir el churn pasivo, reinsertar la tarjeta en el top-of-wallet y reencantar al cliente con beneficios vigentes.
- **Métricas Clave:** `Tasa de reactivación de cartera inactiva, churn reduction, ROI de campañas de retención.`
- **Disparadores Clave (Triggers):** `reactivacion`, `reactiva`, `inactivo`, `dormido`, `vuelve a usar`, `te extrañamos`, `retoma tus beneficios`, `vuelve a comprar`, `recupera`, `winback`, `recuperacion`

**Cuándo Usar:**
- ✅ Comunicaciones dirigidas exclusivamente a clientes que llevan 30, 60 o 90 días sin usar su tarjeta.
- ✅ Ofertas con mensaje emotivo o comercial del tipo 'te extrañamos' o 'tenemos un beneficio especial para tu regreso'.
- ✅ Campañas de winback con bono de cashback al retomar el hábito de uso.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para tarjetas nuevas que nunca han hecho una compra (elegir 06_primera_compra.png).
- ❌ NO usar para clientes altamente activos y frecuentes (elegir 08_meta_de_transacciones.png o 26_meta_de_facturacion.png).

**Copies de Ejemplo:**
- "¡Te extrañamos! Vuelve a usar tu Tarjeta de Crédito y recibe un 30% de descuento en tu próxima compra."
- "Retoma tus compras con tus tarjetas del Chile y participa por grandes premios este mes."

---

### 🔹 [08] `08_meta_de_transacciones.png` · Meta por Cantidad de Transacciones (Frecuencia)
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/08_meta_de_transacciones.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/08_meta_de_transacciones.png" alt="Meta por Cantidad de Transacciones (Frecuencia)" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Composición 3D protagonizada por tres vouchers o boletas de compra de papel blanco troquelado apilados en abanico con líneas horizontales azul marino que simulan ítems facturados. En el plano frontal inferior derecho se sitúa una diana circular de tiro al blanco en azul cobalto y blanco con círculos concéntricos y una flecha aerodinámica azul certeramente clavada en el centro exacto (bullseye).

- **Concepto Semántico:** Desafío promocional condicionado a alcanzar una cantidad o frecuencia específica de transacciones (ej. haz 3 compras, 5 compras).
- **Intención de Negocio:** Elevar la frecuencia semanal de uso de la tarjeta convirtiéndola en el medio preferente para microtransacciones y compras cotidianas.
- **Métricas Clave:** `Frecuencia de transacciones por cliente (Tx/mes), engagement cotidiano, habitualidad de uso.`
- **Disparadores Clave (Triggers):** `meta de transacciones`, `meta de compras`, `cantidad de compras`, `frecuencia`, `haz 3 compras`, `haz 5 compras`, `desafio de compras`, `concurso transacciones`, `conteo de compras`, `numero de transacciones`

**Cuándo Usar:**
- ✅ Campañas del tipo: 'Haz 5 compras durante este mes y gana $15.000 de devolución'.
- ✅ Desafíos por frecuencia de compras donde el monto individual de cada transacción no es la condición principal.
- ✅ Gamificación donde acumular sellos, boletas o transacciones desbloquea un beneficio mayor.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar cuando la condición es alcanzar un monto monetario acumulado como $200.000 (elegir 26_meta_de_facturacion.png).
- ❌ NO usar si solo se exige una única primera compra (elegir 06_primera_compra.png).

**Copies de Ejemplo:**
- "Realiza 5 compras con tu Tarjeta del Chile durante el mes y asegura tus entradas al cine."
- "¡Cumple el desafío! Haz 3 compras de cualquier monto y recibe 15 Dólares-Premio de regalo."

---

### 🔹 [09] `09_cashback.png` · Cashback & Reintegro Posterior de Dinero
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/09_cashback.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/09_cashback.png" alt="Cashback & Reintegro Posterior de Dinero" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Pila de monedas tridimensionales de oro macizo satinado con bordes definidos. Al frente destaca una gran moneda circular dorada con el signo de divisa '$' grabado en alto relieve. Al fondo, una flecha arqueada en 3D en azul cobalto brillante realiza una trayectoria curva descendente apuntando directamente hacia el montón de monedas, simbolizando la restitución o retorno de dinero a la cuenta del titular.

- **Concepto Semántico:** Reembolso monetario que se abona con posterioridad en el estado de cuenta o cuenta bancaria tras haber efectuado la compra.
- **Intención de Negocio:** Incentivo comercial de alta tracción para estimular facturación en rubros estratégicos mediante abono en cuenta sin rebaja de ticket en caja.
- **Métricas Clave:** `Facturación total, adopción de promociones monetarias, satisfacción del titular.`
- **Disparadores Clave (Triggers):** `cashback`, `devolucion`, `reintegro`, `abono`, `abono en cuenta`, `te devolvemos`, `recibe en tu cuenta`, `reembolso`, `bonificacion monetaria`, `plata de vuelta`, `devolucion de dinero`

**Cuándo Usar:**
- ✅ Beneficios expresados en dinero que se reintegra posteriormente (ej. 'Te devolvemos $20.000 por compras sobre $80.000').
- ✅ Abonos en el siguiente estado de cuenta de la tarjeta de crédito.
- ✅ Promociones de reembolso bancario directo.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para descuentos directos en el precio en caja o cupón del comercio (elegir 24_descuento.png).
- ❌ NO usar si la recompensa es en puntos o Dólares-Premio (elegir 10_dolares_premio.png).

**Copies de Ejemplo:**
- "Compra con tu Tarjeta de Crédito y te devolvemos $15.000 directo en tu próximo estado de cuenta."
- "Recibe hasta un 20% de cashback en tus compras de fin de semana en comercios adheridos."

---

### 🔹 [10] `10_dolares_premio.png` · Dólares-Premio (DP) · Programa Travel Club
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/10_dolares_premio.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/10_dolares_premio.png" alt="Dólares-Premio (DP) · Programa Travel Club" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Moneda circular dorada tridimensional con borde grueso biselado en oro pulido. En el centro plano de la moneda destacan en alto relieve las letras mayúsculas 'DP' en tipografía geométrica bold. En la parte superior derecha de la circunferencia sobresale una estrella tridimensional dorada de 5 puntas con vértices redondeados, símbolo característico del programa de fidelización Travel Club Banco de Chile.

- **Concepto Semántico:** Unidad de valor del programa de lealtad Travel Club de Banco de Chile para acumulación y canje de pasajes, productos y experiencias.
- **Intención de Negocio:** Vincular el gasto con la recompensa aspiracional de viajes y fidelizar clientes a través de la acumulación de la moneda propia del banco.
- **Métricas Clave:** `Acumulación y redención de DP, gasto por cliente fidelizado, retención en planes Travel.`
- **Disparadores Clave (Triggers):** `dolares premio`, `dp`, `travel club`, `acumula dp`, `canje de dolares premio`, `programa travel`, `puntos travel`, `dolares de premio`, `travel duty`, `puntos bch`

**Cuándo Usar:**
- ✅ Cualquier comunicación que informe tasa de acumulación de Dólares-Premio (ej. '1,5% de acumulación en tus compras').
- ✅ Campañas de canje en el catálogo Travel Duty o pasajes aéreos.
- ✅ Bonos de bienvenida entregados en forma de DP.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para devolución de dinero en pesos chilenos a la cuenta (elegir 09_cashback.png).
- ❌ NO usar para promociones de porcentaje de descuento directo (elegir 24_descuento.png).

**Copies de Ejemplo:**
- "Acumula el doble de Dólares-Premio en todas tus compras del mes con tu Tarjeta Travel."
- "Canjea tus DP acumulados por pasajes, hoteles y miles de productos en Travel Club."

---

### 🔹 [11] `11_supermercado.png` · Supermercados & Alimentación del Hogar
- **Familia Semántica:** Rubros de Consumo
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/11_supermercado.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/11_supermercado.png" alt="Supermercados & Alimentación del Hogar" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Carrito de compras clásico de supermercado en perspectiva isométrica 3D. Estructura de rejilla metálica cromada con chasis y manubrio ergonómico en azul corporativo Banco de Chile. Ruedas esféricas móviles y bolsas de compras o productos en tonos suaves asomando del interior, simbolizando el abastecimiento familiar.

- **Concepto Semántico:** Compras cotidianas de víveres, despensa y abarrotes en cadenas de supermercados (Jumbo, Lider, Santa Isabel, Unimarc).
- **Intención de Negocio:** Capturar el gasto recurrente más grande de la canasta básica familiar posicionando a la tarjeta como medio de pago predeterminado en el supermercado.
- **Métricas Clave:** `Frecuencia semanal, volumen de gasto en categoría alimentos, share de billetera en retail de alimentación.`
- **Disparadores Clave (Triggers):** `supermercado`, `supermercados`, `alimentos`, `jumbo`, `lider`, `santa isabel`, `unimarc`, `tottus`, `despensa`, `compras del hogar`, `abarrotes`, `mercadería`

**Cuándo Usar:**
- ✅ Promociones de días específicos en supermercados (ej. 'Lunes de supermercados').
- ✅ Descuentos en Jumbo, Lider, Unimarc o Santa Isabel.
- ✅ Campañas de ahorro en la compra de la canasta familiar.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para restaurantes, cenas o comidas preparadas fuera del hogar (elegir 12_gastronomia_restaurantes.png).
- ❌ NO usar para pedidos de comida rápida por aplicación (elegir 18_delivery.png).

**Copies de Ejemplo:**
- "Disfruta de hasta 20% de descuento en Jumbo los días lunes pagando con tus Tarjetas del Chile."
- "Ahorra en tus compras de supermercado todos los fines de semana."

---

### 🔹 [12] `12_gastronomia_restaurantes.png` · Gastronomía, Restaurantes & Salidas Gourmet
- **Familia Semántica:** Rubros de Consumo
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/12_gastronomia_restaurantes.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/12_gastronomia_restaurantes.png" alt="Gastronomía, Restaurantes & Salidas Gourmet" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Cloche tradicional de servicio gastronómico (campana de platos gourmet) 3D en acabado metálico brillante azul oscuro con perilla superior dorada, asentada sobre un plato redondo de presentación con cubiertos cruzados (tenedor y cuchillo elegantes) finamente modelados en 3D.

- **Concepto Semántico:** Restaurantes, cenas, comidas fuera del hogar, bares y experiencias culinarias presenciales.
- **Intención de Negocio:** Vincular la tarjeta al ocio y momentos sociales premium de los clientes, estimulando tickets de fin de semana.
- **Métricas Clave:** `Gasto en restaurantes de jueves a domingo, facturación en terminales POS gastronómicos.`
- **Disparadores Clave (Triggers):** `restaurante`, `restaurantes`, `gastronomia`, `comida`, `cenas`, `almuerzos`, `gourmet`, `salidas a comer`, `bares`, `sabores del chile`, `mesas`

**Cuándo Usar:**
- ✅ Programa 'Sabores del Chile' o convenios gastronómicos del banco.
- ✅ Descuentos de hasta 40% o 50% en restaurantes de alta cocina y cadenas asociadas.
- ✅ Comunicaciones sobre salidas nocturnas y cenas de fin de semana.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para cafeterías, desayunos o pastelerías de consumo matinal rápido (elegir 13_cafe_cafeterias.png).
- ❌ NO usar para pedidos a domicilio por app móvil (elegir 18_delivery.png).

**Copies de Ejemplo:**
- "Vive una experiencia gastronómica inolvidable con hasta 40% de descuento en restaurantes asociados."
- "Jueves y viernes gourmet: paga con tu Tarjeta Infinite y disfruta de beneficios exclusivos en gastronomía."

---

### 🔹 [13] `13_cafe_cafeterias.png` · Cafeterías, Café & Pausas Diarias
- **Familia Semántica:** Rubros de Consumo
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/13_cafe_cafeterias.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/13_cafe_cafeterias.png" alt="Cafeterías, Café & Pausas Diarias" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Taza de café de cerámica blanca y azul 3D apoyada sobre un plato circular a juego, de la cual ascienden volutas estilizadas de vapor aromático tridimensional. En el lateral o superficie se aprecia un grano de café tostado dorado con textura volumétrica y brillo suave.

- **Concepto Semántico:** Pausas cotidianas, cafeterías de especialidad, cadenas de café (Starbucks, Dunkin', Juan Valdez) y desayunos.
- **Intención de Negocio:** Incentivar la microtransacción diaria de alta frecuencia y fidelización en la rutina matinal del cliente.
- **Métricas Clave:** `Transacciones matinales (8:00 a 11:00 AM), recurrencia semanal, penetración contactless.`
- **Disparadores Clave (Triggers):** `cafe`, `cafeteria`, `cafeterias`, `starbucks`, `dunkin`, `juan valdez`, `desayuno`, `pausa cafe`, `coffee`, `pasteleria`

**Cuándo Usar:**
- ✅ Alianzas comerciales con Starbucks, Dunkin', Juan Valdez o cafeterías locales.
- ✅ Promociones matutinas de café gratis o 2x1 en cafeterías asociadas.
- ✅ Incentivos de pago rápido con contactless o billetera en pausas de trabajo.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para restaurantes de comidas completas o cenas formales (elegir 12_gastronomia_restaurantes.png).
- ❌ NO usar para compras de supermercado (elegir 11_supermercado.png).

**Copies de Ejemplo:**
- "Comienza tus mañanas con energía: 30% de descuento en Starbucks pagando con tus tarjetas del Chile."
- "Disfruta de un café de especialidad con beneficios exclusivos todos los días."

---

### 🔹 [14] `14_combustible.png` · Combustible, Bencina & Estaciones de Servicio
- **Familia Semántica:** Rubros de Consumo
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/14_combustible.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/14_combustible.png" alt="Combustible, Bencina & Estaciones de Servicio" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Dispensador de combustible / surtidor de bencina 3D estilizado en azul marino y blanco institucional. Cuenta con una manguera flexible negra conectada a una pistola metálica de despacho colgada lateralmente, pantalla digital iluminada con indicador de litros y gota de combustible dorada brillante en relieve frontal.

- **Concepto Semántico:** Carga de combustible, bencina, diésel y servicios en estaciones de servicio (Shell, Copec, Petrobras).
- **Intención de Negocio:** Fidelizar un gasto obligatorio de movilidad de alto valor mediante descuentos por litro, capturando fidelidad en días clave.
- **Métricas Clave:** `Gasto en estaciones de servicio, carga de combustible por cliente, transacciones de movilidad.`
- **Disparadores Clave (Triggers):** `combustible`, `bencina`, `gasolina`, `estacion de servicio`, `shell`, `copec`, `petrobras`, `litro`, `descuento por litro`, `carga de combustible`, `auto`, `movilidad`

**Cuándo Usar:**
- ✅ Promociones de descuento fijo o porcentual por litro de bencina (ej. '$50 o $100 de dto por litro').
- ✅ Días temáticos de combustible (ej. 'Lunes o domingos en Shell').
- ✅ Alianzas con apps de estaciones de servicio (MiCopiloto, Muevo, PagoClick).

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para traslados privados o vans al aeropuerto (elegir 30_traslado_aeropuerto.png).
- ❌ NO usar para pasajes de avión o trenes (elegir 19_viajes_turismo.png).

**Copies de Ejemplo:**
- "Carga combustible los lunes en Shell y obtén $100 de descuento por litro pagando con tus Tarjetas del Chile."
- "Ahorra en tus viajes por carretera con beneficios exclusivos en estaciones de servicio."

---

### 🔹 [15] `15_farmacia_salud.png` · Farmacias, Salud & Cuidado Personal
- **Familia Semántica:** Rubros de Consumo
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/15_farmacia_salud.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/15_farmacia_salud.png" alt="Farmacias, Salud & Cuidado Personal" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Composición 3D protagonizada por un maletín médico / botiquín de primeros auxilios azul marino con cruz de salud blanca en relieve, acompañado en primer plano por una cápsula medicinal tridimensional bicolor (azul y blanco brillante) y un frasco de bienestar.

- **Concepto Semántico:** Compras en farmacias, medicamentos, cuidado de la salud, dermocosmética y bienestar personal.
- **Intención de Negocio:** Acompañar al cliente en gastos sensibles de salud y protección familiar con descuentos directos en cadenas de farmacia.
- **Métricas Clave:** `Volumen de compra en farmacias (Cruz Verde, Salcobrand, Farmacias Ahumada), uso mensual recurrente.`
- **Disparadores Clave (Triggers):** `farmacia`, `farmacias`, `salud`, `medicamentos`, `cruz verde`, `salcobrand`, `farmacias ahumada`, `bienestar`, `dermocosmetica`, `cuidado personal`, `remedios`

**Cuándo Usar:**
- ✅ Descuentos semanales o mensuales en Cruz Verde, Salcobrand o Farmacias Ahumada.
- ✅ Promociones en categorías de cuidado infantil, medicamentos o dermocosmética.
- ✅ Beneficios de salud preventiva y bienestar del titular y sus cargas.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para seguros médicos de viaje internacional (elegir 19_viajes_turismo.png).
- ❌ NO usar para compras en supermercados (elegir 11_supermercado.png).

**Copies de Ejemplo:**
- "Cuida tu salud con hasta 30% de descuento en Cruz Verde pagando con tus Tarjetas del Chile."
- "Todos los martes son de farmacia: aprovecha descuentos exclusivos en medicamentos y bienestar."

---

### 🔹 [16] `16_retail_shopping.png` · Retail, Shopping, Tiendas & Moda
- **Familia Semántica:** Rubros de Consumo
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/16_retail_shopping.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/16_retail_shopping.png" alt="Retail, Shopping, Tiendas & Moda" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Conjunto de bolsas de compras de papel shopping premium 3D en azul marino y celeste con manillas de cordón blanco brillante. Al frente se exhibe una etiqueta colgante de tienda (hangtag) con ojal plateado y símbolo de vestuario/moda grabado en relieve.

- **Concepto Semántico:** Tiendas por departamento, centros comerciales (malls), moda, calzado, vestuario y compras de ocio.
- **Intención de Negocio:** Capturar compras estacionales de ticket medio-alto en vestuario, decoración y retail en fechas comerciales clave.
- **Métricas Clave:** `Ticket promedio en retail, volumen de compras en centros comerciales, campañas día de la madre/padre/navidad.`
- **Disparadores Clave (Triggers):** `retail`, `shopping`, `tiendas`, `malls`, `vestuario`, `moda`, `ropa`, `calzado`, `tiendas por departamento`, `compras presenciales mall`, `falabella`, `ripley`, `paris`

**Cuándo Usar:**
- ✅ Campañas de compras en centros comerciales (Mallplaza, Parque Arauco, Costanera Center).
- ✅ Descuentos en marcas de vestuario, moda, zapatería y accesorios.
- ✅ Promociones de temporada (cambio de temporada otoño/invierno, primavera/verano).

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar si el foco específico es comprar artículos electrónicos o smartphones (elegir 17_tecnologia.png).
- ❌ NO usar si la compra se realiza online en el extranjero (elegir 28_ecommerce_internacional.png).

**Copies de Ejemplo:**
- "Renueva tu clóset con hasta 40% de descuento en tiendas de moda y shopping seleccionadas."
- "Aprovecha este fin de semana en malls con beneficios exclusivos pagando con tus Tarjetas del Chile."

---

### 🔹 [17] `17_tecnologia.png` · Tecnología, Dispositivos & Electrónica
- **Familia Semántica:** Rubros de Consumo
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/17_tecnologia.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/17_tecnologia.png" alt="Tecnología, Dispositivos & Electrónica" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Composición tecnológica 3D que integra un monitor/pantalla plana sin marcos en azul marino metálico con gráfico de procesador digital, un smartphone de alta gama apoyado al frente y unos audífonos inalámbricos circumaurales estilizados con detalles plateados y LED azul.

- **Concepto Semántico:** Smartphones, computadores, notebooks, consolas de videojuegos, audio de alta fidelidad y electrodomésticos.
- **Intención de Negocio:** Financiar bienes durables de alto valor típicamente asociados a cuotas sin interés y campañas Cyber.
- **Métricas Clave:** `Financiamiento en cuotas (CSI), volumen de compra de alto ticket, transacciones tecnológicas.`
- **Disparadores Clave (Triggers):** `tecnologia`, `electronica`, `computacion`, `celulares`, `smartphones`, `notebooks`, `gadgets`, `videojuegos`, `electro`, `macbook`, `iphone`, `audio`

**Cuándo Usar:**
- ✅ Promociones en tiendas tecnológicas (MacOnline, Samsung, PC Factory, Reifstore).
- ✅ Lanzamientos de nuevos dispositivos móviles o consolas.
- ✅ Campañas de cuotas sin interés para la compra de equipamiento tecnológico.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para compras de retail general como vestuario o calzado (elegir 16_retail_shopping.png).
- ❌ NO usar para servicios digitales de streaming (elegir 20_entretenimiento_musica.png o 23_pago_recurrente.png).

**Copies de Ejemplo:**
- "Equípate con lo último en tecnología en hasta 12 cuotas sin interés con tu Tarjeta de Crédito."
- "Lleva tu nuevo smartphone con descuentos imperdibles en tiendas de electrónica asociadas."

---

### 🔹 [18] `18_delivery.png` · Delivery, Pedidos por App & Envíos Rápidos
- **Familia Semántica:** Rubros de Consumo
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/18_delivery.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/18_delivery.png" alt="Delivery, Pedidos por App & Envíos Rápidos" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Mochila cúbica térmica de repartidor de delivery 3D en azul corporativo con bandas reflectantes blancas y asa superior, acompañada de un cronómetro / reloj de entrega rápida o scooter estilizado que denota velocidad e inmediatez en el despacho.

- **Concepto Semántico:** Pedidos de comida y productos a domicilio a través de aplicaciones móviles (PedidosYa, Rappi, Uber Eats).
- **Intención de Negocio:** Fomentar el registro de la tarjeta como medio de pago preferente en plataformas de última milla con alta frecuencia de uso.
- **Métricas Clave:** `Transacciones en apps de delivery, COF en plataformas de última milla, uso en horario nocturno y fines de semana.`
- **Disparadores Clave (Triggers):** `delivery`, `pedidosya`, `rappi`, `uber eats`, `pedidos a domicilio`, `a domicilio`, `envios`, `comida a domicilio`, `despacho a casa`, `apps de delivery`

**Cuándo Usar:**
- ✅ Descuentos en PedidosYa, Rappi o Uber Eats.
- ✅ Campañas de despacho gratis en pedidos de cena o fines de semana.
- ✅ Incentivos para enrolar la tarjeta en aplicaciones de comida a domicilio.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para cenas o salidas presenciales a restaurantes físicos (elegir 12_gastronomia_restaurantes.png).
- ❌ NO usar para compras de supermercado presenciales (elegir 11_supermercado.png).

**Copies de Ejemplo:**
- "Pide lo que quieras por PedidosYa y obtén 30% de descuento pagando con tus tarjetas del Chile."
- "Tus viernes saben mejor: disfruta de delivery gratis en tus restaurantes favoritos con Rappi."

---

### 🔹 [19] `19_viajes_turismo.png` · Viajes, Turismo & Vacaciones (Genérico)
- **Familia Semántica:** Mecánicas, Crossborder & Travel
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/19_viajes_turismo.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/19_viajes_turismo.png" alt="Viajes, Turismo & Vacaciones (Genérico)" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Globo terráqueo tridimensional en azul zafiro con siluetas de continentes en relieve blanco suave, circundado por la estela orbital de un avión comercial 3D en miniatura que surca los cielos en trayectoria ascendente.

- **Concepto Semántico:** Turismo general, paquetes de vacaciones, pasajes aéreos, destinos nacionales e internacionales y escapadas.
- **Intención de Negocio:** Posicionar a Banco de Chile y su alianza con aerolíneas y agencias como el banco líder para viajar.
- **Métricas Clave:** `Venta de pasajes en cuotas, paquetes turísticos, facturación en aerolíneas y hoteles.`
- **Disparadores Clave (Triggers):** `viajes`, `turismo`, `vacaciones`, `vuelos`, `pasajes`, `paquetes turisticos`, `escapadas`, `aerolineas`, `latam`, `sky`, `verano`, `invierno`, `viajar`

**Cuándo Usar:**
- ✅ Promociones de pasajes aéreos en cuotas sin interés o canje de puntos.
- ✅ Campañas de vacaciones de verano o vacaciones de invierno.
- ✅ Paquetes turísticos completos ofrecidos por agencias de viajes asociadas.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar si el foco exclusivo es el acceso a salas de espera de aeropuerto (elegir 29_lounge_salon_vip.png).
- ❌ NO usar si el beneficio es el traslado físico hacia el aeropuerto (elegir 30_traslado_aeropuerto.png).
- ❌ NO usar si la comunicación se enfoca en compras físicas en el extranjero (elegir 27_compra_internacional_crossborder.png).

**Copies de Ejemplo:**
- "Planifica tus próximas vacaciones con hasta 12 cuotas sin interés en pasajes y hoteles."
- "Descubre el mundo con los beneficios que tu Tarjeta Banco de Chile tiene para viajar."

---

### 🔹 [20] `20_entretenimiento_musica.png` · Entretenimiento, Conciertos, Cines & Eventos
- **Familia Semántica:** Rubros de Consumo
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/20_entretenimiento_musica.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/20_entretenimiento_musica.png" alt="Entretenimiento, Conciertos, Cines & Eventos" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Auriculares de diadema circumaurales (headphones) 3D en azul corporativo con almohadillas acolchadas y diadema curva ergonómica, rodeados de notas musicales volumétricas flotantes (corcheas y semicorcheas) y un ticket de cine o entrada a espectáculo con borde dentado.

- **Concepto Semántico:** Música, preventas exclusivas de conciertos, festivales (Lollapalooza), entradas al cine y streaming.
- **Intención de Negocio:** Aprovechar la fuerte asociación de Banco de Chile con la música en vivo y el entretenimiento para atraer público joven y fidelizar.
- **Métricas Clave:** `Adopción de preventas exclusivas, compra de entradas con tarjeta de crédito/débito, vinculación emocional.`
- **Disparadores Clave (Triggers):** `entretenimiento`, `concierto`, `conciertos`, `musica`, `cine`, `cineplanet`, `cinepolis`, `lollapalooza`, `preventa`, `entradas`, `espectaculos`, `eventos`, `teatro`

**Cuándo Usar:**
- ✅ Preventas exclusivas para clientes Banco de Chile de conciertos internacionales.
- ✅ Descuentos en entradas de cine (Cineplanet, Cinépolis) y confitería.
- ✅ Promociones del festival Lollapalooza Chile o espectáculos masivos.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para compras de retail o vestuario (elegir 16_retail_shopping.png).
- ❌ NO usar para suscripciones de streaming sin contexto de evento en vivo si el foco es el cobro mensual (elegir 23_pago_recurrente.png).

**Copies de Ejemplo:**
- "Accede a la preventa exclusiva de entradas con 20% de descuento pagando con tus tarjetas del Chile."
- "Disfruta del mejor cine todos los días con entradas a precio preferencial para clientes del banco."

---

### 🔹 [21] `21_contactless.png` · Pago Sin Contacto (Contactless / Tap to Pay)
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/21_contactless.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/21_contactless.png" alt="Pago Sin Contacto (Contactless / Tap to Pay)" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Tarjeta de crédito Banco de Chile en perspectiva diagonal acercándose hacia un plano emisor de radiofrecuencia (NFC). Tres ondas expansivas radiales tridimensionales luminosas en azul cian y blanco emergen del punto de aproximación, simbolizando la velocidad y seguridad de la tecnología 'Tap to Pay' sin contacto físico.

- **Concepto Semántico:** Tecnología de pago por aproximación NFC mediante la tarjeta plástica física acercándola al terminal POS.
- **Intención de Negocio:** Acelerar la velocidad en caja, modernizar la experiencia del usuario y reducir el desgaste del plástico frente al chip insertado.
- **Métricas Clave:** `Porcentaje de transacciones sin contacto sobre el total presencial, velocidad de transacción, conveniencia.`
- **Disparadores Clave (Triggers):** `contactless`, `sin contacto`, `nfc`, `tap to pay`, `acerca tu tarjeta`, `pagar acercando`, `pago rapido`, `aproximacion`, `tap`

**Cuándo Usar:**
- ✅ Campañas educativas sobre la rapidez y seguridad de pagar sin entregar la tarjeta.
- ✅ Incentivos por realizar pagos contactless en transporte o comercios rápidos.
- ✅ Diferenciación frente a la inserción tradicional de chip.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar si el pago se realiza a través de un teléfono inteligente (elegir 04_wallet_pago_movil.png).
- ❌ NO usar para compras por internet (elegir 03_ecommerce.png).

**Copies de Ejemplo:**
- "Paga en segundos: solo acerca tu tarjeta Contactless al terminal y listo."
- "Disfruta de una experiencia de pago más rápida, higiénica y segura con tecnología sin contacto."

---

### 🔹 [22] `22_card_on_file_cof.png` · Card on File (COF) & Tarjeta Guardada en Apps
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/22_card_on_file_cof.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/22_card_on_file_cof.png" alt="Card on File (COF) & Tarjeta Guardada en Apps" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Tarjeta de crédito 3D azul Banco de Chile insertada de forma segura dentro de un contenedor digital estilizado o caja de credenciales protegida por un candado digital cromado, representando el almacenamiento cifrado y automático de los datos de la tarjeta en aplicaciones móviles preferidas.

- **Concepto Semántico:** Inscripción y almacenamiento de la tarjeta de crédito como método de pago predeterminado en aplicaciones cotidianas (Uber, Spotify, Mercado Libre).
- **Intención de Negocio:** Fijar la tarjeta como medio de pago 'invisible' por defecto, capturando cobros automáticos futuros sin fricción en el checkout.
- **Métricas Clave:** `Tasa de enrolamiento COF, transacciones recurrentes no periódicas, retención de clientes.`
- **Disparadores Clave (Triggers):** `card on file`, `cof`, `inscribir tarjeta`, `guardar tarjeta`, `apps favoritas`, `tarjeta registrada`, `metodo de pago predeterminado`, `uber`, `spotify`, `mercado libre`

**Cuándo Usar:**
- ✅ Campañas que premian guardar la tarjeta en aplicaciones de transporte, streaming o comercio electrónico.
- ✅ Comunicaciones del tipo: 'Inscribe tu tarjeta en Uber y recibe tu primer viaje con 50% de descuento'.
- ✅ Incentivos de seguridad sobre almacenamiento seguro de credenciales con tokenización.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para pagos mensuales fijos de servicios básicos como luz o agua (elegir 23_pago_recurrente.png).
- ❌ NO usar si el cliente compra puntualmente en una web sin guardar los datos (elegir 03_ecommerce.png).

**Copies de Ejemplo:**
- "Inscribe tu Tarjeta de Crédito en tus apps favoritas como Uber, Spotify y Netflix y simplifica tus pagos."
- "Guarda tu tarjeta en Mercado Libre y disfruta de compras más rápidas con total seguridad."

---

### 🔹 [23] `23_pago_recurrente.png` · Pago Recurrente, PAT & Cuentas Automáticas
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/23_pago_recurrente.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/23_pago_recurrente.png" alt="Pago Recurrente, PAT & Cuentas Automáticas" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Calendario mensual 3D en azul marino y blanco con hojas de calendario superpuestas, acompañado de un símbolo circular de flechas de repetición periódica automática (engranaje de ciclo o refresh continuo) con un check de pago completado en el centro.

- **Concepto Semántico:** Pago Automático de Cuentas (PAT), suscripciones mensuales continuas, cobros desatendidos de servicios básicos, seguros o telecomunicaciones.
- **Intención de Negocio:** Asegurar un flujo mensual predecible e ineludible de facturación mediante la adhesión de cuentas básicas al cargo automático.
- **Métricas Clave:** `Cuentas inscritas en PAT, volumen mensual de cargos automáticos, reducción de churn de cartera.`
- **Disparadores Clave (Triggers):** `pago recurrente`, `pat`, `pago automatico`, `cuentas`, `servicios basicos`, `autopistas`, `suscripciones`, `cargo mensual`, `cuenta automatica`, `pago automatico de cuentas`

**Cuándo Usar:**
- ✅ Campañas que incentivan la inscripción de cuentas de luz, agua, gas, telecomunicaciones o autopistas a PAT.
- ✅ Promociones de cashback por cada nueva cuenta inscrita en pago automático.
- ✅ Recordatorios de desatención de cobros y tranquilidad financiera mensual.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar si solo se invita a guardar la tarjeta en una app para compras esporádicas (elegir 22_card_on_file_cof.png).
- ❌ NO usar para compras en cuotas comerciales (elegir 25_cuotas_sin_interes_csi.png).

**Copies de Ejemplo:**
- "Inscribe tus cuentas de luz, agua y telefonía a PAT y olvídate de las fechas de vencimiento."
- "Recibe $5.000 de cashback por cada cuenta que inscribas en Pago Automático este mes."

---

### 🔹 [24] `24_descuento.png` · Descuento Directo, Rebaja % OFF & Promoción
- **Familia Semántica:** Mecánicas, Crossborder & Travel
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/24_descuento.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/24_descuento.png" alt="Descuento Directo, Rebaja % OFF & Promoción" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Símbolo volumétrico tridimensional de porcentaje '%' en color azul cobalto brillante (#0032A0) con cantos redondeados y reflejos especulares de luz, acompañado de un destello estelar en relieve que transmite la idea de ahorro inmediato y oportunidad promocional destacada.

- **Concepto Semántico:** Rebaja porcentual o monetaria aplicada instantáneamente sobre el precio de venta en caja o checkout.
- **Intención de Negocio:** Mecánica promocional reina para traccionar volumen rápido en comercios aliados mediante el gancho del ahorro visible directo.
- **Métricas Clave:** `Conversión de campaña, facturación bruta en comercios adheridos, atractivo promocional percibido.`
- **Disparadores Clave (Triggers):** `descuento`, `% off`, `porcentaje de descuento`, `rebaja`, `ahorro directo`, `promocion`, `oferta`, `precio especial`, `30% de descuento`, `40% off`, `dto`

**Cuándo Usar:**
- ✅ Cualquier oferta que reduzca el precio de compra en el acto (ej. '30% de descuento los días martes').
- ✅ Bloques destacados de ahorro en campañas de alianzas comerciales.
- ✅ Cupones de rebaja inmediata al ingresar el RUT o código de promoción.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar cuando el dinero se devuelve semanas después en el estado de cuenta (elegir 09_cashback.png).
- ❌ NO usar cuando la recompensa se otorga en puntos o Dólares-Premio (elegir 10_dolares_premio.png).

**Copies de Ejemplo:**
- "Obtén hasta un 40% de descuento en las mejores marcas pagando con tus Tarjetas Banco de Chile."
- "Aprovecha este descuento exclusivo directo en caja durante todo el fin de semana."

---

### 🔹 [25] `25_cuotas_sin_interes_csi.png` · Cuotas Sin Interés (CSI) & Financiamiento a Plazos
- **Familia Semántica:** Mecánicas, Crossborder & Travel
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/25_cuotas_sin_interes_csi.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/25_cuotas_sin_interes_csi.png" alt="Cuotas Sin Interés (CSI) & Financiamiento a Plazos" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Conjunto de bloques modulares tridimensionales o tarjetas fraccionadas en serie secuencial (3, 6, 12) en azul marino y blanco, con la inscripción tridimensional '0%' en acabado dorado o plateado, denotando financiamiento en cuotas a tasa cero y precio contado.

- **Concepto Semántico:** Financiamiento fraccionado de compras en 3, 6, 12 o hasta 24 cuotas sin recargo de interés.
- **Intención de Negocio:** Viabilizar la compra de bienes de alto ticket (viajes, tecnología, muebles, automotriz) facilitando el flujo de caja del titular.
- **Métricas Clave:** `Facturación financiada, ticket promedio por compra, colocación de crédito comercial sin riesgo de mora.`
- **Disparadores Clave (Triggers):** `cuotas sin interes`, `csi`, `cuotas`, `3 cuotas`, `6 cuotas`, `12 cuotas`, `precio contado`, `financiamiento`, `paga en cuotas`, `a plazos`, `sin interes`

**Cuándo Usar:**
- ✅ Ofertas de financiamiento a precio contado (ej. 'Hasta 12 cuotas sin interés en tecnología y viajes').
- ✅ Campañas de pago de permisos de circulación o contribuciones en cuotas a tasa cero.
- ✅ Compras de alto valor en tiendas por departamento o clínicas.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para descuentos inmediatos en el valor total de compra (elegir 24_descuento.png).
- ❌ NO usar para devolución de dinero posterior (elegir 09_cashback.png).

**Copies de Ejemplo:**
- "Paga tus compras grandes en hasta 12 cuotas sin interés con tu Tarjeta de Crédito."
- "Financia tus proyectos a precio contado y mantén el control de tu presupuesto mensual."

---

### 🔹 [26] `26_meta_de_facturacion.png` · Meta por Monto de Facturación (Spend Target)
- **Familia Semántica:** Medios de Pago & Ciclo de Uso
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/26_meta_de_facturacion.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/26_meta_de_facturacion.png" alt="Meta por Monto de Facturación (Spend Target)" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Gráfico de barras ascendente en perspectiva 3D en azul cobalto con tres columnas de altura creciente, coronado por una flecha tridimensional ascendente blanca brillante y una bolsa de caudales o fajo de billetes dorados en la cima, indicando el logro de una cota monetaria elevada.

- **Concepto Semántico:** Desafío promocional condicionado a alcanzar un monto total acumulado de gasto en pesos chilenos (ej. gasta $300.000 o $500.000).
- **Intención de Negocio:** Aumentar el spend acumulado mensual por titular mediante metas de facturación agresivas con premios escalonados.
- **Métricas Clave:** `Facturación total mensual (spend per active), volumen promedio de gasto, captura de excedentes.`
- **Disparadores Clave (Triggers):** `meta de facturacion`, `spend target`, `monto acumulado`, `gasta 100000`, `gasta 300000`, `acumula compras`, `meta monetaria`, `volumen de gasto`, `desafio de monto`

**Cuándo Usar:**
- ✅ Campañas que condicionan el premio a un umbral de gasto en pesos (ej. 'Acumula $250.000 en compras y gana $25.000').
- ✅ Metas escalonadas de fin de año o campañas de Navidad por volumen de facturación.
- ✅ Segmentación de clientes VIP para incentivar consumo de alto rango.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar cuando la condición es el número de transacciones independientes (ej. haz 5 compras) (elegir 08_meta_de_transacciones.png).
- ❌ NO usar si solo se pide realizar la primera compra debut (elegir 06_primera_compra.png).

**Copies de Ejemplo:**
- "Acumula $300.000 en compras durante el mes con tu Tarjeta de Crédito y recibe una bonificación especial."
- "Alcanza tu meta de facturación mensual y participa por premios millonarios."

---

### 🔹 [27] `27_compra_internacional_crossborder.png` · Compra Internacional Presencial (Crossborder)
- **Familia Semántica:** Mecánicas, Crossborder & Travel
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/27_compra_internacional_crossborder.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/27_compra_internacional_crossborder.png" alt="Compra Internacional Presencial (Crossborder)" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Tarjeta de crédito física Banco de Chile 3D sobrevolando o cruzando un mapa terráqueo internacional, acompañada de símbolos de divisas extranjeras (símbolo de dólar americano $ y euro €) en acabado dorado brillante flotando en órbita, simbolizando el uso presencial de la tarjeta en comercios físicos alrededor del mundo.

- **Concepto Semántico:** Uso de la tarjeta física fuera de las fronteras chilenas durante viajes de turismo o negocios (compras en moneda extranjera en el extranjero).
- **Intención de Negocio:** Capturar el gasto transfronterizo del titular en el extranjero frente al uso de efectivo u otras tarjetas internacionales.
- **Métricas Clave:** `Volumen crossborder presencial, margen cambiario (FX margin), gasto en moneda extranjera.`
- **Disparadores Clave (Triggers):** `crossborder`, `compra internacional`, `compras en el extranjero`, `fuera de chile`, `compras en dolares`, `viajes al exterior`, `gasto extranjero`, `tiendas en el extranjero`, `pos internacional`

**Cuándo Usar:**
- ✅ Campañas previas a temporadas de vacaciones sobre uso de tarjetas en el extranjero.
- ✅ Promociones de comisión cero en compras internacionales presenciales.
- ✅ Consejos de seguridad y cobertura de seguro en comercios físicos del exterior.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para compras electrónicas por internet desde Chile en sitios extranjeros como Amazon (elegir 28_ecommerce_internacional.png).
- ❌ NO usar si el beneficio es el pasaje de avión o paquete turístico (elegir 19_viajes_turismo.png).

**Copies de Ejemplo:**
- "Viaja y compra seguro: usa tus Tarjetas Banco de Chile en comercios de todo el mundo sin comisión internacional."
- "Tus compras en el extranjero acumulan Dólares-Premio con la mejor tasa del mercado."

---

### 🔹 [28] `28_ecommerce_internacional.png` · Ecommerce Internacional & Compras Online en el Exterior
- **Familia Semántica:** Mecánicas, Crossborder & Travel
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/28_ecommerce_internacional.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/28_ecommerce_internacional.png" alt="Ecommerce Internacional & Compras Online en el Exterior" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Globo terráqueo tridimensional estilizado con meridianos luminosos, conectado con un cursor de flecha de navegación web 3D y un carrito de compras digital en color blanco y azul flotando sobre coordenadas globales, con un distintivo monetario 'USD' o monedas internacionales en relieve.

- **Concepto Semántico:** Compras no presenciales por internet en tiendas extranjeras facturadas en dólares o moneda extranjera (Amazon, AliExpress, Shein, eBay, Asos).
- **Intención de Negocio:** Fomentar el uso de tarjetas de crédito chilenas para compras online en plataformas transfronterizas compitiendo con tarjetas fintech o prepago.
- **Métricas Clave:** `Volumen CNP internacional, transacciones en marketplaces extranjeros, facturación USD online.`
- **Disparadores Clave (Triggers):** `ecommerce internacional`, `amazon`, `aliexpress`, `shein`, `ebay`, `compras online exterior`, `sitios extranjeros`, `tiendas de afuera`, `cnp internacional`, `comprar en dolares online`

**Cuándo Usar:**
- ✅ Campañas de compras en Amazon, AliExpress, Shein o marketplaces internacionales.
- ✅ Beneficios de cashback o cuotas sin interés en compras online extranjeras.
- ✅ Eventos globales de compra como Black Friday estadounidense o Cyber compras internacionales.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para compras físicas presenciales en tiendas del extranjero durante un viaje (elegir 27_compra_internacional_crossborder.png).
- ❌ NO usar para tiendas digitales chilenas que cobran en pesos (elegir 03_ecommerce.png).

**Copies de Ejemplo:**
- "Aprovecha este Black Friday comprando en Amazon y AliExpress con tu Tarjeta de Crédito Banco de Chile."
- "Tus compras online en el exterior sin comisiones sorpresa y con la máxima seguridad antifraude."

---

### 🔹 [29] `29_lounge_salon_vip.png` · Salones VIP & Lounge de Aeropuerto
- **Familia Semántica:** Mecánicas, Crossborder & Travel
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/29_lounge_salon_vip.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/29_lounge_salon_vip.png" alt="Salones VIP & Lounge de Aeropuerto" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Elegante sillón lounge individual de sala de espera VIP en 3D, tapizado en cuero premium azul noche con reposabrazos acolchados, junto a una mesa auxiliar redonda minimalista de pedestal dorado con una copa de cortesía y luz cálida de ambiente distendido.

- **Concepto Semántico:** Acceso exclusivo y estancias de descanso preferencial en salones VIP de aeropuertos nacionales e internacionales (Salones Pacific Club, Visa Airport Companion).
- **Intención de Negocio:** Atributo de valor premium para tarjetas de alto segmento (Visa Signature, Visa Infinite) que justifica el costo de mantención y fideliza al viajero frecuente.
- **Métricas Clave:** `Satisfacción de clientes segmento Premium/Banca Privada, uso de accesos VIP contratados, lealtad.`
- **Disparadores Clave (Triggers):** `lounge`, `salon vip`, `salones vip`, `pacific club`, `visa airport companion`, `aeropuerto vip`, `sala vip`, `espera aeropuerto`, `sala lounge`, `vip lounge`

**Cuándo Usar:**
- ✅ Comunicaciones que informan la cantidad de accesos anuales a Salones Pacific Club incluidos en el plan.
- ✅ Beneficios del programa Visa Airport Companion en terminales aéreas internacionales.
- ✅ Bienvenida a nuevos clientes de tarjetas Infinite y Signature destacando sus atributos de confort en viaje.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para turismo o pasajes de avión genéricos (elegir 19_viajes_turismo.png).
- ❌ NO usar para el servicio de transfer o transporte al aeropuerto (elegir 30_traslado_aeropuerto.png).

**Copies de Ejemplo:**
- "Disfruta de hasta 12 accesos gratuitos al año a Salones Pacific Club con tu Tarjeta Visa Infinite."
- "Haz que tu espera en el aeropuerto sea un placer con salas VIP exclusivas en todo el mundo."

---

### 🔹 [30] `30_traslado_aeropuerto.png` · Traslado Privado al Aeropuerto (Transfer)
- **Familia Semántica:** Mecánicas, Crossborder & Travel
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/icons/30_traslado_aeropuerto.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/icons/30_traslado_aeropuerto.png" alt="Traslado Privado al Aeropuerto (Transfer)" width="64" height="64" style="display:block; margin:0 auto;" />`

> **Descripción Visual Morfológica (3D):**  
> Vehículo de transporte de pasajeros moderno tipo van / minivan ejecutiva 3D en azul corporativo con lunas tintadas y faros aerodinámicos iluminados, avanzando de perfil con una maleta de viaje cargada en el maletero, denotando servicio de chófer privado y transfer puntual hacia la terminal aérea.

- **Concepto Semántico:** Servicio de transporte privado terrestre (van o automóvil ejecutivo) hacia o desde el aeropuerto (ej. convenio Transvip).
- **Intención de Negocio:** Resolver una necesidad logística crítica del viaje con una solución cómoda y sin costo adicional para clientes de planes de alta gama.
- **Métricas Clave:** `Utilización de cupos de traslado, satisfacción neta de clientes Travel, fidelización de ejecutivos frecuentes.`
- **Disparadores Clave (Triggers):** `traslado aeropuerto`, `transfer`, `transvip`, `van aeropuerto`, `transporte aeropuerto`, `traslado gratis`, `chofer aeropuerto`, `transfer ejecutivo`, `viaje al aeropuerto`

**Cuándo Usar:**
- ✅ Comunicación de traslados gratuitos incluidos en el plan anual (ej. '4 traslados al año hacia el aeropuerto').
- ✅ Convenios y descuentos con Transvip u operadores de transporte hacia el aeropuerto de Santiago o regiones.
- ✅ Parrillas de beneficios de viajes de temporada alta.

**Cuándo NO Usar (Anti-patrones):**
- ❌ NO usar para bencina o carga de combustible de autos particulares (elegir 14_combustible.png).
- ❌ NO usar para la estancia en salones VIP dentro del aeropuerto (elegir 29_lounge_salon_vip.png).

**Copies de Ejemplo:**
- "Inicia tus vacaciones sin preocupaciones: reserva tu traslado gratuito al aeropuerto con tu Tarjeta Travel."
- "Disfruta de hasta 4 traslados ejecutivos al aeropuerto al año con tu Plan Travel Infinite."

---

## ✈️ DOSSIER EXHAUSTIVO: LOS 10 ÍCONOS TRAVEL CLUB BANCO DE CHILE

### 🔸 [T01] `01_bch_icono_ticket_viaje_ncde7f.png` · Ticket de Vuelo / Boarding Pass Travel Club
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/travel/01_bch_icono_ticket_viaje_ncde7f.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/travel/01_bch_icono_ticket_viaje_ncde7f.png" alt="Ticket de Vuelo / Boarding Pass Travel Club" width="64" height="64" />`

> **Descripción Visual Morfológica:**  
> Pase de abordar (boarding pass) tridimensional en acabado blanco satinado con franjas azul corporativo. Muestra una silueta de avión despegando en relieve, código de barras troquelado y datos de vuelo estilizados.

- **Concepto Semántico:** Pasajes aéreos, boletos de avión, check-in y tickets de viaje emitidos a través de Travel Club.
- **Disparadores (Triggers):** `boarding pass`, `ticket viaje`, `pasaje aereo`, `boleto de avion`, `check in`, `ticket de vuelo`, `pasaje travel`
- **Cuándo Usar:** Promociones directas de compra de pasajes con Dólares-Premio o cuotas sin interés en aerolíneas.
- **Cuándo NO Usar:** No usar para compras en tiendas comunes o supermercados.

---

### 🔸 [T02] `02_bch_icono_dolares_premio_pplf0o.png` · Moneda Dólares-Premio Travel Club
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/travel/02_bch_icono_dolares_premio_pplf0o.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/travel/02_bch_icono_dolares_premio_pplf0o.png" alt="Moneda Dólares-Premio Travel Club" width="64" height="64" />`

> **Descripción Visual Morfológica:**  
> Moneda tridimensional dorada brillante con las iniciales 'DP' grabadas en el centro y una estrella dorada característica del programa Travel Club en la parte superior.

- **Concepto Semántico:** Moneda propia del programa de lealtad Travel Club para acumulación y canje.
- **Disparadores (Triggers):** `moneda dp`, `dolares premio travel`, `canje travel club`, `puntos travel club`, `saldo dp`
- **Cuándo Usar:** Bloques de acumulación o saldo de puntos del programa de fidelización.
- **Cuándo NO Usar:** No usar para cashback en pesos o descuentos en caja.

---

### 🔸 [T03] `03_bch_icono_cuotas_viaje_kml5fp.png` · Cuotas Sin Interés en Pasajes y Turismo
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/travel/03_bch_icono_cuotas_viaje_kml5fp.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/travel/03_bch_icono_cuotas_viaje_kml5fp.png" alt="Cuotas Sin Interés en Pasajes y Turismo" width="64" height="64" />`

> **Descripción Visual Morfológica:**  
> Composición 3D que une un avión comercial con bloques numéricos de cuotas (3 a 12 cuotas) con el rótulo de tasa cero, orientado específicamente a compras turísticas.

- **Concepto Semántico:** Financiamiento de pasajes aéreos, cruceros y paquetes de viaje en cuotas sin interés.
- **Disparadores (Triggers):** `cuotas viaje`, `cuotas turismo`, `pasajes en cuotas`, `financiamiento travel`, `cuotas sin interes viaje`
- **Cuándo Usar:** Ofertas de pasajes en 3, 6 o 12 cuotas sin interés en aerolíneas y agencias.
- **Cuándo NO Usar:** No usar para cuotas de retail o supermercado.

---

### 🔸 [T04] `04_bch_icono_tasa_preferencial_viajes_qwzxxt.png` · Tasa Preferencial de Cambio para Viajeros
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/travel/04_bch_icono_tasa_preferencial_viajes_qwzxxt.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/travel/04_bch_icono_tasa_preferencial_viajes_qwzxxt.png" alt="Tasa Preferencial de Cambio para Viajeros" width="64" height="64" />`

> **Descripción Visual Morfológica:**  
> Símbolos de divisas ($ y USD) en 3D entrelazados con una flecha verde descendente de ventaja cambiaria y tasa preferencial de compra de dólares.

- **Concepto Semántico:** Tipo de cambio preferencial en compra de dólares para titulares de tarjetas Banco de Chile.
- **Disparadores (Triggers):** `tasa preferencial`, `tipo de cambio travel`, `cambio de dolares`, `dolar preferencial`, `fx preferencial`
- **Cuándo Usar:** Campañas de compra de moneda extranjera previa a las vacaciones.
- **Cuándo NO Usar:** No usar para compras comunes en pesos.

---

### 🔸 [T05] `05_bch_icono_tarjeta_activada_extranjero_h03q2v.png` · Tarjeta Habilitada para el Extranjero (Aviso de Viaje)
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/travel/05_bch_icono_tarjeta_activada_extranjero_h03q2v.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/travel/05_bch_icono_tarjeta_activada_extranjero_h03q2v.png" alt="Tarjeta Habilitada para el Extranjero (Aviso de Viaje)" width="64" height="64" />`

> **Descripción Visual Morfológica:**  
> Tarjeta de crédito física junto a un globo terráqueo y un checkmark verde de validación de aviso de viaje registrado.

- **Concepto Semántico:** Configuración de seguridad y habilitación de uso internacional antes de viajar.
- **Disparadores (Triggers):** `aviso de viaje`, `tarjeta en el extranjero`, `habilitar para viajar`, `seguridad en viaje`, `tarjeta habilitada exterior`
- **Cuándo Usar:** Checklists previos a las vacaciones para recordar activar la tarjeta en la app antes de salir de Chile.
- **Cuándo NO Usar:** No usar para activación de tarjeta nueva por primera vez.

---

### 🔸 [T06] `06_bch_icono_traslado_aeropuerto_r9goav.png` · Van Ejecutiva de Transfer Aeropuerto Travel
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/travel/06_bch_icono_traslado_aeropuerto_r9goav.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/travel/06_bch_icono_traslado_aeropuerto_r9goav.png" alt="Van Ejecutiva de Transfer Aeropuerto Travel" width="64" height="64" />`

> **Descripción Visual Morfológica:**  
> Minivan ejecutiva moderna 3D en azul institucional con maleta cargada y ruta trazada hacia el aeropuerto.

- **Concepto Semántico:** Servicio de transfer o van ejecutiva al aeropuerto exclusivo del catálogo Travel Club.
- **Disparadores (Triggers):** `transfer travel`, `van travel`, `traslado travel`, `van aeropuerto travel`, `movilizacion travel`
- **Cuándo Usar:** Bloques dedicados al beneficio de traslado en comunicaciones Travel Club.
- **Cuándo NO Usar:** No usar para combustible o transporte público.

---

### 🔸 [T07] `07_bch_icono_avion_despegue_gcez6a.png` · Avión en Despegue & Vuelos Internacionales
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/travel/07_bch_icono_avion_despegue_gcez6a.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/travel/07_bch_icono_avion_despegue_gcez6a.png" alt="Avión en Despegue & Vuelos Internacionales" width="64" height="64" />`

> **Descripción Visual Morfológica:**  
> Avión comercial bimotor de fuselaje ancho en ángulo de ascenso de 45 grados sobre una estela de condensación azulada.

- **Concepto Semántico:** Vuelos internacionales de larga distancia, despegue de vacaciones y destinos lejanos.
- **Disparadores (Triggers):** `avion despegue`, `vuelo internacional`, `despegue`, `vuelos largos`, `escapada en avion`
- **Cuándo Usar:** Cabeceras hero de campañas de vuelos al exterior y ferias de viajes.
- **Cuándo NO Usar:** No usar para compras de supermercado o retail.

---

### 🔸 [T08] `08_bch_icono_hotel_premium_aylvme.png` · Hoteles, Resorts & Alojamiento Premium
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/travel/08_bch_icono_hotel_premium_aylvme.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/travel/08_bch_icono_hotel_premium_aylvme.png" alt="Hoteles, Resorts & Alojamiento Premium" width="64" height="64" />`

> **Descripción Visual Morfológica:**  
> Fachada de hotel 5 estrellas moderno en 3D con marquesina iluminada, palmeras y estrellas doradas de categorización hotelera.

- **Concepto Semántico:** Estadías, resorts all-inclusive, hoteles boutique y reservas de alojamiento.
- **Disparadores (Triggers):** `hotel`, `resort`, `alojamiento`, `hoteles premium`, `estadia`, `hospedaje`, `booking travel`
- **Cuándo Usar:** Beneficios de noches de cortesía, descuentos en cadenas hoteleras y paquetes all inclusive.
- **Cuándo NO Usar:** No usar para restaurantes sin alojamiento.

---

### 🔸 [T09] `09_bch_icono_maleta_viaje_ntmoww.png` · Maleta de Viaje & Equipaje de Vacaciones
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/travel/09_bch_icono_maleta_viaje_ntmoww.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/travel/09_bch_icono_maleta_viaje_ntmoww.png" alt="Maleta de Viaje & Equipaje de Vacaciones" width="64" height="64" />`

> **Descripción Visual Morfológica:**  
> Valija rígida de viaje 3D en azul cobalto con asa telescópica plateada desplegada, 4 ruedas dobles 360° y etiquetas de destino.

- **Concepto Semántico:** Preparación del viaje, equipaje, vacaciones de temporada y turismo.
- **Disparadores (Triggers):** `maleta`, `equipaje`, `valija`, `hacer maleta`, `vacaciones travel`, `preparar viaje`
- **Cuándo Usar:** Campañas de temporada de verano, consejos de viaje y promociones de equipaje gratuito.
- **Cuándo NO Usar:** No usar para compras de supermercado.

---

### 🔸 [T10] `10_bch_icono_bono_bienvenida_iaohbl.png` · Caja de Regalo & Bono de Bienvenida Travel
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/travel/10_bch_icono_bono_bienvenida_iaohbl.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/travel/10_bch_icono_bono_bienvenida_iaohbl.png" alt="Caja de Regalo & Bono de Bienvenida Travel" width="64" height="64" />`

> **Descripción Visual Morfológica:**  
> Caja de regalo 3D en color azul marino brillante envuelta con una cinta dorada sedosa y gran lazo superior, de la que emanan destellos luminosos de puntos.

- **Concepto Semántico:** Bono de bienvenida, regalo por contratación de plan Travel y puntos de apertura.
- **Disparadores (Triggers):** `bono bienvenida travel`, `regalo travel`, `premio bienvenida`, `caja regalo travel`, `puntos de regalo`
- **Cuándo Usar:** Piezas de contratación de nuevos planes Travel que incluyen regalo o puntos de apertura.
- **Cuándo NO Usar:** No usar para reactivación de clientes antiguos.

---

## 🏛️ DOSSIER EXHAUSTIVO: LOGOTIPOS OFICIALES BANCO DE CHILE

### 🔹 [L01] `banco_de_chile.png` · Logotipo Institucional Horizontal Banco de Chile
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/logos/banco_de_chile.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/logos/banco_de_chile.png" alt="Logotipo Institucional Horizontal Banco de Chile" height="32" />`

> **Descripción Visual:**  
> Logotipo institucional horizontal completo de Banco de Chile en tipografía gótica corporativa azul marino (#002464) sobre fondo 100% transparente con canal alfa limpio.

- **Concepto:** Identidad corporativa principal para cabeceras y encabezados de correo.
- **Disparadores (Triggers):** `logo banco de chile`, `wordmark bch`, `logotipo principal`, `marca bch`, `cabecera bch`
- **Cuándo Usar:** Encabezado superior izquierdo o central de cualquier correo o diapositiva de Banco de Chile sobre fondo blanco o claro.
- **Cuándo NO Usar:** No usar sobre fondos oscuros azul marino si no cuenta con contraste suficiente.

---

### 🔹 [L02] `bch_logo.png` · Isotipo Estrella Azul Oficial Banco de Chile
- **URL Canónica CDN:** `https://mkt-visa.vercel.app/assets/bch/logos/bch_logo.png`
- **Snippet HTML:** `<img src="https://mkt-visa.vercel.app/assets/bch/logos/bch_logo.png" alt="Isotipo Estrella Azul Oficial Banco de Chile" height="32" />`

> **Descripción Visual:**  
> Isotipo icónico de estrella estilizada de Banco de Chile en color azul corporativo brillante en alta resolución con fondo transparente.

- **Concepto:** Monograma e isotipo para favicons, marcas de agua, avatares y co-branding compacto.
- **Disparadores (Triggers):** `estrella bch`, `isotipo banco de chile`, `icono banco de chile`, `logo cuadrado bch`, `favicon bch`
- **Cuándo Usar:** Firmas de pie de página, viñetas de lista, iconos de app o co-branding compacto.
- **Cuándo NO Usar:** No usar como encabezado principal si se requiere la lectura del nombre completo de la institución.

---

## ⚖️ CRITERIOS CRÍTICOS DE DESEMPATE SEMÁNTICO
Guía rápida para resolver ambivalencias comunes en requerimientos de marketing:

### 1. Cashback vs Descuento
- **Cashback (`09_cashback.png`)**: Dinero devuelto con posterioridad en la cuenta corriente o estado de cuenta. *Palabras clave:* reintegro, abono, te devolvemos, abono en cuenta.
- **Descuento (`24_descuento.png`)**: Rebaja directa e inmediata en el precio de venta en caja o web. *Palabras clave:* % OFF, 30% descuento, precio rebajado, cupón de ahorro.

### 2. Activación vs Primera Compra vs Reactivación
- **Activación (`05_activacion.png`)**: Producto nuevo recibido físicamente; se debe encender, desbloquear o definir PIN.
- **Primera Compra (`06_primera_compra.png`)**: Producto ya habilitado que realiza su primera transacción histórica (debut del cliente).
- **Reactivación (`07_reactivacion.png`)**: Cliente antiguo que dejó de usar la tarjeta en los últimos 30 a 90 días (winback de inactivos).

### 3. Ecommerce Nacional vs Ecommerce Internacional
- **Ecommerce Nacional (`03_ecommerce.png`)**: Comercios chilenos que operan en pesos (Mercado Libre Chile, Falabella, Paris, tiendas locales).
- **Ecommerce Internacional (`28_ecommerce_internacional.png`)**: Plataformas radicadas en el extranjero que facturan en dólares (Amazon, AliExpress, Shein, eBay).

### 4. Card on File (COF) vs Pago Recurrente (PAT)
- **Card on File (`22_card_on_file_cof.png`)**: Guardar la tarjeta en apps para compras puntuales a demanda (Uber, PedidosYa, Cabify).
- **Pago Recurrente (`23_pago_recurrente.png`)**: Mandato de cargo mensual fijo o variable desatendido (cuentas de luz, agua, autopistas, colegios).

### 5. Meta de Transacciones vs Meta de Facturación
- **Meta de Transacciones (`08_meta_de_transacciones.png`)**: Condición expresada en número de compras (ej. 'haz 5 compras de cualquier monto').
- **Meta de Facturación (`26_meta_de_facturacion.png`)**: Condición expresada en monto acumulado en pesos (ej. 'acumula $300.000 en compras').

---

## 🤖 PROMPT DE SISTEMA LISTO PARA INYECTAR EN AGENTES LLM
```text
Eres el Selector Determinista de Iconografía para Medios de Pago de Banco de Chile y Visa.
Tu tarea es analizar el requerimiento textual del usuario, extraer el concepto semántico dominante y devolver el ícono oficial más adecuado de la biblioteca BCH (80 activos verificados).

Reglas Obligatorias:
1. NUNCA inventes nombres de archivo ni rutas relativas locales.
2. SIEMPRE utiliza la URL absoluta de producción en Vercel: https://mkt-visa.vercel.app/assets/bch/...
3. Aplica la Prioridad Semántica: Acción > Mecánica/Condición > Rubro > Producto > Contexto.
4. Consulta la descripción visual morfológica de la matriz para verificar la idoneidad estética y conceptual.
5. Devuelve la salida en formato JSON con la siguiente estructura:
{
  "icon_id": "06",
  "icon_name": "Primera Compra",
  "filename": "06_primera_compra.png",
  "cdn_url": "https://mkt-visa.vercel.app/assets/bch/icons/06_primera_compra.png",
  "html_tag": "<img src=\"https://mkt-visa.vercel.app/assets/bch/icons/06_primera_compra.png\" alt=\"Primera Compra\" width=\"64\" height=\"64\" />",
  "reason": "La campaña incentiva el debut transaccional del cliente nuevo.",
  "confidence": 0.99
}
```


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
| **[01]** | Tarjeta de Crédito Genérica | `01_medios_pago_ciclo_uso` | `01_tarjeta_visa.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/01_tarjeta_visa.png` |
| **[02]** | Pago Presencial POS | `01_medios_pago_ciclo_uso` | `02_pago_presencial_pos.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/02_pago_presencial_pos.png` |
| **[03]** | Ecommerce Nacional | `01_medios_pago_ciclo_uso` | `03_ecommerce.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/03_ecommerce.png` |
| **[04]** | Wallet & Pago Móvil | `01_medios_pago_ciclo_uso` | `04_wallet_pago_movil.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/04_wallet_pago_movil.png` |
| **[05]** | Activación de Tarjeta | `01_medios_pago_ciclo_uso` | `05_activacion.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/05_activacion.png` |
| **[06]** | Primera Compra | `01_medios_pago_ciclo_uso` | `06_primera_compra.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/06_primera_compra.png` |
| **[07]** | Reactivación de Clientes | `01_medios_pago_ciclo_uso` | `07_reactivacion.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/07_reactivacion.png` |
| **[08]** | Meta de Transacciones | `01_medios_pago_ciclo_uso` | `08_meta_de_transacciones.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/08_meta_de_transacciones.png` |
| **[09]** | Cashback / Devolución | `01_medios_pago_ciclo_uso` | `09_cashback.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/09_cashback.png` |
| **[10]** | Dólares-Premio (DP) | `01_medios_pago_ciclo_uso` | `10_dolares_premio.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/01_medios_pago_ciclo_uso/10_dolares_premio.png` |
| **[11]** | Supermercados | `02_rubros_consumo` | `11_supermercado.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/11_supermercado.png` |
| **[12]** | Gastronomía & Restaurantes | `02_rubros_consumo` | `12_gastronomia_restaurantes.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/12_gastronomia_restaurantes.png` |
| **[13]** | Cafeterías & Coffee | `02_rubros_consumo` | `13_cafe_cafeterias.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/13_cafe_cafeterias.png` |
| **[14]** | Combustible & Bencina | `02_rubros_consumo` | `14_combustible.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/14_combustible.png` |
| **[15]** | Farmacias & Salud | `02_rubros_consumo` | `15_farmacia_salud.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/15_farmacia_salud.png` |
| **[16]** | Retail & Shopping | `02_rubros_consumo` | `16_retail_shopping.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/16_retail_shopping.png` |
| **[17]** | Tecnología & Electro | `02_rubros_consumo` | `17_tecnologia.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/17_tecnologia.png` |
| **[18]** | Delivery & Apps de Envíos | `02_rubros_consumo` | `18_delivery.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/18_delivery.png` |
| **[19]** | Viajes & Turismo | `02_rubros_consumo` | `19_viajes_turismo.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/19_viajes_turismo.png` |
| **[20]** | Entretenimiento & Conciertos | `02_rubros_consumo` | `20_entretenimiento_musica.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/02_rubros_consumo/20_entretenimiento_musica.png` |
| **[21]** | Pago Sin Contacto (Contactless) | `03_mecanicas_crossborder_travel` | `21_contactless.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/21_contactless.png` |
| **[22]** | Card on File (COF) | `03_mecanicas_crossborder_travel` | `22_card_on_file_cof.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/22_card_on_file_cof.png` |
| **[23]** | Pago Recurrente / PAT | `03_mecanicas_crossborder_travel` | `23_pago_recurrente.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/23_pago_recurrente.png` |
| **[24]** | Descuento / Porcentaje OFF | `03_mecanicas_crossborder_travel` | `24_descuento.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/24_descuento.png` |
| **[25]** | Cuotas Sin Interés (CSI) | `03_mecanicas_crossborder_travel` | `25_cuotas_sin_interes_csi.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/25_cuotas_sin_interes_csi.png` |
| **[26]** | Meta de Facturación | `03_mecanicas_crossborder_travel` | `26_meta_de_facturacion.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/26_meta_de_facturacion.png` |
| **[27]** | Compra Internacional Presencial | `03_mecanicas_crossborder_travel` | `27_compra_internacional_crossborder.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/27_compra_internacional_crossborder.png` |
| **[28]** | Ecommerce Internacional | `03_mecanicas_crossborder_travel` | `28_ecommerce_internacional.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/28_ecommerce_internacional.png` |
| **[29]** | Salones VIP & Travel Lounge | `03_mecanicas_crossborder_travel` | `29_lounge_salon_vip.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/29_lounge_salon_vip.png` |
| **[30]** | Traslado al Aeropuerto | `03_mecanicas_crossborder_travel` | `30_traslado_aeropuerto.png` | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/03_mecanicas_crossborder_travel/30_traslado_aeropuerto.png` |

### ⚡ Regla de Selección 2D vs 3D para LLMs y Diseñadores:
- **Usar versión 3D (`assets/bch/icons/...`)**: Cuando el diseño principal use componentes 3D renderizados, degradados con volumen, tarjetas metálicas o piezas hero ricas en textura.
- **Usar versión 2D (`assets/bch/iconos_bch_2d_30/...`)**: Cuando la interfaz o email siga una guía de diseño plana (*Flat Design*), infografías sencillas, badges circulares pequeños (< 32px) o comunicaciones corporativas sobrias.


---

## 🎨 GRUPO 4 · ÍCONOS 2D EXTENDIDOS — CONTEXTOS ESPECÍFICOS, INNOVACIÓN & CANALES

> **Rango:** 31–40 · **Disponibles físicamente:** 31–38 (39 y 40 pendientes de subida)  
> **CDN base:** `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/{filename}`

Este grupo **complementa** y **no reemplaza** la biblioteca base de 30 íconos 2D. Activar cuando el mensaje requiere mayor precisión contextual que los rubros generales del Grupo 2 o las mecánicas del Grupo 3.

### 🔑 Principio de especificidad:
> Si el mensaje puede usar un ícono más específico del Grupo 4, siempre preferirlo sobre el genérico del Grupo base.

### 📋 Catálogo Grupo 4:

| ID | Archivo | Concepto | CDN URL | Usar cuando |
|---|---|---|---|---|
| 31 | `31_inteligencia_artificial.png` | Inteligencia Artificial | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/31_inteligencia_artificial.png` | IA, chatbot, automatización inteligente, experiencias AI |
| 32 | `32_streaming_suscripciones.png` | Streaming & Suscripciones | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/32_streaming_suscripciones.png` | Netflix, Spotify, plataformas de contenido, mensualidades digitales |
| 33 | `33_cine.png` | Cine | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/33_cine.png` | Películas, entradas al cine, Cinema |
| 34 | `34_conciertos_musica_en_vivo.png` | Conciertos & Música en Vivo | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/34_conciertos_musica_en_vivo.png` | Recitales, festivales, preventas, shows |
| 35 | `35_moda_vestuario.png` | Moda & Vestuario | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/35_moda_vestuario.png` | Ropa, moda, fashion, retail textil |
| 36 | `36_hogar.png` | Hogar & Deco | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/36_hogar.png` | Casa, muebles, decoración, línea blanca, mejoramiento del hogar |
| 37 | `37_mascotas.png` | Mascotas | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/37_mascotas.png` | Veterinaria, pet shop, animales, perros, gatos |
| 38 | `38_salud_clinica_medico.png` | Salud Clínica & Médico | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/38_salud_clinica_medico.png` | Clínicas, médico, consultas, prestación de salud |
| 39 | `39_seguridad_proteccion.png` | Seguridad & Protección | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/39_seguridad_proteccion.png` | Compra segura, antifraude, respaldo, protección |
| 40 | `40_app_canal_digital.png` | App Canal Digital | `https://mkt-visa.vercel.app/assets/bch/iconos_bch_2d_30/iconos_bch_2d_grupo4_10/40_app_canal_digital.png` | App Mi Banco, autogestión, canal digital |

### ⚡ Diferencias críticas Grupo 4 vs Base:

| Situación | ❌ No usar | ✅ Usar Grupo 4 |
|---|---|---|
| Campaña habla de IA | `17_tecnologia` | `31_inteligencia_artificial` |
| Pago en plataformas streaming | `23_pago_recurrente` | `32_streaming_suscripciones` |
| Descuento en cine | `20_entretenimiento_musica` | `33_cine` |
| Preventa concierto | `20_entretenimiento_musica` | `34_conciertos_musica_en_vivo` |
| Beneficio en moda/ropa | `16_retail_shopping` | `35_moda_vestuario` |
| Compras para el hogar | `16_retail_shopping` | `36_hogar` |
| Beneficio en veterinaria | `15_farmacia_salud` | `37_mascotas` |
| Atención médica/clínica | `15_farmacia_salud` | `38_salud_clinica_medico` |
| Compra segura online | `01_tarjeta_visa` | `39_seguridad_proteccion` |
| App del banco (autogestión) | `04_wallet_pago_movil` | `40_app_canal_digital` |

### 🔢 Keywords de Activación Grupo 4:

| Keywords | Ícono |
|---|---|
| `IA`, `inteligencia artificial`, `chatbot`, `asistente AI`, `automatización` | 31 |
| `streaming`, `suscripción`, `plataforma digital`, `mensualidad contenido` | 32 |
| `cine`, `película`, `cinema`, `entrada cine` | 33 |
| `concierto`, `recital`, `festival`, `preventa show`, `música en vivo` | 34 |
| `moda`, `vestuario`, `ropa`, `fashion` | 35 |
| `hogar`, `muebles`, `casa`, `decoración`, `línea blanca` | 36 |
| `mascotas`, `veterinaria`, `pet`, `perro`, `gato` | 37 |
| `clínica`, `médico`, `consulta`, `salud asistencial` | 38 |
| `seguridad`, `protección`, `antifraude`, `compra segura` | 39 |
| `app`, `canal digital`, `app Mi Banco`, `autogestión` | 40 |

