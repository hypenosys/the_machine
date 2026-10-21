# Registro de brechas (Gap Register) — THE MACHINE

**Fecha de auditoría:** Octubre de 2026
**Auditor independiente:** Jules — Team de Auditoría Técnica Independiente
**Estado:** Activo / Auditoría Integral

---

## Metodología y taxonomía

Cada brecha identificada en THE MACHINE se cataloga con un identificador estable (`GAP-XXX`) y se clasifica según su dominio, causa raíz, impacto, severidad y prioridad.

### Dominios
- **Arquitectura**: Abstracciones, ontologías, acoplamiento, modelos de datos y evolución.
- **Seguridad**: Control de acceso, aislamientos, modelo de amenazas y vector de ataque.
- **Documentación / Gobernanza**: Contradicciones, jerarquía normativa, licenciamiento y estado de ADR.
- **Reproducibilidad / Calidad**: Pruebas, CI/CD, verficiación y determinismo.

### Escala de Severidad y Prioridad
- **Critical / P0**: Bloqueante absoluto de seguridad o arquitectura. Impide cualquier prototipado seguro.
- **High / P1**: Riesgo grave de diseño o inconsistencia normativa mayor. Requiere resolución previa a implementación.
- **Medium / P2**: Deuda técnica, ambigüedad documental o falta de especificación secundaria.
- **Low / P3**: Mejora de accesibilidad, estilo o mantenimiento menor.

---

## Tabla resumida de brechas

| ID | Dominio | Hallazgo resumido | Severidad | Prioridad | Estado |
|---|---|---|---|---|---|
| **GAP-001** | Gobernanza / Licencias | Ausencia de archivo `LICENSE` y menciones contradictorias de "software libre". | Critical | P0 | Open |
| **GAP-002** | Seguridad / Cobertura | Amenazas TH-012, TH-016 y TH-019 carecen de pruebas negativas o suites especificadas. | High | P1 | Open |
| **GAP-003** | Arquitectura / Epistemología | Ambigüedad en la semántica del núcleo epistemológico (tiempo de validez vs tiempo de registro). | High | P1 | Open |
| **GAP-004** | Seguridad / Modelo | Fronteras de confianza ambiguas entre el motor de persistencia y el Action Gateway. | High | P1 | Open |
| **GAP-005** | Documentación | ADRs 0001..0005 permanecen en estado `Proposed` sin procedimiento de adopción formal. | High | P1 | Open |
| **GAP-006** | Arquitectura / Escalabilidad | Ontología prematura en `Claim` y `Assessment` puede imponer complejidad accidental masiva. | Medium | P2 | Open |
| **GAP-007** | Reproducibilidad | CI/CD limitado a validación documental y linting Markdown básico sin tests de especificación. | Medium | P2 | Open |
| **GAP-008** | Seguridad / Privacidad | Estrategia de sanitización de logs (`TH-015`) indocumentada a nivel de estructura de datos. | Medium | P2 | Open |
| **GAP-009** | Documentación | Discrepancia entre la guía para principiantes y el nivel técnico requerido en preimplementación. | Low | P3 | Open |
| **GAP-010** | Gobernanza | Inexistencia de un proceso normativo formal para elevar candidatos a especificaciones aprobadas. | Medium | P2 | Open |

---

## Fichas detalladas de brechas

