# PR #33 — adjudicación semántica de nueve asociaciones requisito–ADR

**Fuente congelada:** `3c61ec43e4abb65a7c96339c2a9274938bea24ae`. Se han contrastado el texto de los ADR-0001..0005, `docs/02-diseno/security/requirements.md` y el informe `pr33-adr-threat-nominal-crossref-gaps-2026-10-23.md`. **Naturaleza:** propuesta editorial de justificación, no modificación ni aceptación de ADR; `HOLD / NO-GO`.

## Matriz de adjudicación

| Requisito / amenaza | ADR citado | Texto sustantivo del ADR que permite relacionarlo | Juicio documental |
|---|---|---|---|
| `SEC-REQ-001 / TH-001` | `ADR-0004` | «Una propuesta del modelo es dato no confiable»; el gateway valida identidad, permiso y contexto | **Relación sustantiva plausible**: protege la frontera entre salida del modelo y autoridad; no sustituye la defensa de ingestión de ADR-0001 |
| `SEC-REQ-008 / TH-017` | `ADR-0003` | «Las políticas de privacidad pueden exigir borrado verificable y deben prevalecer sobre la retención»; INV-011 limita retención | **Relación sustantiva explícita** aunque TH-017 no se enumere |
| `SEC-REQ-008 / TH-009` | `ADR-0005` | «Definir retención, rectificación, supresión y minimización antes de persistir información» | **Relación sustantiva explícita** aunque TH-009 no se enumere |
| `SEC-REQ-010 / TH-011` | `ADR-0005` | INV-017: «reiniciar no debe repetir efectos externos»; INV-018: «no declarar éxito sin recibo verificable» | **Relación parcial**: evita repetición por reinicio, pero no demuestra prevención general de replay ni exactly-once remoto |
| `SEC-REQ-013 / TH-018` | `ADR-0002` | Revisión de crates y transitivas, procedencia, builds offline; INV-005 dependencia revisada, INV-006 scripts, INV-007 inventario | **Relación sustantiva explícita**; omisión del ID TH-018 en sección inexistente de amenazas |
| `SEC-REQ-014 / TH-020` | `ADR-0001` | «Tratar ... salidas de modelos ... como no confiables»; INV-003 fallos de validación sin efectos | **Relación sustantiva plausible**, sin promesa de detectar modelo comprometido |
| `SEC-REQ-014 / TH-020` | `ADR-0004` | `ActionProposal` separada de `AuthorizationDecision` y `ExecutionReceipt`; salida del modelo sin autoridad | **Relación sustantiva plausible**, defensa ante efectos, no integridad del modelo |
| `SEC-REQ-016 / TH-019` | `ADR-0001` | INV-004 «las acciones sensibles requieren política y aprobación independiente» | **Relación parcial**: aprobación independiente no especifica todas las funciones administrativas ni separación de deberes completa |
| `SEC-REQ-016 / TH-019` | `ADR-0004` | Gateway requiere «aprobación adicional si procede» | **Relación parcial**: condición discrecional, insuficiente para afirmar separación obligatoria de deberes en cambios sensibles |

## Resolución documental propuesta

- **Seis** asociaciones tienen una relación sustantiva explícita o plausible que justifica conservar la cita del ADR, sin equipararla a mitigación validada: SEC-REQ-001/ADR-0004; SEC-REQ-008/ADR-0003 y /ADR-0005; SEC-REQ-013/ADR-0002; SEC-REQ-014/ADR-0001 y /ADR-0004.
- **Tres** requieren precisar límites del contrato de diseño: SEC-REQ-010/ADR-0005 (replay vs reinicio/idempotencia) y SEC-REQ-016/ADR-0001 y /ADR-0004 (separación de deberes).
- **Cero** cambios automáticos a los ADR: las nueve diferencias son ausencias de referencia literal, no necesariamente errores de arquitectura. Evitar añadir amenazas indiscriminadamente a sus secciones.
- Mantener `SEC-REQ-015..017` y `SEC-015..017` como pruebas propuestas, sin ratificación ni ejecución.

## Criterios de cierre

La cobertura nominal de referencias podrá considerarse explicada editorialmente cuando un revisor acepte la justificación y los límites de cada fila. La **suficiencia de control** seguirá abierta hasta que existan contratos y oráculos aprobados, y la **efectividad** seguirá abierta hasta pruebas reproducibles autorizadas. No confundir estos tres estados.

**Estado:** `NOMINAL_CROSSREF_GAPS = 9` (persisten en texto ADR), `SUBSTANTIVE_EXPLANATIONS_PROPOSED = 9`, `PARTIAL_CONTRACTS = 3`, `ADR_STATUS = PROPOSED`, `HOLD / NO-GO`.
