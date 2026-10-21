# Evaluación de preparación y gates (Readiness Assessment) — THE MACHINE

**Fecha de auditoría:** Octubre de 2026
**Auditor independiente:** Team de Auditoría Técnica Independiente (Jules)
**Estado:** Final / Entregable de Auditoría

---

## 1. Resumen de evaluación

El objetivo de esta evaluación es determinar si **THE MACHINE** cumple con los requisitos y condiciones necesarias para superar la fase de preimplementación y autorizar la creación del primer prototipo experimental en Rust (*vertical slice offline*).

La evaluación se basa en el examen riguroso de evidencias directas (*Evidence-First*), descartando supuestos no probados o declaraciones intencionales no respaldadas por artefactos verificables.

---

## 2. Estado de evaluación de los Readiness Gates (G0 - G5)

| Gate | Denominación | Criterios de Aceptación | Evidencia Inspeccionada | Estado | Justificación del Estado |
|---|---|---|---|---|---|
| **G0** | Documentación de Problema y Principios | Definición clara de misión, alcance, no-objetivos y principios operativos. | `README.md`, `PHILOSOPHY.md`, `GLOSSARY.md`, `AGENTS.md`. | **PASS** | Documentación conceptual y filosófica completa y coherente. |
| **G1** | Investigación y Fuentes | Identificación de estándares, alternativas arquitectónicas y análisis de riesgos. | `docs/01-investigacion/`, `research-evidence.md`. | **PASS** | Análisis de alternativas B/C/D y contraste con estándares (NIST, OWASP, W3C) completados. |
| **G2** | Diseño y Contratos de Datos | ADRs aprobados, contratos de datos unificados, matriz de trazabilidad de seguridad completa. | `docs/02-diseno/`, `docs/03-preimplementacion/`. | **FAIL** | Los 5 ADRs permanecen en `Proposed` (GAP-005). La matriz de seguridad tiene 3 amenazas sin prueba asignada (GAP-002). Falta licencia legal (GAP-001). |
| **G3** | Implementación de Código | Código Rust compilable, tests unitarios, análisis estático (clippy/cargo-audit) y sin `unsafe`. | Árbol de archivos del repositorio. | **NOT ASSESSED** | Bloqueado deliberadamente por instrucción de gobernanza previa a este gate. Zero líneas de código. |
| **G4** | Despliegue y Pruebas Adversariales | Sandbox verificado, pruebas de estrés y recuperación ante fallos en entorno de laboratorio. | N/A | **NOT ASSESSED** | Requiere fase G3 completada. |
| **G5** | Operación y Mantenimiento | Monitorización, rotación de claves, respuesta a incidentes operativa. | N/A | **NOT ASSESSED** | Inaplicable en estado actual. |

---

## 3. Dictamen independiente y veredicto

### VEREDICTO DE AUDITORÍA: **CONDITIONAL GO (Para prototipo experimental aislado)** / **NO-GO (Para implementación de producción o arquitectura Opción A)**

---

## 4. Condiciones obligatorias para autorizar el primer archivo Rust (`main.rs` / `lib.rs`)

Para transformar el **CONDITIONAL GO** en una autorización efectiva de código para el primer corte vertical (*offline proof-of-concept*), el proyecto debe cumplir estrictamente las siguientes **5 condiciones previas**:

1. **Resolución de Licencia (GAP-001)**:
   Añadir el archivo `LICENSE` (Dual MIT / Apache-2.0 o equivalente libre) en la raíz del repositorio.
2. **Adopción de la Arquitectura Simplificada (GAP-006)**:
   Aprobar formalmente la **Opción B** (`architecture-review.md`), descartando la sobreingeniería de las 6 entidades rígidas y adoptando la estructura basada en `Artifact` + `Attestation`.
3. **Cierre de Brechas de Seguridad P1 (GAP-002 y GAP-004)**:
   Asignar especificaciones de prueba a las amenazas TH-012, TH-016 y TH-019 en `verification-plan.md` e incorporar la firma/HMAC de capacidades en reposo.
4. **Aprobación de ADR-0001, ADR-0002 y ADR-0004 (GAP-005)**:
   Cambiar el estado de los ADRs fundamentales de `Proposed` a `Accepted` mediante registro de decisión en `docs/02-diseno/adr/README.md`.
5. **Aprobación del Mapa de Autoridad Documental (GAP-010)**:
   Marcar `contract-authority-map.md` como el estándar normativo vigente para evitar especificaciones contradictorias.

---

## 5. Qué autoriza y qué NO autoriza este veredicto

- **SÍ AUTORIZA (Una vez cumplidas las 5 condiciones previas)**:
  - Crear una única *crate* local de Rust (`the_machine_core`) totalmente desconectada de la red (`#![no_std]` o `std` básico).
  - Implementar únicamente el experimento de demostración offline (dos sensores con lecturas contradictorias y verificación de firma/hash en local).
  - Validar el rendimiento del parseo de datos sintéticos.

- **NO AUTORIZA**:
  - Abrir sockets de red o conectores remotos.
  - Exponer pasarelas de herramientas al sistema operativo host fuera del sandbox.
  - Promocionar el proyecto a versión "producción" o "v1.0".
  - Añadir dependencias de terceros sin auditoría previa (`cargo-audit`).
