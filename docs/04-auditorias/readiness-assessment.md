# Evaluación de preparación y gates (Readiness Assessment) — THE MACHINE

**Fecha de auditoría:** Octubre de 2026
**Auditor independiente:** Team de Auditoría Técnica Independiente (Jules)
**Estado:** Informe de preparación / Evaluación de gates

---

## 1. Resumen de evaluación

El objetivo de este documento es evaluar el grado de preparación de **THE MACHINE** para aportar un juicio técnico independiente sobre un eventual primer experimento de prueba de concepto en Rust (*vertical slice A: laboratorio offline de dos sensores*), contrastando los criterios documentados en `docs/02-diseno/security/security-gates.md` y `docs/03-preimplementacion/readiness-review.md`.

*Aclaración de autoridad*: El veredicto de este informe constituye la **recomendación técnica del auditor**. La autorización efectiva para iniciar cualquier desarrollo en código corresponde de forma exclusiva a la decisión del titular o gobernanza del proyecto.

---

## 2. Evaluación detallada por Gate (G0 - G5)

| Gate | Criterios Oficiales de Aceptación | Evidencia Inspeccionada | Evaluación Actual de Auditoría | Justificación Detallada |
|---|---|---|---|---|
| **G0** Documentación | Problema, activos, datos, límites de confianza y uso indebido descritos. | `README.md`, `PHILOSOPHY.md`, `GLOSSARY.md`, `docs/00-empezar/`, `docs/02-diseno/security/threat-model-v0.md`. | **PARCIAL** (Alineado con `readiness-review.md`) | La documentación filosófica y de partida existe. Sin embargo, se clasifica como PARCIAL porque los activos concretos y el alcance exacto del producto mínimo requieren formalización final por el titular. |
| **G1** Investigación | Fuentes contrastadas, alternativas analizadas, riesgos identificados. | `docs/01-investigacion/`, `architecture-review.md`, `research-evidence.md`. | **PARCIAL / BLOQUEADO EN RED** | Existen estudios preliminares y comparación de alternativas (Opciones A, B, C, D). No obstante, la contrastación externa por red estuvo BLOQUEADA en esta auditoría, y los experimentos de investigación están pendientes de validación en código. |
| **G2** Diseño | ADRs en estado Accepted, contratos de datos definidos, matriz de permisos y plan de pruebas negativas. | `docs/02-diseno/adr/`, `docs/02-diseno/security/requirements.md`, `traceability.md`. | **BLOQUEADO** | Los 5 ADRs continúan en estado `Proposed`. La matriz de seguridad presenta 3 amenazas sin prueba asignada (`GAP-002`) para el diseño global. Faltan contratos de datos definitivos aprobados. |
| **G3** Implementación | Código Rust compilable, tests unitarios, análisis estático sin advertencias. | Árbol del repositorio. | **NO INICIADO** | No se ha escrito código Rust. Inexistencia de archivos `.rs`. |
| **G4** Despliegue | Sandbox verificado, pruebas de estrés y recuperación. | N/A | **NO INICIADO** | Requiere fase G3. |
| **G5** Operación | Monitorización, rotación de claves, respuesta a incidentes. | N/A | **NO INICIADO** | Inaplicable en estado actual. |

---

## 3. Recomendación del auditor y estado del proyecto

- **ESTADO VIGENTE DEL PROYECTO**: **HOLD / NO-GO para escribir código**.
- **RECOMENDACIÓN DEL AUDITOR**: **CONDITIONAL GO (Recomendación condicionada exclusivamente para evaluar un experimento minimalista offline)**.

---

## 4. Condiciones bajo las cuales el titular podría evaluar una autorización

Si el titular del proyecto decide considerar la recomendación del auditor para autorizar un experimento minimalista offline de dos sensores que se contradicen (`docs/03-preimplementacion/vertical-slice-a.md`), se sugiere requerir previamente el cumplimiento de las siguientes condiciones:

1. **Clarificación del alcance de la prueba**: Definir explícitamente que el experimento `vertical-slice-a` es un ejecutable local desconectado sin red, sin persistencia en disco y sin pasarela de herramientas externas.
2. **Decisión de gobernanza sobre la licencia (GAP-001)**: Definir la política de licenciamiento antes de publicar o distribuir el código resultante.
3. **Formalización del contrato del experimento**: Aprobar el esquema de estructuras de datos sintéticas necesarias para representar la lectura de los dos sensores sin presuponer la adopción definitiva de la Opción A o B para todo el proyecto.
4. **Revisión de seguridad del corte vertical**: Confirmar que el ejecutable del experimento no abre sockets ni invoca comandos del sistema host.

---

## 5. Alcance y restricciones

Mientras no exista una decisión expresa de autorización emitida por el titular del proyecto:
- El proyecto permanece en **HOLD / NO-GO para código**.
- Queda prohibido añadir archivos de código funcional Rust, crates o flujos de integración continua al repositorio.
- Cualquier autorización posterior dependerá de la decisión del titular y se limitará estrictamente al experimento local e in-memory evaluado.
