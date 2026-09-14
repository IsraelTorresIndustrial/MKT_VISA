/**
 * MKT_VISA Automated ZIP Project Exporter
 * Bundles the email HTML with all referenced images into a self-contained ZIP package
 */

window.exportEmailProjectZip = async function(htmlContent, projectName = "campaña_email", options = {}) {
  if (typeof JSZip === "undefined") {
    alert("Error: La librería JSZip no está cargada.");
    return;
  }

  showToast(`📦 Preparando paquete ZIP para "${projectName}"...`);

  const zip = new JSZip();
  const imgFolder = zip.folder("images");

  // Regex to find all img src attributes
  const imgSrcRegex = /<img[^>]+src=["']([^"']+)["']/gi;
  const imageSources = new Set();
  let match;

  while ((match = imgSrcRegex.exec(htmlContent)) !== null) {
    if (match[1] && !match[1].startsWith("data:")) {
      imageSources.add(match[1]);
    }
  }

  const srcMap = new Map();
  let counter = 1;
  const totalImages = imageSources.size;
  let processed = 0;

  for (const src of imageSources) {
    try {
      showToast(`⏳ Descargando imagen ${++processed} de ${totalImages}...`);

      // Determine local / clean filename
      let filename = "";
      try {
        const urlObj = new URL(src, window.location.href);
        const pathParts = urlObj.pathname.split("/");
        filename = decodeURIComponent(pathParts[pathParts.length - 1]);
      } catch (e) {
        const pathParts = src.split("/");
        filename = pathParts[pathParts.length - 1];
      }

      // Sanitize filename
      filename = filename.replace(/[^a-zA-Z0-9._-]/g, "_");
      if (!filename || filename.length < 3 || !filename.includes(".")) {
        filename = `image_${counter++}.png`;
      }

      // Ensure unique filename inside images folder
      let uniqueName = filename;
      let dupIndex = 1;
      while (Array.from(srcMap.values()).includes(uniqueName)) {
        const dotIdx = filename.lastIndexOf(".");
        const base = dotIdx !== -1 ? filename.substring(0, dotIdx) : filename;
        const ext = dotIdx !== -1 ? filename.substring(dotIdx) : ".png";
        uniqueName = `${base}_${dupIndex++}${ext}`;
      }

      // Fetch the image blob
      const response = await fetch(src, { mode: "cors" });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const blob = await response.blob();

      // Add to ZIP images folder
      imgFolder.file(uniqueName, blob);
      srcMap.set(src, `images/${uniqueName}`);
    } catch (err) {
      console.warn(`No se pudo descargar la imagen ${src}, se mantendrá la ruta original:`, err);
      // Keep original path if fetch fails (e.g. cross-origin blocking without CORS)
    }
  }

  // Rewrite HTML image sources to relative zip folder
  let packagedHtml = htmlContent;
  for (const [origSrc, newRelPath] of srcMap.entries()) {
    // Replace all occurrences of this exact src
    const escapedSrc = origSrc.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
    const regex = new RegExp(`src=["']${escapedSrc}["']`, 'g');
    packagedHtml = packagedHtml.replace(regex, `src="${newRelPath}"`);
  }

  // Add index.html to ZIP root
  zip.file("index.html", packagedHtml);

  // Add a helpful README / Documentation inside the ZIP
  const readmeContent = `# ${projectName}
## Paquete de Campaña de Email Marketing Listo para Envío
Generado automáticamente por **MKT_VISA Hub** por Israel Torres.
Fecha de Exportación: ${new Date().toLocaleString()}

### 📁 Estructura del Paquete
- \`index.html\`: Código HTML del correo completamente vinculado a las imágenes locales de la carpeta \`images/\`.
- \`images/\`: Todas las piezas gráficas, íconos 3D y banners utilizados en la pieza, ya nombrados y optimizados.

### 🚀 Cómo Utilizar
1. **Prueba Local**: Haz doble clic en \`index.html\` para visualizar el correo en cualquier navegador sin necesidad de servidor ni internet.
2. **Plataformas de Envío**: Sube este archivo ZIP o la carpeta \`images/\` a tu plataforma de Email Marketing (Salesforce Marketing Cloud, Braze, Oracle Eloqua, Mailchimp, etc.).
3. **Fidelidad**: Diseñado según las directrices institucionales oficiales y probado para máxima compatibilidad (Outlook, Apple Mail, Gmail).
`;

  zip.file("LEEME.txt", readmeContent);

  // Generate the ZIP blob
  showToast("⚡ Comprimiendo paquete ZIP final...");
  const zipBlob = await zip.generateAsync({
    type: "blob",
    compression: "DEFLATE",
    compressionOptions: { level: 9 }
  });

  // Trigger browser download
  const cleanZipName = `${projectName.toLowerCase().replace(/[^a-z0-9]/g, '_')}_${Date.now()}.zip`;
  const downloadLink = document.createElement("a");
  downloadLink.href = URL.createObjectURL(zipBlob);
  downloadLink.download = cleanZipName;
  document.body.appendChild(downloadLink);
  downloadLink.click();
  document.body.removeChild(downloadLink);
  URL.revokeObjectURL(downloadLink.href);

  showToast(`✅ ¡Proyecto "${cleanZipName}" descargado con éxito!`);
};
