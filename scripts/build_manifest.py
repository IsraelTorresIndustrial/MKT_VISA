import os
import json
import struct

BASE_DIR = os.path.abspath("public/assets")
MANIFEST_PATH = os.path.abspath("src/data/assets_manifest.json")

BCH_30_METADATA = {
    "01_tarjeta.png": {
        "title": "Tarjeta de Crédito Genérica",
        "category": "Medios de Pago",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Medio de pago principal / Portafolio de Tarjetas",
        "rubro": "General",
        "rule": "Usar cuando el mensaje explica el medio de pago o portafolio de tarjetas sin especificar canal ni condición técnica.",
        "tags": ["tarjeta", "credito", "medio de pago", "plastico", "bch", "visa", "chile"]
    },
    "02_pago_presencial_pos.png": {
        "title": "Pago Presencial POS",
        "category": "Medios de Pago",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Compra en terminal de punto de venta físico",
        "rubro": "Tiendas Físicas",
        "rule": "Usar para compras en comercio físico con terminal POS.",
        "tags": ["pos", "presencial", "terminal", "tienda fisica", "compra"]
    },
    "03_ecommerce.png": {
        "title": "Ecommerce Nacional",
        "category": "Medios de Pago",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Compra online en comercios nacionales",
        "rubro": "Online",
        "rule": "Usar para compras online locales, sitios web y comercio electrónico nacional.",
        "tags": ["ecommerce", "online", "carrito", "web", "tienda digital"]
    },
    "04_wallet_pago_movil.png": {
        "title": "Wallet & Pago Móvil",
        "category": "Medios de Pago",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Billetera digital / Smartphone / Smartwatch",
        "rubro": "Digital / Móvil",
        "rule": "Usar para Apple Pay, Google Wallet, Garmin Pay o pago con celular.",
        "tags": ["wallet", "apple pay", "google pay", "celular", "pago movil", "contactless"]
    },
    "05_activacion.png": {
        "title": "Activación de Tarjeta",
        "category": "Ciclo de Vida",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Encendido / Primera habilitación de la tarjeta",
        "rubro": "Onboarding",
        "rule": "Usar para etapas iniciales de activación, bienvenida y primer encendido del plástico.",
        "tags": ["activacion", "onboarding", "bienvenida", "primer uso", "desbloqueo"]
    },
    "06_primera_compra.png": {
        "title": "Primera Compra",
        "category": "Ciclo de Vida",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Incentivo a la transacción debut",
        "rubro": "Onboarding",
        "rule": "Usar cuando la campaña premia o estimula realizar la primera compra del cliente.",
        "tags": ["primera compra", "debut", "incentivo", "inicio", "transaccion"]
    },
    "07_reactivacion.png": {
        "title": "Reactivación de Clientes",
        "category": "Ciclo de Vida",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Recuperación de clientes inactivos o dormidos",
        "rubro": "Retención / Winback",
        "rule": "Usar en comunicaciones M1-M3 dirigidas a clientes inactivos o en riesgo de fuga.",
        "tags": ["reactivacion", "inactivo", "retencion", "winback", "vuelve a usar"]
    },
    "08_meta_de_transacciones.png": {
        "title": "Meta de Transacciones",
        "category": "Mecánicas de Campaña",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Desafío por número de compras (ej. haz 3 compras)",
        "rubro": "Frecuencia",
        "rule": "Usar cuando la condición para ganar el beneficio es alcanzar un conteo mínimo de transacciones.",
        "tags": ["meta", "transacciones", "frecuencia", "concurso", "desafio", "compras"]
    },
    "09_cashback.png": {
        "title": "Cashback / Devolución",
        "category": "Beneficios",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Abono en dinero / Reembolso en estado de cuenta",
        "rubro": "Recompensa",
        "rule": "Usar cuando el beneficio es dinero devuelto directo a la cuenta o tarjeta.",
        "tags": ["cashback", "devolucion", "dinero", "reembolso", "abono", "beneficio"]
    },
    "10_dolares_premio.png": {
        "title": "Dólares-Premio (DP)",
        "category": "Beneficios",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Programa de lealtad Travel Club Banco de Chile",
        "rubro": "Lealtad",
        "rule": "Usar para acumulación o canje de Dólares-Premio en compras y campañas de lealtad.",
        "tags": ["dolares premio", "dp", "travel", "travel club", "lealtad", "canje", "puntos"]
    },
    "11_supermercado.png": {
        "title": "Supermercados",
        "category": "Rubros de Consumo",
        "family": "Rubros de Consumo",
        "concept": "Compras de alimentación y abastecimiento del hogar",
        "rubro": "Supermercados",
        "rule": "Usar en promociones de supermercados (Jumbo, Lider, Santa Isabel, Unimarc).",
        "tags": ["supermercado", "comida", "despensa", "jumbo", "lider", "rubro"]
    },
    "12_gastronomia_restaurantes.png": {
        "title": "Gastronomía & Restaurantes",
        "category": "Rubros de Consumo",
        "family": "Rubros de Consumo",
        "concept": "Restaurantes, bares y salidas a comer",
        "rubro": "Gastronomía",
        "rule": "Usar en beneficios culinarios, descuentos en restaurantes o días temáticos de gastronomía.",
        "tags": ["restaurante", "gastronomia", "comida", "cena", "almuerzo", "gourmet"]
    },
    "13_cafe_cafeterias.png": {
        "title": "Cafeterías & Coffee",
        "category": "Rubros de Consumo",
        "family": "Rubros de Consumo",
        "concept": "Cafés, pastelerías y pausas diarias",
        "rubro": "Cafeterías",
        "rule": "Usar para alianzas con Starbucks, Dunkin', Juan Valdez y consumo recurrente en cafeterías.",
        "tags": ["cafe", "starbucks", "dunkin", "cafeteria", "desayuno", "snack"]
    },
    "14_combustible.png": {
        "title": "Combustible & Bencina",
        "category": "Rubros de Consumo",
        "family": "Rubros de Consumo",
        "concept": "Carga de combustible y estaciones de servicio",
        "rubro": "Combustible",
        "rule": "Usar para descuentos en Shell, Copec, Petrobras o beneficios por litro.",
        "tags": ["combustible", "bencina", "estacion de servicio", "shell", "copec", "auto"]
    },
    "15_farmacia_salud.png": {
        "title": "Farmacias & Salud",
        "category": "Rubros de Consumo",
        "family": "Rubros de Consumo",
        "concept": "Medicamentos, bienestar y cuidado personal",
        "rubro": "Salud",
        "rule": "Usar en alianzas con Cruz Verde, Salcobrand, Ahumada y centros de salud.",
        "tags": ["farmacia", "salud", "cruz verde", "medicamentos", "bienestar"]
    },
    "16_retail_shopping.png": {
        "title": "Retail & Shopping",
        "category": "Rubros de Consumo",
        "family": "Rubros de Consumo",
        "concept": "Tiendas por departamento, moda y vestuario",
        "rubro": "Retail",
        "rule": "Usar para compras de ropa, calzado, centros comerciales y tiendas de retail.",
        "tags": ["retail", "shopping", "moda", "ropa", "mall", "tienda"]
    },
    "17_tecnologia.png": {
        "title": "Tecnología & Electro",
        "category": "Rubros de Consumo",
        "family": "Rubros de Consumo",
        "concept": "Dispositivos, computación y electrónica",
        "rubro": "Tecnología",
        "rule": "Usar en promociones de smartphones, computadores, televisores y gadgets.",
        "tags": ["tecnologia", "gadgets", "celulares", "computacion", "electronica"]
    },
    "18_delivery.png": {
        "title": "Delivery & Apps de Envíos",
        "category": "Rubros de Consumo",
        "family": "Rubros de Consumo",
        "concept": "PedidosYa, Rappi, Uber Eats y envíos rápidos",
        "rubro": "Delivery",
        "rule": "Usar para descuentos en aplicaciones de entrega a domicilio y última milla.",
        "tags": ["delivery", "pedidosya", "rappi", "uber eats", "envios", "app"]
    },
    "19_viajes_turismo.png": {
        "title": "Viajes & Turismo",
        "category": "Travel & Crossborder",
        "family": "Mecánicas, Crossborder & Travel",
        "concept": "Vuelos, paquetes turísticos y escapadas",
        "rubro": "Travel",
        "rule": "Usar para agencias de viaje, pasajes aéreos y promociones de turismo.",
        "tags": ["viajes", "turismo", "vuelos", "aerolineas", "vacaciones", "travel"]
    },
    "20_entretenimiento_musica.png": {
        "title": "Entretenimiento & Conciertos",
        "category": "Rubros de Consumo",
        "family": "Rubros de Consumo",
        "concept": "Cines, preventas de conciertos y streaming",
        "rubro": "Entretenimiento",
        "rule": "Usar para preventas exclusivas Banco de Chile, cines (Cineplanet, Cinépolis) y eventos.",
        "tags": ["entretenimiento", "conciertos", "musica", "cine", "entradas", "preventa"]
    },
    "21_contactless.png": {
        "title": "Pago Sin Contacto (Contactless)",
        "category": "Medios de Pago",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Tecnología NFC / Acercar y pagar",
        "rubro": "Tecnología de Pago",
        "rule": "Usar cuando el foco es la rapidez y seguridad de pagar acercando la tarjeta o reloj.",
        "tags": ["contactless", "nfc", "sin contacto", "rapido", "seguridad", "pos"]
    },
    "22_card_on_file_cof.png": {
        "title": "Card on File (COF)",
        "category": "Medios de Pago",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Tarjeta inscrita en apps favoritas",
        "rubro": "Inscripción / Recurrencia",
        "rule": "Usar para campañas que piden inscribir la tarjeta en Uber, Spotify, Netflix, Mercado Libre, etc.",
        "tags": ["card on file", "cof", "inscribir", "guardar tarjeta", "apps favoritas"]
    },
    "23_pago_recurrente.png": {
        "title": "Pago Recurrente / PAT",
        "category": "Medios de Pago",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Pago automático de cuentas y suscripciones",
        "rubro": "PAT / Servicios",
        "rule": "Usar para pago automático de cuentas de luz, agua, autopistas, seguros o donaciones.",
        "tags": ["pago recurrente", "pat", "cuentas", "suscripciones", "servicios", "automatico"]
    },
    "24_descuento.png": {
        "title": "Descuento / Porcentaje OFF",
        "category": "Beneficios",
        "family": "Mecánicas, Crossborder & Travel",
        "concept": "Porcentaje de rebaja directa en el total de compra",
        "rubro": "Promoción",
        "rule": "Usar cuando el beneficio principal es un porcentaje de rebaja directa (ej. 20%, 30%, 40% OFF).",
        "tags": ["descuento", "porcentaje", "off", "ahorro", "promocion", "oferta"]
    },
    "25_cuotas_sin_interes_csi.png": {
        "title": "Cuotas Sin Interés (CSI)",
        "category": "Beneficios",
        "family": "Mecánicas, Crossborder & Travel",
        "concept": "Financiamiento en 3, 6, 12 o más cuotas a tasa cero",
        "rubro": "Financiamiento",
        "rule": "Usar para destacar la posibilidad de pagar en cuotas sin recargo de interés.",
        "tags": ["cuotas", "sin interes", "csi", "financiamiento", "meses", "credito"]
    },
    "26_meta_de_facturacion.png": {
        "title": "Meta de Facturación",
        "category": "Mecánicas de Campaña",
        "family": "Medios de Pago & Ciclo de Uso",
        "concept": "Desafío por monto acumulado (ej. gasta $100.000)",
        "rubro": "Gasto",
        "rule": "Usar cuando la recompensa se activa al alcanzar un monto acumulado de compras.",
        "tags": ["meta de facturacion", "monto", "gasto", "facturacion", "desafio", "acumula"]
    },
    "27_compra_internacional_crossborder.png": {
        "title": "Compra Internacional Presencial",
        "category": "Travel & Crossborder",
        "family": "Mecánicas, Crossborder & Travel",
        "concept": "Uso de la tarjeta fuera de Chile en comercios físicos",
        "rubro": "Crossborder",
        "rule": "Usar para compras presenciales durante viajes al extranjero.",
        "tags": ["crossborder", "internacional", "viaje", "extranjero", "compras fuera", "dolares"]
    },
    "28_ecommerce_internacional.png": {
        "title": "Ecommerce Internacional",
        "category": "Travel & Crossborder",
        "family": "Mecánicas, Crossborder & Travel",
        "concept": "Compras online en moneda extranjera desde Chile",
        "rubro": "Crossborder Online",
        "rule": "Usar para Amazon, AliExpress, Shein, eBay o servicios digitales facturados en el exterior.",
        "tags": ["ecommerce internacional", "amazon", "aliexpress", "dolares", "online exterior"]
    },
    "29_lounge_salon_vip.png": {
        "title": "Salones VIP & Travel Lounge",
        "category": "Travel & Crossborder",
        "family": "Mecánicas, Crossborder & Travel",
        "concept": "Acceso a salones VIP en aeropuertos nacionales e internacionales",
        "rubro": "Aeropuerto",
        "rule": "Usar para accesos a Salones Pacific Club, VIP Lounge y salas de espera de alta gama.",
        "tags": ["lounge", "salon vip", "pacific club", "aeropuerto", "travel lounge", "confort"]
    },
    "30_traslado_aeropuerto.png": {
        "title": "Traslado al Aeropuerto",
        "category": "Travel & Crossborder",
        "family": "Mecánicas, Crossborder & Travel",
        "concept": "Servicio de van o conductor privado hacia/desde el aeropuerto",
        "rubro": "Aeropuerto",
        "rule": "Usar para beneficio de transporte y transfer al aeropuerto incluido en planes Travel.",
        "tags": ["traslado", "aeropuerto", "transfer", "van", "viaje", "movilizacion"]
    }
}