### GAP-001 — Ausencia de archivo de licencia legal (LICENSE)
- **ID:** GAP-001
- **Dominio:** Gobernanza y Licenciamiento
- **Hallazgo:** El repositorio no contiene ningún archivo `LICENSE` ni `LICENSE-APACHE`/`LICENSE-MIT`, aunque en `CONTRIBUTING.md` y `README.md` se promociona como proyecto de código abierto.
- **Evidencia:** Inspección directa del árbol raíz del repositorio. No existen archivos de licencia.
- **Causa probable:** Omisión inicial durante la fase de documentación y especificación teórica.
- **Impacto:** Jurídico y de derechos de autor. Legalmente, el código y documentación sin licencia explícita se consideran bajo derechos de autor reservados ("All Rights Reserved"), impidiendo su libre reutilización o contribución pública segura.
- **Probabilidad:** Alta (100% verificado en repositorio).
- **Severidad:** Critical
- **Prioridad:** P0
- **Propuesta de corrección:** Definir y añadir el archivo de licencia correspondiente (p. ej., Dual License MIT / Apache-2.0, estándar en el ecosistema Rust).
- **Dependencias:** Decisión del titular del proyecto.
- **Criterio de cierre:** Presencia del archivo de licencia en la raíz y declaración explícita en `README.md`.
- **Estado:** Open

---

### GAP-002 — Incobertura de pruebas negativas para amenazas TH-012, TH-016 y TH-019
- **ID:** GAP-002
- **Dominio:** Seguridad y Verificación
- **Hallazgo:** Las amenazas TH-012 (Confused Deputy), TH-016 (Backup irrecuperable) y TH-019 (Insider abuse) están mapeadas a requisitos (SEC-REQ-017, SEC-REQ-015, SEC-REQ-016), pero carecen de pruebas especificadas (`SEC-XXX`) en la matriz de trazabilidad.
- **Evidencia:** `docs/02-diseno/security/requirements.md` y `docs/02-diseno/security/traceability.md`.
- **Causa probable:** Cierre prematuro de la matriz de requisitos antes de redactar los escenarios de prueba negativos.
- **Impacto:** Imposibilidad de verificar si los controles propuestos frente a escalada de privilegios indirecta e incidentes de recuperación son efectivos.
- **Probabilidad:** Alta (brecha de diseño comprobada).
- **Severidad:** High
- **Prioridad:** P1
- **Propuesta de corrección:** Diseñar e incorporar las especificaciones de prueba `SEC-015` (Recuperación de backups sintéticos), `SEC-016` (Separación de deberes en ops) y `SEC-017` (Prevención de Confused Deputy en delegación de capacidades).
- **Dependencias:** Ninguna.
- **Criterio de cierre:** Integración de los casos de prueba en `verification-plan.md` y matriz de trazabilidad actualizada.
- **Estado:** Open

---

### GAP-003 — Ambigüedad en la semántica temporal del núcleo epistemológico
- **ID:** GAP-003
- **Dominio:** Arquitectura / Epistemología
- **Hallazgo:** El modelo de `Claim` y `EvidenceLink` no distingue explícitamente entre el tiempo de validez del hecho en el mundo real (*valid time*) y el tiempo de registro en el sistema (*transaction time*).
- **Evidencia:** `docs/03-preimplementacion/claim-semantics-v0.md` y `general-epistemic-contract-v0.md`.
- **Causa probable:** Simplificación de la ontología epistemológica en la fase preliminar.
- **Impacto:** Incapacidad para manejar retractaciones retroactivas, correcciones históricas o razonamiento sobre estados pasados sin corromper la auditoría inmutable.
- **Probabilidad:** Alta en escenarios del mundo real.
- **Severidad:** High
- **Prioridad:** P1
- **Propuesta de corrección:** Incorporar el paradigma Bitemporal (Valid Time vs Transaction Time) en el contrato de datos del núcleo.
- **Dependencias:** ADR-0003.
- **Criterio de cierre:** Especificación bitemporal integrada en `general-epistemic-contract-v0.md`.
- **Estado:** Open

---

