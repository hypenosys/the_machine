# PR #33 — cobertura de trazabilidad amenaza → requisito (23-10-2026)

**Corte inmutable inspeccionado:** `5d722e3e6dcc42418d47be4a77b7b0c6d6a08c56`. **Fuentes:** `docs/02-diseno/security/threat-model-v0.md` y `docs/02-diseno/security/requirements.md`. **Método:** lectura de contenido y análisis de las filas de tabla `| TH-... |` y `| SEC-REQ-... |` por sus identificadores. No es una prueba de implementación, ni una revisión de suficiencia de mitigaciones. `HOLD / NO-GO`.

## Resultados

| Indicador | Observación |
|---|---:|
| Filas de amenaza `TH-001..TH-020` | 20 |
| Filas de requisito `SEC-REQ-001..SEC-REQ-017` | 17 |
| Amenazas distintas referenciadas por requisitos | **20/20** |
| Amenazas sin requisito asociado | **0** |
| Referencias a amenazas inexistentes | **0** |
| Identificadores de fila de amenaza duplicados | **0** |
| Identificadores de fila de requisito duplicados | **0** |
| Requisitos con campo de prueba `Pendiente` | **3** |

## Asociaciones con prueba pendiente

| Requisito | Amenaza | ADR citado | Prueba |
|---|---|---|---|
| `SEC-REQ-015` | `TH-016` (backup irrecuperable) | `ADR-0005` | `Pendiente` |
| `SEC-REQ-016` | `TH-019` (insider abuse) | `ADR-0001, 0004` | `Pendiente` |
| `SEC-REQ-017` | `TH-012` (confused deputy) | `ADR-0004` | `Pendiente` |

## Interpretación

**Resultado limitado: trazabilidad nominal completa (20/20).** Una amenaza asociada a un requisito puede seguir mal mitigada, carecer de propietario, no tener prueba ejecutada o no cubrir escenarios de abuso relevantes. La tabla de requisitos declara expresamente que es `PROPUESTO` y que `VERIFIED` exige resultado reproducible ligado a commit, entorno y datos sintéticos.

El campo `SEC-001..SEC-014` es una **referencia nominal de prueba**, no evidencia de ejecución ni PASS. No se ha evaluado en esta pasada la existencia de sus procedimientos completos ni la suficiencia de los ADR. Las tres pruebas pendientes deben permanecer abiertas sin crear resultados sintéticos.

**Decisión:** `TRACEABILITY_ID_COVERAGE = 20/20`; `IMPLEMENTATION_VERIFICATION = NOT_EVALUATED`; `TEST_EXECUTION = NOT_EVALUATED`; `HOLD/NO-GO` inalterado.
