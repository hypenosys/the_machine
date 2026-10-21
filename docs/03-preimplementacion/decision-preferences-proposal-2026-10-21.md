# Propuesta de decisiones y dependencias — preferencias recibidas el 21-10-2026

**Estado:** BORRADOR PARA DELIBERACIÓN / NO RATIFICADO · **HOLD / NO-GO**.
**Rama de trabajo:** `docs/independent-review-remediation-20261021`; PR #25.
**Cotitulares declarados:** @Axlfc y @TopperH4rley. Las preferencias expresadas por un interlocutor no acreditan consentimiento de ambos, identidad ni delegación vigente.

## Texto candidato de decisión

### P-01 — GAP-010: delegación formal delimitada
**Preferencia recibida:** modelo de delegación formal a @Axlfc, Mantenedor Principal propuesto.

**Redacción candidata:** «Los cotitulares podrán conferir a @Axlfc, previa aceptación verificable y acta conjunta, una delegación **revocable y de alcance expreso** para decisiones técnicas ordinarias, coordinación de revisiones, priorización y mantenimiento documental. La delegación identificará facultades concretas, límites, fecha de inicio, duración o revisión periódica, suplencia, publicidad del registro y procedimiento de revocación. **No** incluye, salvo acuerdo conjunto expreso y específico, cambios de titularidad, licencias, derechos de terceros, precedencia normativa, definición o aprobación de gates, excepciones para código/ejecución, tratamiento de datos reales, privacidad ni cambios a esta propia delegación. El desacuerdo sobre materia reservada mantiene HOLD. Los permisos de GitHub no prueban autoridad normativa.»

**Para ratificar:** aceptación verificable de ambos cotitulares y del delegado, registro de versión y alcance, regla de consentimiento conjunto, revocación y tratamiento de conflicto de intereses. **GAP-010 permanece abierto.**

### P-02 — G3: separar tres permisos
**Preferencia recibida:** desdoblar inicio de código, ejecución y merge.

**Redacción candidata:** «Se establecerán tres autorizaciones independientes y trazables: (A) **AUT-CODE**, permiso acotado para crear/modificar código, con lenguaje, rama, duración, dependencias y revocación; (B) **AUT-EXEC**, permiso para compilar/ejecutar harness, tests, CI o experimentos, con entorno, E/S, red, secretos, datos, retención y criterios de parada; (C) **AUT-MERGE**, permiso para integrar cambios de código tras revisión y comprobaciones aplicables. Ninguna autorización implica las otras; un merge técnico posible no es autorización normativa. La fusión **solo documental** seguirá su propio proceso y no concede A, B ni C. Los nombres AUT-* son etiquetas propuestas, **no gates activos**. La ubicación y numeración definitiva de G3 frente al gate histórico de pre-merge se decidirán mediante acta de precedencia y actualización coordinada de fuentes.»

**Para ratificar:** resolver explícitamente D-05/REV-05, fijar autoridad y criterios de entrada/salida por permiso, reconciliar `security-gates.md` y `staged-authorization-protocol-v1.md`. **No se concede ninguna autorización.**

### P-03 — DEC-07 / GAP-001: GPL como candidata para software
**Preferencia recibida:** familia GPL.

**Redacción candidata:** «Se evaluará **GPL-3.0** para software futuro, con preferencia inicial por identificar si corresponde **GPL-3.0-only** o **GPL-3.0-or-later**; esta diferencia se someterá a decisión específica. Se estudiarán compatibilidad de dependencias y componentes, contribuciones, titulares de copyright, obligaciones de distribución, interacción con servicios y posibles excepciones antes de publicar software bajo esa licencia. `LICENSE.md` mantiene CC BY 4.0 **solo para la documentación original cubierta**; la preferencia GPL no relicencia automáticamente documentos, materiales de terceros ni software aún inexistente.»

**Para ratificar:** inventario de derechos y dependencias, variante exacta, política de contribuciones, tratamiento de archivos mixtos y decisión competente de ambos cotitulares o autoridad formalmente delegada para esa materia (hoy no delegada). **GAP-001 abierto.**

### P-04 — DEC-01 / DEC-02: primer corte offline
**Preferencia recibida:** laboratorio de evidencia sintética offline.

