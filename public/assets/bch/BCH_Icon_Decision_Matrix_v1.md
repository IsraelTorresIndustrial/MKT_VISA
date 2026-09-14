# Banco de Chile · Icon Decision Matrix
## Sistema de decisión para selección de iconografía en campañas de medios de pago

**Versión:** 1.0  
**Ámbito:** Banco de Chile · Medios de Pago · Visa  
**Objetivo:** permitir que cualquier LLM, agente o sistema de diseño seleccione de forma consistente el icono más adecuado según el objetivo, mecánica, comportamiento, rubro o contexto de una campaña.

---

# 1. Principio general

La librería está compuesta por 30 iconos agrupados en tres familias:

1. **Medios de Pago & Ciclo de Uso**  
   Representan el medio de pago, el momento del journey o el comportamiento que se busca generar.

2. **Rubros de Consumo**  
   Representan el contexto de gasto o categoría comercial donde ocurre la compra.

3. **Mecánicas, Crossborder & Travel**  
   Representan una condición comercial, modalidad de uso o experiencia específica.

La selección del icono debe responder primero a la siguiente pregunta:

> **¿Qué concepto necesita entender el usuario en menos de 2 segundos?**

No seleccionar un icono porque “se ve bonito”.  
Seleccionarlo porque representa el significado principal del bloque o mensaje.

---

# 2. Regla de prioridad semántica

Cuando una comunicación contenga varios conceptos, elegir el icono según este orden:

1. **Acción principal del cliente**
2. **Mecánica o condición de la campaña**
3. **Rubro**
4. **Producto**
5. **Contexto o experiencia**

Ejemplo:

> “Obtén 30% de descuento en supermercados pagando con tu Tarjeta de Crédito.”

Si el bloque explica el beneficio → **24_descuento**  
Si el bloque explica dónde usarlo → **11_supermercado**  
Si el bloque explica el medio de pago → **01_tarjeta**

No intentar representar todo con un solo icono.

---

# 3. Regla de un concepto por icono

Cada icono debe representar una sola idea principal.

Correcto:

- Tarjeta → medio de pago
- Supermercado → rubro
- Cashback → recompensa
- Reactivación → comportamiento
- Ecommerce internacional → canal + contexto internacional

Incorrecto:

- Usar “cashback” para representar cualquier descuento
- Usar “ecommerce” para cualquier compra
- Usar “travel” para cualquier transacción internacional
- Usar “tarjeta” cuando existe un icono más específico para el comportamiento

---

# 4. Regla de especificidad

Siempre preferir el icono más específico disponible.

Ejemplos:

- Compra online internacional → **28_ecommerce_internacional**, no **03_ecommerce**
- Compra presencial internacional → **27_compra_internacional_crossborder**
- Pago periódico automático → **23_pago_recurrente**, no **01_tarjeta**
- Tarjeta guardada → **22_card_on_file_cof**, no **04_wallet_pago_movil**
- Uso de Lounge → **29_lounge_salon_vip**, no **19_viajes_turismo**

---

# 5. Árbol de decisión rápido

```text
¿El mensaje trata sobre un medio de pago?
│
├── Sí → ¿Qué modalidad?
│   ├── Tarjeta genérica → 01_tarjeta
│   ├── POS / compra física → 02_pago_presencial_pos
│   ├── Ecommerce nacional → 03_ecommerce
│   ├── Wallet / pago móvil → 04_wallet_pago_movil
│   ├── Contactless → 21_contactless
│   ├── Card on File → 22_card_on_file_cof
│   └── Pago recurrente → 23_pago_recurrente
│
¿El mensaje trata sobre etapa o comportamiento del cliente?
│
├── Activación → 05_activacion
├── Primera compra → 06_primera_compra
├── Reactivación → 07_reactivacion
├── Meta de transacciones → 08_meta_de_transacciones
└── Meta de facturación → 26_meta_de_facturacion
│
¿El mensaje trata sobre incentivo?
│
├── Cashback → 09_cashback
├── Dólares-Premio → 10_dolares_premio
├── Descuento → 24_descuento
└── Cuotas sin interés → 25_cuotas_sin_interes_csi
│
¿El mensaje trata sobre un rubro?
│
├── Supermercado → 11
├── Gastronomía → 12
├── Café → 13
├── Combustible → 14
├── Farmacia → 15
├── Retail → 16
├── Tecnología → 17
├── Delivery → 18
├── Viajes → 19
└── Entretenimiento → 20
│
¿El mensaje es internacional o Travel?
│
├── Compra internacional genérica/presencial → 27
├── Ecommerce internacional → 28
├── Lounge → 29
└── Traslado aeropuerto → 30
```

