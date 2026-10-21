# Protocolo de Autorización por Etapas y Desacoplamiento de Gates — THE MACHINE (v1)

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Ubicación:** `docs/03-preimplementacion/staged-authorization-protocol-v1.md`
**Carácter:** **CANDIDATO NO NORMATIVO** (Protocolo de gobernanza por etapas; no autoriza código por sí mismo).
**Estado del proyecto:** **HOLD / NO-GO (Cero código ejecutable, cero manifiestos Cargo)**

---

## 1. Principio de Desacoplamiento Estricto y Armonización Histórica de Gates

En resolución directa del **Defecto B-06** y para evitar la colisión con la nomenclatura histórica de readiness gates (`readiness-assessment.md`, `traceability.md`, `auditoria-integral-2026-10.md`), el presente protocolo **mantiene intacta la definición original de Gates G0..G5** y modela el proceso de laboratorio pre-código como **subgates explícitos** dentro del Gate G2 de Diseño.

```
+---------------------------------------------------------------------------------------------------+
| ARMONIZACIÓN DE READINESS GATES G0..G5 Y SUBGATES DE LABORATORIO PRE-CÓDIGO                      |
|                                                                                                   |
|  [G0: Doc/Investigación] -> [G1: Alcance] -> [G2: Diseño & Protocolo Experimental]               |
|                                                     ├── Subgate G2.1: Aprobación Documental       |
|                                                     ├── Subgate G2.2: Laboratorio Acotado (Harness)|
|                                                     ├── Subgate G2.3: Obtención de Evidencia      |
|                                                     └── Subgate G2.4: Selección de Arquitectura   |
|                                                                                                   |
|                                            ↓ (HOLD / NO-GO)                                       |
|  [G3: Implementación Rust] ---------------> [G4: Despliegue] ---------> [G5: Operación]            |
+---------------------------------------------------------------------------------------------------+
```

### Invariantes del Protocolo
1. **G3 es Históricamente la Transición a Código:** Se confirma que **Gate G3 es la puerta de implementación de software en Rust**. Pasar de G2 a G3 exige el cumplimiento total de los requisitos de pre-código y una decisión expresa `GO` del titular.
2. **Sin Transiciones Automáticas:** Ningún subgate dentro de G2 (G2.1, G2.2, G2.3, G2.4) concede autorización automática para pasar a G3 ni para escribir código Rust.
3. **Autoridad Exclusiva:** Toda transición entre gates y subgates exige una decisión de gobernanza explícita, registrada y firmada por el titular del proyecto (@Axlfc).

---

## 2. Definición de Gates Históricos (G0..G5) y Subgates de Laboratorio (G2.1..G2.4)

### Gate G0 — Documentación e Investigación Preliminar
- **Definición Histórica:** Investigación fundacional, filosofía y principios educativos (`readiness-assessment.md`).
- **Estado:** EVALUACIÓN HISTÓRICA CONDICIONAL; la aprobación formal de G0 depende de la ratificación del marco de gates por el titular.

### Gate G1 — Delimitación de Alcance y Especificación Candidate
- **Definición Histórica:** Delimitación de activos, fronteras de confianza y especificaciones candidatas (`readiness-assessment.md`).
- **Estado:** EVALUACIÓN HISTÓRICA CONDICIONAL; la aprobación formal de G1 depende de la ratificación del marco de gates por el titular.

---

### Gate G2 — Diseño de Arquitectura, Modelado de Amenazas y Protocolo Experimental (Estado Actual)
Contiene la fase de consolidación y deliberación pre-código, articulada en cuatro subgates independientes:

#### Subgate G2.1 — Aprobación Documental del Protocolo y Paquete v1
- **Propósito:** Ratificar el marco metodológico, los contratos comparativos, la matriz de trazabilidad y las reglas de deliberación sin autorizar software ni pruebas.
- **Condiciones de Entrada:** Entrega del Paquete de Decisión v1 (`decision-package-v1.md`), Contrato Comparativo v1 (`comparative-contract-v1.md`) y Matriz de Trazabilidad v1 (`traceability-matrix-v1.md`).
- **Evidencia Requerida:** Consistencia interna comprobada, ausencia de contradicciones y ausencia de código ejecutable.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Resultado:** Aprobación del marco documental (**Subgate G2.1 Aprobado**). El proyecto permanece en **HOLD**.