**Redacción candidata:** «Se priorizará como primer alcance de diseño un laboratorio local, offline, con datos sintéticos, sin secretos, efectos externos, red ni datos personales reales. Se compararán **R1 (seis entidades), R2 (Artifact + Attestation), Híbrida C y Baseline D** bajo las mismas entradas y criterios; ningún ganador se presupone. El **corte funcional A** no equivale a seleccionar la arquitectura R1. Se exige un segundo dominio no sensor, oráculos independientes versionados, controles positivos y negativos, abstención y denominadores fijados antes de observar resultados. El alcance elegido **no autoriza construir ni ejecutar** el laboratorio.»

**Para ratificar:** DEC-03, DEC-04, DEC-05 y DEC-06, perfiles de dominio, manifiesto de casos, amenazas, permisos AUT-CODE/AUT-EXEC y revisión independiente. F-10/E-10 original continúa BLOQUEADO.

## Matriz de dependencias (sin decisiones ejecutivas)

| Orden | Dependencia | Requisito de salida documental | Estado actual | Desbloquea solo si se ratifica |
|---|---|---|---|---|
| 0 | PR #25 / revisión | Auditoría del diff, revisión competente y aprobación documental | DRAFT, HOLD; revisión solicitada, no equivale a aprobación | Posible consolidación documental, **no código** |
| 1 | GAP-010 / P-01 | Acta conjunta, aceptación de @Axlfc, delegación delimitada, revocación y precedencia | Preferencia expresada, **no ratificada** | Autoridad válida para decisiones delegadas futuras |
| 2 | D-05 / G3 / P-02 | Tres permisos separados, semántica de G3 y reconciliación de fuentes | **Colisión normativa abierta** | Procedimiento de autorizaciones, no su concesión |
| 3 | DEC-07 / GAP-001 / P-03 | GPL-3.0-only vs -or-later, derechos, dependencias y contribuciones | **Candidata**; CC BY 4.0 documental existente | Elección de licencia de software, no desarrollo |
| 4 | DEC-01/02 / P-04 | Alcance offline, R1/R2/C/D sin ganador, segundo dominio | **Candidato** | Base de especificación de comparación |
| 5 | DEC-03/06 | Frontera núcleo/harness, E/S, reloj, dependencias, formatos y entorno | Pendiente | Contrato acotado para solicitar AUT-CODE |
| 6 | DEC-04 | Exclusión de datos reales, retención/supresión y evidencia de borrado | F-10/E-10 BLOQUEADO | Política de privacidad aplicable al alcance |
| 7 | DEC-05 + REV-13/17/20 | Oráculos, fixtures, perfiles, controles, marcas temporales y referencias | No ejecutado, pendiente de aprobación | Protocolo verificable, no resultados |
| 8 | REV-16/18 | Independencia de revisión; efectos remotos excluidos o contratados aparte | Pendiente | Revisión de seguridad y delimitación de efectos |
| 9 | AUT-CODE (propuesto) | Autorización competente, alcance, duración y revocación | **NO CONCEDIDO** | Solo escritura de código dentro del alcance |
| 10 | AUT-EXEC (propuesto) | Permiso separado para compilación, pruebas y experimentos | **NO CONCEDIDO** | Solo ejecución acotada, no merge |
| 11 | AUT-MERGE (propuesto) | Revisión, evidencia, cumplimiento de políticas y aprobación competente | **NO CONCEDIDO** | Posible integración de código, no despliegue |

**Dependencias no necesariamente secuenciales:** los puntos 3 a 8 pueden prepararse documentalmente en paralelo tras definir autoridad y precedencia. Ninguna fila «desbloquea» automáticamente otra; cada permiso exige decisión propia.

## Registro de aceptación propuesto (vacío deliberadamente)

| Persona/rol | Declaración de aceptación de esta versión | Fecha y referencia verificable |
|---|---|---|
| @Axlfc — cotitular / delegado propuesto | **PENDIENTE** | — |
| @TopperH4rley — cotitular | **PENDIENTE** | — |
| Revisión independiente competente | **PENDIENTE** | — |

**Invariantes:** ADR-0001..0005 continúan Proposed; G2.1 pendiente; G2.2..G2.4 bloqueados; G3 sin semántica ratificada; no se han ejecutado pruebas; no se afirma cero contradicciones. Esta propuesta **no modifica `GOVERNANCE.md` ni los gates vigentes** y no sustituye las decisiones DEC-01..08 de la hoja candidata.
