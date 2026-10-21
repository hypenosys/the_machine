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
| **GAP-001** | Gobernanza / Licencias | Ausencia de archivo `LICENSE` en la raíz. Limitación legal para redistribución pública. | Medium / Legal | P2 (P1 si se publica) | Open |
| **GAP-002** | Seguridad / Cobertura | Amenazas TH-012, TH-016 y TH-019 carecen de pruebas especificadas en el plan global. | High | P1 (Para sistema completo) | Open |
| **GAP-003** | Arquitectura / Especificación | `unified-specification-candidate-v0.md` menciona tiempos, pero falta especificación formal, serialización y reglas de verificación. | High | P1 | Open |
| **GAP-004** | Seguridad / Modelo de Adversario | Falta definir modelo de adversario y anclaje de confianza para persistencia local de capacidades. | High | P1 (Para persistencia) | Open |
| **GAP-005** | Gobernanza / ADRs | Los ADRs 0001..0005 permanecen en estado `Proposed` sin procedimiento de adopción formal. | High | P1 | Open |
| **GAP-006** | Arquitectura / Evaluacion | El modelo de 6 entidades presenta hipótesis de complejidad accidental que requiere prueba experimental. | Medium | P2 | Open |
| **GAP-007** | Reproducibilidad / QA | Inexistencia de flujos de CI/CD para linters Markdown y validación de enlaces relativos. | Medium | P2 | Open |
| **GAP-008** | Seguridad / Privacidad | Estrategia de sanitización de logs indocumentada a nivel de tipos y formateadores. | Medium | P2 | Open |
| **GAP-009** | Accesibilidad / DX | Desconexión entre el tono divulgativo de `00-empezar/` y el rigor de `03-preimplementacion/`. | Low | P3 | Open |
| **GAP-010** | Gobernanza | Mapa de Autoridad Documental permanece como propuesta sin adopción formal. | Medium | P2 | Open |

---

## Fichas detalladas de brechas

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

### GAP-002 — Incobertura de pruebas especificadas para amenazas TH-012, TH-016 y TH-019
- **ID:** GAP-002
- **Dominio:** Seguridad y Verificación
- **Hallazgo:** Las amenazas TH-012 (Confused Deputy), TH-016 (Backup irrecuperable) y TH-019 (Insider abuse) están mapeadas a requisitos en `requirements.md`, pero carecen de pruebas asignadas (`SEC-XXX`) en `traceability.md`.
- **Evidencia:** `docs/02-diseno/security/requirements.md` y `traceability.md`.
- **Impacto:** Faltan escenarios de prueba definidos en la planificación de seguridad global para validar dichos controles. **Aclaración de alcance**: No bloquea un primer experimento minimalista offline de dos sensores si dicho corte vertical no incluye delegación de capacidades, copias de seguridad ni roles de administración.
- **Severidad:** High
- **Prioridad:** P1 para el diseño completo de seguridad.
- **Propuesta de corrección:** Diseñar e incorporar las especificaciones de prueba `SEC-015`, `SEC-016` y `SEC-017` en la planificación global de seguridad.
- **Estado:** Open

---

### GAP-003 — Incompleitud en la especificación formal y serialización de tiempos
- **ID:** GAP-003
- **Dominio:** Arquitectura / Especificación Temporal
- **Hallazgo:** Aunque `docs/03-preimplementacion/unified-specification-candidate-v0.md` (línea 35) menciona explícitamente `valid_time`, `recorded_time` y `assessed_time`, y `claim-semantics-v0.md` menciona el tiempo referido, el proyecto carece de un esquema formalizado de tipos, formato de serialización y reglas de verificación en tiempo de ejecución para consultas temporales (*time-travel queries*).
- **Evidencia:** `docs/03-preimplementacion/unified-specification-candidate-v0.md` y `claim-semantics-v0.md`.
- **Impacto:** Ambigüedad sobre cómo el motor de persistencia serializa y valida las marcas temporales en memoria y reposo.
- **Severidad:** High
- **Prioridad:** P1
- **Propuesta de corrección:** Definir los tipos de datos temporales, representación ISO-8601/Unix timestamp y reglas de validación en la especificación del núcleo.
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
