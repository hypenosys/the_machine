# Evaluación de preparación y gates (Readiness Assessment) — THE MACHINE

**Fecha de auditoría:** Octubre de 2026
**Auditor independiente:** Team de Auditoría Técnica Independiente (Jules)
**Estado:** Informe de preparación / Evaluación de gates

---

## 1. Resumen de evaluación

El objetivo de este documento es evaluar el grado de preparación de **THE MACHINE** para autorizar el primer experimento de prueba de concepto en Rust (*vertical slice A: laboratorio offline de dos sensores*), contrastando los criterios documentados en `docs/02-diseno/security/security-gates.md` y `docs/03-preimplementacion/readiness-review.md`.

---

## 2. Evaluación detallada por Gate (G0 - G5)

| Gate | Criterios Oficiales de Aceptación | Evidencia Inspeccionada | Evaluación Actual de Auditoría | Justificación Detallada |
|---|---|---|---|---|
| **G0** Documentación | Problema, activos, datos, límites de confianza y uso indebido descritos. | `README.md`, `PHILOSOPHY.md`, `GLOSSARY.md`, `docs/00-empezar/`, `docs/02-diseno/security/threat-model-v0.md`. | **PARCIAL** (Alineado con `readiness-review.md`) | La documentación filosófica y de partida existe. Sin embargo, se clasifica como PARCIAL porque los activos concretos y el alcance exacto del producto mínimo requieren formalización final de gobernanza. |
| **G1** Investigación | Fuentes contrastadas, alternativas analizadas, riesgos identificados. | `docs/01-investigacion/`, `architecture-review.md`, `research-evidence.md`. | **PARCIAL / BLOQUEADO EN RED** | Existen estudios preliminares y comparación de alternativas (Opciones A, B, C, D). No obstante, la contrastación externa por red estuvo BLOQUEADA en esta auditoría, y los experimentos de investigación están pendientes de validación en código. |
| **G2** Diseño | ADRs en estado Accepted, contratos de datos definidos, matriz de permisos y plan de pruebas negativas. | `docs/02-diseno/adr/`, `docs/02-diseno/security/requirements.md`, `traceability.md`. | **BLOQUEADO** | Los 5 ADRs continúan en estado `Proposed`. La matriz de seguridad presenta 3 amenazas sin prueba asignada (`GAP-002`) para el diseño global. Faltan contratos de datos definitivos aprobados. |
| **G3** Implementación | Código Rust compilable, tests unitarios, análisis estático sin advertencias. | Árbol del repositorio. | **NO INICIADO** | No se ha escrito código Rust. Inexistencia de archivos `.rs`. |
| **G4** Despliegue | Sandbox verificado, pruebas de estrés y recuperación. | N/A | **NO INICIADO** | Requiere fase G3. |
| **G5** Operación | Monitorización, rotación de claves, respuesta a incidentes. | N/A | **NO INICIADO** | Inaplicable en estado actual. |

---

## 3. Dictamen independiente y veredicto

### VEREDICTO DE AUDITORÍA: **CONDITIONAL GO (Limitado a un prototipo minimalista offline)** / **NO-GO (Para arquitectura de producción o adopción definitiva de Opción A)**

---

## 4. Condiciones para autorizar el primer experimento de código (`vertical-slice-a`)

Para autorizar la creación del primer experimento offline de dos sensores que se contradicen (`docs/03-preimplementacion/vertical-slice-a.md`), el proyecto debe cumplir las siguientes **condiciones simplificadas**:

1. **Clarificación del alcance de la prueba**: Definir explícitamente que el experimento `vertical-slice-a` es un ejecutable local desconectado sin red, sin persistencia en disco y sin pasarela de herramientas externas.
2. **Decisión de gobernanza sobre la licencia (GAP-001)**: Definir la política de licenciamiento antes de publicar o distribuir el código resultante.
3. **Formalización del contrato del experimento**: Aprobar el esquema de estructuras de datos sintéticas necesarias para representar la lectura de los dos sensores sin presuponer la adopción definitiva de la Opción A o B para todo el proyecto.
4. **Revisión de seguridad del corte vertical**: Confirmar que el ejecutable del experimento no abre sockets ni invoca comandos del sistema host.

---

## 5. Alcance de la autorización

- **AUTORIZADO (Tras cumplir las condiciones preliminares del experimento)**:
  - Crear una *crate* local de Rust para simular la ingesta de dos lecturas de sensores contradictorias y comprobar la detección de inconsistencias en memoria.

- **NO AUTORIZADO**:
  - Abrir sockets de red o conectores remotos.
  - Ejecutar herramientas del sistema host.
  - Almacenar datos en bases de datos persistentes sin haber resuelto la especificación de integridad y seguridad de reposo.
  - Promocionar el prototipo como software listo para producción.