### GAP-004 — Indefinición de la frontera de confianza entre Persistencia y Action Gateway
- **ID:** GAP-004
- **Dominio:** Seguridad y Arquitectura
- **Hallazgo:** Los límites de confianza TB-05 (Policy Engine → Action Gateway) y TB-06 (Kernel → Persistencia) no aclaran si la base de datos local puede alterar o falsificar capacidades almacenadas si el almacenamiento es manipulado en disco.
- **Evidencia:** `docs/02-diseno/security/data-flow-diagrams.md` y `adr/0004-authorization-and-action-gateway.md`.
- **Causa probable:** Asumir que el almacenamiento local es un entorno de confianza implícita.
- **Impacto:** Si un atacante modifica la base de datos SQLite/Local, podría concederse permisos elevados en el Action Gateway sin pasar por la firma o verificación del kernel.
- **Probabilidad:** Media.
- **Severidad:** High
- **Prioridad:** P1
- **Propuesta de corrección:** Requerir firma criptográfica o autenticación Mac (HMAC) de las capacidades e invariantes de autorización antes de persistirlas.
- **Dependencias:** ADR-0001, ADR-0004.
- **Criterio de cierre:** Mecanismo de integridad de capacidades en reposo documentado en ADR-0004.
- **Estado:** Open

---

### GAP-005 — Estado de ADRs estancado en "Proposed" sin procedimiento de aprobación
- **ID:** GAP-005
- **Dominio:** Gobernanza / Arquitectura
- **Hallazgo:** Los 5 Registros de Decisiones de Arquitectura (`ADR-0001` a `ADR-0005`) figuran como `Proposed`. No existe un protocolo claro sobre quién o mediante qué criterio cambian a `Accepted`.
- **Evidencia:** Directorio `docs/02-diseno/adr/`.
- **Causa probable:** Falta de un rol de revisión técnica o autoridad de gobierno antes de la congelación del diseño.
- **Impacto:** Ambigüedad sobre qué reglas de arquitectura son vinculantes y cuáles son sugerencias o borradores.
- **Probabilidad:** Alta.
- **Severidad:** High
- **Prioridad:** P1
- **Propuesta de corrección:** Establecer la regla en `docs/02-diseno/adr/README.md` donde un ADR pasa a `Accepted` tras superar una revisión de seguridad y arquitectura formal con evidencia.
- **Dependencias:** Ninguna.
- **Criterio de cierre:** Cambio de estado de ADRs respaldado por registros de revisión.
- **Estado:** Open

---

