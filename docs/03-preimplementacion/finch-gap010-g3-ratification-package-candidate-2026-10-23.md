# Paquete Finch — decisión conjunta sobre GAP-010 y G3

**Estado:** DECISIÓN PROPUESTA / NO RATIFICADA. **Fecha:** 2026-10-23. **Cotitulares declarados:** @Axlfc y @TopperH4rley. **Efecto presente:** ninguno sobre gates, licencias, código, ejecución, merge o despliegue. **HOLD / NO-GO** permanece.

## 1. Problema que se somete a decisión

**GAP-010:** `GOVERNANCE.md` y `contract-authority-map.md` son propuestas. No existe una regla ratificada que acredite qué fuentes prevalecen, quién ratifica ni cómo se registra el consentimiento. **G3:** `docs/02-diseno/security/security-gates.md` define G3 como control **antes de fusionar código ejecutable**, mientras `docs/03-preimplementacion/staged-authorization-protocol-v1.md` propone G3 como puerta **antes de iniciar implementación Rust**. Ambas fuentes reconocen expresamente la colisión; ninguna puede sustituir a la otra por interpretación editorial.

## 2. Resolución Finch recomendada para GAP-010 — DEC-GOV-010

**Opción recomendada: delegación limitada, revocable, con reserva de materias.**

**Cláusula A — legitimidad.** La entrada en vigor requiere aceptación explícita y atribuible de ambos cotitulares respecto de **esta versión exacta**, con mecanismo acordado de identidad, consentimiento, publicación, impugnación y revocación. Hasta entonces, toda regla de este documento es candidata. El silencio, un comentario ambiguo, un commit o permisos GitHub no constituyen ratificación.

**Cláusula B — jerarquía por competencia y estado.** Si se ratifica, aplicar por orden: (1) actas vigentes expresamente ratificadas y dentro de su competencia y alcance; (2) decisiones/ADR expresamente aceptados por autoridad competente, dentro de su alcance y sin contradecir actas reservadas; (3) normas de gobernanza y seguridad ratificadas; (4) especificaciones técnicas ratificadas y versionadas; (5) propuestas, informes de auditoría, experimentos y deliberaciones como evidencia no vinculante. **No se presume precedencia entre documentos del mismo nivel**: si son incompatibles y no hay acto expreso de supersesión, registrar `CONTRADICTION_OPEN` y mantener HOLD para la actividad afectada. La fuente posterior no prevalece por fecha, número de PR o merge. La jerarquía solo regirá desde su ratificación; no reescribe la autoridad histórica.

**Cláusula C — delegación.** Tras ratificación y aceptación expresa del delegado, @Axlfc podrá decidir prioridades, clasificación de incidencias, coordinación de revisiones y discrepancias técnicas ordinarias **no normativas**, con motivación y registro. Quedan reservados a ambos cotitulares: titularidad, licencias, derechos de terceros, precedencia normativa, cambios de gobernanza, gates, permisos de código/ejecución/merge, excepciones DEC-08, datos reales, privacidad y revocación o ampliación de la delegación. No se activa por este borrador.

**Cláusula D — desacuerdo y revocación.** Una objeción fundada sobre materia reservada suspende la decisión afectada hasta resolución conjunta; una revocación atribuible se registra con fecha, alcance y efecto prospectivo, sin borrar actas históricas. No hay consentimiento por silencio. La suspensión de un permiso no implica destruir evidencia.

**Cláusula E — prueba de autoridad.** Cada decisión futura contendrá `decision_id`, texto/version/commit, objeto, competencia, decisores identificados, declaraciones de consentimiento, revisiones independientes, límites, inicio, caducidad o revisión, revocación, supersesiones y referencias verificables. Si falta un campo esencial: `PENDING`.

## 3. Resolución Finch recomendada para G3 — DEC-GATE-003

**Opción recomendada: conservar G3 histórico como puerta de integración y crear permisos separados, sin renumeración retroactiva.** Esta opción minimiza reinterpretaciones de fuentes existentes.

