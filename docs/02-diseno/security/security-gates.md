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

## Colisión de definiciones — nota de conciliación documental (PR #25, 21-10-2026)

**No resuelta normativamente (GAP-010 / REV-05).** Este archivo denomina G3 a los controles **antes de fusionar código ejecutable**; `docs/03-preimplementacion/staged-authorization-protocol-v1.md` propone G3 como puerta **antes de comenzar la implementación**. Son hitos diferentes y no pueden intercambiarse por simple equivalencia terminológica. La lectura propuesta del protocolo por etapas **no sustituye** esta definición histórica hasta ratificación expresa de la autoridad competente. Ninguna de las dos redacciones concede permiso actual para escribir, compilar, ejecutar o fusionar código. Se mantiene **HOLD / NO-GO**; las eventuales excepciones de laboratorio exigen DEC-08 delimitada y verificable. No se ha efectuado ratificación conjunta de @Axlfc y @TopperH4rley.

## Estado de esta iteración
Solo se han redactado documentos G0/G1/G2 **preliminares**. Ningún gate se declara superado. La documentación puede fusionarse como propuesta; no habilita despliegue.
