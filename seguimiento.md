# Seguimiento Técnico e Historial (CAP03_E04 y CAP03_E05)
## 1. Cronología de un Issue público cerrado (CAP03_E04)
- Enlace consultado: https://github.com/git/git/issues (Documentación pública de referencia)
- Problema: Un comando mostraba una salida confusa cuando faltaba un argumento de ruta.
- Debate: Los colaboradores solicitaron los pasos exactos para reproducirlo y el sistema operativo usado.
- Solución: Se corrigió la validación del parámetro y se cerró el Issue vinculando el commit de corrección.
- Qué faltó para resolverlo más rápido: Incluir desde el reporte inicial el comando exacto ejecutado y la versión de la herramienta.
## 2. Exploración de tres commits públicos (CAP03_E05)
| Versión / Commit | Autor Público | Archivo Modificado | Finalidad Observable (Corrección o Mejora) |
|---|---|---|---|
| Commit 1 | Colaborador Doc | README.md | Corrección: Arregla un error tipográfico en las instrucciones de inicio |
| Commit 2 | Colaborador Dev | src/parser.py | Mejora: Añade validación para evitar fallos con líneas vacías en archivos de datos |
| Commit 3 | Colaborador QA | tests/test_core.py | Mejora: Agrega una prueba unitaria para verificar el cálculo de totales |
