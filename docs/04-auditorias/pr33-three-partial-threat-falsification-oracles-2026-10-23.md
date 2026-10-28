# PR #33 — tres oráculos candidatos para amenazas con cobertura parcial (REV-19)

**Base documental:** commit `6efb7da3bf08a6ddf24c160d7d8c29667c406c97`; `docs/02-diseno/security/requirements.md`, `verification-plan.md` y `traceability.md`. **Estado:** `PROPOSED / NOT RUN`. Se trata de extensiones conceptuales sin ID `SEC-###` asignado para evitar colisión con el registro histórico. `HOLD / NO-GO`.

## Candidato O-TH008 — Contradicciones ocultas

**Relación:** `TH-008 → SEC-REQ-006`; `SEC-006` comprueba un conflicto epistemológico concreto, no todos los mecanismos de ocultación.

**Fixture sintético propuesto:** dos afirmaciones sobre el mismo objeto, predicado, unidades y ventana de validez, con valores lógicamente incompatibles y procedencias diferenciadas. Un tercer evento intenta reemplazar una afirmación, alterar su clasificación o presentar una síntesis sin mencionar el conflicto. Separar `valid_time`, `recorded_time` y `assessed_time`.

**Oráculo candidato:** la vista derivada debe preservar la existencia de ambas evidencias, indicar `CONFLICTED` cuando la incompatibilidad esté demostrada y mantener la procedencia de la síntesis. No confundir desacuerdo real con `INSUFFICIENT` o `NOT_COMPARABLE`. La política de supresión autorizada puede exigir borrar datos y prevalece sobre retención de evidencia.

**Falsador:** el sistema presenta una afirmación como única certeza pese a existir otra evidencia comparable e incompatible aún retenible, o elimina sin rastro lógico una contradicción sin una operación autorizada de supresión.

**Precondiciones no resueltas:** representación formal de predicados, ventanas temporales, política de vistas y borrado, observador externo y reglas de comparación. **No demuestra** integridad frente a un administrador que altera el almacenamiento.

## Candidato O-TH017 — Retención indebida

**Relación:** `TH-017 → SEC-REQ-008`; `SEC-008` especifica supresión sintética condicionada a una política, pero no valida automáticamente vencimiento de retención.

**Fixture sintético propuesto:** registros y derivados con tiempos de creación y expiración declarados, dos clases de retención, una excepción de conservación justificada y copias simuladas enumeradas (índice, caché y backup lógico). Reloj controlado y política versionada.

**Oráculo candidato:** al superar el plazo aplicable, la política debe decidir explícitamente qué dato se suprime, se anonimiza de forma irreversible bajo criterios definidos o permanece por excepción autorizada; las copias dentro del alcance deben seguir el resultado de la política. Un resultado `PASS` exige inspección independiente de **todas las copias declaradas dentro del alcance** y justificación de excepciones.

**Falsador:** dato vencido accesible sin excepción válida en una copia incluida en el inventario; excepción aplicada fuera de su finalidad, plazo o autoridad; declarar borrado físico por mera ocultación de interfaz.

**Precondiciones no resueltas:** jurisdicción y base jurídica, clases de datos, plazos, congelación legal, semántica de backups, minimización, tiempo fiable y prueba de borrado. **No demuestra** eliminación de soportes físicos ni cumplimiento normativo general.

## Candidato O-TH014 — Pérdida de energía y recuperación

**Relación:** `TH-014 → SEC-REQ-011`; `SEC-011` contempla truncamiento sintético de un log local, no pérdida física de alimentación.

**Fixture sintético propuesto:** secuencia de eventos con checkpoints, estado duradero confirmado y escrituras pendientes; modelar cortes en puntos predefinidos antes/durante/después de persistir y antes/después del recibo. Para una futura prueba autorizada, distinguir un **simulador determinista de fallos** de un ensayo real de pérdida de energía.

**Oráculo candidato:** tras recuperar, no presentar como confirmado un evento no duradero; recuperar un prefijo verificablemente consistente o abortar explícitamente, sin corrupción silenciosa; si el estado del efecto externo es incierto, etiquetarlo `UNKNOWN` y exigir reconciliación antes de reintentar.

**Falsador:** confirmar un evento ausente del estado recuperado, continuar sobre corrupción indetectada o repetir automáticamente un efecto irreversible cuyo resultado anterior es incierto.

**Precondiciones no resueltas:** modelo de durabilidad, orden de fsync/commit, almacenamiento y filesystem, garantías del hardware, testigo externo, punto de corte y aislamiento. **Una simulación no demuestra resistencia real a un apagón**; la prueba física queda fuera de alcance y no autorizada.

## Reglas de asignación y evidencia

1. Mantener `SEC-006`, `SEC-008` y `SEC-011` sin ampliación retrospectiva de resultados.
2. Reservar nuevos IDs de prueba solo después de cotejar el inventario histórico y obtener aprobación del protocolo de numeración. Los nombres `O-TH008`, `O-TH017` y `O-TH014` son etiquetas **de propuesta**, no tests ratificados.
3. Para cada futuro ensayo, exigir versión de fixture y oráculo, entorno, autoría, revisión, evidencia independiente y resultados `PASS / FAIL / INCONCLUSIVE / NOT_RUN` sin colapsar incertidumbre.
4. Ninguna extensión levanta `GAP-010`, `DEC-GATE-003`, `DEC-08` o `HOLD / NO-GO`.

**Resultado de esta iteración:** `ORACLES_PROPOSED = 3`; `ORACLES_RATIFIED = 0`; `TESTS_EXECUTED = 0`; `IMPLEMENTATION_AUTHORIZED = NO`.
