# Security gates — Condiciones para avanzar

## G0 — Documentación (antes de investigar)
Problema, activos, datos, límites de confianza y uso indebido descritos. **No equivale a seguridad verificada.**

## G1 — Investigación (antes de aceptar un ADR)
Fuentes contrastadas, alternativas, riesgos, restricciones de licencia y amenazas concretas. Revisión por al menos una persona distinta de quien propone la decisión, cuando haya equipo disponible.

## G2 — Diseño (antes de implementar)
ADR Accepted, contrato de datos, matriz de permisos, plan de pruebas negativas, política de datos, rollback y criterios de aceptación.

## G3 — Implementación (antes de fusionar código ejecutable)
Pruebas locales registradas, análisis estático, dependencias revisadas, secretos ausentes, permisos mínimos y cambios revisados. Sin resultados inventados.

## G4 — Despliegue (antes de conectar fuentes o herramientas reales)
Tests adversariales, recuperación, aislamiento y límites de recursos verificados en entorno representativo; riesgos residuales aceptados explícitamente por responsable autorizado.

## G5 — Operación
Monitorización respetuosa con la privacidad, respuesta a incidentes, revisión periódica de permisos, rotación de secretos y pruebas de restauración.

## Estado de esta iteración
Solo se han redactado documentos G0/G1/G2 **preliminares**. Ningún gate se declara superado. La documentación puede fusionarse como propuesta; no habilita despliegue.
