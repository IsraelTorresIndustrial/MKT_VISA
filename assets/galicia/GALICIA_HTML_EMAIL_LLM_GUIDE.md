# 🦁 Banco Galicia · Guía de Selección de Íconos y Headers para LLM Email Maker
> **Propósito Exclusivo:** Este documento es una directiva de referencia para agentes LLM y herramientas de generación de correo electrónico.  
> **Alcance:** Define con exactitud qué activo utilizar para cada contexto comercial o beneficio, su URL CDN canónica de producción en Vercel Edge y el snippet de inserción de imagen correspondiente.  
> **Nota de Alcance:** No contiene reglas de diseño o maquetación HTML de correos; su única función es asegurar la selección 100% correcta de íconos y headers oficiales de Banco Galicia.

---

## ⚡ 1. DIRECTIVA DE URLs CDN (PRODUCCIÓN VERCEL EDGE)

Todos los activos deben insertarse utilizando obligatoriamente las URLs absolutas canónicas de Vercel:

```text
Headers Hero Sin Texto (1100px):
https://mkt-visa.vercel.app/assets/galicia/headers/{filename}.png

Íconos 3D Oficiales:
https://mkt-visa.vercel.app/assets/galicia/icons/{filename}.png

Logotipo Institucional:
https://mkt-visa.vercel.app/assets/galicia/logos/{filename}.png
```

---

## 🏷️ 2. FORMATOS ESTÁNDAR DE INSERCIÓN `<img>`

Para garantizar nitidez retina y evitar desbordes:

### 2.1 Inserción de Íconos 3D (48x48px o 56x56px)
```html
<img src="https://mkt-visa.vercel.app/assets/galicia/icons/{filename}.png" alt="{Nombre del Concepto}" width="48" height="48" border="0" style="display:block; margin:0 auto;" />
```

### 2.2 Inserción de Headers Hero Sin Texto (550px o 600px ancho de correo)
```html
<img src="https://mkt-visa.vercel.app/assets/galicia/headers/{filename}.png" alt="Beneficios Galicia Visa" width="550" border="0" style="display:block; width:100%; max-width:550px; height:auto; margin:0 auto;" />
```

### 2.3 Inserción de Logotipo de Cabecera (Header / Barra Superior)
```html
<img src="https://mkt-visa.vercel.app/assets/galicia/logos/logo_galicia_header.png" alt="Banco Galicia" width="40" height="38" border="0" style="display:inline-block; vertical-align:middle;" />
```

---

## 🎯 3. TABLA MAESTRA DE DECISIÓN: CONTEXTO → ACTIVO → URL CANÓNICA

### 3.1 Headers Hero Sin Texto (Imágenes de Cabecera)

| Si el correo trata sobre... | Disparadores / Palabras Clave | Archivo a Usar | URL Canónica CDN |
|---|---|---|---|
| **Cafeterías, desayunos, pastelería o rutina diaria de consumo** | `cafeterias`, `desayuno`, `cafe`, `starbucks`, `havanna`, `rutina`, `mañanas`, `take away` | `header_promos_visa_permanentes_07.png` | `https://mkt-visa.vercel.app/assets/galicia/headers/header_promos_visa_permanentes_07.png` |
| **Compras en comercios físicos, indumentaria, cuotas o shoppings** | `shopping`, `locales`, `tiendas fisicas`, `cuotas sin interes`, `indumentaria`, `moda`, `ahorra y compra` | `header_promos_visa_permanentes_08.png` | `https://mkt-visa.vercel.app/assets/galicia/headers/header_promos_visa_permanentes_08.png` |
| **Pagos sin contacto (Tap to Pay), NFC o billeteras digitales (MODO, Apple Pay)** | `contactless`, `nfc`, `tap to pay`, `modo`, `apple pay`, `google pay`, `acercar al lector`, `pagar con celu` | `header_promos_visa_permanentes_09.png` | `https://mkt-visa.vercel.app/assets/galicia/headers/header_promos_visa_permanentes_09.png` |
| **Compras online, delivery a domicilio o correos con grilla extensa inferior** | `ecommerce`, `online`, `delivery`, `envios`, `pedidosya`, `mercadolibre`, `paquete`, `grilla extensa` | `header_promos_visa_permanentes_10.png` | `https://mkt-visa.vercel.app/assets/galicia/headers/header_promos_visa_permanentes_10.png` |
| **Comunicaciones institucionales sobrias, tutoriales o onboarding digital** | `onboarding`, `tutorial`, `como pagar`, `resumen`, `notificacion`, `sobrio`, `minimalista`, `marfil` | `header_promos_visa_permanentes_11.png` | `https://mkt-visa.vercel.app/assets/galicia/headers/header_promos_visa_permanentes_11.png` |
| **Grandes eventos comerciales, mega ofertas o lanzamientos masivos** | `hotsale`, `cybermonday`, `blackfriday`, `mega promos`, `semana galicia`, `alerta promo`, `urgente` | `header_promos_visa_permanentes_12.png` | `https://mkt-visa.vercel.app/assets/galicia/headers/header_promos_visa_permanentes_12.png` |

