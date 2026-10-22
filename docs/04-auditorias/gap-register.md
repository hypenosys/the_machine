# Registro de brechas (Gap Register) — THE MACHINE

**Fecha de auditoría:** Octubre de 2026
**Auditor independiente:** Jules — Team de Auditoría Técnica Independiente
**Estado:** Activo / Auditoría Integral

---

## Metodología y taxonomía

Cada brecha identificada en THE MACHINE se cataloga con un identificador estable (`GAP-XXX`) y se clasifica según su dominio, causa raíz, impacto, severidad y prioridad.

### Escala de Severidad y Prioridad
- **Critical / P0**: Bloqueante absoluto para el objetivo inmediato.
- **High / P1**: Riesgo grave de diseño o inconsistencia normativa mayor. Requiere resolución previa a la congelación definitiva de arquitectura.
- **Medium / P2**: Deuda técnica, ambigüedad documental o falta de especificación secundaria.
- **Low / P3**: Mejora de accesibilidad, estilo o mantenimiento menor.

---

## Tabla resumida de brechas

| ID | Dominio | Hallazgo resumido | Severidad | Prioridad | Estado |
|---|---|---|---|---|---|
| **GAP-001** | Gobernanza / Licencias | Inventario de derechos de terceros y cierre formal incompletos; licencia de software futuro pendiente. | Medium / Legal | P2 (P1 si se publica) | Open |
| **GAP-002** | Seguridad / Cobertura | SEC-015..017 están ahora especificadas y trazadas como propuestas; siguen sin ejecutarse, por lo que no hay cobertura verificada. | High | P1 (Para sistema completo) | Open |
| **GAP-003** | Arquitectura / Especificación | Hay semántica temporal y perfiles de serialización candidatos, pero falta un contrato general ratificado para tipos, serialización y consultas temporales. | High | P1 | Open |
| **GAP-004** | Seguridad / Modelo de Adversario | Falta definir modelo de adversario y anclaje de confianza para persistencia local de capacidades. | High | P1 (Para persistencia) | Open |
| **GAP-005** | Gobernanza / ADRs | Los ADRs 0001..0005 permanecen en estado `Proposed` sin procedimiento de adopción formal. | High | P1 | Open |
| **GAP-006** | Arquitectura / Evaluacion | El modelo de 6 entidades presenta hipótesis de complejidad accidental que requiere prueba experimental. | Medium | P2 | Open |
| **GAP-007** | Reproducibilidad / QA | Inexistencia de flujos de CI/CD para linters Markdown y validación de enlaces relativos. | Medium | P2 | Open |
| **GAP-008** | Seguridad / Privacidad | Estrategia de sanitización de logs indocumentada a nivel de tipos y formateadores. | Medium | P2 | Open |
| **GAP-009** | Accesibilidad / DX | Desconexión entre el tono divulgativo de `00-empezar/` y el rigor de `03-preimplementacion/`. | Low | P3 | Open |
| **GAP-010** | Gobernanza | Mapa de Autoridad Documental permanece como propuesta sin adopción formal. | Medium | P2 | Open |

---

## Fichas detalladas de brechas

