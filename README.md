# Andina Market 360
## Problema
Objetivo comercial: Consolidar automáticamente las ventas de Lima, Ica y Arequipa sin editar informes manualmente para evitar errores de cálculo.
## Funcionalidades
- Lectura del archivo ficticio data/ventas.csv (12 operaciones).
- Cálculo automatizado de totales por sede y exportación a docs/data/resumen.json.
- Verificación mediante 4 pruebas unitarias automatizadas.
## Estructura de Carpetas
- data/: Datos simulados (ventas.csv).
- src/: Script de procesamiento (resumen.py).
- tests/: Pruebas automáticas (test_resumen.py).
- docs/: Tablero web estático (index.html, style.css, data/resumen.json).
- .github/: Flujos de automatización (workflows/ci.yml).
## Cómo ejecutar el análisis
    python src/resumen.py
    python src/resumen.py --json docs/data/resumen.json
    python -m unittest discover -s tests -v
Propósito: Facilitar la revisión de ventas por sede mediante un tablero estático.
