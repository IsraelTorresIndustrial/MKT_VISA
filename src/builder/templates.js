/**
 * MKT_VISA Email Templates & Presets Library
 * Tested HTML email layouts compliant with Outlook, Gmail, Apple Mail & Mobile
 */

window.EMAIL_PRESETS = {
  "bch_bienvenida": {
    "id": "bch_bienvenida",
    "bank": "Banco de Chile",
    "name": "Bienvenida y Activación Nueva TC (Travel Infinite)",
    "description": "Plantilla oficial de onboarding para nuevas tarjetas de crédito con foco en acumulación de Dólares-Premio, salones VIP y traslados.",
    "theme": {
      "primaryColor": "#002464",
      "accentColor": "#0032A0",
      "bgColor": "#F2F4F8",
      "cardBg": "#F5F7FA",
      "borderColor": "#D9E3F2",
      "fontFamily": "Arial, Helvetica, sans-serif"
    },
    "heroBanner": "",
    "clientName": "[Nombre]",
    "h1Text": "Un plan del Chile puede darte más.<br>Conoce una propuesta pensada para ti.",
    "productSubtitle": "TU NUEVO PLAN",
    "productTitle": "Plan Travel Infinite",
    "productDescription": "Más beneficios para tus compras y una experiencia Travel más completa.",
    "cardImage": "assets/bch/logos/banco_de_chile.png",
    "benefits": [
      {
        "icon": "assets/bch/icons/10_dolares_premio.png",
        "badge": "1,2%",
        "title": "Dólares-Premio",
        "description": "de acumulación comunicada para el plan en cada compra."
      },
      {
        "icon": "assets/bch/icons/29_lounge_salon_vip.png",
        "badge": "12",
        "title": "Accesos Salones VIP",
        "description": "al año en salas Pacific Club y aeropuertos preferentes."
      },
      {
        "icon": "assets/bch/icons/30_traslado_aeropuerto.png",
        "badge": "4",
        "title": "Traslados Aeropuerto",
        "description": "al año para iniciar tu viaje con total comodidad."
      }
    ],
    "secondaryText": "<strong>Además:</strong> hasta 50% en restaurantes seleccionados, 2x1 en cines y catálogo completo de canjes en Travel Duty.",
    "ctaText": "Conoce todos tus beneficios",
    "ctaUrl": "https://portales.bancochile.cl/personas/tarjetas-de-credito",
    "legales": "(1) Dólares-Premio: acumulación sujeta a condiciones del programa Travel Club. (2) Salones VIP y traslados: beneficios exclusivos para titulares vigentes del Plan Travel Infinite. (3) Por seguridad, Banco de Chile nunca te solicitará claves personales por correo electrónico."
  },

  "bch_inactividad_m1": {
    "id": "bch_inactividad_m1",
    "bank": "Banco de Chile",
    "name": "Reactivación M1: Descuento + CSI + Dólares-Premio",
    "description": "Campaña de activación temprana con triple incentivo: % OFF en primera compra, Cuotas Sin Interés y bono de Dólares-Premio.",
    "theme": {
      "primaryColor": "#002464",
      "accentColor": "#0032A0",
      "bgColor": "#F2F4F8",
      "cardBg": "#F5F7FA",
      "borderColor": "#D9E3F2",
      "fontFamily": "Arial, Helvetica, sans-serif"
    },
    "heroBanner": "",
    "clientName": "[Nombre]",
    "h1Text": "Tienes 30% de descuento en tu primera compra del mes.<br>Úsalo en todos los comercios.",
    "productSubtitle": "BENEFICIO EXCLUSIVO",
    "productTitle": "Vuelve a usar tu Tarjeta del Chile",
    "productDescription": "Aprovecha tus beneficios y acumula recompensas desde tu próxima compra.",
    "cardImage": "assets/bch/logos/banco_de_chile.png",
    "benefits": [
      {
        "icon": "assets/bch/icons/24_descuento.png",
        "badge": "30% OFF",
        "title": "Descuento en 1ª Compra",
        "description": "Válido en todos los comercios presenciales y online con tope de $20.000."
      },
      {
        "icon": "assets/bch/icons/25_cuotas_sin_interes_csi.png",
        "badge": "3 a 12",
        "title": "Cuotas Sin Interés",
        "description": "En rubros seleccionados y compras del mes sin costo de financiamiento."
      },
      {
        "icon": "assets/bch/icons/09_cashback.png",
        "badge": "$10.000",
        "title": "Dólares-Premio Extra",
        "description": "Abonados directamente al cumplir tu meta transaccional comunicada."
      }
    ],
    "secondaryText": "Revisa más alternativas de canje en <strong>duty.travel.cl</strong> y consulta tus compras en la App Mi Banco.",
    "ctaText": "Revisar condiciones en App Mi Banco",
    "ctaUrl": "https://portales.bancochile.cl",
    "legales": "(1) Descuento válido para compras realizadas dentro del mes calendario. (2) Cuotas sin interés aplican a compras en pesos en comercios adheridos. (3) Este correo es estrictamente informativo y no incluye enlaces directos de autenticación bancaria."
  },

  "visa_crossborder": {
    "id": "visa_crossborder",
    "bank": "Visa",
    "name": "Visa Advisory: Campaña Cross-Border & Viajes",
    "description": "Pieza internacional VCA para incentivo de uso fuera de Chile y ecommerce internacional con beneficios exclusivos.",
    "theme": {
      "primaryColor": "#021E4C",
      "accentColor": "#1434CB",
      "bgColor": "#F4F6FE",
      "cardBg": "#FFFFFF",
      "borderColor": "#C9D6F5",
      "fontFamily": "'Visa Dialect', Segoe UI, Arial, sans-serif"
    },
    "heroBanner": "",
    "clientName": "[Nombre del Titular]",
    "h1Text": "Tu Tarjeta Visa te acompaña en cada destino.<br>Viaja y compra en el extranjero sin preocupaciones.",
    "productSubtitle": "EXPERIENCIA INTERNACIONAL",
    "productTitle": "Visa Cross-Border Advantage",
    "productDescription": "Seguridad global, aceptación universal en más de 200 países y protección en cada transacción.",
    "cardImage": "assets/visa/logos/visa_blue.png",
    "benefits": [
      {
        "icon": "assets/bch/icons/27_compra_internacional_crossborder.png",
        "badge": "GLOBAL",
        "title": "Compras Internacionales",
        "description": "Paga en moneda extranjera con el mejor tipo de cambio interbancario."
      },
      {
        "icon": "assets/bch/icons/28_ecommerce_internacional.png",
        "badge": "ONLINE",
        "title": "Ecommerce Internacional",
        "description": "Seguridad tokenizada para tus compras en Amazon, AliExpress y streaming."
      },
      {
        "icon": "assets/bch/icons/21_contactless.png",
        "badge": "NFC",
        "title": "Pago Sin Contacto",
        "description": "Acerca tu tarjeta o dispositivo móvil en terminales POS de todo el mundo."
      }
    ],
    "secondaryText": "Con el respaldo y monitoreo antifraude continuo las 24 horas de la red VisaNet.",
    "ctaText": "Conoce los beneficios de tu Tarjeta Visa",
    "ctaUrl": "https://www.visa.cl",
    "legales": "Los beneficios de asistencia médica y seguros de viaje aplican al pagar la totalidad del pasaje con tu tarjeta Visa válida. Consulta términos y coberturas en visa.cl/portal-beneficios."
  }
};

