# PR #33 — discrepancias nominales requisito ↔ ADR ↔ amenaza

**Corte:** `b3bfda71cc9137ca43b342a36dd33487c0dbcbcc`. **Fuentes:** tabla de `docs/02-diseno/security/requirements.md` y sección `## Amenazas` de cada ADR-0001…0005. Comparación literal de IDs, **no** juicio sobre suficiencia semántica. `HOLD / NO-GO`.

## Resultado

Se identificaron **23 asociaciones requisito–ADR**. En **9** de ellas, al menos una amenaza asignada al requisito **no aparece identificada literalmente** en el ADR citado. El ADR existe en todos los casos; se trata de un vacío de *cross-reference* y no de un archivo roto.

| Requisito | ADR | Amenaza del requisito ausente en la enumeración ADR | Lectura preliminar |
|---|---|---|---|
| `SEC-REQ-001` | `ADR-0004` | `TH-001` | Gateway trata propuestas del modelo como datos no confiables, pero no enumera TH-001 |
| `SEC-REQ-008` | `ADR-0003` | `TH-017` | Política de privacidad y borrado tratada, sin ID de retención fuera de plazo |
| `SEC-REQ-008` | `ADR-0005` | `TH-009` | Retención/minimización tratadas, sin ID TH-009 |
| `SEC-REQ-010` | `ADR-0005` | `TH-011` | Reinicio y efectos externos tratados, sin ID de replay |
| `SEC-REQ-013` | `ADR-0002` | `TH-018` | Dependencias y cadena de suministro tratadas, sin ID de dependencia comprometida |
| `SEC-REQ-014` | `ADR-0001` | `TH-020` | Salidas de modelos tratadas como no confiables, sin ID de modelo comprometido |
| `SEC-REQ-014` | `ADR-0004` | `TH-020` | Modelo no concede permisos, sin ID TH-020 |
| `SEC-REQ-016` | `ADR-0001` | `TH-019` | Aprobación independiente de acciones sensibles, sin ID de insider abuse |
| `SEC-REQ-016` | `ADR-0004` | `TH-019` | Aprobación adicional prevista, sin ID TH-019 |

## Adjudicación

- `ADR_TARGET_EXISTS = 23/23` (integridad de ruta, comprobada anteriormente).
- `ADR_THREAT_ID_MATCH = 14/23` y `ADR_THREAT_ID_GAP = 9/23` **bajo el criterio literal** de que cada ADR citado enumere todas las amenazas del requisito.
- Este criterio es una propuesta de consistencia documental, **no** una obligación de diseño previamente ratificada. Un ADR puede ser relevante para un requisito sin enumerar todas sus amenazas; por tanto **no** se declara que haya nueve errores de seguridad ni nueve contradicciones semánticas.
- La corrección mínima candidata es añadir trazabilidad explícita y justificada (por ejemplo, una matriz `ADR ↔ TH ↔ SEC-REQ`) **sin reescribir ni ratificar unilateralmente los ADR Proposed**. Cualquier asociación no justificada debe discutirse, no añadirse mecánicamente.
- `SEC-015..017` siguen propuestas, no ejecutadas. Este análisis no modifica puertas de implementación ni de merge.

**Estado:** `NOMINAL_TRACEABILITY_GAPS_FOUND = 9`; `SECURITY_CONTROL_VERIFICATION = NOT_RUN`; `HOLD / NO-GO`.
