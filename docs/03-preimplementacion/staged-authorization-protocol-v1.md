# Protocolo de Autorización por Etapas y Desacoplamiento de Gates — THE MACHINE (v1)

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Ubicación:** `docs/03-preimplementacion/staged-authorization-protocol-v1.md`
**Carácter:** **CANDIDATO NO NORMATIVO** (Protocolo de gobernanza por etapas; no autoriza código por sí mismo).
**Estado del proyecto:** **HOLD / NO-GO (Cero código ejecutable, cero manifiestos Cargo)**

---

## 1. Principio de Desacoplamiento Estricto de Autoridad

En resolución directa de la circularidad identificada en el **Defecto B-06**, el presente protocolo establece la separación absoluta entre aprobar un protocolo de experimentación y autorizar la ejecución real del experimento o la posterior escritura de código.

### Invariantes del Protocolo
1. **Sin Transiciones Automáticas:** El cumplimiento exitoso de las condiciones de entrada/salida de una etapa **NO concede autorización automática** para avanzar a la siguiente etapa.
2. **Autoridad Exclusiva:** Toda transición entre etapas exige una decisión de gobernanza explícita, registrada y firmada por el titular del proyecto (@Axlfc).
3. **Reversibilidad y Parada de Emergencia:** El titular del proyecto conserva la facultad de devolver el proyecto a estado **HOLD** o reajustar cualquier etapa previa en cualquier momento.

---

## 2. Definición de Etapas y Gates de Autorización (G0..G5)

El ciclo de vida del proyecto pre-código se estructura en seis puertas de autorización (*Gates*) totalmente independientes y secuenciales:

```
+-----------------------------------------------------------------------------------+
| FLUJO DE GATES DE AUTORIZACIÓN POR ETAPAS (G0 -> G5)                             |
|                                                                                   |
|  [G0: Protocolo] ---> [G1: Lab Sintético] ---> [G2: Evidencia]                   |
|         |                     |                      |                            |
|     (HOLD/GO)             (HOLD/GO)              (HOLD/GO)                       |
|         v                     v                      v                            |
|  [G3: Arquitectura] -> [G4: Pre-Code / Rust] -> [G5: Release]                     |
+-----------------------------------------------------------------------------------+
```

---

### Gate G0 — Aprobación Documental del Protocolo y Paquete de Decisión
- **Propósito:** Ratificar el marco metodológico, los contratos comparativos, la matriz de trazabilidad y las reglas de deliberación sin autorizar software ni pruebas.
- **Condiciones de Entrada:** Entrega del Paquete de Decisión v1 (`decision-package-v1.md`), Contrato Comparativo v1 (`comparative-contract-v1.md`) y Matriz de Trazabilidad v1 (`traceability-matrix-v1.md`).
- **Evidencia Requerida:** Consistencia interna comprobada, ausencia de contradicciones y ausencia de código ejecutable.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Resultado de Transición:** Aprobación del marco documental (**Gate G0 Aprobado**). El proyecto permanece en **HOLD** para las fases siguientes.

---

### Gate G1 — Autorización Expresa para Laboratorio Sintético Acotado
- **Propósito:** Conceder permiso acotado y exclusivo para construir y ejecutar el arnés de prueba sintético offline (*Offline Test Harness*) con datos en memoria volátil.
- **Condiciones de Entrada:** Gate G0 formalmente aprobado; delimitación estricta del alcance (cero red, cero persistencia, cero datos reales).
- **Evidencia Requerida:** Orden de ejecución del titular especificando los límites del laboratorio sintético.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Resultado de Transición:** Autorización para ejecutar el experimento de laboratorio acotado (**Gate G1 GO**). **No autoriza código de producción ni crates definitivos.**

---

### Gate G2 — Obtención y Evaluación de Evidencia Experimental Sintética
- **Propósito:** Recopilar y analizar de manera imparcial los resultados observables producidos por las alternativas R1, R2, Híbrida C y Baseline D ante los fixtures F-01..F-10 y R-01..R-08.
- **Condiciones de Entrada:** Finalización de las corridas sintéticas del laboratorio G1.
- **Evidencia Requerida:** Informe de resultados del laboratorio documentando fidelidad, sobrecarga de tipos, comportamiento ante datos incompletos y abstenciones producidas.
- **Autoridad:** Titular del proyecto (@Axlfc) tras revisión técnica del equipo.
- **Resultado de Transición:** Informe de evidencia experimental validado (**Gate G2 Completado**).

---

### Gate G3 — Selección Formal de la Arquitectura de Representación
- **Propósito:** Deliberar y seleccionar la arquitectura de representación definitiva (R1, R2, Híbrida C o D) basándose estrictamente en la evidencia experimental recopilada en G2.
- **Condiciones de Entrada:** Gate G2 completado; matriz comparativa respaldada por datos de prueba sintética.
- **Evidencia Requerida:** Documento de decisión de arquitectura firmado por el titular justificando la elección elegida.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Resultado de Transición:** Elección de arquitectura ratificada (**Gate G3 Aprobado**).

---

### Gate G4 — Pre-code Gate & Autorización Expresa de Implementación en Rust
- **Propósito:** Evaluar el cumplimiento de todos los requisitos previos a la escritura de código de producción (resolución de licencias, revisión de modelo de amenazas, ADRs aceptados).
- **Condiciones de Entrada:** Gate G3 aprobado; `GAP-001` (Licencia) resuelto; `ADR-0001..0005` sometidos a votación final; plan de pruebas de seguridad `SEC-001..017` completado.
- **Evidencia Requerida:** Lista de verificación de pre-código aprobada; resolución formal del titular autorizando el inicio de la fase de código Rust.
- **Autoridad:** Titular del proyecto (@Axlfc) en exclusiva.
- **Resultado de Transición:** Transición a la fase de implementación (**Gate G4 GO / Transición a Código**).

---

### Gate G5 — Verificación Post-implementación, Auditoría y Release
- **Propósito:** Auditar el código Rust producido, verificar la ausencia de unsafe unapproved, validar suites de pruebas unitarias/integración y autorizar la publicación o release.
- **Condiciones de Entrada:** Código Rust totalmente implementado y verificado en la fase de desarrollo.
- **Evidencia Requerida:** Dictamen de auditoría final con veredicto PASS o PASSED WITH CONDITIONS; informe de trazabilidad al 100%.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Resultado de Transición:** Release pública autorizada (**Gate G5 Aprobado**).

---

## 3. Cuadro Resumen de Dependencias entre Gates

| Gate | Nombre de la Etapa | Permite Código Rust | Requiere Autorización Expresa | Estado Actual |
|---|---|---|---|---|
| **G0** | Aprobación Documental del Protocolo | NO | SÍ (Titular) | **PENDIENTE DE DELIBERACIÓN** |
| **G1** | Autorización de Laboratorio Acotado | NO (Solo Harness local) | SÍ (Titular) | **BLOQUEADO (Requiere G0)** |
| **G2** | Obtención de Evidencia Experimental | NO | SÍ (Titular) | **BLOQUEADO (Requiere G1)** |
| **G3** | Selección de Arquitectura | NO | SÍ (Titular) | **BLOQUEADO (Requiere G2)** |
| **G4** | Pre-code Gate (Implementación Rust) | SÍ (Tras aprobación) | SÍ (Titular en exclusiva) | **HOLD / NO-GO** |
| **G5** | Verificación Final y Release | SÍ | SÍ (Titular) | **BLOQUEADO (Requiere G4)** |
