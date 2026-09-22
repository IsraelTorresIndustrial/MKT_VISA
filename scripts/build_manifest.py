#!/usr/bin/env python3
"""
build_manifest.py — Generador Maestro del Manifiesto de Activos
================================================================
ÚNICA FUENTE DE VERDAD para src/data/assets_data.js

Cómo agregar un nuevo set de íconos
------------------------------------
Opción A — Solo carpeta (auto-derivado):
  1. Crea la carpeta dentro del banco correcto
  2. Agrega entrada en BANK_CONFIG con carpeta, category, family
  3. python3 scripts/build_manifest.py

Opción B — Con metadata rica (recomendado para BCH):
  1. Crea carpeta y sube los íconos
  2. Agrega entradas en METADATA_TABLE por filename
  3. python3 scripts/build_manifest.py

Convención de nombres
---------------------
  NN_concepto_resumido.png   (íconos BCH numerados)
  nombre-icono-high.svg      (íconos Visa SVG)
"""

import os, json, struct, pathlib, re
from collections import Counter

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_FILE  = REPO_ROOT / "src" / "data" / "assets_data.js"
CDN_BASE   = "https://mkt-visa.vercel.app"

# ═══════════════════════════════════════════════════════════════════════════
# CDN_REWRITES: mapea prefijo ruta relativa → prefijo CDN
# ═══════════════════════════════════════════════════════════════════════════
CDN_REWRITES = [
    ("assets/banco_de_chile/",  f"{CDN_BASE}/assets/bch/"),
    ("assets/galicia/",         f"{CDN_BASE}/assets/galicia/"),
    ("assets/visa/",            f"{CDN_BASE}/assets/visa/"),
]

def make_cdn_url(rel_path: str) -> str:
    for prefix, cdn_prefix in CDN_REWRITES:
        if rel_path.startswith(prefix):
            return cdn_prefix + rel_path[len(prefix):]
    return f"{CDN_BASE}/{rel_path}"

# ═══════════════════════════════════════════════════════════════════════════
# BANK_CONFIG: qué carpetas escanear por banco
# Tupla: (rel_folder, category, family, featured, only_svg_high)
# ═══════════════════════════════════════════════════════════════════════════
BANK_CONFIG = {
    # Tupla: (rel_folder, category, family, featured, only_svg_high, recursive)
    "Banco de Chile": [
        ("banco_de_chile/icons",            "Íconos 3D",       "Medios de Pago & Ciclo de Uso",   True,  False, False),
        ("banco_de_chile/iconos_bch_2d_30", "Íconos 2D",       "Iconografía 2D Banco de Chile",    False, False, True),
        ("banco_de_chile/travel",           "Travel & Turismo", "Mecánicas, Crossborder & Travel", False, False, False),
        ("banco_de_chile/logos",            "Logotipos",        "Identidad Corporativa",            True,  False, False),
    ],
    "Galicia": [
        ("galicia/icons",     "Íconos 3D",    "Iconografía Galicia",       True,  False, False),
        ("galicia/headers",   "Banners Hero", "Headers sin Texto Galicia", True,  False, False),
        ("galicia/logos",     "Logotipos",    "Identidad Galicia",        True,  False, False),
        ("galicia/creatives", "Banners Hero", "Creatividades Galicia",     False, False, False),
    ],
    "Visa": [
        ("visa/icons/assets/visa-icons/svg/visa", "SVG", "Visa Icons Official SVG", False, True, False),
        ("visa/logos",     "Logotipos",    "Visa Brand Standards", False, False, False),
        ("visa/creatives", "Banners Hero", "Visa Creatives",       False, False, False),
    ],
}

# ═══════════════════════════════════════════════════════════════════════════
# VISA SVG CATEGORIES: clasifica por prefijo del nombre
# ═══════════════════════════════════════════════════════════════════════════
VISA_SVG_CATEGORIES = {
    ("account-add","card-corporate","card-debit","card-generic","card-manage",
     "card-manage-alt","card-number","card-off","card-prepaid","card-suspend",
     "card-verify","pos","pos-alt","qr","scan-card","tap"): "Pagos",
    ("balance","bill","bill-alt","fast","mobile-transfer","money-add",
     "money-request","money-send","money-withdrawn","on-hold","receipt",
     "return","split","transactions","transactions-new"): "Transacciones",
    ("account-favorite","account","account-lock","account-remove","atm",
     "savings-account","wallet-default","wallet"): "Cuenta y Wallet",
    ("currency-convert-alt","currency-convert","currency-euro","currency",
     "currency-pound","currency-usd","currency-yen"): "Divisas",
    ("auth-code","auth-face","auth-reauthorize","auth-voice","device-secure",
     "fingerprint","fraud","id-number","key-change","key","password-hide",
     "password-show","security-firewall","security","security-lock",
     "security-protection","security-unlock","sign-in","sign-out",
     "signature","token"): "Seguridad",
    ("check-international","global","map-directions","map","map-location-current",
     "map-location","roadsign","transit-airplane","transit-car","transit-train",
     "travel-notifications"): "Viajes",
    ("acquirer","bonus-points","cart","gift","issuer","marketplace","merchant",
     "offers-deal","offers","reward","shipping","store-closed","store-open"): "Comercio",
    ("analytics","dashboard","data","report","statistics","trending"): "Analítica",
    ("chat","customer-support","email","error","help","information","message",
     "mobile-success","notifications","phone","question","success",
     "support-ticket","warning"): "Comunicación",
    ("company","contact","government","handshake"): "Identidad",
    ("device-laptop","device-mobile","device-wearable"): "Dispositivos",
}

def get_visa_svg_category(stem: str) -> str:
    base = stem.replace("-high","").replace("-low","").replace("-tiny","")
    for keys, cat in VISA_SVG_CATEGORIES.items():
        for k in keys:
            if base == k or base.startswith(k + "-"):
                return cat
    return "UI"

