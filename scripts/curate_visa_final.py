#!/usr/bin/env python3
"""
Curación final de iconos SVG de Visa.
Mantiene solo los high.svg realmente útiles para sistemas de pagos,
marketing financiero, UI y flujos de cliente.
"""

import pathlib, shutil, json, os, re

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
SVG_DIR = REPO_ROOT / "assets" / "visa" / "icons" / "assets" / "visa-icons" / "svg" / "visa"
BACKUP_DIR = REPO_ROOT / "assets" / "visa" / "icons" / "backup_pre_final"
MANIFEST_FILE = REPO_ROOT / "src" / "data" / "assets_data.js"

# ──────────────────────────────────────────────────────────────────
# Lista curada manualmente: solo iconos que aportan valor real
# Categorías: pagos, tarjetas, seguridad, identidad, viajes,
#             transacciones, comercios, UI esencial, alertas
# ──────────────────────────────────────────────────────────────────
KEEP = {
    # ── Tarjetas & Pagos ──
    "card-generic-high.svg",
    "card-debit-high.svg",
    "card-corporate-high.svg",
    "card-prepaid-high.svg",
    "card-number-high.svg",
    "card-manage-high.svg",
    "card-manage-alt-high.svg",
    "card-off-high.svg",
    "card-suspend-high.svg",
    "card-verify-high.svg",
    "scan-card-high.svg",
    "pos-high.svg",
    "pos-alt-high.svg",
    "qr-high.svg",
    "tap-high.svg",
    "contactless-high.svg",

    # ── Dinero & Transacciones ──
    "money-add-high.svg",
    "money-send-high.svg",
    "money-request-high.svg",
    "money-withdrawn-high.svg",
    "transactions-high.svg",
    "transactions-new-high.svg",
    "receipt-high.svg",
    "bill-high.svg",
    "bill-alt-high.svg",
    "balance-high.svg",
    "split-high.svg",
    "transfer-high.svg",
    "mobile-transfer-high.svg",
    "return-high.svg",
    "refund-high.svg",
    "on-hold-high.svg",
    "fast-high.svg",

    # ── Wallet & Cuenta ──
    "wallet-high.svg",
    "wallet-default-high.svg",
    "savings-account-high.svg",
    "account-high.svg",
    "account-add-high.svg",
    "account-remove-high.svg",
    "account-favorite-high.svg",
    "account-lock-high.svg",
    "atm-high.svg",

    # ── Divisa & Moneda ──
    "currency-high.svg",
    "currency-usd-high.svg",
    "currency-euro-high.svg",
    "currency-pound-high.svg",
    "currency-yen-high.svg",
    "currency-convert-high.svg",
    "currency-convert-alt-high.svg",

    # ── Seguridad & Autenticación ──
    "security-high.svg",
    "security-lock-high.svg",
    "security-unlock-high.svg",
    "security-protection-high.svg",
    "security-firewall-high.svg",
    "fingerprint-high.svg",
    "auth-face-high.svg",
    "auth-code-high.svg",
    "auth-voice-high.svg",
    "auth-reauthorize-high.svg",
    "device-secure-high.svg",
    "key-high.svg",
    "key-change-high.svg",
    "password-hide-high.svg",
    "password-show-high.svg",
    "id-number-high.svg",
    "token-high.svg",
    "fraud-high.svg",
    "sign-in-high.svg",
    "sign-out-high.svg",
    "signature-high.svg",

    # ── Viajes & Transporte ──
    "transit-airplane-high.svg",
    "transit-car-high.svg",
    "transit-train-high.svg",
    "travel-notifications-high.svg",
    "map-high.svg",
    "map-location-high.svg",
    "map-location-current-high.svg",
    "map-directions-high.svg",
    "global-high.svg",
    "roadsign-high.svg",
    "check-international-high.svg",

    # ── Comercio & Merchant ──
    "merchant-high.svg",
    "store-open-high.svg",
    "store-closed-high.svg",
    "cart-high.svg",
    "marketplace-high.svg",
    "offers-high.svg",
    "offers-deal-high.svg",
    "bonus-points-high.svg",
    "reward-high.svg",
    "gift-high.svg",
    "shipping-high.svg",
    "issuer-high.svg",
    "acquirer-high.svg",

    # ── Reportes & Analytics ──
    "analytics-high.svg",
    "report-high.svg",
    "statistics-high.svg",
    "trending-high.svg",
    "dashboard-high.svg",
    "data-high.svg",

    # ── Notificaciones & Comunicación ──
    "notifications-high.svg",
    "alert-high.svg",
    "warning-high.svg",
    "error-high.svg",
    "success-high.svg",
    "information-high.svg",
    "help-high.svg",
    "question-high.svg",
    "chat-high.svg",
    "message-high.svg",
    "email-high.svg",
    "phone-high.svg",
    "customer-support-high.svg",
    "support-ticket-high.svg",

    # ── Identidad & Perfil ──
    "contact-high.svg",
    "company-high.svg",
    "government-high.svg",
    "handshake-high.svg",

    # ── Dispositivos ──
    "device-mobile-high.svg",
    "device-laptop-high.svg",
    "device-wearable-high.svg",
    "mobile-success-high.svg",

    # ── UI Esencial ──
    "search-high.svg",
    "filter-high.svg",
    "settings-high.svg",
    "close-high.svg",
    "add-high.svg",
    "delete-high.svg",
    "edit-high.svg",
    "save-high.svg",
    "share-high.svg",
    "copy-high.svg",
    "download-high.svg",
    "file-download-high.svg",
    "file-upload-high.svg",
    "export-high.svg",
    "send-high.svg",
    "refresh-high.svg",
    "history-high.svg",
    "calendar-high.svg",
    "schedule-high.svg",
    "time-high.svg",
    "home-high.svg",
    "menu-high.svg",
    "arrow-back-high.svg",
    "arrow-forward-high.svg",
    "arrow-up-high.svg",
    "arrow-down-high.svg",
    "chevron-left-high.svg",
    "chevron-right-high.svg",
    "chevron-up-high.svg",
    "chevron-down-high.svg",
    "checkmark-high.svg",
    "check-high.svg",
    "sort-ascending-high.svg",
    "sort-descending-high.svg",
    "view-grid-high.svg",
    "view-list-high.svg",
    "zoom-in-high.svg",
    "zoom-out-high.svg",
}