/**
 * Compiles a structured configuration into a bulletproof email HTML string
 */
window.generateEmailHtml = function(config, options = {}) {
  const isRelative = options.relativePaths !== false;
  const baseUrl = options.baseUrl || "";

  const resolvePath = (path) => {
    if (!path) return "";
    if (path.startsWith("http://") || path.startsWith("https://") || path.startsWith("data:")) {
      return path;
    }
    if (isRelative) {
      // In ZIP relative mode, assets become images/filename.ext
      const parts = path.split("/");
      const filename = parts[parts.length - 1];
      return options.zipMode ? `images/${filename}` : path;
    }
    return baseUrl ? `${baseUrl.replace(/\/$/, '')}/${path.replace(/^\//, '')}` : path;
  };

  const theme = config.theme || {
    primaryColor: "#002464",
    accentColor: "#0032A0",
    bgColor: "#F2F4F8",
    cardBg: "#F5F7FA",
    borderColor: "#D9E3F2",
    fontFamily: "Arial, Helvetica, sans-serif"
  };

  const benefitsHtml = (config.benefits || []).map((b, idx) => {
    const isLast = idx === (config.benefits.length - 1);
    const colWidth = Math.floor(600 / config.benefits.length) - (config.benefits.length > 1 ? 12 : 0);
    return `
      <td class="stack" width="${colWidth}" valign="top" align="center" style="width:${colWidth}px;background-color:${theme.cardBg};border:1px solid ${theme.borderColor};border-radius:8px;text-align:center;padding:18px 14px;">
        <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0">
          <tr>
            <td align="center" style="padding-bottom:12px;">
              <img src="${resolvePath(b.icon)}" width="64" height="64" alt="${b.title}" border="0" style="display:block;width:64px;height:64px;margin:0 auto;object-fit:contain;">
            </td>
          </tr>
          ${b.badge ? `
          <tr>
            <td align="center">
              <span style="display:inline-block;font-size:22px;line-height:26px;font-weight:bold;color:${theme.accentColor};">${b.badge}</span>
            </td>
          </tr>` : ''}
          <tr>
            <td align="center" style="padding-top:4px;">
              <p style="margin:0;font-size:15px;line-height:20px;font-weight:bold;color:${theme.primaryColor};font-family:${theme.fontFamily};">${b.title}</p>
              <p style="margin:6px 0 0 0;font-size:12px;line-height:17px;color:#44516A;font-family:${theme.fontFamily};">${b.description}</p>
            </td>
          </tr>
        </table>
      </td>
      ${!isLast ? '<td class="gap" width="16" style="width:16px;font-size:0;line-height:0;">&nbsp;</td>' : ''}
    `;
  }).join('');

  return `<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="x-apple-disable-message-reformatting">
  <meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
  <title>${config.productTitle || 'Comunicaciones Oficiales'}</title>
  <style>
    body { margin:0; padding:0; background-color:${theme.bgColor}; }
    table { border-collapse:collapse; mso-table-lspace:0pt; mso-table-rspace:0pt; }
    td, p, a, h1, h2 { font-family:${theme.fontFamily}; }
    @media only screen and (max-width:720px) {
      .wrap { width:100%!important; max-width:100%!important; min-width:100%!important; }
      .hero-img { width:100%!important; max-width:100%!important; height:auto!important; }
      .pad { padding-left:20px!important; padding-right:20px!important; }
      .stack { display:block!important; width:100%!important; max-width:100%!important; margin-bottom:14px!important; }
      .gap { display:none!important; }
      .h1-title { font-size:24px!important; line-height:30px!important; }
      .btn-cta { width:100%!important; display:block!important; text-align:center!important; }
    }
  </style>
</head>
<body style="margin:0;padding:0;background-color:${theme.bgColor};">
  <table role="presentation" width="100%" cellspacing="0" cellpadding="0" border="0" style="width:100%;margin:0;padding:20px 0;background-color:${theme.bgColor};">
    <tr>
      <td align="center">
        <!-- Main Email Container (700px) -->
        <table role="presentation" class="wrap" width="700" cellspacing="0" cellpadding="0" border="0" align="center" style="width:700px;max-width:700px;margin:0 auto;background-color:#FFFFFF;border-radius:12px;overflow:hidden;box-shadow:0 4px 16px rgba(0,36,100,0.06);">
          
          ${config.heroBanner ? `
          <!-- HERO BANNER -->
          <tr>
            <td align="center" valign="top" style="padding:0;margin:0;line-height:0;">
              <img class="hero-img" src="${resolvePath(config.heroBanner)}" width="700" alt="Campaña" border="0" style="display:block;width:700px;max-width:700px;height:auto;border:0;">
            </td>
          </tr>` : ''}

          <!-- SALUDO PERSONALIZADO -->
          <tr>
            <td class="pad" align="left" style="padding:22px 50px 14px 50px;color:${theme.primaryColor};">
              <p style="margin:0;font-size:17px;line-height:24px;font-weight:bold;color:${theme.primaryColor};">${config.clientName || '[Nombre]'}</p>
            </td>
          </tr>

          <!-- HEADER PRINCIPAL -->
          <tr>
            <td class="pad" align="center" bgcolor="${theme.primaryColor}" style="padding:28px 40px;background-color:${theme.primaryColor};text-align:center;">
              <h1 class="h1-title" style="margin:0;font-size:28px;line-height:36px;font-weight:bold;color:#FFFFFF;text-align:center;">
                ${config.h1Text}
              </h1>
            </td>
          </tr>

          <!-- PRODUCT PROTAGONIST SECTION -->
          <tr>
            <td class="pad" align="center" style="padding:32px 50px 12px 50px;text-align:center;">
              <p style="margin:0 0 6px 0;font-size:13px;line-height:18px;font-weight:bold;letter-spacing:1px;color:${theme.accentColor};text-transform:uppercase;">
                ${config.productSubtitle || 'PROPUESTA EXCLUSIVA'}
              </p>
              <h2 style="margin:0 0 10px 0;font-size:26px;line-height:32px;font-weight:bold;color:${theme.primaryColor};">
                ${config.productTitle || 'Plan Exclusivo'}
              </h2>
              <p style="margin:0;font-size:15px;line-height:22px;color:#44516A;max-width:540px;">
                ${config.productDescription || ''}
              </p>
            </td>
          </tr>

          ${config.cardImage ? `
          <!-- CARD SHOWCASE -->
          <tr>
            <td class="pad" align="center" style="padding:10px 50px 22px 50px;">
              <table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" align="center" style="width:600px;background-color:${theme.cardBg};border:1px solid ${theme.borderColor};border-radius:10px;">
                <tr>
                  <td align="center" style="padding:24px 20px;">
                    <img src="${resolvePath(config.cardImage)}" width="220" alt="Tarjeta" border="0" style="display:block;max-width:240px;width:100%;height:auto;margin:0 auto;filter:drop-shadow(0 6px 14px rgba(0,0,0,0.12));">
                  </td>
                </tr>
              </table>
            </td>
          </tr>` : ''}

          <!-- BENEFITS GRID -->
          <tr>
            <td class="pad" align="center" style="padding:10px 50px 24px 50px;">
              <table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" align="center" style="width:600px;table-layout:fixed;">
                <tr>
                  ${benefitsHtml}
                </tr>
              </table>
            </td>
          </tr>

          ${config.secondaryText ? `
          <!-- SECONDARY HIGHLIGHT -->
          <tr>
            <td class="pad" align="center" style="padding:0 50px 26px 50px;">
              <table role="presentation" width="600" cellspacing="0" cellpadding="0" border="0" align="center" style="width:600px;background-color:#EEF3FB;border:1px solid ${theme.borderColor};border-radius:8px;">
                <tr>
                  <td align="center" style="padding:16px 20px;text-align:center;">
                    <p style="margin:0;font-size:14px;line-height:21px;color:${theme.primaryColor};">
                      ${config.secondaryText}
                    </p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>` : ''}

          ${config.ctaText ? `
          <!-- CTA BUTTON -->
          <tr>
            <td class="pad" align="center" style="padding:8px 50px 34px 50px;text-align:center;">
              <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" style="margin:0 auto;">
                <tr>
                  <td align="center" bgcolor="${theme.accentColor}" style="border-radius:8px;background-color:${theme.accentColor};">
                    <a href="${config.ctaUrl || '#'}" class="btn-cta" target="_blank" style="display:inline-block;padding:16px 36px;font-size:16px;font-weight:bold;color:#FFFFFF;text-decoration:none;border-radius:8px;letter-spacing:0.5px;">
                      ${config.ctaText}
                    </a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>` : ''}

          <!-- LEGAL DISCLAIMER & FOOTER -->
          <tr>
            <td class="pad" align="left" bgcolor="#F8FAFC" style="padding:24px 50px 30px 50px;background-color:#F8FAFC;border-top:1px solid ${theme.borderColor};">
              <p style="margin:0 0 10px 0;font-size:13px;line-height:18px;font-weight:bold;color:${theme.primaryColor};">Información y Condiciones</p>
              <p style="margin:0;font-size:11px;line-height:17px;color:#64748B;">
                ${config.legales || 'Comunicaciones confidenciales y comerciales emitidas de acuerdo a normativas vigentes.'}
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>`;
};
