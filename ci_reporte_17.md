# Reporte de Integracion Continua - GitHub Actions (CAP17_E01 - CAP17_E05)

## 1. Estructura del flujo (CAP17_E01)
- Archivo: .github/workflows/ci.yml
- Sistema operativo del runner: ubuntu-latest
- Version de Python: 3.11

## 2. Eventos disparadores (CAP17_E02)
- Eventos configurados: push y pull_request sobre la rama main.
- Proposito: Impedir que cambios con errores de calculo lleguen al tablero principal.

## 3. Pasos automatizados (CAP17_E03)
1. Checkout del codigo fuente (actions/checkout@v4).
2. Configuracion de Python (actions/setup-python@v5).
3. Ejecucion de 4 pruebas unitarias con unittest.
4. Ejecucion de src/resumen.py y comprobacion de existencia de docs/data/resumen.json.

## 4. Simulacion local previa al envio (CAP17_E04)
- Resultado local: 4 tests en estado OK y archivo docs/data/resumen.json generado sin errores.

## 5. Interpretacion de resultados en Actions (CAP17_E05)
- Estado esperado en GitHub Actions: Verde (Success).
- Criterio ante fallo: Si una prueba falla, el job devuelve codigo distinto de cero y bloquea la integracion.
