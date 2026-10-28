# Auditoría documental incremental — PR #33 — 2026-10-23

**Estado:** registro de comprobación parcial, no certificación global. **Referencia inspeccionada:** rama `docs/finch-consistency-consolidation-20261023` en la revisión `9936fbe0d11127ff9c08789157e2502d80ecaa82` (antes de añadir este informe). **No son pruebas de software ni auditoría semántica exhaustiva.**

## Método y cobertura

- Se obtuvo el árbol Git recursivo de la rama: **105 entradas, 95 documentos `.md`**.
- Se inspeccionó el texto de **12 documentos**, escogidos por su importancia para autoridad, gates, semántica, trazabilidad y la PR.
- Se extrajeron enlaces Markdown inline de la forma `[etiqueta](destino)` y se resolvieron las rutas locales relativas contra el árbol. Se aceptaron rutas a archivos y directorios con `README.md`.
- Se excluyeron de la comprobación los enlaces externos y los fragmentos `#ancla`; no se verificaron enlaces de referencia, enlaces generados, anclas GitHub ni enlaces en texto sin formato.
- **Resultado:** 32 enlaces Markdown inline encontrados en los 12 archivos; **0 rutas locales inexistentes detectadas**. La cifra incluye enlaces no locales en el recuento bruto; no debe presentarse como «32 enlaces locales verificados».
- Un intento previo de auditar los 95 documentos en una sola operación excedió el límite de llamadas disponible y **no generó resultado global válido**.

## Archivos inspeccionados

| Archivo | Enlaces inline encontrados | Rutas locales inexistentes detectadas |
|---|---:|---:|
| `GOVERNANCE.md` | 2 | 0 |
| `docs/03-preimplementacion/contract-authority-map.md` | 0 | 0 |
| `docs/03-preimplementacion/owner-ratification-sheet-candidate-v1.md` | 1 | 0 |
| `docs/03-preimplementacion/staged-authorization-protocol-v1.md` | 3 | 0 |
| `docs/03-preimplementacion/finch-consistency-decision-register-2026-10-23.md` | 13 | 0 |
| `docs/03-preimplementacion/README.md` | 13 | 0 |
| `docs/02-diseno/security/security-gates.md` | 0 | 0 |
| `docs/03-preimplementacion/decision-package-v1.md` | 0 | 0 |
| `docs/03-preimplementacion/general-epistemic-contract-v0.md` | 0 | 0 |
| `docs/03-preimplementacion/provenance-assurance-matrix-v0.md` | 0 | 0 |
| `docs/03-preimplementacion/claim-semantics-v0.md` | 0 | 0 |
| `docs/03-preimplementacion/traceability-matrix-v1.md` | 0 | 0 |
| **TOTAL** | **32** | **0** |

## Coherencia semántica: observaciones, no certificaciones

1. `security-gates.md` define G3 antes de fusionar código ejecutable; `staged-authorization-protocol-v1.md` propone G3 antes de comenzar la implementación. **Colisión normativa abierta**; la PR no decide precedencia.
2. `traceability-matrix-v1.md` califica F-11/E-11 y F-12/E-12 como propuestas, no pruebas existentes. El registro Finch se corrigió para mantener ese estado.
3. `general-epistemic-contract-v0.md` y `provenance-assurance-matrix-v0.md` distinguen resultados epistemológicos de garantías de procedencia. **No se ha demostrado compatibilidad de implementación ni equivalencia automática.**
4. El estado HOLD/NO-GO para código permanece; una PR documental revisable no modifica la autoridad de los cotitulares.

## Hallazgos y límites

- **LINK-001 — sin incidencia en muestra:** no se detectaron rutas locales rotas mediante el método descrito. **Cobertura: 12/95 documentos**, no 95/95.
- **GATE-001 — abierto:** G3 conserva dos interpretaciones históricas/propuestas; necesita decisión competente.
- **COV-001 — abierto:** faltan 83 documentos por inspeccionar con este método, además de anclas, referencias Markdown y URLs externas.
- **SEM-001 — abierto:** la ausencia de enlaces rotos no demuestra ausencia de contradicciones conceptuales, normativas, temporales ni jurídicas.
- **IND-001 — abierto:** no consta revisión independiente ni ratificación conjunta para cerrar gates o cambiar estados.

## Criterio de continuación

Auditar el resto por lotes reproducibles, conservar recuentos exactos y añadir únicamente hallazgos verificables con ruta y alcance. Antes de declarar «documentación coherente» se requiere un registro completo de contradicciones y su disposición, revisión independiente y resolución de las decisiones reservadas. No declarar cero contradicciones globales por una muestra sin errores.
