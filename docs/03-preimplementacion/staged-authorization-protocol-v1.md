# Protocolo de Autorización por Etapas y Desacoplamiento de Gates — THE MACHINE (v1)

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Ubicación:** `docs/03-preimplementacion/staged-authorization-protocol-v1.md`
**Carácter:** **CANDIDATO NO NORMATIVO** (Protocolo de gobernanza por etapas; no autoriza código por sí mismo).
**Estado de gobernanza:** **HOLD / NO-GO** (sin autorización de código, compilación ni ejecución; este protocolo no certifica la ausencia de artefactos en todas las ramas)

---

## 1. Propuesta de Desacoplamiento y Contraste de Gates Históricos

En resolución directa del **Defecto B-06** y para evitar la colisión con la nomenclatura histórica de readiness gates (`readiness-assessment.md`, `traceability.md`, `auditoria-integral-2026-10.md`), el presente protocolo **propone una lectura de Gates G0..G5 pendiente de ratificación** y modela el proceso de laboratorio pre-código como **subgates explícitos** dentro del Gate G2 de Diseño.

```
+---------------------------------------------------------------------------------------------------+
| PROPUESTA NO RATIFICADA: GATES G0..G5 Y SUBGATES DE LABORATORIO PRE-CÓDIGO                      |
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

### Reglas candidatas del protocolo (no ratificadas)
1. **G3 — interpretación candidata:** Se propone que **Gate G3 sea la puerta de implementación de software en Rust**; otras fuentes históricas lo sitúan antes de fusionar código ejecutable. La discrepancia requiere decisión del titular. Pasar de G2 a G3 exige el cumplimiento total de los requisitos de pre-código y una decisión expresa `GO` del titular.
2. **Sin Transiciones Automáticas:** Ningún subgate dentro de G2 (G2.1, G2.2, G2.3, G2.4) concede autorización automática para pasar a G3 ni para escribir código Rust.
3. **Autoridad propuesta:** Toda transición requeriría decisión explícita y registrada del titular; forma de firma, acreditación y revocación pendientes de decisión (REV-16 / GAP-010).

---

### Nota de revisión pendiente de ratificación (REV-01 / REV-03 / REV-05 / REV-06)

Este protocolo es **candidato**, no una modificación efectiva de los gates históricos. Su afirmación de «armonización» es una hipótesis que requiere contrastar `security/security-gates.md`, `security/traceability.md` y los readiness reviews. Ante discrepancias prevalece **HOLD** hasta decisión expresa del titular sobre precedencia documental y autoridad. El significado de G3 (permiso para comenzar código frente a permiso para fusionarlo) sigue **SIN RATIFICAR**.

G2.2 plantea construir un harness mientras el estado general prohíbe código ejecutable. **No hay excepción vigente**. Antes de autorizar cualquier experimento debe definirse por escrito si se admite código desechable, lenguaje, ubicación, duración, límites de E/S, dependencias, revisión y destrucción; una autorización documental G2.1 por sí sola no permite escribir ni ejecutar ese código. Las condiciones que siguen son **propuestas de entrada**, no gates superados.

## 2. Interpretación candidata de Gates (G0..G5) y Subgates (G2.1..G2.4)

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
- **Evidencia Requerida (propuesta):** Consistencia interna de los documentos candidatos, registro explícito de contradicciones residuales y delimitación comprobable del alcance documental. La ausencia de código ejecutable en todo el repositorio **no se presume ni se declara verificada**; si se exige como condición, deberán definirse el árbol, las ramas, la revisión y el método de inspección.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Resultado posible solo tras ratificación expresa:** Aprobación documental de G2.1; **actualmente PENDIENTE**. Incluso si se aprobase, el proyecto seguiría en **HOLD** para código y experimentos.

#### Subgate G2.2 — Autorización Expresa para Laboratorio Sintético Acotado (Harness)
- **Propósito:** Conceder permiso acotado y exclusivo para construir y ejecutar el arnés de prueba sintético offline (*Offline Test Harness*) con datos en memoria volátil.
- **Condiciones de Entrada:** Subgate G2.1 formalmente aprobado; delimitación estricta del alcance (cero red, cero persistencia duradera, cero datos reales); fixtures sintéticos normalizados, reglas de oráculo versionadas, tolerancias explícitas y esquema de salida fijados conforme a `comparative-contract-v1.md` §1.2; resolución expresa de la distinción entre código de laboratorio y código de producto, formato de intercambio y política de dependencias. Cualquier excepción adicional requiere registro específico del titular y no se presume por la aprobación de G2.1.
- **Evidencia Requerida:** Orden de ejecución del titular especificando los límites del laboratorio sintético.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Resultado condicionado a ratificación futura:** Solo una orden separada y específica del titular podría autorizar construir/ejecutar el laboratorio acotado. **Actualmente G2.2 está BLOQUEADO; no autoriza código de producción ni crates definitivos.**

#### Subgate G2.3 — Obtención y Evaluación de Evidencia Experimental Sintética
- **Propósito:** Recopilar y analizar los resultados observables producidos por las alternativas R1, R2, Híbrida C y Baseline D ante los fixtures sintéticos F-01..F-09 y cualquier caso adicional autorizado expresamente. **F-10/E-10 original permanece BLOQUEADO** y no forma parte de la ejecución por defecto.
- **Condiciones de Entrada (propuesta):** Existencia de corridas sintéticas autorizadas, con evidencia íntegra y reproducible identificada por versión de fixtures, reglas, entorno y resultados observados. Una ejecución terminada no equivale a PASS ni habilita automáticamente G2.3.
- **Evidencia Requerida (propuesta):** Informe de resultados por arquitectura y fixture con entrada, oráculo previo, salida, controles positivos/negativos, fallos, abstenciones, versión del entorno y limitaciones; registrar FAIL y NO EVALUABLE sin ocultarlos.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Resultado (propuesto):** Informe revisado con fallos y límites explícitos; la valoración de evidencia no constituye selección de arquitectura ni ratificación automática de G2.3.

#### Subgate G2.4 — Selección Formal de la Arquitectura de Representación
- **Propósito:** Deliberar y seleccionar la arquitectura de representación definitiva (R1, R2, Híbrida C o D) basándose en la evidencia de G2.3.
- **Condiciones de Entrada:** Subgate G2.3 completado; matriz comparativa respaldada por datos de prueba sintética.
- **Evidencia Requerida:** Documento de decisión de arquitectura firmado por el titular.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Resultado:** Elección de arquitectura ratificada (**Subgate G2.4 Aprobado**).

---

### Gate G3 — Pre-code Gate & Transición a Implementación de Software en Rust
- **Interpretación Candidata (NO RATIFICADA):** Transición a la fase de implementación de código ejecutable en Rust; la fuente `security/security-gates.md` utiliza el criterio previo a fusionar código ejecutable. No hay precedencia decidida.
- **Propósito propuesto (NO RATIFICADO):** Evaluar el cumplimiento de todos los requisitos previos a la escritura de código (resolución de licencias `GAP-001`, revisión de modelo de amenazas `GAP-002`, ADRs aceptados `GAP-005`, Subgate G2.4 aprobado).
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
| **G2.2** | Autorización de Laboratorio Acotado | NO; posible excepción de harness solo con orden separada | SÍ (Titular) | **BLOQUEADO (Requiere G2.1 y excepción específica)** |
| **G2.3** | Obtención de Evidencia Experimental | NO | SÍ (Titular) | **BLOQUEADO (Requiere G2.2)** |
| **G2.4** | Selección de Arquitectura | NO | SÍ (Titular) | **BLOQUEADO (Requiere G2.3)** |
| **G3** | Implementación Rust (Pre-code Gate) | SÍ (Tras aprobación) | SÍ (Titular en exclusiva) | **HOLD / NO-GO** |
| **G4** | Despliegue y Aislamiento | SÍ | SÍ (Titular) | **BLOQUEADO (Requiere G3)** |
| **G5** | Operación y Mantenimiento | SÍ | SÍ (Titular) | **BLOQUEADO (Requiere G4)** |
