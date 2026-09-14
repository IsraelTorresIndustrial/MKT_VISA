# Catálogo Oficial de Íconos Visa (Nova Icons System)
## Librería Vectorial Estandarizada para HTML, Presentaciones Ejecutivas y PPTX

Esta librería centraliza los **333 íconos oficiales** de Visa Product Design System (`@visa/nova-icons-svg`), mapeados con nombres semánticos para facilitar su reutilización en dashboards, slides y piezas de comunicación.

---

## 🚀 Cómo Utilizar la Librería

### 1. En JavaScript / HTML (Recomendado)
```html
<script type="module">
  import { getVisaIcon } from "./assets/visa-icons/visa-icons.js";
  
  // Inyectar ícono de Cross-Border en color Visa Blue (32px)
  const iconHtml = getVisaIcon("crossborder", { size: 32, color: "#1434CB" });
  document.getElementById("icon-container").innerHTML = iconHtml;
</script>
```

### 2. Con Tag `<img />` o SVG Directo
```html
<!-- Desde ruta canónica -->
<img src="./assets/visa-icons/svg/canonical/crossborder.svg" width="24" height="24" alt="Cross-Border" />

<!-- Con Data URL generado por helper -->
<img src="data:image/svg+xml;utf8,..." width="24" height="24" />
```

### 3. Con Clases CSS Utilitarias
```html
<link rel="stylesheet" href="./assets/visa-icons/visa-icons.css">

<div class="visa-icon-badge visa-icon-badge-gold">
  <!-- SVG inyectado con clase visa-icon-md -->
</div>
```

---

## 📂 Mapeo Semántico por Categorías

### 🏷️ AI & Innovation

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`ai`** | `visa/artificial-intelligence-high.svg` | [`svg/canonical/ai.svg`](svg/canonical/ai.svg) | `ai`, `genai`, `llm`, `intelligence` |
| **`ai-alt`** | `visa/artificial-intelligence-alt-high.svg` | [`svg/canonical/ai-alt.svg`](svg/canonical/ai-alt.svg) | `sparkles`, `stars`, `ai-creative` |
| **`artificial-intelligence`** | `visa/artificial-intelligence-high.svg` | [`svg/canonical/artificial-intelligence.svg`](svg/canonical/artificial-intelligence.svg) | `ai`, `deeplearning`, `models` |
| **`automation`** | `visa/code-run-high.svg` | [`svg/canonical/automation.svg`](svg/canonical/automation.svg) | `bot`, `process`, `workflow`, `automation` |
| **`chat-ai`** | `visa/chat-ai-high.svg` | [`svg/canonical/chat-ai.svg`](svg/canonical/chat-ai.svg) | `chatbot`, `assistant`, `agent`, `prompt` |
| **`idea`** | `visa/idea-high.svg` | [`svg/canonical/idea.svg`](svg/canonical/idea.svg) | `lightbulb`, `innovation`, `concept`, `strategy` |
| **`sparkles`** | `visa/artificial-intelligence-alt-high.svg` | [`svg/canonical/sparkles.svg`](svg/canonical/sparkles.svg) | `magic`, `smart`, `ai-boost` |

### 🏷️ Cards & Credentials

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`card`** | `visa/card-generic-high.svg` | [`svg/canonical/card.svg`](svg/canonical/card.svg) | `card`, `credit-card`, `debit-card`, `plastic` |
| **`corporate-card`** | `visa/card-corporate-high.svg` | [`svg/canonical/corporate-card.svg`](svg/canonical/corporate-card.svg) | `corporate`, `b2b-card`, `commercial-card` |
| **`credit-card`** | `visa/card-generic-high.svg` | [`svg/canonical/credit-card.svg`](svg/canonical/credit-card.svg) | `visa-card`, `revolving`, `tc` |
| **`debit-card`** | `visa/card-debit-high.svg` | [`svg/canonical/debit-card.svg`](svg/canonical/debit-card.svg) | `debit`, `checking`, `current-account` |
| **`prepaid-card`** | `visa/card-prepaid-high.svg` | [`svg/canonical/prepaid-card.svg`](svg/canonical/prepaid-card.svg) | `prepaid`, `gift-card`, `virtual` |
| **`scan-card`** | `visa/scan-card-high.svg` | [`svg/canonical/scan-card.svg`](svg/canonical/scan-card.svg) | `nfc`, `camera-scan`, `card-reader` |
| **`token`** | `visa/token-high.svg` | [`svg/canonical/token.svg`](svg/canonical/token.svg) | `tokenization`, `vts`, `security-token`, `digital-credential` |
| **`wallet`** | `visa/wallet-high.svg` | [`svg/canonical/wallet.svg`](svg/canonical/wallet.svg) | `apple-pay`, `google-pay`, `digital-wallet`, `wallet` |

