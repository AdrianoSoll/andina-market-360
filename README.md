# Andina Market 360 - Dashboard Comercial Integrado
## Problema Empresarial
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
Alcance del informe: Mostrará el resumen de ventas desglosado por cada sede (Lima, Ica y Arequipa).
Actualización remota: Sincronización verificada desde el repositorio central.
Segunda actualización remota: Pendiente de inspección con git fetch.
Fuente de datos: El archivo data/ventas.csv contiene registros 100% ficticios creados para práctica.

## Objetivo (CAP12_E01)
Consolidar las ventas regionales de forma automatizada y reproducible.

## Requisitos
Python 3 estandar y Git (sin dependencias externas).

## Datos
Informacion 100% ficticia almacenada en [data/ventas.csv](data/ventas.csv).

## Ejecucion e Inicio rapido (CAP12_E03)
```bash
python -m unittest discover -s tests
python src/resumen.py
```

## Tabla de Indicadores (CAP12_E02)
*Nota: Totales generados automaticamente a partir de datos de ejemplo (no confundir con resultados empresariales reales).*

| Sede | Indicador | Formula | Fuente |
|---|---|---|---|
| Lima | Total sede Lima | Suma(total) de Lima | data/ventas.csv |
| Ica | Total sede Ica | Suma(total) de Ica | data/ventas.csv |
| Arequipa | Total sede Arequipa | Suma(total) de Arequipa | data/ventas.csv |

## Enlaces Relativos (CAP12_E04 y CAP12_E05)
- [Manual](docs/manual.md)
- [Datos de ventas](data/ventas.csv)
- [Guia de contribucion](CONTRIBUTING.md)