---

### 3.2 Servicios Básicos, Pagos de Cuentas & Conectividad

| Si el beneficio o mensaje trata sobre... | Disparadores / Palabras Clave | Archivo a Usar | URL Canónica CDN |
|---|---|---|---|
| **Facturas de electricidad y consumo de luz** | `luz`, `electricidad`, `edenor`, `edesur`, `epec`, `edelap`, `factura electrica`, `lampara` | `luz_lampara.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/luz_lampara.png` |
| **Facturas de gas natural de red o garrafas** | `gas`, `gas natural`, `metrogas`, `naturgy`, `camuzzi`, `ecogas`, `calefaccion` | `gas.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/gas.png` |
| **Facturas de agua corriente, potable o saneamiento** | `agua`, `aysa`, `aguas cordobesas`, `canilla`, `saneamiento`, `factura de agua`, `expensas` | `canilla.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/canilla.png` |
| **Fechas de vencimiento, alertas de cobro o mora** | `vencimiento`, `fecha limite`, `factura por vencer`, `recordatorio de pago`, `cuota`, `evitar mora` | `auriculares_2.png` *(Calendario 3D)* | `https://mkt-visa.vercel.app/assets/galicia/icons/auriculares_2.png` |
| **Pagos express, acreditación instantánea o flash** | `en el acto`, `inmediato`, `al instante`, `pago flash`, `rayo`, `rapido`, `oferta relampago` | `rayo.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/rayo.png` |
| **Abonos de Internet del hogar, Wi-Fi o fibra óptica** | `wifi`, `internet`, `fibra optica`, `flow`, `telecentro`, `movistar fibra`, `conectividad` | `wi_fi.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/wi_fi.png` |
| **App Galicia móvil, Billetera MODO o recargas celulares** | `celular`, `app galicia`, `modo`, `apple pay`, `wallet`, `recarga movil`, `confirmacion de debito` | `celular.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/celular.png` |

---

### 3.3 Galicia Seguros & Coberturas

| Si el beneficio o mensaje trata sobre... | Disparadores / Palabras Clave | Archivo a Usar | URL Canónica CDN |
|---|---|---|---|
| **Seguro automotor, remolque o auxilio mecánico** | `seguro auto`, `automotor`, `vehiculo`, `auxilio mecanico`, `grua`, `cobertura terceros`, `todo riesgo` | `seguro_auto.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/seguro_auto.png` |
| **Seguro de hogar, vivienda o combinado familiar** | `seguro hogar`, `vivienda`, `casa`, `departamento`, `combinado familiar`, `robo`, `incendio`, `plomeria` | `seguro_hogar.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/seguro_hogar.png` |
| **Seguro de vida individual o bienestar familiar** | `seguro de vida`, `vida`, `familia`, `proteccion familiar`, `bienestar`, `accidentes personales` | `seguro_vida.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/seguro_vida.png` |
| **Ecosistema integral de seguros o póliza activa** | `seguros`, `galicia seguros`, `poliza activa`, `cobertura asegurada`, `tranquilidad`, `respaldo` | `seguros.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/seguros.png` |
| **Protección ante imprevistos o fondo de emergencia** | `imprevistos`, `dias de lluvia`, `contingencias`, `fondo de reserva`, `asistencia`, `paraguas` | `paraguas.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/paraguas.png` |
| **Asistencia médica, salud o cobertura de urgencias** | `salud`, `primeros auxilios`, `asistencia medica`, `urgencias`, `farmacias`, `asistencia al viajero` | `primeros_auxilios.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/primeros_auxilios.png` |