### GAP-006 — Complejidad accidental y ontología prematura
- **ID:** GAP-006
- **Dominio:** Arquitectura
- **Hallazgo:** Requerir que cada afirmación simple pase por la estructura completa de 6 conceptos epistemológicos (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`) introduce una sobrecarga masiva para casos de uso básicos.
- **Evidencia:** `docs/03-preimplementacion/epistemic-review-decision.md` y `general-epistemic-contract-v0.md`.
- **Causa probable:** Inclinación hacia la generalización teórica previa al enfrentamiento con problemas concretos.
- **Impacto:** Fricción excesiva para el desarrollo de adaptadores, degradación de rendimiento y barrera de entrada para colaboradores.
- **Probabilidad:** Alta.
- **Severidad:** Medium
- **Prioridad:** P2
- **Propuesta de corrección:** Adoptar la Alternativa B (Núcleo mínimo de procedencia) donde la semántica detallada sea opcional y delegada a perfiles de dominio.
- **Dependencias:** `architecture-review.md`.
- **Criterio de cierre:** Aprobación de especificación simplificada.
- **Estado:** Open

---

### GAP-007 — Ausencia de integración continua para validaciones documentales
- **ID:** GAP-007
- **Dominio:** Calidad / Reproducibilidad
- **Hallazgo:** No existen workflows de GitHub Actions (`.github/workflows`) para validar automáticamente enlaces rotos, sintaxis Markdown, trazabilidad de requisitos o validez de esquemas.
- **Evidencia:** Inexistencia del directorio `.github/` en el árbol del proyecto.
- **Causa probable:** Enfoque exclusivo en la producción de documentación manual.
- **Impacto:** Riesgo constante de degradación documental, enlaces rotos y referencias desactualizadas a medida que el proyecto crezca.
- **Probabilidad:** Alta.
- **Severidad:** Medium
- **Prioridad:** P2
- **Propuesta de corrección:** Crear un workflow CI basico con `markdownlint` y comprobador de enlaces relativos.
- **Dependencias:** Ninguna.
- **Criterio de cierre:** Workflow de CI activo y ejecutable en repositorio.
- **Estado:** Open

---

### GAP-008 — Indefinición de la estructura de sanitización de logs de auditoría
- **ID:** GAP-008
- **Dominio:** Seguridad / Privacidad
- **Hallazgo:** El requisito `SEC-REQ-012` exige que los logs no revelen secretos o datos sensibles, pero no existe una especificación de qué campos se redactan ni el formato del log estructurado.
- **Evidencia:** `docs/02-diseno/adr/0005-logging-recovery-and-data-lifecycle.md`.
- **Causa probable:** Diferimiento del diseño de esquemas de trazabilidad a la fase de implementación.
- **Impacto:** Filtración involuntaria de credenciales o PII (información personal identificable) en los registros de auditoría durante las primeras pruebas.
- **Probabilidad:** Media.
- **Severidad:** Medium
- **Prioridad:** P2
- **Propuesta de corrección:** Diseñar el esquema JSON/estructurado del log definiendo tipos de datos seguros y redactores automáticos (`Redacted<T>`).
- **Dependencias:** ADR-0005.
- **Criterio de cierre:** Especificación de log seguro redactada en ADR-0005.
- **Estado:** Open

---

### GAP-009 — Fricción de accesibilidad entre guía de inicio y especificación
- **ID:** GAP-009
- **Dominio:** Accesibilidad / Experiencia de Desarrollador
- **Hallazgo:** `docs/00-empezar/` utiliza un lenguaje extremadamente divulgativo y simplificado ("para no programadores"), mientras que la carpeta `03-preimplementacion/` exige conceptos avanzados de epistemología, lógica formal y seguridad sin un puente conceptual claro.
- **Evidencia:** Comparación de `docs/00-empezar/primer-experimento.md` vs `docs/03-preimplementacion/unified-specification-candidate-v0.md`.
- **Causa probable:** Redacción orientada a dos audiencias distintas sin integrar un itinerario progresivo real.
- **Impacto:** Desorientación de los lectores no técnicos o nuevos colaboradores al saltar del material divulgativo a las especificaciones.
- **Probabilidad:** Alta.
- **Severidad:** Low
- **Prioridad:** P3
- **Propuesta de corrección:** Rearreglar el itinerario pedagógico con un nivel intermedio en `docs/01-investigacion/`.
- **Dependencias:** `README.md`.
- **Criterio de cierre:** Itinerario actualizado en `README.md`.
- **Estado:** Open

---

### GAP-010 — Indefinición del proceso normativo de consolidación de especificaciones
- **ID:** GAP-010
- **Dominio:** Gobernanza
- **Hallazgo:** Documentos clave como `unified-specification-candidate-v0.md` y `design-freeze-candidate-v0.md` contienen títulos sugestivos de autoridad, pero el mapa de autoridad (`contract-authority-map.md`) sigue marcado como "propuesta".
- **Evidencia:** `docs/03-preimplementacion/contract-authority-map.md`.
- **Causa probable:** Proliferación de documentos de síntesis sin una regla de resolución formal.
- **Impacto:** Confusión sobre cuál es la especificación vigente en caso de discrepancia.
- **Probabilidad:** Media.
- **Severidad:** Medium
- **Prioridad:** P2
- **Propuesta de corrección:** Aprobar formalmente el Mapa de Autoridad Documental mediante una decisión explícita de gobernanza.
- **Dependencias:** Gobernanza del proyecto.
- **Criterio de cierre:** Documento `contract-authority-map.md` marcado como `APPROVED`.
- **Estado:** Open
