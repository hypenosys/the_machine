# Registro de decisiones de arquitectura (ADR)

Un ADR es una decisión técnica revisable, no una orden irrevocable. Este índice es la **fuente de verdad del estado de las decisiones**.

## Estados
- **Proposed**: pendiente de investigación y revisión; NO autoriza implementación.
- **Accepted**: decisión aprobada con evidencia y criterios de verificación.
- **Superseded**: sustituida por otro ADR; mantener el historial.
- **Rejected**: alternativa descartada, con motivos.
- **Deprecated**: vigente solo para compatibilidad temporal.

## Índice
| ID | Tema | Estado |
|---|---|---|
| [0001](0001-security-first-trust-boundaries.md) | Límites de confianza y seguridad desde el inicio | Proposed |
| [0002](0002-rust-dependency-minimization.md) | Rust, dependencias y cadena de suministro | Proposed |
| [0003](0003-evidence-and-epistemic-integrity.md) | Integridad epistémica y procedencia | Proposed |
| [0004](0004-authorization-and-action-gateway.md) | Autorización de acciones y separación del LLM | Proposed |
| [0005](0005-logging-recovery-and-data-lifecycle.md) | Auditoría, recuperación y ciclo de vida de datos | Proposed |

## Plantilla profesional
Cada ADR incluye contexto, decisión, alternativas, consecuencias, supuestos, activos y amenazas, controles, invariantes, requisitos trazables, plan de migración, verificación, criterios de revisión y referencias. No se aprueba un ADR sin revisión técnica y de seguridad independientes. Nunca cambiar un ADR Accepted retroactivamente: crear uno nuevo que lo sustituya.

[Modelo para nuevos ADR](TEMPLATE.md) · [Modelo de amenazas](../security/threat-model-v0.md)