# ═══════════════════════════════════════════════════════════════════════════
# METADATA_TABLE: metadata rica por filename
# Si un filename NO está aquí, se auto-genera desde el nombre
# ═══════════════════════════════════════════════════════════════════════════
METADATA_TABLE = {
    # ── BCH 3D ──────────────────────────────────────────────────────────────
    "01_tarjeta.png": {"title":"Tarjeta de Crédito Genérica","category":"Íconos 3D","family":"Medios de Pago & Ciclo de Uso","concept":"Medio de pago principal / Portafolio de Tarjetas","rubro":"General","rule":"Usar cuando el mensaje explica el medio de pago o portafolio sin especificar canal ni condición técnica.","tags":["tarjeta","credito","medio de pago","plastico","bch","visa","chile"],"is_featured":True},
    "02_pago_presencial_pos.png": {"title":"Pago Presencial POS","category":"Íconos 3D","family":"Medios de Pago & Ciclo de Uso","concept":"Compra en terminal POS físico","rubro":"Tiendas Físicas","rule":"Usar para compras en comercio físico con terminal POS.","tags":["pos","presencial","terminal","tienda fisica","compra"],"is_featured":True},
    "03_ecommerce.png": {"title":"Ecommerce Nacional","category":"Íconos 3D","family":"Medios de Pago & Ciclo de Uso","concept":"Compra online en comercios nacionales","rubro":"Online","rule":"Usar para compras online locales y comercio electrónico nacional.","tags":["ecommerce","online","carrito","web","tienda digital"],"is_featured":True},
    "04_wallet_pago_movil.png": {"title":"Wallet & Pago Móvil","category":"Íconos 3D","family":"Medios de Pago & Ciclo de Uso","concept":"Billetera digital / Smartphone / Smartwatch","rubro":"Digital / Móvil","rule":"Usar para Apple Pay, Google Wallet, pago con celular. Si el foco es la app del banco, usar 40.","tags":["wallet","apple pay","google pay","celular","pago movil","contactless"],"is_featured":True},
    "05_activacion.png": {"title":"Activación de Tarjeta","category":"Íconos 3D","family":"Medios de Pago & Ciclo de Uso","concept":"Encendido / Primera habilitación de la tarjeta","rubro":"Onboarding","rule":"Usar para etapas iniciales de activación, bienvenida y primer encendido.","tags":["activacion","onboarding","bienvenida","primer uso","desbloqueo"],"is_featured":True},
    "06_primera_compra.png": {"title":"Primera Compra","category":"Íconos 3D","family":"Medios de Pago & Ciclo de Uso","concept":"Incentivo a la transacción debut","rubro":"Onboarding","rule":"Usar cuando la campaña premia o estimula realizar la primera compra del cliente.","tags":["primera compra","debut","incentivo","inicio","transaccion"],"is_featured":True},
    "07_reactivacion.png": {"title":"Reactivación de Clientes","category":"Íconos 3D","family":"Medios de Pago & Ciclo de Uso","concept":"Recuperación de clientes inactivos","rubro":"Retención / Winback","rule":"Usar en comunicaciones M1-M3 dirigidas a clientes inactivos.","tags":["reactivacion","inactivo","retencion","winback"],"is_featured":True},
    "08_meta_de_transacciones.png": {"title":"Meta de Transacciones","category":"Íconos 3D","family":"Medios de Pago & Ciclo de Uso","concept":"Desafío por número de compras","rubro":"Frecuencia","rule":"Usar cuando la condición es alcanzar un conteo mínimo de transacciones.","tags":["meta","transacciones","frecuencia","desafio","compras"],"is_featured":True},
    "09_cashback.png": {"title":"Cashback / Devolución","category":"Íconos 3D","family":"Medios de Pago & Ciclo de Uso","concept":"Abono en dinero / Reembolso","rubro":"Recompensa","rule":"Usar cuando el beneficio es dinero devuelto directo a la cuenta o tarjeta.","tags":["cashback","devolucion","dinero","reembolso","abono","beneficio"],"is_featured":True},
    "10_dolares_premio.png": {"title":"Dólares-Premio (DP)","category":"Íconos 3D","family":"Medios de Pago & Ciclo de Uso","concept":"Programa de lealtad Travel Club","rubro":"Lealtad","rule":"Usar para acumulación o canje de Dólares-Premio.","tags":["dolares premio","dp","travel","travel club","lealtad","canje"],"is_featured":True},
    "11_supermercado.png": {"title":"Supermercados","category":"Íconos 3D","family":"Rubros de Consumo","concept":"Compras de alimentación","rubro":"Supermercados","rule":"Usar en promociones de supermercados (Jumbo, Lider, Santa Isabel).","tags":["supermercado","comida","despensa","jumbo","lider"],"is_featured":True},
    "12_gastronomia_restaurantes.png": {"title":"Gastronomía & Restaurantes","category":"Íconos 3D","family":"Rubros de Consumo","concept":"Restaurantes, bares y salidas a comer","rubro":"Gastronomía","rule":"Usar en beneficios culinarios y descuentos en restaurantes.","tags":["restaurante","gastronomia","comida","cena","almuerzo"],"is_featured":True},
    "13_cafe_cafeterias.png": {"title":"Cafeterías & Coffee","category":"Íconos 3D","family":"Rubros de Consumo","concept":"Cafés, pastelerías y pausas diarias","rubro":"Cafeterías","rule":"Usar para alianzas con Starbucks, Dunkin', Juan Valdez.","tags":["cafe","starbucks","dunkin","cafeteria","desayuno"],"is_featured":True},
    "14_combustible.png": {"title":"Combustible & Bencina","category":"Íconos 3D","family":"Rubros de Consumo","concept":"Carga de combustible y estaciones de servicio","rubro":"Combustible","rule":"Usar para descuentos en Shell, Copec, Petrobras.","tags":["combustible","bencina","estacion","shell","copec","auto"],"is_featured":True},
    "15_farmacia_salud.png": {"title":"Farmacias & Salud","category":"Íconos 3D","family":"Rubros de Consumo","concept":"Medicamentos, bienestar y cuidado personal","rubro":"Salud","rule":"Usar en alianzas con Cruz Verde, Salcobrand, Ahumada. Para salud clínica usar 38.","tags":["farmacia","salud","cruz verde","medicamentos","bienestar"],"is_featured":True},
    "16_retail_shopping.png": {"title":"Retail & Shopping","category":"Íconos 3D","family":"Rubros de Consumo","concept":"Tiendas, moda y vestuario general","rubro":"Retail","rule":"Usar para retail general. Para moda específica usar 35, para hogar usar 36.","tags":["retail","shopping","moda","ropa","mall","tienda"],"is_featured":True},
    "17_tecnologia.png": {"title":"Tecnología & Electro","category":"Íconos 3D","family":"Rubros de Consumo","concept":"Dispositivos, computación y electrónica","rubro":"Tecnología","rule":"Usar para smartphones, computadores, gadgets. Para IA usar 31.","tags":["tecnologia","gadgets","celulares","computacion","electronica"],"is_featured":True},
    "18_delivery.png": {"title":"Delivery & Apps de Envíos","category":"Íconos 3D","family":"Rubros de Consumo","concept":"PedidosYa, Rappi, Uber Eats","rubro":"Delivery","rule":"Usar para descuentos en apps de entrega a domicilio.","tags":["delivery","pedidosya","rappi","uber eats","envios"],"is_featured":True},
    "19_viajes_turismo.png": {"title":"Viajes & Turismo","category":"Íconos 3D","family":"Mecánicas, Crossborder & Travel","concept":"Vuelos, paquetes turísticos y escapadas","rubro":"Travel","rule":"Usar para agencias de viaje, pasajes aéreos y turismo.","tags":["viajes","turismo","vuelos","aerolineas","vacaciones"],"is_featured":True},
    "20_entretenimiento_musica.png": {"title":"Entretenimiento Genérico","category":"Íconos 3D","family":"Rubros de Consumo","concept":"Entretenimiento general","rubro":"Entretenimiento","rule":"Usar solo si el mensaje es entretenimiento amplio. Para cine usar 33, conciertos usar 34.","tags":["entretenimiento","conciertos","musica","cine","entradas"],"is_featured":True},
    "21_contactless.png": {"title":"Pago Sin Contacto (Contactless)","category":"Íconos 3D","family":"Mecánicas, Crossborder & Travel","concept":"NFC / Acercar y pagar","rubro":"Tecnología de Pago","rule":"Usar cuando el foco es rapidez y seguridad de pago NFC.","tags":["contactless","nfc","sin contacto","rapido","seguridad"],"is_featured":True},
    "22_card_on_file_cof.png": {"title":"Card on File (COF)","category":"Íconos 3D","family":"Mecánicas, Crossborder & Travel","concept":"Tarjeta inscrita en apps favoritas","rubro":"Inscripción","rule":"Usar para campañas que piden inscribir la tarjeta en Uber, Spotify, Netflix, etc.","tags":["card on file","cof","inscribir","guardar tarjeta","apps favoritas"],"is_featured":True},
    "23_pago_recurrente.png": {"title":"Pago Recurrente / PAT","category":"Íconos 3D","family":"Mecánicas, Crossborder & Travel","concept":"Pago automático de cuentas","rubro":"PAT / Servicios","rule":"Usar para PAT de servicios básicos. Para streaming usar 32.","tags":["pago recurrente","pat","cuentas","suscripciones","servicios"],"is_featured":True},
    "24_descuento.png": {"title":"Descuento / % OFF","category":"Íconos 3D","family":"Mecánicas, Crossborder & Travel","concept":"Porcentaje de rebaja directa","rubro":"Promoción","rule":"Usar cuando el beneficio principal es un % de rebaja directa.","tags":["descuento","porcentaje","off","ahorro","promocion"],"is_featured":True},
    "25_cuotas_sin_interes_csi.png": {"title":"Cuotas Sin Interés (CSI)","category":"Íconos 3D","family":"Mecánicas, Crossborder & Travel","concept":"Financiamiento en cuotas a tasa cero","rubro":"Financiamiento","rule":"Usar para destacar pagar en cuotas sin recargo de interés.","tags":["cuotas","sin interes","csi","financiamiento","meses"],"is_featured":True},
    "26_meta_de_facturacion.png": {"title":"Meta de Facturación","category":"Íconos 3D","family":"Mecánicas, Crossborder & Travel","concept":"Desafío por monto acumulado","rubro":"Gasto","rule":"Usar cuando la recompensa se activa al alcanzar un monto acumulado.","tags":["meta facturacion","monto","gasto","desafio","acumula"],"is_featured":True},
    "27_compra_internacional_crossborder.png": {"title":"Compra Internacional Presencial","category":"Íconos 3D","family":"Mecánicas, Crossborder & Travel","concept":"Tarjeta en comercios físicos en el extranjero","rubro":"Crossborder","rule":"Usar para compras presenciales durante viajes al extranjero.","tags":["crossborder","internacional","viaje","extranjero","compras fuera"],"is_featured":True},
    "28_ecommerce_internacional.png": {"title":"Ecommerce Internacional","category":"Íconos 3D","family":"Mecánicas, Crossborder & Travel","concept":"Compras online en moneda extranjera","rubro":"Crossborder Online","rule":"Usar para Amazon, AliExpress, Shein, eBay o servicios en el exterior.","tags":["ecommerce internacional","amazon","aliexpress","dolares","online exterior"],"is_featured":True},
    "29_lounge_salon_vip.png": {"title":"Salones VIP & Travel Lounge","category":"Íconos 3D","family":"Mecánicas, Crossborder & Travel","concept":"Acceso a salones VIP en aeropuertos","rubro":"Aeropuerto","rule":"Usar para Salones Pacific Club, VIP Lounge y salas de espera premium.","tags":["lounge","salon vip","pacific club","aeropuerto","travel lounge"],"is_featured":True},
    "30_traslado_aeropuerto.png": {"title":"Traslado al Aeropuerto","category":"Íconos 3D","family":"Mecánicas, Crossborder & Travel","concept":"Van o conductor privado al aeropuerto","rubro":"Aeropuerto","rule":"Usar para beneficio de transporte y transfer al aeropuerto en planes Travel.","tags":["traslado","aeropuerto","transfer","van","viaje"],"is_featured":True},

    # ── BCH 2D base (01-30): mismos conceptos pero categoría 2D ─────────
    "01_tarjeta_visa.png": {"title":"Tarjeta de Crédito (2D)","category":"Íconos 2D","family":"Medios de Pago & Ciclo de Uso","concept":"Tarjeta Visa plana 2D","rubro":"General","rule":"Versión 2D. Piezas planas o infografías. Para 3D usar 01_tarjeta.","tags":["tarjeta","credito","visa","2d","bch"],"is_featured":False},
    "02_pago_presencial_pos.png": {"title":"POS Presencial (2D)","category":"Íconos 2D","family":"Medios de Pago & Ciclo de Uso","concept":"POS físico 2D","rubro":"Tiendas Físicas","rule":"Versión 2D POS presencial.","tags":["pos","presencial","2d","bch"],"is_featured":False},
    "03_ecommerce.png": {"title":"Ecommerce Nacional (2D)","category":"Íconos 2D","family":"Medios de Pago & Ciclo de Uso","concept":"Compra online 2D","rubro":"Online","rule":"Versión 2D ecommerce.","tags":["ecommerce","online","2d","bch"],"is_featured":False},
    "04_wallet_pago_movil.png": {"title":"Wallet & Pago Móvil (2D)","category":"Íconos 2D","family":"Medios de Pago & Ciclo de Uso","concept":"Billetera digital 2D","rubro":"Digital / Móvil","rule":"Versión 2D wallet. Si el foco es la app del banco usar 40.","tags":["wallet","pago movil","2d","bch"],"is_featured":False},
    "05_activacion.png": {"title":"Activación (2D)","category":"Íconos 2D","family":"Medios de Pago & Ciclo de Uso","concept":"Activación tarjeta 2D","rubro":"Onboarding","rule":"Versión 2D activación.","tags":["activacion","2d","bch"],"is_featured":False},
    "06_primera_compra.png": {"title":"Primera Compra (2D)","category":"Íconos 2D","family":"Medios de Pago & Ciclo de Uso","concept":"Primera compra 2D","rubro":"Onboarding","rule":"Versión 2D primera compra.","tags":["primera compra","2d","bch"],"is_featured":False},
    "07_reactivacion.png": {"title":"Reactivación (2D)","category":"Íconos 2D","family":"Medios de Pago & Ciclo de Uso","concept":"Reactivación 2D","rubro":"Retención","rule":"Versión 2D reactivación.","tags":["reactivacion","inactivo","2d","bch"],"is_featured":False},
    "08_meta_de_transacciones.png": {"title":"Meta de Transacciones (2D)","category":"Íconos 2D","family":"Medios de Pago & Ciclo de Uso","concept":"Meta transacciones 2D","rubro":"Frecuencia","rule":"Versión 2D meta transacciones.","tags":["meta","transacciones","2d","bch"],"is_featured":False},
    "09_cashback.png": {"title":"Cashback (2D)","category":"Íconos 2D","family":"Medios de Pago & Ciclo de Uso","concept":"Cashback 2D","rubro":"Recompensa","rule":"Versión 2D cashback.","tags":["cashback","devolucion","2d","bch"],"is_featured":False},
    "10_dolares_premio.png": {"title":"Dólares-Premio (2D)","category":"Íconos 2D","family":"Medios de Pago & Ciclo de Uso","concept":"DP Travel 2D","rubro":"Lealtad","rule":"Versión 2D dólares-premio.","tags":["dolares premio","dp","2d","bch"],"is_featured":False},
    "11_supermercado.png": {"title":"Supermercados (2D)","category":"Íconos 2D","family":"Rubros de Consumo","concept":"Supermercados 2D","rubro":"Supermercados","rule":"Versión 2D.","tags":["supermercado","2d","bch"],"is_featured":False},
    "12_gastronomia_restaurantes.png": {"title":"Gastronomía (2D)","category":"Íconos 2D","family":"Rubros de Consumo","concept":"Restaurantes 2D","rubro":"Gastronomía","rule":"Versión 2D.","tags":["restaurante","gastronomia","2d","bch"],"is_featured":False},
    "13_cafe_cafeterias.png": {"title":"Cafeterías (2D)","category":"Íconos 2D","family":"Rubros de Consumo","concept":"Cafeterías 2D","rubro":"Cafeterías","rule":"Versión 2D.","tags":["cafe","2d","bch"],"is_featured":False},
    "14_combustible.png": {"title":"Combustible (2D)","category":"Íconos 2D","family":"Rubros de Consumo","concept":"Combustible 2D","rubro":"Combustible","rule":"Versión 2D.","tags":["combustible","2d","bch"],"is_featured":False},
    "15_farmacia_salud.png": {"title":"Farmacias (2D)","category":"Íconos 2D","family":"Rubros de Consumo","concept":"Farmacia 2D","rubro":"Salud","rule":"Versión 2D farmacia. Para salud clínica usar 38.","tags":["farmacia","salud","2d","bch"],"is_featured":False},
    "16_retail_shopping.png": {"title":"Retail & Shopping (2D)","category":"Íconos 2D","family":"Rubros de Consumo","concept":"Retail 2D","rubro":"Retail","rule":"Versión 2D retail general. Para moda usar 35, hogar usar 36.","tags":["retail","shopping","2d","bch"],"is_featured":False},
    "17_tecnologia.png": {"title":"Tecnología (2D)","category":"Íconos 2D","family":"Rubros de Consumo","concept":"Tecnología hardware 2D","rubro":"Tecnología","rule":"Versión 2D tecnología. Para IA usar 31.","tags":["tecnologia","gadgets","2d","bch"],"is_featured":False},
    "18_delivery.png": {"title":"Delivery (2D)","category":"Íconos 2D","family":"Rubros de Consumo","concept":"Delivery 2D","rubro":"Delivery","rule":"Versión 2D.","tags":["delivery","rappi","2d","bch"],"is_featured":False},
    "19_viajes_turismo.png": {"title":"Viajes (2D)","category":"Íconos 2D","family":"Mecánicas, Crossborder & Travel","concept":"Viajes 2D","rubro":"Travel","rule":"Versión 2D.","tags":["viajes","turismo","2d","bch"],"is_featured":False},
    "20_entretenimiento_musica.png": {"title":"Entretenimiento Genérico (2D)","category":"Íconos 2D","family":"Rubros de Consumo","concept":"Entretenimiento amplio 2D","rubro":"Entretenimiento","rule":"Versión 2D genérico. Para cine usar 33, conciertos usar 34.","tags":["entretenimiento","2d","bch"],"is_featured":False},
    "21_contactless.png": {"title":"Contactless (2D)","category":"Íconos 2D","family":"Mecánicas, Crossborder & Travel","concept":"NFC 2D","rubro":"Tecnología de Pago","rule":"Versión 2D.","tags":["contactless","nfc","2d","bch"],"is_featured":False},
    "22_card_on_file_cof.png": {"title":"Card on File (2D)","category":"Íconos 2D","family":"Mecánicas, Crossborder & Travel","concept":"COF 2D","rubro":"Inscripción","rule":"Versión 2D COF.","tags":["card on file","cof","2d","bch"],"is_featured":False},
    "23_pago_recurrente.png": {"title":"Pago Recurrente PAT (2D)","category":"Íconos 2D","family":"Mecánicas, Crossborder & Travel","concept":"PAT 2D","rubro":"PAT / Servicios","rule":"Versión 2D PAT. Para streaming usar 32.","tags":["pago recurrente","pat","2d","bch"],"is_featured":False},
    "24_descuento.png": {"title":"Descuento (2D)","category":"Íconos 2D","family":"Mecánicas, Crossborder & Travel","concept":"% OFF 2D","rubro":"Promoción","rule":"Versión 2D descuento.","tags":["descuento","off","2d","bch"],"is_featured":False},
    "25_cuotas_sin_interes_csi.png": {"title":"CSI Cuotas Sin Interés (2D)","category":"Íconos 2D","family":"Mecánicas, Crossborder & Travel","concept":"CSI 2D","rubro":"Financiamiento","rule":"Versión 2D CSI.","tags":["cuotas","sin interes","2d","bch"],"is_featured":False},
    "26_meta_de_facturacion.png": {"title":"Meta de Facturación (2D)","category":"Íconos 2D","family":"Mecánicas, Crossborder & Travel","concept":"Meta facturación 2D","rubro":"Gasto","rule":"Versión 2D.","tags":["meta facturacion","2d","bch"],"is_featured":False},
    "27_compra_internacional_crossborder.png": {"title":"Compra Internacional (2D)","category":"Íconos 2D","family":"Mecánicas, Crossborder & Travel","concept":"Crossborder presencial 2D","rubro":"Crossborder","rule":"Versión 2D.","tags":["crossborder","internacional","2d","bch"],"is_featured":False},
    "28_ecommerce_internacional.png": {"title":"Ecommerce Internacional (2D)","category":"Íconos 2D","family":"Mecánicas, Crossborder & Travel","concept":"Ecommerce internacional 2D","rubro":"Crossborder Online","rule":"Versión 2D.","tags":["ecommerce internacional","amazon","2d","bch"],"is_featured":False},
    "29_lounge_salon_vip.png": {"title":"Salones VIP (2D)","category":"Íconos 2D","family":"Mecánicas, Crossborder & Travel","concept":"Salones VIP 2D","rubro":"Aeropuerto","rule":"Versión 2D.","tags":["lounge","salon vip","2d","bch"],"is_featured":False},
    "30_traslado_aeropuerto.png": {"title":"Traslado Aeropuerto (2D)","category":"Íconos 2D","family":"Mecánicas, Crossborder & Travel","concept":"Transfer aeropuerto 2D","rubro":"Aeropuerto","rule":"Versión 2D.","tags":["traslado","aeropuerto","2d","bch"],"is_featured":False},

    # ── BCH 2D Grupo 4 (31-40) ───────────────────────────────────────────
    "31_inteligencia_artificial.png": {"title":"Inteligencia Artificial","category":"Íconos 2D","family":"Grupo 4 · Contextos Específicos, Innovación & Canales","concept":"IA, chatbots, automatización inteligente","rubro":"Innovación","rule":"Usar para IA, chatbot, experiencias AI. Para hardware/gadgets usar 17.","tags":["ia","inteligencia artificial","chatbot","automatizacion","ai","innovacion","2d","bch"],"is_featured":False},
    "32_streaming_suscripciones.png": {"title":"Streaming & Suscripciones","category":"Íconos 2D","family":"Grupo 4 · Contextos Específicos, Innovación & Canales","concept":"Plataformas de streaming y suscripciones digitales","rubro":"Entretenimiento Digital","rule":"Usar para Netflix, Spotify, contenido digital. Para PAT genérico usar 23.","tags":["streaming","suscripcion","netflix","spotify","plataforma digital","2d","bch"],"is_featured":False},
    "33_cine.png": {"title":"Cine","category":"Íconos 2D","family":"Grupo 4 · Contextos Específicos, Innovación & Canales","concept":"Películas, entradas al cine","rubro":"Cine","rule":"Usar para beneficios de cine. NO usar 20 (entretenimiento genérico).","tags":["cine","pelicula","cinema","entrada cine","2d","bch"],"is_featured":False},
    "34_conciertos_musica_en_vivo.png": {"title":"Conciertos & Música en Vivo","category":"Íconos 2D","family":"Grupo 4 · Contextos Específicos, Innovación & Canales","concept":"Recitales, festivales, preventas y shows","rubro":"Música en Vivo","rule":"Usar para conciertos, preventas exclusivas. NO usar 20.","tags":["concierto","recital","festival","preventa","musica en vivo","2d","bch"],"is_featured":False},
    "35_moda_vestuario.png": {"title":"Moda & Vestuario","category":"Íconos 2D","family":"Grupo 4 · Contextos Específicos, Innovación & Canales","concept":"Ropa, moda y fashion","rubro":"Moda","rule":"Usar para moda/ropa específicamente. Para retail general usar 16.","tags":["moda","vestuario","ropa","fashion","2d","bch"],"is_featured":False},
    "36_hogar.png": {"title":"Hogar & Deco","category":"Íconos 2D","family":"Grupo 4 · Contextos Específicos, Innovación & Canales","concept":"Casa, muebles, decoración, línea blanca","rubro":"Hogar","rule":"Usar para mejoramiento del hogar, muebles, decoración. Para retail general usar 16.","tags":["hogar","muebles","casa","decoracion","linea blanca","2d","bch"],"is_featured":False},
    "37_mascotas.png": {"title":"Mascotas","category":"Íconos 2D","family":"Grupo 4 · Contextos Específicos, Innovación & Canales","concept":"Veterinaria, pet shop y animales","rubro":"Mascotas","rule":"Usar para veterinaria, pet shops, cuidado de mascotas.","tags":["mascotas","veterinaria","pet","perro","gato","animales","2d","bch"],"is_featured":False},
    "38_salud_clinica_medico.png": {"title":"Salud Clínica & Médico","category":"Íconos 2D","family":"Grupo 4 · Contextos Específicos, Innovación & Canales","concept":"Atención médica, clínicas y prestación de salud","rubro":"Salud Clínica","rule":"Usar para clínicas, médicos, consultas. Para farmacia/medicamentos usar 15.","tags":["clinica","medico","consulta","salud asistencial","2d","bch"],"is_featured":False},
    "39_seguridad_proteccion.png": {"title":"Seguridad & Protección","category":"Íconos 2D","family":"Grupo 4 · Contextos Específicos, Innovación & Canales","concept":"Compra segura, antifraude y protección","rubro":"Seguridad","rule":"Usar cuando el mensaje central es seguridad, protección o compra segura.","tags":["seguridad","proteccion","antifraude","compra segura","respaldo","2d","bch"],"is_featured":False},
    "40_app_canal_digital.png": {"title":"App Canal Digital","category":"Íconos 2D","family":"Grupo 4 · Contextos Específicos, Innovación & Canales","concept":"App del banco, autogestión y canal digital","rubro":"Canal Digital","rule":"Usar cuando el foco es la app del banco o autogestión. Si el foco es PAGAR con celular, usar 04.","tags":["app","canal digital","app mi banco","autogestion","celular banco","2d","bch"],"is_featured":False},


    # ── GALICIA ICONS (Servicios, Seguros, Entretenimiento) ─────────────────
    "wi_fi.png": {
        "title": "Wi-Fi & Internet Fibra Óptica", "category": "Íconos 3D", "family": "Servicios & Conectividad",
        "concept": "Conectividad a Internet de alta velocidad, banda ancha, fibra óptica y abonos hogareños",
        "rubro": "Internet & Conectividad", "rule": "Usar para facturas y promociones en abonos de internet (Personal Flow, Telecentro, Movistar Fibra, Claro) y débito automático de telecomunicaciones.",
        "tags": ["wifi","internet","conectividad","servicios","galicia","fibra"], "is_featured": True
    },
    "auriculares.png": {
        "title": "Auriculares & Streaming de Audio", "category": "Íconos 3D", "family": "Entretenimiento & Salidas",
        "concept": "Música, podcasts, suscripciones de audio y plataformas de streaming (Spotify, YouTube Music)",
        "rubro": "Audio & Streaming", "rule": "Usar para suscripciones de streaming musical, podcasts, compra de auriculares y audio.",
        "tags": ["auriculares","musica","streaming","spotify","audio","galicia"], "is_featured": True
    },
    "auriculares_2.png": {
        "title": "Calendario de Vencimientos & Pagos (auriculares_2.png)", "category": "Íconos 3D", "family": "Servicios Básicos & Pagos",
        "concept": "Calendario de mesa con signo de exclamación de alerta y pila de monedas para vencimientos de facturas",
        "rubro": "Vencimientos & Pagos", "rule": "ATENCIÓN LLM: A pesar del nombre del archivo, representa visualmente un CALENDARIO DE MESA con signo de exclamación y monedas. Usar para fechas de vencimiento de facturas, recordatorios de pago de resumen, adhesión a débito automático y alertas de cobro próximo.",
        "tags": ["vencimiento","fecha de pago","calendario","factura","cuotas","alerta","deuda","debito automatico","galicia"], "is_featured": True
    },
    "canilla.png": {
        "title": "Agua Potable & Servicios Sanitarios", "category": "Íconos 3D", "family": "Servicios Básicos & Pagos",
        "concept": "Pago de facturas de agua potable y saneamiento (AySA, Aguas Cordobesas, Aguas Santafesinas)",
        "rubro": "Servicios Públicos", "rule": "Usar para pago de servicios de agua, facturas sanitarias, expensas y suministro hídrico.",
        "tags": ["canilla","agua","aysa","servicios","cuentas","galicia"], "is_featured": True
    },
    "celular.png": {
        "title": "Billetera Digital & Confirmación Móvil", "category": "Íconos 3D", "family": "Servicios & Conectividad",
        "concept": "Mano con smartphone mostrando tarjeta Galicia flotante y tilde de confirmación de pago",
        "rubro": "Banca Móvil & Wallet", "rule": "Usar para pagos móviles con celular, adhesión a MODO / Apple Pay / Google Wallet, recarga de saldo y confirmación de operaciones en App Galicia.",
        "tags": ["celular","smartphone","app galicia","modo","apple pay","wallet","pago movil","recargas","galicia"], "is_featured": True
    },
    "cine.png": {
        "title": "Cine & Proyección de Películas", "category": "Íconos 3D", "family": "Entretenimiento & Salidas",
        "concept": "Claqueta de cine con carrete de película cinematográfica y cinta de celuloide",
        "rubro": "Cine & Espectáculos", "rule": "Usar para campañas principales de cine, 2x1 en entradas (Hoyts, Cinemark, Showcase), estrenos y festivales audiovisuales.",
        "tags": ["cine","peliculas","cinemark","hoyts","entradas","cartelera","galicia"], "is_featured": True
    },
    "cine_2.png": {
        "title": "Claqueta de Cine (Minimalista)", "category": "Íconos 3D", "family": "Entretenimiento & Salidas",
        "concept": "Claqueta cinematográfica frontal con franjas diagonales en diseño limpio",
        "rubro": "Cine & Espectáculos", "rule": "Usar como variante limpia de claqueta para botones, grillas compactas o llamadas a la acción rápidas de cine.",
        "tags": ["cine","claqueta","peliculas","estrenos","minimalista","galicia"], "is_featured": True
    },
    "entradas.png": {
        "title": "Entradas & Tickets Dobles (2x1)", "category": "Íconos 3D", "family": "Entretenimiento & Salidas",
        "concept": "Par de tickets de espectáculo superpuestos para promociones 2x1 y eventos generales",
        "rubro": "Espectáculos & Tickets", "rule": "Usar para compra de tickets, promociones 2x1 en salidas, cines o recitales generales.",
        "tags": ["entradas","tickets","2x1","shows","recitales","eventos","galicia"], "is_featured": True
    },
    "entradas_2.png": {
        "title": "Entradas Exclusivas Galicia (Cruz de Santiago)", "category": "Íconos 3D", "family": "Entretenimiento & Salidas",
        "concept": "Par de tickets de espectáculo con el emblema oficial de la Cruz de Santiago de Banco Galicia",
        "rubro": "Espectáculos & Preventas", "rule": "Usar para preventas exclusivas Galicia, acceso VIP con Tarjeta Galicia, recitales sponsoreados y descuentos en festivales de música.",
        "tags": ["entradas","tickets","preventa","cruz de santiago","recitales","shows","galicia"], "is_featured": True
    },
    "gas.png": {
        "title": "Gas Natural & Servicios de Red", "category": "Íconos 3D", "family": "Servicios Básicos & Pagos",
        "concept": "Hornalla con llama azul y naranja para facturas de gas natural (Metrogas, Naturgy, Camuzzi, Ecogas)",
        "rubro": "Servicios Públicos", "rule": "Usar para pago de facturas de gas de red, garrafas, calefacción y débitos automáticos del hogar.",
        "tags": ["gas","metrogas","naturgy","camuzzi","servicios","calefaccion","galicia"], "is_featured": True
    },
    "luz_lampara.png": {
        "title": "Electricidad & Luz Hogar", "category": "Íconos 3D", "family": "Servicios Básicos & Pagos",
        "concept": "Lamparita incandescente naranja para facturas de electricidad (Edenor, Edesur, EPEC, Edelap)",
        "rubro": "Servicios Públicos", "rule": "Usar para pago de facturas de luz domiciliaria o comercial y servicios de suministro eléctrico.",
        "tags": ["luz","electricidad","edenor","edesur","epec","lampara","servicios","galicia"], "is_featured": True
    },
    "microfono.png": {
        "title": "Micrófono Vocal de Mano (Recitales)", "category": "Íconos 3D", "family": "Entretenimiento & Salidas",
        "concept": "Micrófono de mano vocal para recitales, música en vivo, canto y festivales",
        "rubro": "Música & Shows", "rule": "Usar para recitales masivos, shows de música en vivo, bandas y conciertos.",
        "tags": ["microfono","recitales","conciertos","musica en vivo","canto","galicia"], "is_featured": True
    },
    "microfono_2.png": {
        "title": "Micrófono con Soporte de Pie (Stand-up & Podcast)", "category": "Íconos 3D", "family": "Entretenimiento & Salidas",
        "concept": "Micrófono en soporte de pie circular para stand-up comedy, podcasts, streaming y conferencias",
        "rubro": "Humor & Streaming", "rule": "Usar para obras de stand-up comedy, transmisiones en vivo, streaming, podcasts, radio y eventos humorísticos.",
        "tags": ["microfono","soporte","standup","podcast","streaming","comedia","shows","galicia"], "is_featured": True
    },
    "paraguas.png": {
        "title": "Protección ante Imprevistos", "category": "Íconos 3D", "family": "Seguros & Coberturas",
        "concept": "Paraguas abierto a franjas naranjas y blancas para cobertura y contingencias",
        "rubro": "Seguros & Asistencia", "rule": "Usar para conceptos de respaldo patrimonial, protección ante imprevistos, cobertura integral y fondos de emergencia.",
        "tags": ["paraguas","proteccion","seguros","respaldo","imprevistos","galicia"], "is_featured": True
    },
    "pochoclos.png": {
        "title": "Pochoclos de Cine (Cilíndrico Clásico)", "category": "Íconos 3D", "family": "Entretenimiento & Salidas",
        "concept": "Balde cilíndrico a rayas con pochoclos abundantes para Candy Bar de cines",
        "rubro": "Cine & Snacks", "rule": "Usar para beneficios en candy bar de cines, pochoclos y snacks de entretenimiento.",
        "tags": ["pochoclos","popcorn","candybar","cine","snacks","galicia"], "is_featured": True
    },
    "pochoclos_2.png": {
        "title": "Pochoclos Dinámicos (Popcorn al Aire)", "category": "Íconos 3D", "family": "Entretenimiento & Salidas",
        "concept": "Balde de pochoclos con aro naranja y grano de pochoclo saltando en el aire",
        "rubro": "Cine & Snacks", "rule": "Usar para promociones enérgicas de Candy Bar, combos 2x1 y estrenos pochocleros.",
        "tags": ["pochoclos","popcorn","candybar","cine","combos","galicia"], "is_featured": True
    },
    "primeros_auxilios.png": {
        "title": "Asistencia Médica & Salud", "category": "Íconos 3D", "family": "Seguros & Coberturas",
        "concept": "Corazón 3D con cruz médica blanca de primeros auxilios",
        "rubro": "Salud & Seguros", "rule": "Usar para seguros de salud, coberturas de urgencias médicas, asistencia al viajero y bienestar familiar.",
        "tags": ["primeros auxilios","salud","medico","emergencias","botiquin","seguros","galicia"], "is_featured": True
    },
    "rayo.png": {
        "title": "Energía & Pago Inmediato Flash", "category": "Íconos 3D", "family": "Servicios & Transacciones",
        "concept": "Rayo 3D naranja y blanco para transacciones instantáneas y velocidad de acreditación",
        "rubro": "Transacciones", "rule": "Usar para destacar pagos instantáneos, acreditación en el acto, ofertas relámpago y pagos sin contacto.",
        "tags": ["rayo","energia","rapido","express","flash","pago inmediato","galicia"], "is_featured": True
    },
    "seguro_auto.png": {
        "title": "Seguro Automotor Galicia", "category": "Íconos 3D", "family": "Seguros & Coberturas",
        "concept": "Auto escarabajo naranja frente a escudo protector con la Cruz de Santiago de Galicia",
        "rubro": "Seguros", "rule": "Usar para pólizas de automotor Galicia Seguros, auxilio mecánico en ruta, cobertura contra terceros y todo riesgo.",
        "tags": ["seguro auto","automotor","vehiculo","escarabajo","poliza","galicia seguros","galicia"], "is_featured": True
    },
    "seguro_hogar.png": {
        "title": "Seguro de Hogar & Vivienda", "category": "Íconos 3D", "family": "Seguros & Coberturas",
        "concept": "Manos protectoras envolviendo una casa naranja para combinado familiar",
        "rubro": "Seguros", "rule": "Usar para Galicia Seguros de hogar, cobertura contra incendio, robo, daños por agua y asistencia domiciliaria.",
        "tags": ["seguro hogar","vivienda","casa","combinado familiar","galicia seguros","galicia"], "is_featured": True
    },
    "seguro_vida.png": {
        "title": "Seguro de Vida & Familia", "category": "Íconos 3D", "family": "Seguros & Coberturas",
        "concept": "Busto de persona protegido por un escudo con cruz médica y pulso cardíaco ECG",
        "rubro": "Seguros", "rule": "Usar para seguros de vida individual y colectivo, indemnización, protección económica y bienestar familiar.",
        "tags": ["seguro vida","vida","salud","electrocardiograma","proteccion familiar","galicia seguros","galicia"], "is_featured": True
    },
    "seguros.png": {
        "title": "Galicia Seguros Integral (Escudo con Tilde)", "category": "Íconos 3D", "family": "Seguros & Coberturas",
        "concept": "Escudo de seguridad naranja 3D con tilde blanca central de verificación y tranquilidad",
        "rubro": "Seguros", "rule": "Usar para el ecosistema integral de pólizas Galicia Seguros, verificación de cobertura y tranquilidad patrimonial.",
        "tags": ["seguros","polizas","escudo","tilde","coberturas","galicia seguros","galicia"], "is_featured": True
    },
    "teatro.png": {
        "title": "Teatro & Artes Escénicas", "category": "Íconos 3D", "family": "Entretenimiento & Salidas",
        "concept": "Máscaras teatrales clásicas de comedia y tragedia (con lágrima blanca)",
        "rubro": "Cultura & Teatro", "rule": "Usar para obras de teatro, espectáculos en Calle Corrientes, comedia musical y eventos culturales.",
        "tags": ["teatro","mascaras","comedia","tragedia","calle corrientes","espectaculos","cultura","galicia"], "is_featured": True
    },

    # ── GALICIA HEADERS (Banners Hero Sin Texto) ───────────────────────────
    "header_promos_visa_permanentes_07.png": {
        "title": "Header Promos Visa #07 · Café & Rutinas Diarias", "category": "Banners Hero", "family": "Headers sin Texto Galicia",
        "concept": "Fotografía lifestyle (1100x504): Joven con cabello rosado sosteniendo bandeja de café y celular con tilde de confirmación, onda orgánica naranja a la izquierda",
        "rubro": "Gastronomía Diaria & Cafeterías", "rule": "Usar en correos de microgastronomía, cafés al paso, desayunos, salidas cotidianas y compras de bajo monto con Visa.",
        "tags": ["header","banner","cafe","desayuno","lifestyle","celular","visa","galicia","hero","sin texto"], "is_featured": True
    },
    "header_promos_visa_permanentes_08.png": {
        "title": "Header Promos Visa #08 · Compras en Tienda Física & Cuotas", "category": "Banners Hero", "family": "Headers sin Texto Galicia",
        "concept": "Fotografía comercial (1100x504): Mujer sonriendo pagando con tarjeta física sobre POS en mostrador, con badges flotantes naranjas 'ahorrá' y 'comprá'",
        "rubro": "Shopping & Tiendas Físicas", "rule": "Usar para compras presenciales en shoppings, indumentaria, planes de cuotas sin interés y promociones en comercios físicos.",
        "tags": ["header","banner","shopping","pos","tienda fisica","cuotas","comisiones","visa","galicia","hero","sin texto"], "is_featured": True
    },
    "header_promos_visa_permanentes_09.png": {
        "title": "Header Promos Visa #09 · Contactless & Billeteras Digitales", "category": "Banners Hero", "family": "Headers sin Texto Galicia",
        "concept": "Fotografía primer plano (1100x502): Mano apoyando smartphone con tarjeta Galicia Visa digital sobre lector POS contactless que indica 'Acercar al lector'",
        "rubro": "Pagos Móviles & NFC", "rule": "Usar para campañas de pagos sin contacto (Tap to Pay), enrolamiento de tarjetas en Apple Pay / Google Wallet / MODO y tecnología contactless.",
        "tags": ["header","banner","contactless","nfc","modo","apple pay","pago movil","pos","visa","galicia","hero","sin texto"], "is_featured": True
    },
    "header_promos_visa_permanentes_10.png": {
        "title": "Header Promos Visa #10 · Ecommerce & Envíos (Compacto)", "category": "Banners Hero", "family": "Headers sin Texto Galicia",
        "concept": "Fotografía lifestyle compacta (1100x463, fondo blanco puro): Joven recibiendo paquete de delivery sosteniendo café y celular, con badges 'comprá' y 'ahorrá'",
        "rubro": "Ecommerce & Delivery", "rule": "Usar para compras online, delivery a domicilio, compras en marketplaces y correos con grilla extensa de beneficios inferior gracias a su altura compacta.",
        "tags": ["header","banner","compacto","delivery","ecommerce","paquete","cafe","visa","galicia","hero","sin texto"], "is_featured": True
    },
    "header_promos_visa_permanentes_11.png": {
        "title": "Header Promos Visa #11 · Ilustrado Minimalista Claro (Compacto)", "category": "Banners Hero", "family": "Headers sin Texto Galicia",
        "concept": "Ilustración vectorial en viñeta circular (1100x463, fondo crema/marfil limpio): Teléfono naranja pagando sobre POS con ondas de radio y espacio libre para tipografía",
        "rubro": "Fintech & Onboarding", "rule": "Usar para comunicaciones ilustradas, onboarding digital de billeteras móviles, resúmenes transaccionales o correos de diseño sobrio y minimalista.",
        "tags": ["header","banner","compacto","ilustrado","vectorial","minimalista","pos","celular","visa","galicia","hero","sin texto"], "is_featured": True
    },
    "header_promos_visa_permanentes_12.png": {
        "title": "Header Promos Visa #12 · Ilustrado Naranja Galicia Shock (Compacto)", "category": "Banners Hero", "family": "Headers sin Texto Galicia",
        "concept": "Ilustración vectorial sobre fondo sólido naranja corporativo Galicia #F96400 (1100x463): Teléfono naranja pagando sobre POS en viñeta circular blanca de máximo impacto",
        "rubro": "Grandes Eventos & Mega Promos", "rule": "Usar para aperturas de campaña de alto impacto (Hot Sale, Cyber Monday), lanzamientos oficiales masivos y comunicaciones donde el color naranja deba dominar la pantalla.",
        "tags": ["header","banner","compacto","naranja solido","shock","hotsale","cybermonday","visa","galicia","hero","sin texto"], "is_featured": True
    },

    # ── GALICIA LOGOS ──────────────────────────────────────────────────────
    "logo_galicia_header.png": {
        "title": "Logo Banco Galicia (Header)", "category": "Logotipos", "family": "Identidad Galicia",
        "concept": "Logotipo institucional oficial Banco Galicia para cabecera de emails",
        "rubro": "Branding", "rule": "Cabecera principal de correos institucionales de Banco Galicia.",
        "tags": ["logo","branding","galicia","banco galicia","header"], "is_featured": True
    },

    # ── BCH Logos ────────────────────────────────────────────────────────
    "banco_de_chile.png": {"title":"Logo Banco de Chile","category":"Logotipos","family":"Identidad Corporativa","concept":"Logotipo institucional wordmark azul","rubro":"Branding","rule":"Cabecera principal de emails o pie institucional.","tags":["logo","branding","bch","banco de chile","wordmark"],"is_featured":True},
    "bch_logo.png": {"title":"Isotipo Estrella Azul BCH","category":"Logotipos","family":"Identidad Corporativa","concept":"Monograma / favicon institucional","rubro":"Branding","rule":"Usar como favicon, monograma o elemento de marca secundario.","tags":["logo","isotipo","estrella","bch","favicon"],"is_featured":True},
}