### 🏷️ Cross-Border & Travel

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`airplane`** | `visa/transit-airplane-high.svg` | [`svg/canonical/airplane.svg`](svg/canonical/airplane.svg) | `flight`, `airline`, `airport` |
| **`crossborder`** | `visa/global-high.svg` | [`svg/canonical/crossborder.svg`](svg/canonical/crossborder.svg) | `crossborder`, `international`, `global`, `fx` |
| **`currency-exchange`** | `visa/currency-convert-high.svg` | [`svg/canonical/currency-exchange.svg`](svg/canonical/currency-exchange.svg) | `fx`, `exchange`, `conversion` |
| **`global`** | `visa/global-high.svg` | [`svg/canonical/global.svg`](svg/canonical/global.svg) | `worldwide`, `international`, `network` |
| **`international`** | `visa/check-international-high.svg` | [`svg/canonical/international.svg`](svg/canonical/international.svg) | `foreign`, `passport`, `borders` |
| **`location`** | `visa/map-location-high.svg` | [`svg/canonical/location.svg`](svg/canonical/location.svg) | `map`, `pin`, `geolocation`, `destination` |
| **`travel`** | `visa/transit-airplane-high.svg` | [`svg/canonical/travel.svg`](svg/canonical/travel.svg) | `travel`, `flight`, `tourism`, `airplane` |
| **`travel-alerts`** | `visa/travel-notifications-high.svg` | [`svg/canonical/travel-alerts.svg`](svg/canonical/travel-alerts.svg) | `notification`, `roaming`, `abroad` |

### 🏷️ Customer & Engagement

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`check`** | `visa/check-high.svg` | [`svg/canonical/check.svg`](svg/canonical/check.svg) | `done`, `verified`, `active`, `approved` |
| **`checkmark`** | `visa/checkmark-high.svg` | [`svg/canonical/checkmark.svg`](svg/canonical/checkmark.svg) | `success`, `completed`, `approved` |
| **`customer`** | `visa/account-high.svg` | [`svg/canonical/customer.svg`](svg/canonical/customer.svg) | `client`, `user`, `consumer`, `account-holder` |
| **`favorite`** | `visa/favorite-star-fill-high.svg` | [`svg/canonical/favorite.svg`](svg/canonical/favorite.svg) | `star`, `top-of-wallet`, `favorite`, `preferred` |
| **`gift`** | `visa/gift-high.svg` | [`svg/canonical/gift.svg`](svg/canonical/gift.svg) | `cashback`, `perk`, `benefit`, `promotion` |
| **`help`** | `visa/help-high.svg` | [`svg/canonical/help.svg`](svg/canonical/help.svg) | `faq`, `guide`, `documentation` |
| **`loyalty`** | `visa/bonus-points-high.svg` | [`svg/canonical/loyalty.svg`](svg/canonical/loyalty.svg) | `loyalty-program`, `rewards`, `points`, `fidelizacion` |
| **`settings`** | `visa/settings-high.svg` | [`svg/canonical/settings.svg`](svg/canonical/settings.svg) | `configuration`, `preferences`, `rules` |
| **`star`** | `visa/favorite-star-fill-high.svg` | [`svg/canonical/star.svg`](svg/canonical/star.svg) | `rating`, `highlight`, `vip` |
| **`support`** | `visa/customer-support-high.svg` | [`svg/canonical/support.svg`](svg/canonical/support.svg) | `helpdesk`, `contact-center`, `assistance` |
| **`user`** | `visa/account-high.svg` | [`svg/canonical/user.svg`](svg/canonical/user.svg) | `profile`, `member`, `cardholder` |