#### Subgate G2.2 — Autorización Expresa para Laboratorio Sintético Acotado (Harness)
- **Propósito:** Conceder permiso acotado y exclusivo para construir y ejecutar el arnés de prueba sintético offline (*Offline Test Harness*) con datos en memoria volátil.
- **Condiciones de Entrada:** Subgate G2.1 formalmente aprobado; delimitación estricta del alcance (cero red, cero persistencia, cero datos reales).
- **Evidencia Requerida:** Orden de ejecución del titular especificando los límites del laboratorio sintético.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Resultado:** Permiso para ejecutar el laboratorio acotado (**Subgate G2.2 GO**). **No autoriza código de producción ni crates definitivos.**

#### Subgate G2.3 — Obtención y Evaluación de Evidencia Experimental Sintética
- **Propósito:** Recopilar y analizar los resultados observables producidos por las alternativas R1, R2, Híbrida C y Baseline D ante los fixtures sintéticos F-01..F-10.
- **Condiciones de Entrada:** Finalización de las corridas sintéticas del laboratorio G2.2.
- **Evidencia Requerida:** Informe de resultados del laboratorio documentando fidelidad, sobrecarga de tipos, comportamiento ante datos incompletos y abstenciones.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Resultado:** Informe de evidencia experimental validado (**Subgate G2.3 Completado**).

#### Subgate G2.4 — Selección Formal de la Arquitectura de Representación
- **Propósito:** Deliberar y seleccionar la arquitectura de representación definitiva (R1, R2, Híbrida C o D) basándose en la evidencia de G2.3.
- **Condiciones de Entrada:** Subgate G2.3 completado; matriz comparativa respaldada por datos de prueba sintética.
- **Evidencia Requerida:** Documento de decisión de arquitectura firmado por el titular.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Resultado:** Elección de arquitectura ratificada (**Subgate G2.4 Aprobado**).

---

### Gate G3 — Pre-code Gate & Transición a Implementación de Software en Rust
- **Definición Histórica:** Transición a la fase de implementación de código ejecutable en Rust.
- **Propósito:** Evaluar el cumplimiento de todos los requisitos previos a la escritura de código (resolución de licencias `GAP-001`, revisión de modelo de amenazas `GAP-002`, ADRs aceptados `GAP-005`, Subgate G2.4 aprobado).
- **Condiciones de Entrada:** Subgate G2.4 aprobado; `GAP-001` (Licencia) resuelto; `ADR-0001..0005` votados; plan de pruebas de seguridad `SEC-001..017` completado.
- **Evidencia Requerida:** Lista de verificación de pre-código aprobada; resolución formal del titular autorizando el inicio de implementación.
- **Autoridad:** Titular del proyecto (@Axlfc) en exclusiva.
- **Estado Actual:** **HOLD / NO-GO**. Ninguna aprobación en G2 autoriza superar Gate G3.

---

### Gate G4 — Despliegue, Aislamiento y Configuración de Entorno
- **Definición Histórica:** Verificación de empaquetado, dependencias y mecanismos de aislamiento en entornos target.
- **Estado:** BLOQUEADO.

### Gate G5 — Operación, Mantenimiento y Auditoría Continua
- **Definición Histórica:** Fase operativa del sistema.
- **Estado:** BLOQUEADO.

---

## 3. Cuadro Resumen de Dependencias y Estado de Gates

| Gate / Subgate | Nombre de la Etapa | Permite Código Rust | Requiere Autorización Expresa | Estado Actual |
|---|---|---|---|---|
| **G0** | Documentación e Investigación | NO | SÍ | EVALUACIÓN HISTÓRICA CONDICIONAL |
| **G1** | Alcance y Especificación Candidate | NO | SÍ | EVALUACIÓN HISTÓRICA CONDICIONAL |
| **G2.1** | Aprobación Documental del Protocolo v1 | NO | SÍ (Titular) | **PENDIENTE DE DELIBERACIÓN** |
| **G2.2** | Autorización de Laboratorio Acotado | NO (Solo Harness local) | SÍ (Titular) | **BLOQUEADO (Requiere G2.1)** |
| **G2.3** | Obtención de Evidencia Experimental | NO | SÍ (Titular) | **BLOQUEADO (Requiere G2.2)** |
| **G2.4** | Selección de Arquitectura | NO | SÍ (Titular) | **BLOQUEADO (Requiere G2.3)** |
| **G3** | Implementación Rust (Pre-code Gate) | SÍ (Tras aprobación) | SÍ (Titular en exclusiva) | **HOLD / NO-GO** |
| **G4** | Despliegue y Aislamiento | SÍ | SÍ (Titular) | **BLOQUEADO (Requiere G3)** |
| **G5** | Operación y Mantenimiento | SÍ | SÍ (Titular) | **BLOQUEADO (Requiere G4)** |
