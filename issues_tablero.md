# Gestion de Tareas con Issues y Projects (CAP13_E01 - CAP13_E05)

## 1. Issue de funcionalidad (CAP13_E01)
- Titulo: feat: grafico de ventas por sede
- Objetivo de gerencia: Visualizar rapidamente el aporte de Lima, Ica y Arequipa.
- Criterios de aceptacion: Mostrar las tres sedes, usar cifras exactas del CSV y tener titulo legible.

## 2. Issue de error reproducible (CAP13_E02)
- Titulo: bug: cifra incorrecta tras editar CSV
- Entrada (muestra ficticia): Fila de prueba con formato decimal coma en lugar de punto.
- Pasos: 1) Editar fila ficticia, 2) Ejecutar python src/resumen.py.
- Resultado observado: ValueError al convertir texto a float.
- Resultado esperado: Sumar correctamente S/ 1845.00 usando punto decimal.

## 3. Clasificacion por etiquetas (CAP13_E03)
- Issue #1 (feat: grafico de ventas por sede) -> Etiquetas: mejora, documentacion (Impacto: facilita lectura ejecutiva).
- Issue #2 (bug: cifra incorrecta tras editar CSV) -> Etiquetas: error, prioridad-alta (Impacto: detiene la generacion del JSON).

## 4. Tablero Kanban de tareas (CAP13_E04)
| Tarea | Estado | Responsable | Evidencia para pasar a Terminado |
|---|---|---|---|
| Validar 12 ventas del CSV | Terminado | Analista Datos | Salida OK de unittest |
| Agregar subtitulo de sedes en web | En proceso | Dev Web | Commit en rama y vista en navegador |
| Disenar vista de productos | Pendiente | Dev Python | Nuevo calculo en resumen.json |

## 5. Cierre con evidencia tecnica (CAP13_E05)
- Issue cerrado: Validar 12 ventas del CSV
- Comentario de resolucion: Resuelto en commit inicial, verificado ejecutando python -m unittest discover -s tests -v sobre tests/test_resumen.py (4 pruebas aprobadas).