---

# 6. Matriz maestra de decisión

| ID | Nombre archivo | Concepto principal | Usar cuando | No usar cuando | Combinaciones frecuentes |
|---|---|---|---|---|---|
| 01 | `01_tarjeta.png` | Tarjeta como medio de pago | El mensaje habla genéricamente de Tarjeta de Crédito/Débito, producto, portafolio o “Tus Tarjetas del Chile” | Existe un comportamiento o modalidad más específica | 24 descuento, 09 cashback, 11–20 rubros |
| 02 | `02_pago_presencial_pos.png` | Compra presencial | Compra en comercio físico, caja, POS, presencial, punto de venta | Ecommerce, wallet o crossborder online | 11–20 rubros, 27 crossborder |
| 03 | `03_ecommerce.png` | Compra online nacional/genérica | Ecommerce, compra online, CNP, web/app de comercio | Compra internacional específica | 24 descuento, 17 tecnología, 18 delivery |
| 04 | `04_wallet_pago_movil.png` | Wallet / pago móvil | Apple Pay, Google Pay, billetera digital, enrolamiento en wallet, pago desde celular | Card on File, pago recurrente o POS tradicional | 05 activación, 21 contactless |
| 05 | `05_activacion.png` | Activación de tarjeta/producto | Activar, habilitar, completar onboarding, tarjeta activa | Primera compra o reactivación de inactivos | 04 wallet, 06 primera compra |
| 06 | `06_primera_compra.png` | Primer uso | Primera compra, primer uso, primera transacción, incentivo inicial | Cliente que ya venía usando y vuelve | 09 cashback, 11–20 rubros, 27/28 crossborder |
| 07 | `07_reactivacion.png` | Reactivación | Inactivos, “vuelve a usar”, recuperación de actividad, retomar uso | Activación de tarjeta nueva | 09 cashback, 24 descuento, rubros |
| 08 | `08_meta_de_transacciones.png` | Meta por cantidad de compras | 5 compras, 10 transacciones, 25 transacciones, frecuencia | Meta monetaria o facturación | 01 tarjeta, 05 activación |
| 09 | `09_cashback.png` | Devolución de dinero | Cashback, devolución, reintegro, abono, bonificación monetaria | Descuento inmediato en precio | 06 primera compra, 07 reactivación, rubros |
| 10 | `10_dolares_premio.png` | Dólares-Premio | Acumulación DP, canje DP, rewards BCH, Travel asociado a DP | Cashback genérico o descuento | 19 viajes, 29 lounge, 30 traslado |
| 11 | `11_supermercado.png` | Supermercado | Supermercados, alimentos, compras del hogar, consumo cotidiano | Gastronomía o delivery | 24 descuento, 09 cashback |
| 12 | `12_gastronomia_restaurantes.png` | Restaurantes | Restaurantes, cenas, comidas fuera del hogar, gastronomía | Café específico o delivery | 24 descuento, 01 tarjeta |
| 13 | `13_cafe_cafeterias.png` | Café / cafeterías | Cafeterías, Starbucks-like, Dunkin-like, consumo frecuente de café | Restaurantes generales | 24 descuento, 07 reactivación |
| 14 | `14_combustible.png` | Combustible | Estaciones de servicio, gasolina, bencina, ahorro por litro | Movilidad general sin combustible | 24 descuento, 09 cashback |
| 15 | `15_farmacia_salud.png` | Farmacia / salud | Farmacias, productos de salud, bienestar cotidiano | Seguros o asistencia médica de viaje | 24 descuento |
| 16 | `16_retail_shopping.png` | Retail / shopping | Vestuario, tiendas, malls, compras generales, moda | Ecommerce si el canal online es lo central | 24 descuento, 25 CSI |
| 17 | `17_tecnologia.png` | Tecnología | Electrónica, notebooks, celulares, gadgets, tiendas tech | Ecommerce genérico sin foco en tecnología | 25 CSI, 03 ecommerce |
| 18 | `18_delivery.png` | Delivery | Pedidos por app, comida a domicilio, despacho | Gastronomía presencial | 03 ecommerce, 24 descuento |
| 19 | `19_viajes_turismo.png` | Viajes / turismo | Viajes, vuelos, turismo, vacaciones, Travel genérico | Lounge o traslado aeropuerto específicos | 10 DP, 27 crossborder |
| 20 | `20_entretenimiento_musica.png` | Entretenimiento | Conciertos, música, cine, eventos, panoramas | Travel o gastronomía | 24 descuento |
| 21 | `21_contactless.png` | Pago contactless | Tap to pay, NFC, “acerca tu tarjeta”, pago sin contacto | Wallet si el foco está en el celular | 02 POS, 04 wallet |
| 22 | `22_card_on_file_cof.png` | Tarjeta guardada | Card on File, enrolar tarjeta en comercio/app, credencial almacenada | Suscripción recurrente o wallet | 03 ecommerce, 05 activación |
| 23 | `23_pago_recurrente.png` | Pago recurrente | Suscripciones, pagos automáticos, cargos periódicos | Tarjeta simplemente guardada sin periodicidad | 22 COF, 03 ecommerce |
| 24 | `24_descuento.png` | Descuento | % descuento, precio rebajado, “hasta 40%”, promoción directa | Cashback o bonificación posterior | 11–20 rubros |
| 25 | `25_cuotas_sin_interes_csi.png` | Cuotas sin interés | 3/6/12 CSI, compra en cuotas, financiamiento sin interés | Descuento o cashback | 16 retail, 17 tecnología, 01 tarjeta |
| 26 | `26_meta_de_facturacion.png` | Meta monetaria | Factura $X, alcanza monto mínimo, spend target, gasto acumulado | Meta por número de transacciones | 01 tarjeta, 09 cashback |
| 27 | `27_compra_internacional_crossborder.png` | Compra internacional | Crossborder genérico, compra fuera de Chile, presencial internacional, gasto extranjero | Ecommerce internacional específicamente | 02 POS, 19 viajes |
| 28 | `28_ecommerce_internacional.png` | Ecommerce internacional | Compra online en comercio extranjero, CNP internacional | Compra física internacional | 03 ecommerce, 24 descuento |
| 29 | `29_lounge_salon_vip.png` | Lounge / salón VIP | Acceso a salón VIP, Visa Airport Companion, beneficios de aeropuerto premium | Travel genérico | 19 viajes, 10 DP |
| 30 | `30_traslado_aeropuerto.png` | Traslado aeropuerto | Transvip-like, transporte hacia/desde aeropuerto, traslado incluido | Movilidad urbana general | 19 viajes, 10 DP |

