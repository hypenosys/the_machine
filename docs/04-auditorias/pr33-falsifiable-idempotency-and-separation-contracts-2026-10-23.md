# PR #33 — criterios falsables para contratos parciales SEC-REQ-010 y SEC-REQ-016

**Corte de referencia:** `e1c9a3c3ad6037ad4bfd340335722aa08d2107c8`. **Naturaleza:** diseño de oráculos y decisiones pendientes, **no** pruebas ejecutadas ni autorización de implementar. Basado en `requirements.md`, `verification-plan.md`, `ADR-0001`, `ADR-0004`, `ADR-0005` y la adjudicación semántica precedente. `HOLD / NO-GO`.

## C-01 — Reintentos, replay y efectos irreversibles (`SEC-REQ-010`, `TH-011`, `ADR-0004/0005`)

**Garantía mínima candidata (offline/local):** para una misma operación identificada inequívocamente, repetir solicitudes o reiniciar el proceso no debe producir más de un efecto local irreversible observable, siempre que el registro de idempotencia sobreviva al reinicio conforme a las precondiciones declaradas.

**Variables que deben fijarse antes de una prueba:** identidad del actor, recurso, huella canónica de parámetros, clave de idempotencia, vigencia y ámbito de la clave, semántica de revocación, límites de persistencia, punto de efecto y observador independiente. La misma clave con parámetros diferentes debe ser rechazada como conflicto, no reutilizada silenciosamente.

**Oráculo falsable candidato:**
- O-01A: solicitud inicial válida → un efecto local observable y recibo atribuible; reintento idéntico → cero efectos adicionales.
- O-01B: reinicio después de persistir el resultado → reintento idéntico → cero efectos adicionales; si la persistencia no está garantizada, resultado **INCONCLUSIVE**, no `PASS`.
- O-01C: misma clave con otro objetivo o parámetros → `REJECTED_CONFLICT`, cero nuevos efectos.
- O-01D: expiración/revocación antes de un nuevo efecto → denegación; no asumir reversión de efectos completados.
- O-01E: caída entre efecto y recibo, si no existe transacción atómica que cubra ambos → estado `UNKNOWN`, reconciliación y prohibición de reintento ciego; no afirmar exactly-once.

**Falsador:** dos efectos locales por una sola operación canónica en el alcance ensayado, o declarar éxito sin recibo verificable. **Exclusiones:** APIs remotas, confirmaciones perdidas, exactly-once distribuido y efectos físicos; requieren contrato aparte y no se autorizan aquí.

## C-02 — Separación de deberes en cambios sensibles (`SEC-REQ-016`, `TH-019`, `ADR-0001/0004`)

**Garantía mínima candidata:** una modificación de política de autorización, concesión de privilegios, desactivación de auditoría o cambio de retención **clasificado previamente como sensible** no puede ser solicitada y aprobada por la misma identidad efectiva, ni aplicada antes de que exista aprobación independiente válida.

**Decisiones pendientes:** inventario exacto de operaciones sensibles; autoridad de proponente y aprobador; autenticación de identidades y representación de delegación; número de aprobadores; vigencia de la aprobación; quorum, conflicto de intereses, revocación, recuperación de emergencia y trazabilidad con privacidad. Ninguna queda ratificada por este documento.

**Oráculo falsable candidato:**
- O-02A: identidad `A` propone y `A` aprueba → `DENY`, cero cambios aplicados.
- O-02B: `A` propone, `B` aprueba pero `B` es una delegación o alias efectivo de `A` → `DENY` salvo política de equivalencia aprobada que realmente preserve independencia; no basta comparar nombres de usuario.
- O-02C: `A` propone, `B` independiente aprueba, pero la aprobación ha caducado o fue revocada → `DENY`.
- O-02D: falta evidencia verificable de identidad o independencia → `DENY/INCONCLUSIVE` según la política de evaluación, **nunca** `PASS` por defecto.
- O-02E: `A` propone y `B` independiente aprueba con alcance y versión de política válidos → **solo** candidato a autorización; debe pasar el resto de controles de gateway y no implica ejecución automática.

**Falsador:** aplicar un cambio sensible con aprobación de la misma identidad efectiva, sin aprobación válida, o usando una aprobación de alcance diferente. **Exclusiones:** no se presume resistencia frente a colusión, administrador de infraestructura omnipotente, robo de credenciales o compromiso del verificador.

## C-03 — Vinculación entre ambas garantías

Una aprobación separada no resuelve idempotencia; una clave de idempotencia no otorga autoridad. Para operaciones sensibles con efectos irreversibles, el oráculo compuesto exige **autorización independiente válida en el punto de uso** y **ausencia de duplicación de efecto**. El fallo de cualquiera de las dos condiciones invalida el resultado positivo compuesto.

## Estado y gate

| Elemento | Estado |
|---|---|
| Criterios y falsadores | **PROPOSED / DOCUMENTED** |
| Oráculos ratificados por cotitulares | **NO** |
| Harness, código y pruebas ejecutadas | **NO** |
| `SEC-010` / `SEC-016` superadas | **NO** |
| Implementación / ejecución / merge autorizados | **NO** |

Estos criterios refinan los tres enlaces parciales previamente detectados: `SEC-REQ-010 ↔ ADR-0005` y `SEC-REQ-016 ↔ ADR-0001/0004`. No modifican el texto ni el estado `Proposed` de ningún ADR.
