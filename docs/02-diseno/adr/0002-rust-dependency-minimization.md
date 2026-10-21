# ADR-0002 — Rust y minimización paranoica de dependencias

**Estado: Proposed · Fecha: 2026-10-21**

## Explicación sencilla
Cada biblioteca ajena ahorra trabajo, pero también introduce código que no controlamos.

## Decisión propuesta
- Rust estable y `std` como base; `#![forbid(unsafe_code)]` en crates propios del núcleo.
- Versiones de compilador documentadas y lockfile versionado para aplicaciones.
- No descargar dependencias durante builds de producción.
- Revisar crates, transitivas, features, build scripts, proc macros, licencias, advisories, mantenimiento y procedencia.
- Reproducibilidad y SBOM como gates; CI sin secretos innecesarios.
- Sin dependencias nuevas por comodidad o popularidad.

## Excepción crítica
**No implementar criptografía, TLS, autenticación o parsers complejos de seguridad desde cero solo para lograr cero dependencias.** Evaluar bibliotecas auditadas o servicios del sistema; documentar el compromiso.

## Alternativas
Cero crates para siempre (rechazado: fomenta implementaciones propias inseguras); usar un framework completo (rechazado como default: superficie amplia); dependencias mínimas justificadas (propuesta).

## Invariantes
INV-005 ninguna dependencia no revisada entra al núcleo; INV-006 no hay ejecución de scripts de build no revisados; INV-007 cada artefacto publicado tiene inventario verificable.

## Verificación
`cargo test --offline`, revisión de lockfile, compilación reproducible, análisis de vulnerabilidades, inventario de licencias, revisión de código inseguro en transitivas. Herramientas concretas por decidir.