def main():
    # Respaldar estado actual
    if BACKUP_DIR.exists():
        shutil.rmtree(BACKUP_DIR)
    shutil.copytree(SVG_DIR, BACKUP_DIR)
    print(f"✅ Backup creado en {BACKUP_DIR.relative_to(REPO_ROOT)}")

    kept = []
    removed = []

    for path in sorted(SVG_DIR.iterdir()):
        if not path.is_file() or path.suffix.lower() != ".svg":
            continue
        name = path.name
        if name in KEEP:
            kept.append(path)
        else:
            path.unlink()
            removed.append(name)

    print(f"\n🗑️  Eliminados: {len(removed)} iconos")
    print(f"✅  Conservados: {len(kept)} iconos")

    # Regenerar manifiesto - leer el actual, borrar entradas Visa, añadir nuevas
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    start_idx = content.find("[")
    end_idx = content.rfind("]")
    prefix = content[:start_idx]
    suffix = content[end_idx+1:]

    data = json.loads(content[start_idx:end_idx+1])
    # Eliminar todas las entradas Visa SVG existentes
    data = [item for item in data if not (item.get("bank") == "Visa" and item.get("format") == "SVG")]

    CDN_BASE = "https://mkt-visa.vercel.app"

    for path in sorted(kept):
        name = path.name
        stem = path.stem  # e.g., card-generic-high
        # Clean title: remove -high suffix, replace - with space, title case
        title = stem.replace("-high", "").replace("-", " ").title()
        rel = path.relative_to(REPO_ROOT).as_posix()
        cdn_url = f"{CDN_BASE}/{rel}"
        entry = {
            "filename": name,
            "rel_path": rel,
            "cdn_url": cdn_url,
            "bank": "Visa",
            "format": "SVG",
            "title": title,
            "category": categorize(stem),
            "family": "Visa Icon Set",
            "concept": f"Icono vectorial: {title}",
            "rubro": "Iconografía",
            "rule": f"Icono oficial Visa {title} en formato SVG escalable.",
            "tags": tags_for(stem),
            "is_featured": False
        }
        data.append(entry)

    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        f.write(prefix)
        f.write("\nwindow.BANK_ASSETS = ")
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write(suffix)

    print(f"\n📄 Manifiesto actualizado con {len(kept)} entradas Visa SVG")

def categorize(stem: str) -> str:
    s = stem.lower()
    if any(k in s for k in ["card", "pos", "qr", "tap", "scan"]):
        return "Pagos"
    if any(k in s for k in ["money", "transaction", "balance", "bill", "receipt", "split", "transfer", "return"]):
        return "Transacciones"
    if any(k in s for k in ["wallet", "account", "saving", "atm"]):
        return "Cuenta y Wallet"
    if any(k in s for k in ["currency", "convert"]):
        return "Divisas"
    if any(k in s for k in ["security", "fingerprint", "auth", "key", "password", "fraud", "sign", "token", "device-secure"]):
        return "Seguridad"
    if any(k in s for k in ["airplane", "transit", "travel", "map", "global", "roadsign", "international"]):
        return "Viajes"
    if any(k in s for k in ["merchant", "store", "cart", "marketplace", "offer", "bonus", "reward", "gift", "ship", "issuer", "acquirer"]):
        return "Comercio"
    if any(k in s for k in ["analytics", "report", "statistic", "trending", "dashboard", "data"]):
        return "Analítica"
    if any(k in s for k in ["notification", "alert", "warning", "error", "success", "info", "help", "question", "chat", "message", "email", "phone", "support", "customer"]):
        return "Comunicación"
    if any(k in s for k in ["contact", "company", "government", "handshake"]):
        return "Identidad"
    if any(k in s for k in ["mobile", "device", "laptop", "wearable"]):
        return "Dispositivos"
    return "UI"

def tags_for(stem: str) -> list:
    base = stem.replace("-high", "").replace("-", "_")
    t = ["visa", "svg", "icon", base]
    cat = categorize(stem).lower()
    if cat not in t:
        t.append(cat)
    return t


if __name__ == "__main__":
    main()