# ═══════════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════════
def get_png_dimensions(fp: pathlib.Path):
    try:
        with open(fp, 'rb') as f:
            d = f.read(24)
            if d[:8] == b'\x89PNG\r\n\x1a\n':
                w, h = struct.unpack('>II', d[16:24])
                return w, h
    except Exception:
        pass
    return 1254, 1254

def humanize(filename: str) -> str:
    stem = pathlib.Path(filename).stem
    stem = re.sub(r'^\d+_', '', stem)
    stem = stem.replace('-high','').replace('-low','').replace('-tiny','')
    return stem.replace('_',' ').replace('-',' ').title()

def make_entry(fp: pathlib.Path, bank: str, default_cat: str, default_family: str, featured: bool) -> dict:
    fn = fp.name
    stat = fp.stat()
    rel  = fp.relative_to(REPO_ROOT).as_posix()
    cdn  = make_cdn_url(rel)
    ext  = fp.suffix.lower()
    fmt  = ext.lstrip('.').upper()
    w, h = get_png_dimensions(fp) if ext == '.png' else ("Vector", "Vector")

    base = {"filename": fn, "rel_path": rel, "cdn_url": cdn, "bank": bank,
            "format": fmt, "width": w, "height": h,
            "size_kb": f"{stat.st_size/1024:.1f} KB", "size_bytes": stat.st_size}

    # ── Visa SVG: auto-derive ──
    if bank == "Visa" and ext == ".svg":
        stem = fp.stem
        cat  = get_visa_svg_category(stem)
        disp = humanize(fn)
        base.update({
            "title": disp, "category": cat, "family": "Visa Icons Official SVG",
            "concept": f"Ícono SVG oficial Visa: {disp}", "rubro": cat,
            "rule": f"Ícono SVG oficial Visa para {cat.lower()}. Usar URL CDN con variante -high.svg.",
            "tags": list(set(["visa","svg","icono","oficial"] + stem.replace("-high","").split("-"))),
            "is_featured": False
        })
        return base

    # ── METADATA_TABLE lookup ──
    if fn in METADATA_TABLE:
        m = METADATA_TABLE[fn]
        # IMPORTANT: category always comes from BANK_CONFIG (default_cat)
        # so 3D icons/ and 2D iconos_bch_2d_30/ with same filename get correct categories.
        base.update({
            "title": m["title"],
            "category": default_cat,
            "family": m.get("family", default_family),
            "concept": m.get("concept",""),
            "rubro": m.get("rubro",""),
            "rule": m.get("rule",""),
            "tags": list(set(m.get("tags", []))),
            "is_featured": m.get("is_featured", featured)
        })
        return base

    # ── Auto fallback ──
    title = humanize(fn)
    base.update({
        "title": title, "category": default_cat, "family": default_family,
        "concept": f"Activo oficial {bank}: {title}", "rubro": bank,
        "rule": f"Activo corporativo oficial. Usar según contexto de {default_cat.lower()}.",
        "tags": list(set([bank.lower(), default_cat.lower(), "icono"] + title.lower().split())),
        "is_featured": featured
    })
    return base

