# PR #33 — índice de consolidación y cierre condicionado de auditorías

**Corte de inventario:** `707cbe3454ab657c3b397f87dba4c6d895c0d3df`, 29 documentos `docs/04-auditorias/pr33-*.md` en ese árbol. **Tipo:** índice editorial y registro de pendientes, no nueva ejecución de verificadores ni certificación global. **Estado:** `HOLD / NO-GO`.

## 1. Familias de evidencia (sin sumar coberturas incompatibles)

| Familia | Informes existentes | Qué puede afirmarse | Qué NO puede afirmarse |
|---|---|---|---|
| Inventario y enlaces históricos | `pr33-incremental-documentation-audit`, `pr33-link-audit-batches`, `pr33-link-audit-batches-d-f`, `pr33-inline-link-coverage-reconciliation` | Muestras y recuentos de cortes anteriores, con método declarado | Verificación homogénea con parser de toda la PR |
| Manifiestos regex | `pr33-reference-manifest-regex-batch-01` a `09`, `pr33-exact-markdown-blob-delta`, `pr33-document-denominator-and-fixture-fence-check` | 162 detecciones regex en el corte de 103 Markdown; diferencias por SHA en cortes posteriores | 162 enlaces CommonMark validados o cero enlaces rotos en HEAD actual |
| Contratos de parser | `pr33-reference-integrity-protocol-candidate`, `pr33-independent-markdown-parser-acceptance-contract`, `pr33-parser-literal-fixtures-candidate`, `pr33-parser-fixture-oracle-critical-review`, `pr33-reference-protocol-crosswalk` | Casos y criterios propuestos, reconciliación de taxonomías | Ejecución de parser AST o resultado PASS |
| Semántica y gobernanza | `pr33-semantic-adjudication-matrix`, `pr33-github-review-and-check-evidence` | Colisiones de gates identificadas y eventos API observados en cortes concretos | Ratificación conjunta de GAP-010/G3, autorización de código o merge |
| Revisión de contenido y seguridad | `pr33-readme-factual-claims-crosscheck`, `pr33-threat-requirement-coverage-crosscheck`, `pr33-security-adr-test-reference-integrity`, `pr33-adr-threat-nominal-crossref-gaps`, `pr33-adr-threat-semantic-adjudication` | Integridad nominal de IDs y nueve asociaciones ADR–amenaza justificadas/limitadas editorialmente | Suficiencia técnica de los controles |
| Oráculos de seguridad | `pr33-falsifiable-idempotency-and-separation-contracts`, `pr33-three-partial-threat-falsification-oracles` | Contratos y falsadores candidatos documentados | Pruebas ratificadas, implementadas o ejecutadas |

**Inventario:** 4 + 11 + 5 + 2 + 5 + 2 = **29 informes**. Las once piezas del grupo «Manifiestos regex» incluyen los nueve lotes y dos informes de comparación/denominador; `pr33-reference-protocol-crosswalk` se cuenta exclusivamente en «Contratos de parser» para evitar doble cómputo. La clasificación es editorial; los documentos pueden citarse entre sí.

## 2. Riesgos de interpretación detectados

1. **Denominadores históricos distintos:** 95, 100, 101, 103 y 117 documentos corresponden a cortes y métodos distintos; no representan un único control incremental acumulativo. El HEAD de inventario tiene 126 Markdown, pero ese dato **no equivale** a 126 archivos parseados.
2. **Cobertura nominal frente a semántica:** 20/20 amenazas con enlace a requisito, 17 requisitos con referencias ADR existentes, 14 tests nominales asignados y tres candidatos adicionales **no** equivalen a 20 amenazas verificadas. Hay nueve asociaciones ADR–amenaza sin mención literal del ID y tres amenazas (`TH-008`, `TH-017`, `TH-014`) que precisan oráculos propios.
3. **Dos clases de pendientes:** `SEC-REQ-015..017` tienen pruebas `SEC-015..017` candidatas sin asignación ratificada; `O-TH008/O-TH017/O-TH014` son extensiones de alcance sin ID `SEC-###`. No confundir ambos grupos.
4. **Aprobación de PR frente a autoridad:** un evento `APPROVED` de GitHub y un comentario `OK` no documentan por sí solos una ratificación conjunta versionada ni `AUT-CODE/AUT-EXEC/AUT-MERGE`.
5. **Alcance de las cifras:** el conteo del árbol Git y los patrones de extensión no prueban ausencia universal de código, ni que otras ramas estén limpias.