manifest = []

def get_png_dimensions(filepath):
    try:
        with open(filepath, 'rb') as f:
            data = f.read(24)
            if data.startswith(b'\x89PNG\r\n\x1a\n') and data[12:16] == b'IHDR':
                w, h = struct.unpack('>LL', data[16:24])
                return w, h
    except Exception:
        pass
    return 1024, 1024

def get_file_info(filepath, rel_path, bank, category_default):
    size_bytes = os.path.getsize(filepath)
    size_kb = f"{round(size_bytes / 1024, 1)} KB"
    width, height = "Vector", "Vector"
    filename = os.path.basename(filepath)
    ext = os.path.splitext(filename)[1].lower()
    
    if ext == ".png":
        width, height = get_png_dimensions(filepath)
    elif ext in [".jpg", ".jpeg", ".webp"]:
        width, height = 1200, 630

    return {
        "filename": filename,
        "rel_path": rel_path,
        "bank": bank,
        "format": ext.replace(".", "").upper(),
        "width": width,
        "height": height,
        "size_kb": size_kb,
        "size_bytes": size_bytes
    }

# 1. BCH 30 Icons
for fn, meta in BCH_30_METADATA.items():
    fp = os.path.join(BASE_DIR, "bch/icons", fn)
    if os.path.exists(fp):
        info = get_file_info(fp, f"assets/bch/icons/{fn}", "Banco de Chile", "Íconos 3D")
        info.update({
            "title": meta["title"],
            "category": "Íconos 3D",
            "family": meta["family"],
            "concept": meta["concept"],
            "rubro": meta["rubro"],
            "rule": meta["rule"],
            "tags": meta["tags"] + ["bch", "banco de chile", "3d", "icono"],
            "is_featured": True
        })
        manifest.append(info)