> **Actualización documental posterior (PR #25, 21-10-2026):** Las afirmaciones de ausencia de licencia de la tabla y del hallazgo original reflejan el corte de auditoría anterior. En esta rama existe ahora [`LICENSE.md`](../../LICENSE.md), aviso CC BY 4.0 para documentación original y materiales no software con derechos suficientes. No se ha realizado inventario completo de derechos de terceros ni elegido licencia para código futuro. **GAP-001 permanece OPEN por alcance y cierre formal**, no por inexistencia actual del archivo en esta rama. La instrucción de incorporar CC BY 4.0 consta en la conversación, sin acreditación de ratificación conjunta de @Axlfc y @TopperH4rley. El historial original se conserva para trazabilidad.

### GAP-001 — Ausencia de archivo de licencia legal (LICENSE)
- **ID:** GAP-001
- **Dominio:** Gobernanza y Licenciamiento
- **Hallazgo:** El repositorio no contiene ningún archivo `LICENSE` ni `LICENSE-APACHE`/`LICENSE-MIT`, aunque en `CONTRIBUTING.md` y `README.md` se menciona intención de código abierto.
- **Evidencia:** Inspección directa de la raíz del repositorio. No existen archivos de licencia.
- **Impacto:** Jurídico y de derechos de autor para redistribución pública. Legalmente, el código y documentación sin licencia explícita se consideran bajo derechos de autor reservados ("All Rights Reserved"). **Aclaración de alcance**: Para la ejecución de un experimento o investigación privada en local, no constituye un bloqueante técnico de código, pero sí una limitación legal previa a cualquier distribución o contribución pública.
- **Severidad:** Medium (Legal)
- **Prioridad:** P2 para investigación privada / P1 previa a publicación abierta.
- **Propuesta de corrección:** Requerir decisión del titular del proyecto sobre la licencia a adoptar (p. ej. Dual MIT/Apache-2.0, MPL-2.0, u otra) e integrar el archivo correspondiente.
- **Estado:** Open

---

### GAP-002 — Cobertura no verificada para amenazas TH-012, TH-016 y TH-019

> **Actualización de estado (master, 22-10-2026):** El hallazgo original describe la falta de asignaciones en el corte auditado. `docs/02-diseno/security/traceability.md` y `verification-plan.md` vinculan ahora TH-012/016/019 con SEC-017/015/016 y sus requisitos. Son diseños candidatos, no pruebas ejecutadas; GAP-002 permanece OPEN hasta que se acuerden, implementen y verifiquen los controles aplicables. Esta actualización no cambia retrospectivamente el hallazgo original.
- **ID:** GAP-002
- **Dominio:** Seguridad y Verificación
- **Hallazgo:** En el corte original auditado, TH-012 (Confused Deputy), TH-016 (Backup irrecuperable) y TH-019 (Insider abuse) carecían de prueba asignada. En el `master` actual están vinculadas a requisitos y especificaciones candidatas SEC-017, SEC-015 y SEC-016, respectivamente; no hay pruebas ejecutadas ni cobertura verificada.
- **Evidencia:** `docs/02-diseno/security/requirements.md` y `traceability.md`.
- **Impacto:** No existe evidencia de ejecución o controles implementados que valide estas amenazas para el sistema completo. **Aclaración de alcance:** No bloquea por sí sola un corte sintético offline que excluya delegación de capacidades, copias de seguridad y roles de administración.
- **Severidad:** High
- **Prioridad:** P1 para el diseño completo de seguridad.
- **Propuesta de corrección:** La etapa de diseño documental está reflejada en el plan y la trazabilidad actuales. Mantener GAP-002 abierto hasta acordar las pruebas aplicables y, solo con autorización separada, implementar y ejecutar los controles pertinentes.
- **Estado:** Open

---

### GAP-003 — Incompletitud en la especificación formal y serialización de tiempos

> **Actualización de estado (master, 22-10-2026):** Los documentos candidatos ahora separan `valid_time`, `recorded_time` y `assessed_time`, y proponen reglas de perfil y un formato para el perfil sintético de temperatura. No existe todavía un contrato general ratificado de tipos, serialización y consultas temporales, ni reglas universales de validación en tiempo de ejecución. GAP-003 permanece OPEN; las propuestas específicas no equivalen a adopción del formato para el núcleo.
- **ID:** GAP-003
- **Dominio:** Arquitectura / Especificación Temporal
- **Hallazgo:** Los documentos candidatos separan `valid_time`, `recorded_time` y `assessed_time`, y un perfil sintético de temperatura propone un formato concreto. Sigue pendiente un contrato general ratificado de tipos, serialización y reglas para consultas temporales (*time-travel queries*); tampoco hay reglas universales adoptadas de validación en tiempo de ejecución.
- **Evidencia:** `docs/03-preimplementacion/claim-semantics-v0.md`, `offline-experiment-contract-candidate-v0.md` y `design-freeze-candidate-v0.md` (candidatos, no normas adoptadas).
- **Impacto:** Ambigüedad sobre el formato e interpretación temporal general; no se ha seleccionado ni especificado un motor de persistencia.
- **Severidad:** High
- **Prioridad:** P1
- **Propuesta de corrección:** Deliberar y, si se aprueba, documentar un contrato temporal general que defina tipos, serialización y consultas; mantener separados los perfiles de dominio y no inferir autorización de implementación.
- **Estado:** Open

---

### GAP-004 — Indefinición del modelo de adversario y anclaje de confianza para persistencia local
- **ID:** GAP-004
- **Dominio:** Seguridad y Arquitectura
- **Hallazgo:** La protección de la persistencia local de capacidades (TB-06) carece de una definición explícita del modelo de adversario.
- **Análisis de límites**: Si un atacante tiene control del sistema operativo host y del binario ejecutable, ninguna firma o HMAC local puede impedir la modificación del estado o las claves. El anclaje de confianza reside en los permisos del SO host e integridad del ejecutable.
- **Evidencia:** `docs/02-diseno/security/data-flow-diagrams.md`.
- **Impacto:** Falta de claridad sobre qué ataques locales están dentro o fuera del alcance de mitigación del software.
- **Severidad:** High
- **Prioridad:** P1
- **Propuesta de corrección:** Documentar explícitamente el modelo de adversario local y las fronteras de confianza del almacenamiento en disco en `data-flow-diagrams.md`.
- **Estado:** Open

---

### GAP-005 — Estado de ADRs en "Proposed" sin procedimiento formal de aprobación
- **ID:** GAP-005
- **Dominio:** Gobernanza / Arquitectura
- **Hallazgo:** Los 5 Registros de Decisiones de Arquitectura (`ADR-0001` a `ADR-0005`) figuran como `Proposed`.
- **Evidencia:** Directorio `docs/02-diseno/adr/`.
- **Impacto:** Indefinición sobre el carácter vinculante de las decisiones propuestas.
- **Severidad:** High
- **Prioridad:** P1
- **Propuesta de corrección:** Establecer el procedimiento de gobernanza para la transición de ADRs a `Accepted` mediante revisión formal del equipo del proyecto.
- **Estado:** Open

---

### GAP-006 — Hipótesis de complejidad accidental en el modelo de 6 entidades
- **ID:** GAP-006
- **Dominio:** Arquitectura
- **Hallazgo:** Requerir la estructura completa de 6 entidades para casos de uso atómicos es una hipótesis de sobrecarga que requiere evaluación empírica.
- **Evidencia:** `docs/03-preimplementacion/epistemic-review-decision.md` y `general-epistemic-contract-v0.md`.
- **Impacto:** Fricción técnica potencial durante la implementación.
- **Severidad:** Medium
- **Prioridad:** P2
- **Propuesta de corrección:** Evaluar experimentalmente la Opción A frente a la Opción B mediante el primer experimento offline de dos sensores.
- **Estado:** Open

---

### GAP-007 — Ausencia de integración continua para validaciones documentales
- **ID:** GAP-007
- **Dominio:** Calidad / Reproducibilidad
- **Hallazgo:** Inexistencia del directorio `.github/workflows` para automatizar linters de Markdown o verificadores de enlaces relativos.
- **Evidencia:** Inspección del árbol de archivos.
- **Impacto:** Riesgo de degradación de enlaces y formato a medida que el proyecto crezca.
- **Severidad:** Medium
- **Prioridad:** P2
- **Propuesta de corrección:** Diseñar e incorporar flujos de CI/CD para comprobación de sintaxis y enlaces relativos.
- **Estado:** Open

---

### GAP-008 — Indefinición de tipos y redactores de datos sensibles en logs
- **ID:** GAP-008
- **Dominio:** Seguridad / Privacidad
- **Hallazgo:** `SEC-REQ-012` exige redactar secretos en logs, pero no se especifican los tipos o formateadores responsables en Rust.
- **Evidencia:** `docs/02-diseno/adr/0005-logging-recovery-and-data-lifecycle.md`.
- **Impacto:** Riesgo de filtración accidental en salidas de depuración si no se diseña la estrategia de tipado.
- **Severidad:** Medium
- **Prioridad:** P2
- **Propuesta de corrección:** Especificar el uso de envoltorios de tipos para datos sensibles en las directrices de codificación.
- **Estado:** Open

---

### GAP-009 — Discrepancia pedagógica entre itinerarios
- **ID:** GAP-009
- **Dominio:** Accesibilidad / DX
- **Hallazgo:** `docs/00-empezar/` utiliza un tono muy básico ("sin saber programar") mientras que `docs/03-preimplementacion/` utiliza terminología técnica avanzada.
- **Evidencia:** Comparación de documentos entre ambas carpetas.
- **Impacto:** Brecha de comprensión para nuevos colaboradores.
- **Severidad:** Low
- **Prioridad:** P3
- **Propuesta de corrección:** Armonizar las rutas de lectura en `README.md`.
- **Estado:** Open

---

### GAP-010 — Indefinición del proceso normativo de consolidación de especificaciones
- **ID:** GAP-010
- **Dominio:** Gobernanza
- **Hallazgo:** Documentos kandidatos de especificación conviven con propuestas sin un estado normativo claramente definido.
- **Evidencia:** `docs/03-preimplementacion/contract-authority-map.md`.
- **Impacto:** Confusión sobre cuál especificación es vinculante.
- **Severidad:** Medium
- **Prioridad:** P2
- **Propuesta de corrección:** Aprobar el Mapa de Autoridad Documental por parte de la gobernanza del proyecto.
- **Estado:** Open
