/**
 * MKT_VISA Interactive Email Builder Controller
 */

window.BuilderStudio = {
  state: null,
  activePreviewMode: "desktop", // "desktop" | "mobile"
  activeTab: "preview", // "preview" | "code"

  init() {
    this.loadPreset("bch_bienvenida");
    this.bindEvents();
  },

  loadPreset(presetId) {
    const preset = window.EMAIL_PRESETS[presetId];
    if (!preset) return;
    this.state = JSON.parse(JSON.stringify(preset));
    this.renderForm();
    this.updatePreview();
  },

  renderForm() {
    const container = document.getElementById("builderFormContainer");
    if (!container) return;

    const s = this.state;
    container.innerHTML = `
      <div class="builder-section">
        <label class="form-label">Plantilla Base</label>
        <select id="presetSelector" class="form-control" onchange="BuilderStudio.loadPreset(this.value)">
          <option value="bch_bienvenida" ${s.id === 'bch_bienvenida' ? 'selected' : ''}>Banco de Chile - Bienvenida & Activación</option>
          <option value="bch_inactividad_m1" ${s.id === 'bch_inactividad_m1' ? 'selected' : ''}>Banco de Chile - Reactivación M1 (Descuento)</option>
          <option value="visa_crossborder" ${s.id === 'visa_crossborder' ? 'selected' : ''}>Visa - Campaña Cross-Border Internacional</option>
        </select>
      </div>

      <div class="builder-section">
        <h4 class="section-heading">1. Cabecera & Saludo</h4>
        <div class="form-group">
          <label class="form-label">Hero Banner (Imagen Superior)</label>
          <div style="display:flex; gap:8px;">
            <input type="text" class="form-control" id="heroBannerInput" value="${s.heroBanner || ''}" oninput="BuilderStudio.updateField('heroBanner', this.value)">
            <button class="btn-card" onclick="BuilderStudio.openAssetPicker('heroBanner')">Elegir...</button>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Nombre del Cliente</label>
          <input type="text" class="form-control" value="${s.clientName || ''}" oninput="BuilderStudio.updateField('clientName', this.value)">
        </div>

        <div class="form-group">
          <label class="form-label">Titular Principal (H1)</label>
          <textarea class="form-control" rows="2" oninput="BuilderStudio.updateField('h1Text', this.value)">${s.h1Text || ''}</textarea>
        </div>
      </div>

      <div class="builder-section">
        <h4 class="section-heading">2. Producto & Tarjeta Protagonista</h4>
        <div class="form-group">
          <label class="form-label">Subtítulo de Producto</label>
          <input type="text" class="form-control" value="${s.productSubtitle || ''}" oninput="BuilderStudio.updateField('productSubtitle', this.value)">
        </div>
        <div class="form-group">
          <label class="form-label">Nombre del Plan / Tarjeta</label>
          <input type="text" class="form-control" value="${s.productTitle || ''}" oninput="BuilderStudio.updateField('productTitle', this.value)">
        </div>
        <div class="form-group">
          <label class="form-label">Descripción del Producto</label>
          <input type="text" class="form-control" value="${s.productDescription || ''}" oninput="BuilderStudio.updateField('productDescription', this.value)">
        </div>
        <div class="form-group">
          <label class="form-label">Arte de la Tarjeta</label>
          <div style="display:flex; gap:8px;">
            <input type="text" class="form-control" id="cardImageInput" value="${s.cardImage || ''}" oninput="BuilderStudio.updateField('cardImage', this.value)">
            <button class="btn-card" onclick="BuilderStudio.openAssetPicker('cardImage')">Elegir...</button>
          </div>
        </div>
      </div>

      <div class="builder-section">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <h4 class="section-heading" style="margin:0;">3. Grilla de Beneficios (${s.benefits.length})</h4>
          <button class="btn-card" onclick="BuilderStudio.addBenefit()">+ Agregar Beneficio</button>
        </div>
        
        <div id="benefitsList">
          ${s.benefits.map((b, idx) => `
            <div class="benefit-item-card">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-size:12px; font-weight:700; color:var(--bch-navy);">Beneficio #${idx + 1}</span>
                <button style="background:none; border:none; color:#EF4444; font-size:11px; cursor:pointer; font-weight:600;" onclick="BuilderStudio.removeBenefit(${idx})">Eliminar</button>
              </div>
              <div style="display:flex; gap:10px; align-items:center; margin-bottom:8px;">
                <img src="${b.icon}" width="40" height="40" style="object-fit:contain; border:1px solid #CBD5E1; border-radius:6px; padding:2px; background:#FFFFFF;" id="benefitIconPreview_${idx}">
                <button class="btn-card" style="flex:1;" onclick="BuilderStudio.openIconPicker(${idx})">Cambiar Ícono...</button>
              </div>
              <div style="display:grid; grid-template-columns: 100px 1fr; gap:8px; margin-bottom:8px;">
                <input type="text" class="form-control" placeholder="Cifra / Badge" value="${b.badge || ''}" oninput="BuilderStudio.updateBenefitField(${idx}, 'badge', this.value)">
                <input type="text" class="form-control" placeholder="Título" value="${b.title || ''}" oninput="BuilderStudio.updateBenefitField(${idx}, 'title', this.value)">
              </div>
              <input type="text" class="form-control" placeholder="Descripción" value="${b.description || ''}" oninput="BuilderStudio.updateBenefitField(${idx}, 'description', this.value)">
            </div>
          `).join('')}
        </div>
      </div>

      <div class="builder-section">
        <h4 class="section-heading">4. Botón de Acción (CTA) & Legales</h4>
        <div class="form-group">
          <label class="form-label">Texto del Botón</label>
          <input type="text" class="form-control" value="${s.ctaText || ''}" oninput="BuilderStudio.updateField('ctaText', this.value)">
        </div>
        <div class="form-group">
          <label class="form-label">URL de Destino</label>
          <input type="text" class="form-control" value="${s.ctaUrl || ''}" oninput="BuilderStudio.updateField('ctaUrl', this.value)">
        </div>
        <div class="form-group">
          <label class="form-label">Texto Secundario Destacado</label>
          <textarea class="form-control" rows="2" oninput="BuilderStudio.updateField('secondaryText', this.value)">${s.secondaryText || ''}</textarea>
        </div>
        <div class="form-group">
          <label class="form-label">Condiciones y Legales</label>
          <textarea class="form-control" rows="3" oninput="BuilderStudio.updateField('legales', this.value)">${s.legales || ''}</textarea>
        </div>
      </div>
    `;
  },

  updateField(field, value) {
    this.state[field] = value;
    this.updatePreview();
  },

  updateBenefitField(idx, field, value) {
    if (this.state.benefits[idx]) {
      this.state.benefits[idx][field] = value;
      this.updatePreview();
    }
  },

  addBenefit() {
    if (this.state.benefits.length >= 4) {
      alert("Máximo 4 beneficios recomendados para correos responsivos.");
      return;
    }
    this.state.benefits.push({
      icon: "assets/bch/icons/01_tarjeta.png",
      badge: "NUEVO",
      title: "Nuevo Beneficio",
      description: "Detalle del beneficio para el cliente."
    });
    this.renderForm();
    this.updatePreview();
  },

  removeBenefit(idx) {
    if (this.state.benefits.length <= 1) {
      alert("Debe haber al menos 1 beneficio.");
      return;
    }
    this.state.benefits.splice(idx, 1);
    this.renderForm();
    this.updatePreview();
  },

  openIconPicker(benefitIndex) {
    window.activeBenefitIconIndex = benefitIndex;
    const modal = document.getElementById("assetPickerModal");
    if (!modal) return;
    
    // Filter only 3D icons and travel icons
    const icons = window.BANK_ASSETS.filter(a => a.category === "Íconos 3D" || a.category === "Travel & Turismo");
    const pickerGrid = document.getElementById("assetPickerGrid");
    pickerGrid.innerHTML = icons.map(icon => `
      <div class="picker-item" onclick="BuilderStudio.selectBenefitIcon('${icon.rel_path}')">
        <img src="${icon.rel_path}" alt="${icon.title}">
        <span>${icon.title}</span>
      </div>
    `).join('');

    modal.classList.add("active");
  },

  selectBenefitIcon(relPath) {
    if (window.activeBenefitIconIndex !== undefined && this.state.benefits[window.activeBenefitIconIndex]) {
      this.state.benefits[window.activeBenefitIconIndex].icon = relPath;
      const previewImg = document.getElementById(`benefitIconPreview_${window.activeBenefitIconIndex}`);
      if (previewImg) previewImg.src = relPath;
      this.updatePreview();
    }
    document.getElementById("assetPickerModal").classList.remove("active");
  },

  openAssetPicker(targetField) {
    window.activeTargetField = targetField;
    const modal = document.getElementById("assetPickerModal");
    if (!modal) return;

    let items = [];
    if (targetField === "cardImage") {
      items = window.BANK_ASSETS.filter(a => a.category === "Tarjetas" || a.category === "Logotipos");
    } else {
      items = window.BANK_ASSETS.filter(a => a.category === "Banners Hero" || a.category === "Logotipos");
    }

    const pickerGrid = document.getElementById("assetPickerGrid");
    pickerGrid.innerHTML = items.map(asset => `
      <div class="picker-item" onclick="BuilderStudio.selectAssetField('${asset.rel_path}')">
        <img src="${asset.rel_path}" alt="${asset.title}">
        <span>${asset.title}</span>
      </div>
    `).join('');

    modal.classList.add("active");
  },

  selectAssetField(relPath) {
    if (window.activeTargetField) {
      this.updateField(window.activeTargetField, relPath);
      const input = document.getElementById(`${window.activeTargetField}Input`);
      if (input) input.value = relPath;
    }
    document.getElementById("assetPickerModal").classList.remove("active");
  },

  getCurrentHtml(isZipMode = false) {
    return window.generateEmailHtml(this.state, {
      relativePaths: true,
      zipMode: isZipMode
    });
  },

  updatePreview() {
    const html = this.getCurrentHtml(false);
    const iframe = document.getElementById("emailPreviewFrame");
    if (iframe) {
      const doc = iframe.contentDocument || iframe.contentWindow.document;
      doc.open();
      doc.write(html);
      doc.close();
    }

    const codeArea = document.getElementById("rawHtmlCode");
    if (codeArea) {
      codeArea.value = html;
    }
  },

  setPreviewMode(mode) {
    this.activePreviewMode = mode;
    const container = document.getElementById("previewFrameWrapper");
    const btnDesk = document.getElementById("btnModeDesktop");
    const btnMob = document.getElementById("btnModeMobile");

    if (mode === "mobile") {
      container.style.maxWidth = "395px";
      btnMob.classList.add("active");
      btnDesk.classList.remove("active");
    } else {
      container.style.maxWidth = "740px";
      btnDesk.classList.add("active");
      btnMob.classList.remove("active");
    }
  },

  setTab(tab) {
    this.activeTab = tab;
    const frameWrap = document.getElementById("previewFrameWrapper");
    const codeWrap = document.getElementById("codeEditorWrapper");
    const tabPrev = document.getElementById("tabBtnPreview");
    const tabCode = document.getElementById("tabBtnCode");

    if (tab === "code") {
      frameWrap.style.display = "none";
      codeWrap.style.display = "block";
      tabCode.classList.add("active");
      tabPrev.classList.remove("active");
    } else {
      frameWrap.style.display = "flex";
      codeWrap.style.display = "none";
      tabPrev.classList.add("active");
      tabCode.classList.remove("active");
      this.updatePreview();
    }
  },

  copyHtml() {
    const html = this.getCurrentHtml(false);
    navigator.clipboard.writeText(html).then(() => {
      showToast("📋 ¡Código HTML copiado al portapapeles!");
    });
  },

  exportZip() {
    const projectName = (this.state.productTitle || "email_campaign").replace(/\s+/g, '_');
    const html = this.getCurrentHtml(true);
    window.exportEmailProjectZip(html, projectName);
  },

  bindEvents() {}
};
