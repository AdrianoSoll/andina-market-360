Problema: Consolidar ventas y mostrar resultados por sede sin editar informes manualmente.
Usuarios: Analistas comerciales, encargados de sede (Lima, Ica, Arequipa) y gerencia.
Resultado esperado: Reporte JSON y tablero web generados automáticamente desde Python.
Preguntas: ¿Qué sede lidera?, ¿qué producto vende más?, ¿cómo cambia el total mensual?
## Herramientas
- Git: Conservar versiones locales de los archivos.
- GitHub: Alojar el repositorio remoto y revisar los cambios en equipo.
- Flujo: archivo -> Git local -> repositorio remoto -> revisión del equipo (ningún paso depende de que GitHub ejecute el código de ventas).
## Estructura de trabajo
- data/: ventas simuladas
- src/: código Python
- tests/: pruebas unitarias
- docs/: página web estática
- .github/: colaboración y flujos
Justificación: El dashboard debe leer resultados generados por Python y no editar el CSV a mano para evitar errores manuales y mantener trazabilidad.
## Criterios de éxito
Metas: importar 12 ventas, calcular totales por sede, aprobar pruebas y mostrar resumen web.
| Indicador | Meta | Responsable | Evidencia requerida |
|---|---|---|---|
| Ventas importadas | 12 operaciones | Analista de Datos | data/ventas.csv |
| Totales por sede | Lima 814, Ica 555, Arequipa 476 | Desarrollador | python src/resumen.py |
| Pruebas unitarias | 4 pruebas correctas | Revisor QA | python -m unittest discover -s tests -v |
| Resumen web | Dashboard activo | Desarrollador Web | docs/data/resumen.json |