### 🏷️ Dashboard & Reporting

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`calendar`** | `visa/calendar-high.svg` | [`svg/canonical/calendar.svg`](svg/canonical/calendar.svg) | `date`, `month`, `planning`, `events` |
| **`dashboard`** | `visa/dashboard-high.svg` | [`svg/canonical/dashboard.svg`](svg/canonical/dashboard.svg) | `dashboard`, `metrics`, `overview`, `cockpit` |
| **`dashboard-ready`** | `visa/dashboard-ready-high.svg` | [`svg/canonical/dashboard-ready.svg`](svg/canonical/dashboard-ready.svg) | `ready`, `live`, `active-dashboard` |
| **`portfolio`** | `visa/portfolio-high.svg` | [`svg/canonical/portfolio.svg`](svg/canonical/portfolio.svg) | `portfolio`, `briefcase`, `assets`, `accounts` |
| **`report`** | `visa/report-high.svg` | [`svg/canonical/report.svg`](svg/canonical/report.svg) | `report`, `document`, `deck`, `summary` |
| **`schedule`** | `visa/schedule-high.svg` | [`svg/canonical/schedule.svg`](svg/canonical/schedule.svg) | `schedule`, `roadmap`, `timeline`, `calendar` |
| **`time`** | `visa/time-high.svg` | [`svg/canonical/time.svg`](svg/canonical/time.svg) | `clock`, `duration`, `hours`, `latency` |

### 🏷️ Data & Analytics

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`analytics`** | `visa/analytics-high.svg` | [`svg/canonical/analytics.svg`](svg/canonical/analytics.svg) | `analytics`, `insights`, `bi`, `reporting` |
| **`data`** | `visa/data-high.svg` | [`svg/canonical/data.svg`](svg/canonical/data.svg) | `data`, `database`, `analytics`, `stats` |
| **`data-alt`** | `visa/data-alt-high.svg` | [`svg/canonical/data-alt.svg`](svg/canonical/data-alt.svg) | `data`, `chart`, `metrics` |
| **`database`** | `visa/data-high.svg` | [`svg/canonical/database.svg`](svg/canonical/database.svg) | `db`, `lakehouse`, `warehouse`, `storage` |
| **`grid`** | `visa/view-grid-high.svg` | [`svg/canonical/grid.svg`](svg/canonical/grid.svg) | `matrix`, `layout`, `grid` |
| **`statistics`** | `visa/statistics-high.svg` | [`svg/canonical/statistics.svg`](svg/canonical/statistics.svg) | `statistics`, `distribution`, `analysis` |
| **`table`** | `visa/table-high.svg` | [`svg/canonical/table.svg`](svg/canonical/table.svg) | `table`, `grid`, `spreadsheet`, `records` |

### 🏷️ E-Commerce & Commercial

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`cart`** | `visa/cart-high.svg` | [`svg/canonical/cart.svg`](svg/canonical/cart.svg) | `cart`, `shopping-cart`, `basket` |
| **`commercial`** | `visa/company-high.svg` | [`svg/canonical/commercial.svg`](svg/canonical/commercial.svg) | `enterprise`, `corporate`, `b2b`, `commercial` |
| **`ecommerce`** | `visa/cart-high.svg` | [`svg/canonical/ecommerce.svg`](svg/canonical/ecommerce.svg) | `ecommerce`, `shopping`, `retail`, `online-store` |
| **`marketplace`** | `visa/marketplace-high.svg` | [`svg/canonical/marketplace.svg`](svg/canonical/marketplace.svg) | `marketplace`, `platform`, `mall` |
| **`merchant`** | `visa/merchant-high.svg` | [`svg/canonical/merchant.svg`](svg/canonical/merchant.svg) | `merchant`, `seller`, `vendor`, `retailer` |
| **`pos`** | `visa/pos-high.svg` | [`svg/canonical/pos.svg`](svg/canonical/pos.svg) | `terminal`, `point-of-sale`, `pos`, `mpos` |
| **`shipping`** | `visa/shipping-high.svg` | [`svg/canonical/shipping.svg`](svg/canonical/shipping.svg) | `delivery`, `logistics`, `shipping`, `package` |
| **`shop`** | `visa/store-open-high.svg` | [`svg/canonical/shop.svg`](svg/canonical/shop.svg) | `store`, `merchant`, `physical-store`, `retail` |
| **`store`** | `visa/store-open-high.svg` | [`svg/canonical/store.svg`](svg/canonical/store.svg) | `shop`, `retail`, `storefront` |