---

# 7. Reglas por familia

## 7.1 Medios de Pago & Ciclo de Uso

Usar esta familia cuando el foco del mensaje sea:

- cómo paga el cliente;
- qué producto usa;
- qué etapa del journey se busca mover;
- qué comportamiento debe completar.

Prioridad típica:

```text
Producto genérico → Tarjeta
Canal físico → POS
Canal digital → Ecommerce / Wallet
Momento inicial → Activación / Primera compra
Cliente inactivo → Reactivación
Meta → Transacciones o Facturación
Recompensa → Cashback o Dólares-Premio
```

---

## 7.2 Rubros de Consumo

Usar esta familia cuando la pregunta principal sea:

> “¿Dónde puede usar la tarjeta o dónde aplica el beneficio?”

No usar rubros para explicar una mecánica.

Ejemplo:

> “30% de descuento en restaurantes”

Bloque “30%” → `24_descuento`  
Bloque “restaurantes” → `12_gastronomia_restaurantes`

---

## 7.3 Mecánicas, Crossborder & Travel

Usar esta familia cuando exista una condición o experiencia específica:

- contactless;
- COF;
- recurrencia;
- descuento;
- CSI;
- meta monetaria;
- internacional;
- lounge;
- traslado.

Esta familia tiene prioridad sobre rubros cuando la condición es el mensaje principal.