- **G2 / preparación:** diseño y evaluación documental; G2.1 no concede escritura ni ejecución. G2.2, si se desea, requiere excepción DEC-08 expresamente delimitada.
- **AUT-CODE:** autorización específica para crear/modificar código, indicando repositorio, rama, lenguaje, alcance, datos, dependencias, duración y revocación. No autoriza compilar, ejecutar, fusionar ni desplegar.
- **AUT-EXEC:** autorización separada para compilar, ejecutar pruebas, harness o CI, con entorno, red, E/S, datos, secretos, límites y criterios de parada. No se deduce de AUT-CODE.
- **G3 histórico / AUT-MERGE:** G3 conserva la función **pre-merge de código ejecutable** documentada en `security-gates.md`. AUT-MERGE es la decisión competente para integrar una revisión específica después de satisfacer controles G3, revisión independiente y demás condiciones. Que G3 sea satisfecho **no** concede automáticamente AUT-MERGE.
- **G4 / G5:** despliegue y operación conservan sus controles propios. Ninguno de AUT-CODE, AUT-EXEC o AUT-MERGE habilita despliegue.

**Tratamiento del protocolo por etapas:** el uso candidato «G3 = inicio de implementación» queda marcado `SUPERSESSION_PROPOSED`, no `SUPERSEDED_RATIFIED`. Si los cotitulares ratifican esta decisión, se deberá actualizar coordinadamente `staged-authorization-protocol-v1.md`, `security-gates.md`, `GOVERNANCE.md`, readiness reviews, matriz de trazabilidad y registro de decisiones; conservar referencias históricas con nota de versión. No modificar ahora su semántica como si el acuerdo ya existiera.

## 4. Matriz de dependencias y condiciones

| Acto | Requisito | Lo que desbloquea si se ratifica | Lo que no desbloquea |
|---|---|---|---|
| DEC-GOV-010 | Consentimiento verificable de ambos cotitulares y aceptación del delegado | Regla de precedencia y delegación ordinaria delimitada | Gates, licencias, código |
| DEC-GATE-003 | DEC-GOV-010 en vigor o mecanismo conjunto explícito equivalente; decisión competente sobre G3 | Definiciones y proceso de permisos | AUT-CODE, AUT-EXEC, AUT-MERGE concretos |
| G2.1 | Protocolo documental, contratos y autoridad válidamente aprobados | Solo aprobación documental | G2.2, código, ejecución |
| DEC-08 / G2.2 | Acta específica, alcance offline/sintético, límites, revocación y controles | Solo actividades de laboratorio expresamente concedidas | Código de producto, datos reales, red, despliegue |
| AUT-CODE | Decisión independiente, revisión exacta y alcance | Escritura delimitada | Compilar/ejecutar/fusionar |
| AUT-EXEC | Decisión independiente, entorno y pruebas delimitados | Ejecución delimitada | Fusionar/desplegar |
| G3 + AUT-MERGE | Controles pre-merge, revisión independiente y acto competente | Integración de revisión específica | G4, G5, ratificación automática de ADR |

## 5. Acta de ratificación — deliberadamente vacía

| Declaración requerida | Estado | Evidencia |
|---|---|---|
| @Axlfc acepta DEC-GOV-010 versión exacta | PENDIENTE | — |
| @TopperH4rley acepta DEC-GOV-010 versión exacta | PENDIENTE | — |
| @Axlfc acepta DEC-GATE-003 versión exacta | PENDIENTE | — |
| @TopperH4rley acepta DEC-GATE-003 versión exacta | PENDIENTE | — |
| @Axlfc acepta la delegación, si se ratifica | PENDIENTE | — |
| Identidad, consentimiento y mecanismo de revocación verificados | PENDIENTE | — |
| Revisión independiente del paquete | PENDIENTE | — |

**No existe voto delegado ni consentimiento implícito.** Una ratificación parcial de GAP-010 no aprueba G3. Una ratificación de G3 no concede permisos AUT-*.

## 6. Decisión editorial de esta PR

Este paquete puede revisarse y corregirse como **propuesta documental**. No cerrar `GAP-010` ni `G3` en el registro de gaps, no cambiar gates a `ACCEPTED`, no alterar licencia de software y no fusionar código por este documento. **Resultado presente: GAP-010 OPEN, G3 BLOCKED_BY_DECISION, HOLD / NO-GO.**
