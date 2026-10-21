# Fuentes y evidencias de investigación técnica — THE MACHINE

**Fecha de auditoría:** Octubre de 2026
**Auditor independiente:** Investigador de Inteligencia Artificial y Epistemología Computacional (Jules)
**Estado:** Final / Entregable de Auditoría

---

## 1. Resumen y política de investigación

El presente documento registra el contraste de las decisiones técnicas y de diseño de **THE MACHINE** frente a la literatura técnica primaria, marcos normativos internacionales y estándares del ecosistema de software libre.

En estricto cumplimiento de los principios **Evidence-First** y **Zero Fabrication**:
1. Se declara expresamente que la consulta activa de internet a través de la red durante la auditoría ha estado en estado **BLOQUEADO** debido a las restricciones del entorno de ejecución aislado.
2. La investigación técnica y el contraste de diseño se basan en la base de conocimientos validados previamente por el equipo de auditoría, citando fuentes primarias oficiales y estándares reconocidos internacionalmente.
3. No se inventan URLs, fechas de consulta ni resultados de búsqueda que no hayan sido verificados.

---

## 2. Marco de estándares y literatura de referencia

A continuación se indexan las referencias estándar utilizadas para contrastar las decisiones de arquitectura, seguridad y procedencia de datos en THE MACHINE:

### 2.1. Seguridad en IA y Sistemas Generativos
- **NIST AI Risk Management Framework (AI RMF 1.0 / NIST SP 800-53)**:
  *Organismo*: National Institute of Standards and Technology (EE. UU.).
  *Aplicabilidad a THE MACHINE*: Proporciona la estructura de Gobernanza, Mapeo, Medición y Gestión de riesgos de IA. Respalda la decisión de aislar las salidas del LLM en un entorno no confiable (*untrusted proposal*).
- **OWASP Top 10 for LLM Applications (v1.1 / v2.0)**:
  *Organismo*: Open Web Application Security Project.
  *Aplicabilidad a THE MACHINE*: Justifica los requisitos `SEC-REQ-001` (Prompt Injection - LLM01), `SEC-REQ-003` (Excessive Agency - LLM08) y `SEC-REQ-004` (Unsecured Egress).
- **MITRE ATLAS™ (Adversarial Threat Landscape for Artificial-Intelligence Systems)**:
  *Organismo*: MITRE Corporation.
  *Aplicabilidad a THE MACHINE*: Mapeo de vectores de ataque adversariales sobre el modelo y la memoria persistente (`TH-001`, `TH-006`).

### 2.2. Seguridad de Software y Cadena de Suministro
- **SLSA (Supply-chain Levels for Software Artifacts - Level 3/4)**:
  *Organismo*: OpenSSF (Open Source Security Foundation).
  *Aplicabilidad a THE MACHINE*: Sustenta la política de minimización de dependencias en Rust (`ADR-0002`), compilación reproducible y *vendoring* estricto.
- **The Rustonomicon & Rust Reference**:
  *Organismo*: Rust Core Team / Security Working Group.
  *Aplicabilidad a THE MACHINE*: Garantías de seguridad de memoria (*memory safety*), usabilidad de `#![no_std]` y diseño de abstracciones sin costo (*zero-cost abstractions*) sin uso de `unsafe` no verificado.

### 2.3. Epistemología Computacional y Procedencia de Datos
- **W3C PROV-DM (PROV Data Model - W3C Recommendation)**:
  *Organismo*: World Wide Web Consortium (W3C).
  *Aplicabilidad a THE MACHINE*: Modelo estándar de procedencia basado en `Entity`, `Activity` y `Agent`. Se utiliza en `architecture-review.md` para contrastar y demostrar que el núcleo ontológico candidato de THE MACHINE (`Source`, `Artifact`, `Claim`, etc.) puede simplificarse adoptando primitivas estándar probadas.
- **Developing Time-Oriented Database Applications in SQL (Richard T. Snodgrass)**:
  *Literatura Académica*: Base conceptual de las bases de datos bitemporales (*Valid Time* vs. *Transaction Time*).
  *Aplicabilidad a THE MACHINE*: Sustenta el hallazgo **GAP-003** sobre la incapacidad del contrato epistemológico actual para manejar retractaciones históricas sin corromper el log inmutable.

---

## 3. Matriz de contraste de decisiones de THE MACHINE vs. Estándares

| Decisión en THE MACHINE | Estándar / Referencia | Resultado del contraste | Dictamen de Auditoría |
|---|---|---|---|
| Minimización estricta de dependencias Cargo (`ADR-0002`) | SLSA Level 3 / OpenSSF | **Alineado**. Reduce drásticamente el riesgo de *typosquatting* y *dependency confusion*. | **Aprobado** (Fundamento sólido). |
| Pasarela de acciones con autorización explícita (`ADR-0004`) | OWASP GenAI LLM08 / NIST SP 800-53 | **Alineado**. Impide que el LLM ejecute comandos en el SO sin intervención del Action Gateway. | **Aprobado** (Diseño robusto). |
| Ausencia de red por defecto (`SEC-REQ-004`) | Local-First / NIST AI RMF | **Alineado**. Maximiza la privacidad y soberanía de datos del usuario local. | **Aprobado**. |
| Núcleo epistemológico de 6 entidades rígidas | W3C PROV-DM / Pragmatismo de Software | **Cuestionado**. Presenta sobreingeniería y complejidad accidental frente a W3C PROV. | **Requiere Rediseño** (Ver Opción B en `architecture-review.md`). |
| Registro de tiempo único (Single Timestamp) | Snodgrass Bitemporal Model | **Incompleto**. Falta *Transaction Time* para gestionar auditoría inmutable de retractaciones. | **Brecha GAP-003** detectada. |

---

## 4. Estado de verificación de la investigación

- **Conocimiento de partida de modelos**: Utilizado para la estructuración y contraste analítico de los ADR y modelos de amenazas.
- **Acceso a red / Web en vivo**: **BLOQUEADO**.
- **Falsación de afirmaciones**: Se confirma que las referencias a estándares citadas en la documentación original de THE MACHINE (NIST, OWASP, MITRE) eran adecuadas en concepto, pero carecían de una matriz de trazabilidad concreta (ahora construida en `security-review.md`).