### 🏷️ Fraud & Security

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`biometric`** | `visa/auth-face-high.svg` | [`svg/canonical/biometric.svg`](svg/canonical/biometric.svg) | `face-id`, `facial-auth`, `identity` |
| **`device-secure`** | `visa/device-secure-high.svg` | [`svg/canonical/device-secure.svg`](svg/canonical/device-secure.svg) | `secure-device`, `hardware-token`, `pos-secure` |
| **`fingerprint`** | `visa/fingerprint-high.svg` | [`svg/canonical/fingerprint.svg`](svg/canonical/fingerprint.svg) | `biometrics`, `passkey`, `touch-id` |
| **`firewall`** | `visa/security-firewall-high.svg` | [`svg/canonical/firewall.svg`](svg/canonical/firewall.svg) | `firewall`, `cyber-defense`, `perimeter` |
| **`fraud`** | `visa/fraud-high.svg` | [`svg/canonical/fraud.svg`](svg/canonical/fraud.svg) | `fraud`, `risk`, `dispute`, `chargeback` |
| **`lock`** | `visa/security-lock-high.svg` | [`svg/canonical/lock.svg`](svg/canonical/lock.svg) | `encryption`, `privacy`, `password`, `lock` |
| **`security`** | `visa/security-high.svg` | [`svg/canonical/security.svg`](svg/canonical/security.svg) | `shield`, `protection`, `safe`, `secure` |
| **`shield`** | `visa/security-protection-high.svg` | [`svg/canonical/shield.svg`](svg/canonical/shield.svg) | `defense`, `safe`, `compliance` |

### 🏷️ Growth & Performance

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`bonus`** | `visa/bonus-points-high.svg` | [`svg/canonical/bonus.svg`](svg/canonical/bonus.svg) | `points`, `bonus`, `points`, `miles` |
| **`goal`** | `visa/goal-high.svg` | [`svg/canonical/goal.svg`](svg/canonical/goal.svg) | `goal`, `target`, `objective`, `kpi` |
| **`growth`** | `visa/trending-high.svg` | [`svg/canonical/growth.svg`](svg/canonical/growth.svg) | `growth`, `increase`, `performance`, `trend` |
| **`reward`** | `visa/reward-high.svg` | [`svg/canonical/reward.svg`](svg/canonical/reward.svg) | `reward`, `loyalty`, `incentive`, `bonus` |
| **`speedometer`** | `visa/speedometer-high.svg` | [`svg/canonical/speedometer.svg`](svg/canonical/speedometer.svg) | `speed`, `efficiency`, `performance`, `sla` |
| **`trending`** | `visa/trending-high.svg` | [`svg/canonical/trending.svg`](svg/canonical/trending.svg) | `trend`, `trajectory`, `uptrend` |
| **`trophy`** | `visa/trophy-high.svg` | [`svg/canonical/trophy.svg`](svg/canonical/trophy.svg) | `winner`, `success`, `achievement`, `award` |

### 🏷️ Issuer & Banking

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`acquirer`** | `visa/acquirer-high.svg` | [`svg/canonical/acquirer.svg`](svg/canonical/acquirer.svg) | `acquirer`, `processing`, `merchant-bank` |
| **`atm`** | `visa/atm-high.svg` | [`svg/canonical/atm.svg`](svg/canonical/atm.svg) | `atm`, `cash-machine`, `dispenser` |
| **`balance`** | `visa/balance-high.svg` | [`svg/canonical/balance.svg`](svg/canonical/balance.svg) | `balance`, `ledger`, `funds` |
| **`bank`** | `visa/issuer-high.svg` | [`svg/canonical/bank.svg`](svg/canonical/bank.svg) | `branch`, `banking`, `finance` |
| **`government`** | `visa/government-high.svg` | [`svg/canonical/government.svg`](svg/canonical/government.svg) | `public-sector`, `central-bank`, `regulation` |
| **`issuer`** | `visa/issuer-high.svg` | [`svg/canonical/issuer.svg`](svg/canonical/issuer.svg) | `bank`, `issuer`, `financial-institution`, `banco` |
| **`savings`** | `visa/savings-account-high.svg` | [`svg/canonical/savings.svg`](svg/canonical/savings.svg) | `savings`, `deposit`, `interest` |