---

# 8. Criterios de desempate

## Cashback vs Descuento

**Cashback**
- devolución posterior;
- abono;
- reintegro;
- “recibe $X”;
- “te devolvemos”.

→ `09_cashback`

**Descuento**
- reducción inmediata;
- “30% dto.”;
- precio rebajado.

→ `24_descuento`

---

## Activación vs Primera Compra

**Activación**
- tarjeta habilitada;
- completar proceso;
- producto listo para usar.

→ `05_activacion`

**Primera compra**
- primer uso real de la tarjeta;
- primera transacción.

→ `06_primera_compra`

---

## Activación vs Reactivación

**Activación**
- producto nuevo.

**Reactivación**
- producto existente que dejó de utilizarse.

---

## Ecommerce vs Ecommerce Internacional

**Ecommerce**
- online, sin dimensión internacional explícita.

→ `03_ecommerce`

**Ecommerce internacional**
- sitio extranjero;
- compra fuera de Chile;
- moneda extranjera;
- crossborder online.

→ `28_ecommerce_internacional`

---

## Compra internacional vs Viaje

**Compra internacional**
- foco en la transacción.

→ `27_compra_internacional_crossborder`

**Viaje**
- foco en experiencia/destino.

→ `19_viajes_turismo`

---

## COF vs Pago recurrente

**COF**
- tarjeta almacenada;
- credencial guardada.

→ `22_card_on_file_cof`

**Pago recurrente**
- cobro automático periódico.

→ `23_pago_recurrente`

---

## Meta de transacciones vs Meta de facturación

**Meta de transacciones**
- cantidad.

Ejemplo: “Realiza 5 compras”.

→ `08_meta_de_transacciones`

**Meta de facturación**
- monto.

Ejemplo: “Acumula $300.000 en compras”.

→ `26_meta_de_facturacion`

---

# 9. Combinaciones recomendadas

Cuando una maqueta permita múltiples iconos, usar máximo 2–3 por módulo.

## Activación temprana

```text
M0 Bienvenida / Activación
05_activacion

M1 Wallet
04_wallet_pago_movil

M1 Card on File
22_card_on_file_cof

M2 Meta de compras
08_meta_de_transacciones

M3 Habitualidad
23_pago_recurrente o 08_meta_de_transacciones
según la mecánica real
```

---

## Inactivos

```text
Concepto principal:
07_reactivacion

Si existe incentivo:
+ 09_cashback
o
+ 24_descuento

Si existe rubro:
+ 11–20 según corresponda
```

---

## Mantención de actividad

```text
Meta por monto:
26_meta_de_facturacion

Meta por frecuencia:
08_meta_de_transacciones
```

---

## Crossborder Ecommerce

```text
28_ecommerce_internacional
```

Opcional:

```text
+ 24_descuento
+ 06_primera_compra
```

---

## Crossborder Presencial

```text
27_compra_internacional_crossborder
```

Opcional:

```text
+ 02_pago_presencial_pos
+ 06_primera_compra
```

---

## Travel

```text
19_viajes_turismo
10_dolares_premio
29_lounge_salon_vip
30_traslado_aeropuerto
```

Seleccionar solo los beneficios efectivamente incluidos.

---

## Cuotas sin interés

```text
25_cuotas_sin_interes_csi
```

Opcional por rubro:

```text
+ 16_retail_shopping
+ 17_tecnologia
+ 11_supermercado
```

---

# 10. Reglas visuales para un LLM

El LLM no debe modificar el significado base del icono.

Puede:

- cambiar tamaño;
- ubicarlo en cards;
- usarlo junto a texto;
- combinarlo con otro icono complementario;
- usar fondo claro u oscuro compatible;
- agregar labels externos.

No debe:

- recolorear arbitrariamente;
- agregar logos dentro del icono;
- cambiar símbolos internos;
- convertir cashback en descuento;
- alterar un rubro para representar otro;
- usar más de 3 iconos en un mismo bloque salvo una matriz/catálogo;
- usar un icono meramente decorativo si existe otro semánticamente correcto.

---

# 11. Selección por palabras clave

## Tarjeta
`tarjeta`, `TC`, `TD`, `medio de pago`, `card`

→ `01_tarjeta`

## Pago presencial
`presencial`, `POS`, `tienda física`, `caja`

→ `02_pago_presencial_pos`

## Ecommerce
`ecommerce`, `online`, `internet`, `CNP`

→ `03_ecommerce`

## Wallet
`wallet`, `billetera`, `Apple Pay`, `Google Pay`, `pago móvil`

→ `04_wallet_pago_movil`

## Activación
`activar`, `habilitar`, `onboarding`, `tarjeta activa`

→ `05_activacion`

## Primera compra
`primera compra`, `primer uso`, `primera transacción`

→ `06_primera_compra`

## Reactivación
`inactivo`, `reactivar`, `volver a usar`, `retoma`

→ `07_reactivacion`

## Meta transacciones
`5 compras`, `25 transacciones`, `frecuencia`, `cantidad de compras`

→ `08_meta_de_transacciones`

## Cashback
`cashback`, `devolución`, `reintegro`, `abono`

→ `09_cashback`

## Dólares-Premio
`DP`, `Dólares-Premio`, `acumula DP`, `canje`

→ `10_dolares_premio`

## Supermercado
`supermercado`, `alimentos`, `groceries`

→ `11_supermercado`

## Gastronomía
`restaurante`, `gastronomía`, `cena`

→ `12_gastronomia_restaurantes`

## Café
`café`, `cafetería`, `Starbucks`, `Dunkin`

→ `13_cafe_cafeterias`

## Combustible
`combustible`, `bencina`, `gasolina`, `estación de servicio`

→ `14_combustible`

## Farmacia
`farmacia`, `salud`, `medicamentos`

→ `15_farmacia_salud`

## Retail
`retail`, `shopping`, `vestuario`, `mall`

→ `16_retail_shopping`

## Tecnología
`tecnología`, `electrónica`, `notebook`, `celular`

→ `17_tecnologia`

## Delivery
`delivery`, `despacho`, `pedido a domicilio`

→ `18_delivery`

## Viajes
`viaje`, `turismo`, `vacaciones`, `Travel`

→ `19_viajes_turismo`

## Entretenimiento
`concierto`, `música`, `cine`, `evento`, `panorama`

→ `20_entretenimiento_musica`

## Contactless
`contactless`, `NFC`, `tap`, `sin contacto`

→ `21_contactless`

## COF
`COF`, `Card on File`, `tarjeta guardada`, `credencial almacenada`

→ `22_card_on_file_cof`

## Recurrente
`suscripción`, `pago automático`, `recurrente`, `cargo mensual`

→ `23_pago_recurrente`

## Descuento
`descuento`, `% dto`, `rebaja`

→ `24_descuento`

## CSI
`cuotas sin interés`, `CSI`, `3 cuotas`, `6 cuotas`, `12 cuotas`

→ `25_cuotas_sin_interes_csi`

## Meta facturación
`meta facturación`, `gasta $`, `acumula $`, `spend target`

→ `26_meta_de_facturacion`

## Crossborder
`internacional`, `crossborder`, `extranjero`, `fuera de Chile`

→ `27_compra_internacional_crossborder`

## Ecommerce internacional
`ecommerce internacional`, `web extranjera`, `compra online internacional`

→ `28_ecommerce_internacional`

## Lounge
`lounge`, `salón VIP`, `Visa Airport Companion`

→ `29_lounge_salon_vip`

## Traslado aeropuerto
`Transvip`, `traslado aeropuerto`, `transfer aeropuerto`

