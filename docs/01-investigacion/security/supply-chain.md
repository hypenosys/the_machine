# SEC-RSCH-009 — Cadena de suministro Rust

**Estado: investigación preliminar; sin auditoría ejecutada.**

## Pregunta
¿Cómo comprobar qué código externo entra al binario y reducir riesgo de compromiso de dependencias, compilación y publicación?

## Medidas candidatas
- `Cargo.lock` versionado para aplicaciones.
- Revisión de dependencias directas y transitivas, features, scripts de build y proc macros.
- Compilaciones offline cuando estén disponibles dependencias verificadas.
- Inventario de componentes (SBOM) y licencias.
- Auditoría de advisories y revisiones de código de dependencias críticas.
- CI con permisos mínimos, acciones fijadas por commit y sin secretos para PR no confiables.
- Firmas/proveniencia de releases solo tras diseñar gestión de claves y rotación.

## Herramientas para evaluar
`cargo audit`, `cargo deny`, `cargo vet`, `cargo metadata`, generadores de SBOM y mecanismos de attestation. **No se presupone que estén instaladas o aprobadas.**

## Limitaciones
Un lockfile no prueba que una dependencia sea segura; un SBOM no detecta malware; un build offline no garantiza reproducibilidad bit a bit.

## Fuentes primarias
- Cargo: https://doc.rust-lang.org/cargo/
- RustSec: https://rustsec.org/
- cargo-vet: https://mozilla.github.io/cargo-vet/
- SLSA: https://slsa.dev/

**Decisión:** pendiente de prueba con proyecto mínimo y revisión de licencias.
