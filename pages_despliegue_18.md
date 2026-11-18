# Publicacion Web Estatica con GitHub Pages (CAP18_E01 - CAP18_E05)

## 1. Verificacion de carpeta de publicacion (CAP18_E01)
- Carpeta fuente: /docs en la rama main.
- Archivos verificados: docs/index.html, docs/style.css, docs/data/resumen.json y docs/manual.md.

## 2. Validacion de rutas relativas (CAP18_E02)
- Enlace de hoja de estilos: href="style.css" (ruta relativa limpia, sin barras iniciales rotas).
- Archivo .nojekyll incluido en docs/ para servir recursos estaticos directamente.

## 3. Configuracion de origen en GitHub Pages (CAP18_E03 y CAP18_E04)
- Ruta en interfaz: Settings -> Pages -> Build and deployment.
- Source: Deploy from a branch.
- Branch: main | Folder: /docs.

## 4. Comprobacion post-despliegue (CAP18_E05)
- URL esperada del tablero: https://adrianosoll.github.io/andina-market-360/
- Verificacion: Muestra las 12 operaciones, el total S/ 1845.00 y el desglose de Lima, Ica y Arequipa.
