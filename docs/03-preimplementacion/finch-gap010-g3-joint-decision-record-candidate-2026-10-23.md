# Acta candidata de decisión conjunta — DEC-GOV-010 y DEC-GATE-003

**Estado:** `READY_FOR_OWNER_REVIEW / NOT_RATIFIED`. **Fecha de preparación:** 2026-10-23. **PR:** #33, rama `docs/finch-consistency-consolidation-20261023`. **Corte de referencia previo a esta acta:** `c5b47d66f1e4b0dac6efb6706d75056922044a6e`. **No contiene firmas, votos ni permisos.**

## Objeto exacto sometido a revisión

**DEC-GOV-010 — propuesta de competencia y precedencia.** Se solicita decidir si se acepta la cláusula A–E del [paquete Finch](finch-gap010-g3-ratification-package-candidate-2026-10-23.md): jerarquía por estado, competencia y alcance; delegación revocable a `@Axlfc` para coordinación y decisiones técnicas ordinarias **no normativas**; materias reservadas a ambos titulares; objeción, revocación y prueba de autoridad. La aceptación no debe interpretarse como permiso de implementación ni como delegación de decisiones reservadas.

**DEC-GATE-003 — propuesta de reconciliación G3.** Se solicita decidir si se conserva `G3` como control **pre-merge** de código ejecutable según `docs/02-diseno/security/security-gates.md`, y se diferencian actos `AUT-CODE`, `AUT-EXEC` y `AUT-MERGE` independientes. El uso de G3 como puerta previa a iniciar Rust en `staged-authorization-protocol-v1.md` seguiría como antecedente histórico candidato hasta que una decisión competente autorice actualizar coordinadamente los textos. Aprobar esta nomenclatura **no concede ninguno de los tres permisos**.

## Protocolo mínimo de registro propuesto

1. Ambos titulares deben acordar cómo se acredita identidad y consentimiento; no se presume que la revisión de PR por sí sola cumpla esa función.
2. Antes de cualquier aceptación, identificar el **commit exacto del paquete Finch** (blob/documento) y el **commit exacto de esta acta**. Los commits de preparación no son firmas.
3. Registrar por separado `DEC-GOV-010` y `DEC-GATE-003`: `ACCEPT / REQUEST_CHANGES / REJECT / ABSTAIN`, motivación y reservas, por cada titular. El silencio no es voto.
4. La aceptación de la delegación por `@Axlfc`, su ámbito, caducidad/revisión y revocación deben ser explícitos. Si las declaraciones discrepan, `PENDING` y `HOLD` para la materia afectada.
5. Designar quién comprueba independencia y autenticidad de las declaraciones, cómo se registra supersesión y desde cuándo surtiría efecto la decisión. Una misma persona no debe certificarse como revisor independiente de su propia declaración.
6. Conservar el historial de propuestas y evidencias ambiguas sin atribuirles efectos retroactivos.

## Campos de decisión — deliberadamente sin rellenar

| Campo | DEC-GOV-010 | DEC-GATE-003 |
|---|---|---|
| Versión exacta del texto revisado | PENDIENTE | PENDIENTE |
| @Axlfc — decisión atribuible y alcance | PENDIENTE | PENDIENTE |
| @TopperH4rley — decisión atribuible y alcance | PENDIENTE | PENDIENTE |
| Mecanismo de identidad y consentimiento aceptado | PENDIENTE | PENDIENTE |
| Revisión independiente acreditada | PENDIENTE | PENDIENTE |
| Fecha de efecto y revisión | PENDIENTE | PENDIENTE |
| Reservas / conflictos / revocación | PENDIENTE | PENDIENTE |
| Estado normativo | **NOT_RATIFIED** | **NOT_RATIFIED** |

## Declaración modelo para publicación por cada titular

> Identificándome como cotitular `@USUARIO` de THE MACHINE, he revisado el paquete Finch `finch-gap010-g3-ratification-package-candidate-2026-10-23.md` en el commit `SHA_EXACTO` y esta acta en `SHA_EXACTO`. Mi decisión sobre `DEC-GOV-010` es `ACEPTO / SOLICITO CAMBIOS / RECHAZO`; sobre `DEC-GATE-003` es `ACEPTO / SOLICITO CAMBIOS / RECHAZO`. Mis reservas y condiciones son: `...`. Reconozco que esta declaración **no** autoriza escribir, compilar, ejecutar, fusionar ni desplegar código. Fecha: `...`.

**Nota:** este modelo solo facilita una manifestación atribuible; el método de autenticación, acuerdo conjunto y revisión independiente continúa pendiente de aceptación competente. No insertar respuestas simuladas en nombre de los titulares.

## Condición de cierre

`GAP-010` y `G3` solo pasarán a `RATIFIED` tras verificar identidad, alcance, versión, autoridad, aceptación de ambos titulares según el mecanismo acordado, reservas, independencia y fecha de efecto. **No** cerrar por un `APPROVED` de PR o un comentario `OK` sin alcance inequívoco.

**Efecto actual:** `HOLD / NO-GO`; `AUT-CODE = NOT_GRANTED`; `AUT-EXEC = NOT_GRANTED`; `AUT-MERGE = NOT_GRANTED`; `DEC-08 = NOT_GRANTED`; `G2.2 = BLOCKED`. No se autoriza merge.