→ `30_traslado_aeropuerto`

---

# 12. Prompt de sistema recomendado para agentes

```text
Eres un selector de iconografía para campañas de medios de pago Banco de Chile.

Tu tarea es identificar el concepto principal de cada bloque y asignar el icono más específico disponible de la librería BCH de 30 iconos.

Reglas:
1. Prioriza significado sobre estética.
2. Usa un solo icono principal por concepto.
3. Prefiere siempre el icono más específico.
4. Diferencia correctamente cashback vs descuento.
5. Diferencia activación vs primera compra vs reactivación.
6. Diferencia meta de transacciones vs meta de facturación.
7. Diferencia ecommerce nacional vs ecommerce internacional.
8. Diferencia COF vs pago recurrente.
9. Usa rubros solo cuando el contexto de consumo sea relevante.
10. No inventes nuevos iconos si existe uno adecuado en la librería.

Al responder entrega:
- icon_id
- icon_name
- filename
- reason
- secondary_icon opcional
- confidence entre 0 y 1
```

---

# 13. Formato de salida recomendado

```json
{
  "icon_id": 28,
  "icon_name": "Ecommerce internacional",
  "filename": "28_ecommerce_internacional.png",
  "reason": "La campaña incentiva una compra online en comercios extranjeros.",
  "secondary_icon": "24_descuento.png",
  "confidence": 0.98
}
```

---

# 14. Ejemplos de decisión

### Caso 1

**Input**

> “Obtén 30% de descuento en tu primera compra internacional online.”

**Salida**

```json
{
  "icon_id": 28,
  "icon_name": "Ecommerce internacional",
  "filename": "28_ecommerce_internacional.png",
  "reason": "El contexto principal es una compra online internacional.",
  "secondary_icons": [
    "06_primera_compra.png",
    "24_descuento.png"
  ],
  "confidence": 0.99
}
```

---

### Caso 2

**Input**

> “Haz 5 compras durante el mes y recibe cashback.”

**Salida**

```json
{
  "icon_id": 8,
  "icon_name": "Meta de transacciones",
  "filename": "08_meta_de_transacciones.png",
  "reason": "La condición principal es alcanzar una cantidad específica de compras.",
  "secondary_icons": [
    "09_cashback.png"
  ],
  "confidence": 0.99
}
```

---

### Caso 3

**Input**

> “Vuelve a usar tu Tarjeta de Crédito y recibe un beneficio.”

**Salida**

```json
{
  "icon_id": 7,
  "icon_name": "Reactivación",
  "filename": "07_reactivacion.png",
  "reason": "La campaña busca recuperar el uso de una tarjeta previamente inactiva.",
  "confidence": 0.98
}
```

---

### Caso 4

**Input**

> “Paga en 6 cuotas sin interés en tecnología.”

**Salida**

```json
{
  "icon_id": 25,
  "icon_name": "Cuotas sin interés",
  "filename": "25_cuotas_sin_interes_csi.png",
  "reason": "La mecánica comercial principal son las cuotas sin interés.",
  "secondary_icons": [
    "17_tecnologia.png"
  ],
  "confidence": 0.99
}
```

---

### Caso 5

**Input**

> “Accede a salones VIP en tus próximos viajes.”

**Salida**

```json
{
  "icon_id": 29,
  "icon_name": "Lounge / Salón VIP",
  "filename": "29_lounge_salon_vip.png",
  "reason": "El beneficio específico comunicado es el acceso a lounge.",
  "secondary_icons": [
    "19_viajes_turismo.png"
  ],
  "confidence": 0.99
}
```

---

# 15. Principio final

> **El icono debe ayudar a entender el mensaje antes de leer el copy.**

Si un LLM tiene dudas entre dos iconos, debe elegir el que represente de forma más específica:

1. la acción requerida;
2. la condición de la campaña;
3. el contexto real de uso.

La librería no busca decorar.  
Busca construir un lenguaje visual consistente para campañas, PPT, landings, emails, dashboards y prototipos de medios de pago Banco de Chile.