### 🏷️ Launch & Strategy

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`fast`** | `visa/fast-high.svg` | [`svg/canonical/fast.svg`](svg/canonical/fast.svg) | `speed`, `quick`, `acceleration`, `express` |
| **`flag`** | `visa/flag-high.svg` | [`svg/canonical/flag.svg`](svg/canonical/flag.svg) | `milestone`, `flag`, `objective`, `checkpoint` |
| **`launch`** | `visa/launch-high.svg` | [`svg/canonical/launch.svg`](svg/canonical/launch.svg) | `rocket`, `launch`, `go-live`, `release` |
| **`roadmap`** | `visa/roadsign-high.svg` | [`svg/canonical/roadmap.svg`](svg/canonical/roadmap.svg) | `path`, `direction`, `strategy`, `roadmap` |

### 🏷️ Partnership & Ecosystem

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`connections`** | `visa/connections-high.svg` | [`svg/canonical/connections.svg`](svg/canonical/connections.svg) | `network`, `nodes`, `integration`, `ecosystem` |
| **`developer`** | `visa/developer-high.svg` | [`svg/canonical/developer.svg`](svg/canonical/developer.svg) | `engineering`, `coder`, `api`, `tech` |
| **`handshake`** | `visa/handshake-high.svg` | [`svg/canonical/handshake.svg`](svg/canonical/handshake.svg) | `agreement`, `collaboration`, `co-branding` |
| **`network`** | `visa/connect-high.svg` | [`svg/canonical/network.svg`](svg/canonical/network.svg) | `links`, `api`, `connectors` |
| **`partnership`** | `visa/handshake-high.svg` | [`svg/canonical/partnership.svg`](svg/canonical/partnership.svg) | `handshake`, `partner`, `alliance`, `deal` |
| **`team`** | `visa/account-add-high.svg` | [`svg/canonical/team.svg`](svg/canonical/team.svg) | `team`, `squad`, `squad-members`, `people` |

### 🏷️ Payments & Money Movement

| Alias Semántico | Función / Uso | Ruta SVG Canónica | Tags Relacionados |
| :--- | :--- | :--- | :--- |
| **`bill`** | `visa/bill-high.svg` | [`svg/canonical/bill.svg`](svg/canonical/bill.svg) | `utility`, `bill-pay`, `invoice` |
| **`contactless`** | `visa/tap-high.svg` | [`svg/canonical/contactless.svg`](svg/canonical/contactless.svg) | `tap`, `rfid`, `contactless` |
| **`currency`** | `visa/currency-high.svg` | [`svg/canonical/currency.svg`](svg/canonical/currency.svg) | `money`, `cash`, `bills`, `coins` |
| **`euro`** | `visa/currency-euro-high.svg` | [`svg/canonical/euro.svg`](svg/canonical/euro.svg) | `euro`, `eur`, `currency` |
| **`money-add`** | `visa/money-add-high.svg` | [`svg/canonical/money-add.svg`](svg/canonical/money-add.svg) | `topup`, `cash-in`, `reload` |
| **`money-request`** | `visa/money-request-high.svg` | [`svg/canonical/money-request.svg`](svg/canonical/money-request.svg) | `request-to-pay`, `billing`, `collection` |
| **`money-send`** | `visa/money-send-high.svg` | [`svg/canonical/money-send.svg`](svg/canonical/money-send.svg) | `transfer`, `p2p`, `remittance`, `visa-direct` |
| **`payments`** | `visa/transactions-high.svg` | [`svg/canonical/payments.svg`](svg/canonical/payments.svg) | `payments`, `transactions`, `checkout`, `money-movement` |
| **`receipt`** | `visa/receipt-high.svg` | [`svg/canonical/receipt.svg`](svg/canonical/receipt.svg) | `ticket`, `receipt`, `voucher`, `invoice` |
| **`tap`** | `visa/tap-high.svg` | [`svg/canonical/tap.svg`](svg/canonical/tap.svg) | `tap-to-pay`, `contactless`, `nfc`, `tap-to-phone` |
| **`transactions`** | `visa/transactions-high.svg` | [`svg/canonical/transactions.svg`](svg/canonical/transactions.svg) | `volume`, `trx`, `transacciones` |
| **`usd`** | `visa/currency-usd-high.svg` | [`svg/canonical/usd.svg`](svg/canonical/usd.svg) | `dollar`, `usd`, `money`, `pricing` |
