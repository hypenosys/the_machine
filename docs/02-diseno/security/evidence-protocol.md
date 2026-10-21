# Protocolo de evidencia para pruebas de seguridad

**Estado: especificación, sin ejecuciones adjuntas.**

Cada ejecución debe publicar un manifiesto legible por humanos y máquinas:

```text
test_id: SEC-001
requirement_id: SEC-REQ-001
source_commit: <sha>
platform: <sistema y arquitectura>
toolchain: <versión>
test_fixture: <ruta y hash de datos sintéticos>
command: <comando exacto>
expected: <resultado esperado>
observed: <resultado observado>
outcome: PASS | FAIL | BLOCKED | INCONCLUSIVE
started_at: <fecha>
operator: <identidad de auditor>
artifacts: <rutas y hashes>
```

## Normas
- Nunca redactar un PASS sin ejecutar la prueba.
- Guardar logs redactados, sin secretos, tokens ni datos personales.
- Preservar FAIL, BLOCKED e INCONCLUSIVE; no convertirlos en éxito.
- Asociar resultados a versiones concretas del código y del entorno.
- Repetir pruebas al cambiar un límite de confianza, dependencia o política.
- Los tests sintéticos no demuestran ausencia de vulnerabilidades.
- Para experimentos con efectos externos, usar un sandbox y autorización específica.

## Evidencia negativa
Si no puede reproducirse una prueba, registrar qué falta, quién lo resolverá y qué decisiones quedan bloqueadas.