# 2. BCH Travel Icons
travel_dir = os.path.join(BASE_DIR, "bch/travel")
if os.path.exists(travel_dir):
    for fn in sorted(os.listdir(travel_dir)):
        if fn.endswith(".png"):
            fp = os.path.join(travel_dir, fn)
            clean_title = fn.replace("_ncde7f.png", "").replace("_pplf0o.png", "").replace("_kml5fp.png", "").replace("_qwzxxt.png", "").replace("_h03q2v.png", "").replace("_r9goav.png", "").replace("_gcez6a.png", "").replace("_aylvme.png", "").replace("_ntmoww.png", "").replace("_iaohbl.png", "").replace(".png", "").replace("bch_icono_", "").replace("_", " ").title()
            info = get_file_info(fp, f"assets/bch/travel/{fn}", "Banco de Chile", "Travel & Turismo")
            info.update({
                "title": clean_title,
                "category": "Travel & Turismo",
                "family": "Mecánicas, Crossborder & Travel",
                "concept": "Recurso gráfico Travel Club oficial",
                "rubro": "Travel",
                "rule": "Usar en bloques de beneficios Travel Club y campañas de viaje.",
                "tags": ["travel", "bch", "turismo", "icono", "viajes"],
                "is_featured": False
            })
            manifest.append(info)