---

### 3.4 Entretenimiento, Cine, Shows & Cultura

| Si el beneficio o mensaje trata sobre... | Disparadores / Palabras Clave | Archivo a Usar | URL Canónica CDN |
|---|---|---|---|
| **Salas de cine, estrenos y 2x1 en películas** | `cine`, `peliculas`, `estrenos`, `cartelera`, `cinemark`, `hoyts`, `showcase`, `2x1 en cine` | `cine.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/cine.png` |
| **Botones de cine, grillas pequeñas o claqueta pura** | `claqueta`, `estrenos breves`, `boton de cine`, `grilla cine`, `pelicula` | `cine_2.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/cine_2.png` |
| **Candy bar de cines y combos clásicos de pochoclos** | `pochoclos`, `popcorn`, `candy bar`, `snacks de cine`, `combo pochoclos`, `balde de pochoclos` | `pochoclos.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/pochoclos.png` |
| **Pochoclos recién hechos o promociones dinámicas** | `pochoclos recien hechos`, `combo gigante`, `popcorn al aire`, `candy bar estreno` | `pochoclos_2.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/pochoclos_2.png` |
| **Tickets y entradas generales (promociones 2x1)** | `entradas`, `tickets`, `2x1`, `boletos`, `pase doble`, `espectaculos generales` | `entradas.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/entradas.png` |
| **Preventas Exclusivas Galicia o recitales con sponsoreo** | `preventa galicia`, `allaccess`, `ticketek`, `movistar arena`, `recitales exclusivos`, `cruz de santiago` | `entradas_2.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/entradas_2.png` |
| **Teatro, musicales y cartelera de Calle Corrientes** | `teatro`, `calle corrientes`, `obras de teatro`, `musicales`, `gran rex`, `opera`, `mascaras` | `teatro.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/teatro.png` |
| **Recitales de música en vivo, bandas y conciertos** | `recitales`, `conciertos`, `musica en vivo`, `bandas`, `canto`, `festivales de musica`, `microfono de mano` | `microfono.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/microfono.png` |
| **Stand-up comedy, humor, podcasts y streaming** | `stand up`, `humor`, `comedia`, `podcast`, `streaming`, `twitch`, `entrevistas`, `unipersonal` | `microfono_2.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/microfono_2.png` |
| **Suscripciones de streaming de audio (Spotify, música)** | `auriculares`, `spotify`, `musica online`, `streaming audio`, `youtube music`, `podcasts`, `vincha` | `auriculares.png` | `https://mkt-visa.vercel.app/assets/galicia/icons/auriculares.png` |

---

## ⚠️ 4. REGLAS DE ORO DE DESAMBIGUACIÓN PARA LLMs

1. **`auriculares_2.png` NO ES MÚSICA**: Visualmente es un calendario de mesa con signo de exclamación `!` y pila de monedas. Usarlo únicamente para **fechas de vencimiento de facturas, recordatorios de cobro y mora**.
2. **`entradas_2.png` vs `entradas.png`**:
   - Si el beneficio es una **Preventa Oficial Banco Galicia** o sponsoreo oficial con Tarjetas Galicia → usar `entradas_2.png` (tiene la Cruz de Santiago grabada).
   - Si es un 2x1 genérico de salidas o cines sin sponsoreo del banco → usar `entradas.png`.
3. **`microfono.png` vs `microfono_2.png`**:
   - Recitales masivos, bandas de música, conciertos → `microfono.png` (micrófono vocal de mano).
   - Stand-up comedy, humor, streaming, podcasts → `microfono_2.png` (micrófono con soporte de pie).
4. **`cine.png` vs `cine_2.png`**:
   - Destacados principales de cartelera → `cine.png` (claqueta + carrete + cinta).
   - Botones CTA o grillas compactas de muchas ofertas → `cine_2.png` (claqueta frontal pura).
5. **Cero URLs Relativas**: Toda referencia debe iniciar con `https://mkt-visa.vercel.app/assets/galicia/...`.
