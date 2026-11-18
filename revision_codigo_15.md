# Ficha de Revision Profesional de Codigo (CAP15_E01 - CAP15_E05)

## 1. Revision de diff delimitado (CAP15_E01)
- Comando ejecutado: git diff aaefd8c...feature/ficha-sedes
- Lineas afectadas: Documentacion/Web (docs/index.html y pull_request_14.md). Datos, codigo Python y pruebas no sufrieron alteraciones riesgosas.

## 2. Solicitud de correccion reproducible (CAP15_E02)
- Observacion respetuosa: El subtitulo del grafico podria resultar ambiguo si no indica la moneda.
- Propuesta: Especificar 'Montos en Soles (S/)' en docs/index.html.
- Evidencia requerida: Captura de la pagina renderizada y ejecucion de unittest sin errores.

## 3. Comprobacion de pruebas del cambio (CAP15_E03)
- Comando: python -m unittest discover -s tests -v
- Resultado: 4 pruebas ejecutadas -> Estado: OK (todas pasaron).

## 4. Distincion entre observacion y bloqueo (CAP15_E04)
- Comentario sugerido (No bloqueante): Mejorar el espaciado CSS del encabezado en docs/style.css.
- Comentario bloqueante (Impide fusionar): Error de calculo en totales por sede, filtracion de credenciales o prueba unitaria rota. Criterio de aceptacion: 4 tests en verde y cero secretos.

## 5. Cierre trazable de la revision (CAP15_E05)
- Fecha: 