# 3. Logos Banco de Chile
bch_logos_dir = os.path.join(BASE_DIR, "bch/logos")
if os.path.exists(bch_logos_dir):
    for fn in sorted(os.listdir(bch_logos_dir)):
        if not fn.startswith("."):
            fp = os.path.join(bch_logos_dir, fn)
            info = get_file_info(fp, f"assets/bch/logos/{fn}", "Banco de Chile", "Logotipos")
            info.update({
                "title": f"Logo Banco de Chile ({fn})",
                "category": "Logotipos",
                "family": "Identidad Corporativa",
                "concept": "Logotipo institucional oficial",
                "rubro": "Branding",
                "rule": "Ubicación en cabecera principal de emails o pie institucional.",
                "tags": ["logo", "branding", "bch", "banco de chile", "wordmark"],
                "is_featured": True
            })
            manifest.append(info)

# 4. BCH Banners & Cards
bch_banners_dir = os.path.join(BASE_DIR, "bch/banners")
if os.path.exists(bch_banners_dir):
    for fn in sorted(os.listdir(bch_banners_dir)):
        if not fn.startswith("."):
            fp = os.path.join(bch_banners_dir, fn)
            info = get_file_info(fp, f"assets/bch/banners/{fn}", "Banco de Chile", "Banners")
            info.update({
                "title": f"Hero Banner ({fn})",
                "category": "Banners Hero",
                "family": "Creatividades de Campaña",
                "concept": "Cabecera visual de alto impacto para email",
                "rubro": "Marketing",
                "rule": "Insertar en la sección superior del email para establecer el tono de la campaña.",
                "tags": ["banner", "hero", "campaña", "bch", "email header"],
                "is_featured": True
            })
            manifest.append(info)