SKIP    = {'.DS_Store', '.gitkeep', 'Thumbs.db', '.gitignore'}
IMG_EXT = {'.png', '.jpg', '.jpeg', '.webp', '.svg', '.gif'}

# ═══════════════════════════════════════════════════════════════════════════
# MAIN SCAN
# ═══════════════════════════════════════════════════════════════════════════
manifest = []
seen     = set()

for bank, specs in BANK_CONFIG.items():
    for rel_folder, default_cat, default_family, featured, only_svg_high, recursive in specs:
        folder = REPO_ROOT / "assets" / rel_folder
        if not folder.exists():
            continue

        if only_svg_high:
            files = sorted(folder.rglob("*.svg"))
        elif recursive:
            files = sorted(folder.rglob("*"))
        else:
            files = sorted(folder.glob("*"))

        for fp in files:
            if not fp.is_file():                              continue
            if fp.name in SKIP or fp.name.startswith('.'):   continue
            if fp.suffix.lower() not in IMG_EXT:             continue
            if only_svg_high and not fp.stem.endswith('-high'): continue

            key = (bank, fp.relative_to(REPO_ROOT).as_posix())
            if key in seen:
                continue
            seen.add(key)

            manifest.append(make_entry(fp, bank, default_cat, default_family, featured))

# ═══════════════════════════════════════════════════════════════════════════
# WRITE
# ═══════════════════════════════════════════════════════════════════════════
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
with open(DATA_FILE, 'w', encoding='utf-8') as f:
    f.write("window.BANK_ASSETS = ")
    json.dump(manifest, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print(f"\n✅  assets_data.js → {len(manifest)} activos totales\n")
stats = Counter(f"{e['bank']} → {e['category']}" for e in manifest)
for k, v in sorted(stats.items()):
    print(f"   {k}: {v}")
print(f"\n   Output: {DATA_FILE.relative_to(REPO_ROOT)}\n")
print("Para agregar íconos nuevos:")
print("  1. Copia los archivos a la carpeta correcta del banco")
print("  2. Añade metadata en METADATA_TABLE si quieres documentación rica")
print("  3. python3 scripts/build_manifest.py")
