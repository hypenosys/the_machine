# Matriz de trazabilidad y cobertura — v0

**Estado: revisión documental, no auditoría de seguridad.**

## Cobertura nominal de amenazas
- TH-001..TH-011 y TH-013..TH-020 tienen al menos un requisito propuesto en [requirements.md](requirements.md).
- TH-012 se vincula a SEC-REQ-017 y a la prueba candidata SEC-017, **PROPUESTA / NO EJECUTADA**.
- TH-016 se vincula a SEC-REQ-015 y a la prueba candidata SEC-015, **PROPUESTA / NO EJECUTADA**.
- TH-019 se vincula a SEC-REQ-016 y a la prueba candidata SEC-016, **PROPUESTA / NO EJECUTADA**.
- Los escenarios de permisos y egress necesitan controles operativos concretos antes de que puedan probarse.
- El listado de 20 amenazas no es exhaustivo: requiere nueva revisión por arquitectura y despliegue.

## Trazabilidad adicional propuesta (no validación)

| Amenaza | Requisito | Prueba candidata | Estado de prueba | Cobertura pretendida |
|---|---|---|---|---|
| TH-012 | SEC-REQ-017 | SEC-017 | PROPOSED / NOT RUN | Delegación sin confused deputy |
| TH-016 | SEC-REQ-015 | SEC-015 | PROPOSED / NOT RUN | Restauración de backup sintético |
| TH-019 | SEC-REQ-016 | SEC-016 | PROPOSED / NOT RUN | Separación de deberes en cambios sensibles |

No se infiere que la existencia de un enlace cubra operacionalmente una amenaza, ni que SEC-015..017 estén aprobados. Las demás pruebas permanecen sujetas a sus condiciones originales.

## Contratos parciales y falsadores (aclaración documental; no ratificada)

La cobertura nominal de `TH-011 → SEC-REQ-010 → SEC-010` **no** equivale a idempotencia remota: el oráculo actual solo contempla un ejecutor local sintético. Un reintento tras efecto con recibo perdido puede dejar un resultado `UNKNOWN`; sin reconciliación, no debe declararse éxito ni repetirse ciegamente una operación irreversible. `ADR-0004` exige idempotencia o intervención humana, mientras `ADR-0005` exige no duplicar efectos tras reiniciar; su interacción necesita contrato aprobado y evidencia antes de considerarse verificada.

La cobertura `TH-019 → SEC-REQ-016 → SEC-016` es **propuesta, no asignación ratificada**: la columna de prueba de `SEC-REQ-016` permanece `Pendiente`. La matriz de autorización exige separación de deberes para cambiar políticas, pero aún no define identidad efectiva, independencia entre proponente y aprobador, alcance, caducidad ni catálogo de operaciones sensibles. Una aprobación por dos cuentas controladas por el mismo actor no demuestra independencia.

Los [oráculos falsables propuestos](../../04-auditorias/pr33-falsifiable-idempotency-and-separation-contracts-2026-10-23.md) y la [aclaración de la matriz de autorización](authorization-matrix.md) documentan estos límites. **No hay pruebas ejecutadas, contratos ratificados ni gates superados**; se mantiene `HOLD / NO-GO`.

## Brechas entre amenazas del requisito y alcance de la prueba (REV-19)

La vinculación `amenaza → requisito → ID de prueba` no equivale a que el estímulo y el oráculo cubran todas las amenazas de la fila. El [plan de verificación](verification-plan.md) distingue tres brechas documentales: `SEC-REQ-006 / TH-008` (más allá del caso de contradicción epistemológica `SEC-006`), `SEC-REQ-008 / TH-017` (plazos y copias frente a supresión sintética `SEC-008`) y `SEC-REQ-011 / TH-014` (corte de energía frente a truncamiento local `SEC-011`).

**Estado:** `THREAT_TO_REQUIREMENT_LINK = PRESENT`, `THREAT_TO_TEST_ORACLE_SUFFICIENCY = OPEN` para esas tres amenazas. Existen tres [oráculos candidatos de falsación](../../04-auditorias/pr33-three-partial-threat-falsification-oracles-2026-10-23.md): `O-TH008`, `O-TH017` y `O-TH014`; sus identificadores no son pruebas `SEC-###` ratificadas. No hay evidencia de pruebas ejecutadas. No se han reasignado identificadores ni ratificado pruebas. `HOLD / NO-GO`.

## Estados separados
| Estado | Significado |
|---|---|
| PROPOSED | Documento o idea en evaluación |
| DESIGNED | Contrato aprobado y revisado |
| IMPLEMENTED | Código presente, sin evidencia suficiente |
| TESTED | Prueba ejecutada con evidencia, resultado explícito |
| VERIFIED | Cumple el criterio bajo el alcance y entorno documentados |
| BLOCKED | Faltan decisiones, herramientas o datos |
| FAILED | Resultado contradice el requisito |

## Gates
G0/G1: documentación e investigación; G2: diseño; G3: implementación; G4: despliegue; G5: operación. Ningún gate queda automáticamente superado por fusionar documentos.

> **Aclaración de trazabilidad (23-10-2026, propuesta no ratificada):** «G3: implementación» es una etiqueta de fase en esta matriz, no una definición suficiente del control ni una autorización. [security-gates.md](security-gates.md) establece históricamente G3 antes de fusionar código ejecutable; el [protocolo por etapas](../../03-preimplementacion/staged-authorization-protocol-v1.md) propone G3 antes de iniciar Rust. La [propuesta DEC-GATE-003](../../03-preimplementacion/finch-gap010-g3-ratification-package-candidate-2026-10-23.md) conservaría el control pre-merge y separaría `AUT-CODE`, `AUT-EXEC` y `AUT-MERGE`. Ninguna propuesta está ratificada; **HOLD / NO-GO**. La cobertura nominal de amenazas no acredita ejecución ni superación de pruebas.


## Política de revisión
Antes de aceptar un ADR, comprobar que cada amenaza relevante tiene al menos un requisito y cada requisito tiene una prueba negativa. La cobertura de enlaces es necesaria pero no suficiente.
