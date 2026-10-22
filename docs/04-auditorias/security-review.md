# Auditoría de seguridad y matriz de amenazas — THE MACHINE

> **Nota de actualización documental (21-10-2026, PR #25):** Este informe conserva su corte histórico, sin reescribir hallazgos retrospectivos. El repositorio ya era público en la consulta GitHub de esa fecha y la rama de PR #25 incorporó `LICENSE.md` con CC BY 4.0 para documentación original cubierta; quedan pendientes derechos de terceros, licencia de software futuro y cierre formal de GAP-001. Las afirmaciones de ausencia de código, conteos de archivos y CI solo se refieren al árbol y revisión que el auditor examinó, no a todas las ramas o entornos. La calificación de auditor «independiente» se conserva como atribución del informe, no como acreditación verificada por esta PR. **HOLD / NO-GO; sin pruebas ejecutadas ni ratificación de gates.**

**Fecha de auditoría:** Octubre de 2026
**Auditor independiente:** Security Architect & Application Security Engineer (Jules)
**Estado:** Informe de auditoría / Revisión de seguridad

---

## 1. Resumen ejecutivo

La presente auditoría de seguridad evalúa el modelo de amenazas v0 (`docs/02-diseno/security/threat-model-v0.md`), los requisitos de seguridad verificables (`docs/02-diseno/security/requirements.md`), los límites de confianza y los mecanismos de trazabilidad documentados para **THE MACHINE**.

El objetivo es determinar la solidez del diseño conceptual de seguridad antes de autorizar la codificación del sistema, separando categóricamente los controles diseñados de aquellos efectivamente implementados o probados.

---

## 2. Evaluación de los límites de confianza (Trust Boundaries)

Se analizan los 8 límites de confianza definidos en `docs/02-diseno/security/data-flow-diagrams.md`:

- **TB-01 (Usuario → Interfaz CLI/Local)**:
  Entrada directa de comandos. Requiere sanitización para evitar inyecciones de comandos en la terminal host.
- **TB-02 (Fuentes externas → Ingestión de datos)**:
  Toda entrada externa (archivos, APIs) debe tratarse como **datos no confiables**.
- **TB-03 (Modelos LLM/IA → Propuestas de acción)**:
  **Frontera Crítica**. Las salidas del modelo son propuestas no confiables sin autoridad ejecutiva implícita.
- **TB-04 (Propuesta → Política de seguridad / Action Gateway)**:
  El evaluador de políticas debe aplicar un esquema *deny-by-default* antes de autorizar la acción.
- **TB-05 (Política → Pasarela de ejecución)**:
  Falta especificar la protección de la decisión de autorización en memoria contra manipulaciones inter-proceso.
- **TB-06 (Kernel → Persistencia local)**:
  **Análisis del modelo de adversario para GAP-004**: Si un atacante tiene acceso al almacenamiento local con privilegios del sistema operativo host, modificar la base de datos o el archivo de políticas local le permitiría alterar las capacidades persistidas. **Anclaje de confianza y límites**: El uso de HMAC o firmas criptográficas locales evita la manipulación accidental o por parte de procesos no privilegiados, pero **no impide** que un atacante que controle las claves locales y el binario modifique el estado. El anclaje de confianza final reside en los permisos del sistema operativo y la integridad del binario ejecutable.
- **TB-07 (Nodo local → Nodo remoto - Futuro)**:
  Fuera de alcance del primer prototipo offline.
- **TB-08 (Cadena de suministro Cargo → Binario compilado)**:
  Abordado conceptualmente en ADR-0002. Minimización de dependencias para reducir la superficie de ataque en compilación.

---

## 3. Matriz de trazabilidad y evaluación de riesgos residuales

Dado que **no existe código funcional ni ejecutables probados**, los riesgos residuales **NO están medidos empíricamente** y se presentan como hipótesis o estados de evaluación pendiente.

| Amenaza | Requisito Verificable | Control Propuesto en Diseño | Prueba Asignada | Evidencia | Brecha / Observación | Riesgo Residual (Evaluación) |
|---|---|---|---|---|---|---|
| **TH-001** (Prompt Injection) | `SEC-REQ-001` | Ingestión de datos sin autoridad ejecutiva; parseo estricto | `SEC-001` | Solo diseño documental | Ninguna | **NO EVALUADO** (Hipótesis: Moderado en prototipo sin red) |
| **TH-002** (Escalada Privilegios) | `SEC-REQ-002` | Sistema de capacidades tipadas, deny-by-default | `SEC-002` | Solo diseño documental | Ninguna | **NO EVALUADO** (Hipótesis: Pendiente de código) |
| **TH-003** (Abuso de herramientas) | `SEC-REQ-003` | Action Gateway tipado con allowlist de herramientas | `SEC-003` | Solo diseño documental | Ninguna | **NO EVALUADO** (Hipótesis: Pendiente de código) |
| **TH-004** (Exfiltración de datos) | `SEC-REQ-004` | Ausencia de conectores de red en diseño offline | `SEC-004` | Solo diseño documental | Ninguna | **NO EVALUADO** (Hipótesis: Bajo si no hay sockets) |
| **TH-005** (DoS / Límites) | `SEC-REQ-005` | Límites de memoria y timeouts en IO | `SEC-005` | Solo diseño documental | Ninguna | **NO EVALUADO** |
| **TH-006** (Memory Poisoning) | `SEC-REQ-006` | Preservación de contradicciones sin resolver | `SEC-006` | Solo diseño documental | **GAP-003** | **NO EVALUADO** |
| **TH-007** (Suplantación de fuente) | `SEC-REQ-007` | Verificación de origen declarada | `SEC-007` | Solo diseño documental | Ninguna | **NO EVALUADO** |
| **TH-008** (Contradicción oculta) | `SEC-REQ-006` | Registro inmutable de eventos de evaluación | `SEC-006` | Solo diseño documental | Ninguna | **NO EVALUADO** |
| **TH-009** (Retención indebida) | `SEC-REQ-008` | Propagación de borrado en cascada sobre derivados | `SEC-008` | Solo diseño documental | **GAP-003** | **NO EVALUADO** |
| **TH-010** (TOCTOU) | `SEC-REQ-009` | Revalidación de capacidades previa al efecto | `SEC-009` | Solo diseño documental | Ninguna | **NO EVALUADO** |
| **TH-011** (Replay Attacks) | `SEC-REQ-010` | Nonces únicos e idempotencia en Action Gateway | `SEC-010` | Solo diseño documental | Ninguna | **NO EVALUADO** |
| **TH-012** (Confused Deputy) | `SEC-REQ-017` | Vinculación estricta Actor + Recurso + Propósito | **SIN ASIGNAR** | **Ninguna** | **GAP-002** | **NO EVALUADO** (Falta especificación de test) |
| **TH-013** (Corrupción persistencia) | `SEC-REQ-011` | Detección de escrituras incompletas | `SEC-011` | Solo diseño documental | Ninguna | **NO EVALUADO** |
| **TH-014** (Pérdida de energía) | `SEC-REQ-011` | Pruebas de interrupción de escritura | `SEC-011` | Solo diseño documental | Ninguna | **NO EVALUADO** |
| **TH-015** (Logs con secretos) | `SEC-REQ-012` | Redacción de datos sensibles en registros | `SEC-012` | Solo diseño documental | **GAP-008** | **NO EVALUADO** (*Secret<T>* es un envoltorio de tipos, no una garantía completa de no-filtración) |
| **TH-016** (Backup irrecuperable) | `SEC-REQ-015` | Ensayos automatizados de restauración sintética | **SIN ASIGNAR** | **Ninguna** | **GAP-002** | **NO EVALUADO** (Falta especificación de test) |
| **TH-017** (Retención fuera plazo) | `SEC-REQ-008` | Políticas de caducidad de datos | `SEC-008` | Solo diseño documental | Ninguna | **NO EVALUADO** |
| **TH-018** (Dependencia compromised) | `SEC-REQ-013` | Revisión de dependencias mediante cargo-audit | `SEC-013` | Solo diseño documental | Ninguna | **NO EVALUADO** |
| **TH-019** (Insider Abuse) | `SEC-REQ-016` | Separación de deberes y auditoría de decisiones | **SIN ASIGNAR** | **Ninguna** | **GAP-002** | **NO EVALUADO** (Falta especificación de test) |
| **TH-020** (Modelo comprometido) | `SEC-REQ-014` | Salida de modelo tratada como propuesta no confiable | `SEC-014` | Solo diseño documental | Ninguna | **NO EVALUADO** |

---

## 4. Estado de la seguridad en cuatro dimensiones

1. **Seguridad Documentada**: **EXISTENTE EN DISEÑO**. Existe un modelo de amenazas STRIDE v0 (`TH-001`..`TH-020`), requisitos verificables (`SEC-REQ-001`..`SEC-REQ-017`) y diagramas de flujo.
2. **Seguridad Implementada**: **PENDIENTE**. No existe código funcional en Rust, conectores ni pasarela de ejecución.
3. **Seguridad Comprobada / Verificada**: **PENDIENTE**. Al no existir binarios compilados, no se ha ejecutado ninguna prueba adversarial ni test unitario.
4. **Seguridad Pendiente**: **TODOS LOS CONTROLES DOCUMENTADOS**. Todos los controles propuestos en el modelo de amenazas y especificaciones de seguridad siguen pendientes de implementación y verificación empírica en código.

---

## 5. Recomendaciones de seguridad

1. **Completar especificaciones de prueba (GAP-002)**: Definir los escenarios de test `SEC-015`, `SEC-016` y `SEC-017` en la planificación global de seguridad. (Nota: Para un experimento minimalista offline de dos sensores que no ejecute acciones externas ni persista estado, estas pruebas no bloquean la prueba de concepto si las funciones correspondientes no están incluidas en el corte vertical).
2. **Clarificar el alcance de `GAP-008`**: Especificar el uso de envoltorios de tipos (como `Secret<T>` de la comunidad Rust) en los tipos de datos sensibles, reconociendo que la prevención total de filtraciones exige además auditorías de formateadores y trazadores de logs.