bch_cards_dir = os.path.join(BASE_DIR, "bch/cards")
if os.path.exists(bch_cards_dir):
    for fn in sorted(os.listdir(bch_cards_dir)):
        if not fn.startswith("."):
            fp = os.path.join(bch_cards_dir, fn)
            info = get_file_info(fp, f"assets/bch/cards/{fn}", "Banco de Chile", "Tarjetas")
            info.update({
                "title": f"Tarjeta ({fn})",
                "category": "Tarjetas",
                "family": "Portafolio de Productos",
                "concept": "Render visual de tarjeta de crédito/débito",
                "rubro": "Medios de Pago",
                "rule": "Mostrar como producto protagonista en fichas y correos comerciales.",
                "tags": ["tarjeta", "plastico", "credito", "bch", "visa"],
                "is_featured": True
            })
            manifest.append(info)

# 5. Visa Logos
visa_logos_dir = os.path.join(BASE_DIR, "visa/logos")
if os.path.exists(visa_logos_dir):
    for fn in sorted(os.listdir(visa_logos_dir)):
        if not fn.startswith("."):
            fp = os.path.join(visa_logos_dir, fn)
            info = get_file_info(fp, f"assets/visa/logos/{fn}", "Visa", "Logotipos")
            info.update({
                "title": f"Visa Logo ({fn})",
                "category": "Logotipos",
                "family": "Visa Brand Standards",
                "concept": "Logotipo oficial Visa",
                "rubro": "Branding",
                "rule": "Cumplir estándares oficiales de contraste (fondo claro vs fondo oscuro).",
                "tags": ["visa", "logo", "branding", "wordmark", "vca"],
                "is_featured": True
            })
            manifest.append(info)

# 6. Other Banks & Artefact
other_banks = [
    ("scotiabank", "Scotiabank"),
    ("santander", "Santander"),
    ("itau", "Itaú"),
    ("artefact", "Artefact")
]
for folder, bank_name in other_banks:
    bdir = os.path.join(BASE_DIR, folder)
    if os.path.exists(bdir):
        for fn in sorted(os.listdir(bdir)):
            if not fn.startswith(".") and os.path.isfile(os.path.join(bdir, fn)):
                fp = os.path.join(bdir, fn)
                info = get_file_info(fp, f"assets/{folder}/{fn}", bank_name, "Logotipos")
                info.update({
                    "title": f"{bank_name} - {fn}",
                    "category": "Logotipos",
                    "family": f"Identidad {bank_name}",
                    "concept": f"Recurso oficial de {bank_name}",
                    "rubro": "Branding",
                    "rule": f"Uso para co-branding y piezas específicas de {bank_name}.",
                    "tags": [bank_name.lower(), "logo", "branding", "banco"],
                    "is_featured": False
                })
                manifest.append(info)

os.makedirs(os.path.dirname(MANIFEST_PATH), exist_ok=True)
with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Manifest created successfully with {len(manifest)} assets indexed!")