## 3. Pendientes para cierre real

| Prioridad | Pendiente | Evidencia mínima de cierre | Estado |
|---|---|---|---|
| P0 | Regla de autoridad `GAP-010` y significado `G3 / DEC-GATE-003` | Ratificación inequívoca de titulares con versión, alcance y mecanismo de decisión | `BLOCKED_BY_DECISION` |
| P0 | `AUT-CODE`, `AUT-EXEC`, `AUT-MERGE`, `DEC-08` | Autorizaciones específicas, separadas y registradas; no inferir de PR review | `NOT_GRANTED` |
| P0 | Licencia de software y dependencia de `GAP-005` | Selección exacta de licencia y compatibilidad revisada | `OPEN` |
| P1 | Contrato remoto de reintentos / estados `UNKNOWN` | Oráculo aprobado y modelo de reconciliación | `PARTIAL_DESIGN` |
| P1 | Identidad efectiva y separación de deberes | Operaciones sensibles, independencia y política de aprobación definidas | `PARTIAL_DESIGN` |
| P1 | Tres amenazas de alcance parcial | Aprobar o rechazar `O-TH008`, `O-TH017`, `O-TH014` con política de numeración | `PROPOSED_ONLY` |
| P1 | Cobertura CommonMark de HEAD | Parser independiente, fixtures, política de anchors/directorios, informe versionado | `NOT_RUN` |
| P2 | Normalización de 29 informes históricos | Mantener cortes SHA y límites, sin reescribir evidencias pasadas | `INDEXED` |

## 4. Criterio de cierre editorial

Se puede cerrar **la organización de los 29 informes** mediante este índice; **no** se puede declarar cierre de seguridad, gobernanza, integridad de enlaces ni ausencia de contradicciones de todo el repositorio. Los siguientes cambios documentales deben atacar un pendiente de la tabla o una contradicción nueva comprobada, no generar un informe redundante.

**Estado final:** `REPORTS_INDEXED = 29`; `GLOBAL_CONSISTENCY_CERTIFIED = NO`; `TESTS_EXECUTED = 0` en esta iteración; `MERGE = NO`; `HOLD / NO-GO`.

## Muestreo incremental de enlaces sobre HEAD posterior (26-10-2026)

**Corte inspeccionado:** `c67b90f8cd5607350ba752dcb426db2187df4987`. Se cotejaron contra el árbol GitHub de ese commit las referencias con forma `] (destino)` —sin el espacio, expresión regular simple— de siete documentos: `docs/03-preimplementacion/README.md`, `docs/02-diseno/security/{verification-plan,traceability,authorization-matrix}.md`, `docs/03-preimplementacion/finch-consistency-decision-register-2026-10-23.md`, `docs/04-auditorias/{readiness-assessment,gap-register}.md`.

**Observación reproducible dentro de ese alcance:** 74 coincidencias de referencias relativas aparentes; 6 destinos no encontrados en el árbol como blobs: `ruta` (dos apariciones), `destino`, `archivo.md`, `img.png`, `no-existe.md`. Las seis coincidencias aparecen en el registro Finch de consistencia, cuyo texto explica expresamente que son ejemplos históricos literales de rutas inexistentes. **No se acredita que sean enlaces activos rotos.** El conteo es de coincidencias regex, no de nodos Markdown.

**Límites:** no se inspeccionaron todos los 129 archivos Markdown del corte; no se resolvieron anchors, directorios, referencias definidas, HTML, escapes ni la semántica CommonMark. El estado del chequeo integral sigue **PENDIENTE / NOT VERIFIED**; no extrapolar el muestreo a un `PASS` global ni mezclarlo con los conteos congelados de otros SHA. Este muestreo no requirió ejecutar código del repositorio ni alterar archivos de producción.
