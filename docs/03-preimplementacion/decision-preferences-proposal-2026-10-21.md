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

## Anexo: delimitación candidata de la delegación (para negociación)

| Materia | @Axlfc tras delegación **válidamente ratificada** | Reserva y salvaguarda |
|---|---|---|
| Agenda, clasificación de incidencias, prioridades y coordinación | Decisión técnica ordinaria documentada | Puede impugnarse por ambos cotitulares; sin cambio de gate |
| Documentación editorial no normativa | Proponer, revisar y coordinar integración bajo reglas de PR | Revisión por persona distinta; no reescribir actas históricas ni aprobarse a sí mismo |
| Diseño técnico no normativo | Resolver desacuerdo ordinario con motivación y alternativas | No convertir recomendación en ADR Accepted ni arquitectura seleccionada |
| Gestión de colaboradores y revisores | Proponer responsables y solicitar revisiones | Permisos GitHub, CODEOWNERS y autoridad normativa son distintos |
| Licencias, propiedad intelectual y terceros | **Sin delegación por defecto** | Acuerdo verificable de ambos cotitulares |
| G3, GAP-010, AUT-CODE/EXEC/MERGE, excepciones y datos reales | **Sin delegación por defecto** | Acta específica de ambos, incluso si existe delegación técnica general |
| Cambios a GOVERNANCE.md, precedencia y revocación de delegación | **Sin delegación por defecto** | Ambos cotitulares; una revocación válida suspende facultades futuras |

**Campos que debe contener el acta:** identificador y hash/revisión del texto; identidad y consentimiento verificable de ambos cotitulares; aceptación del delegado; fecha de entrada en vigor; alcance positivo y exclusiones; duración o fecha de revisión; mecanismo de publicación; resolución de conflicto; suspensión inmediata ante controversia de autoridad; revocación y efecto sobre decisiones previas. **No se propone consentimiento por silencio**. La ausencia de cualquiera de estos elementos mantiene la delegación en estado PENDIENTE.

## Anexo: protocolo de permisos separados (propuesta de semántica, no autorización)

| Permiso | Ejemplo de alcance futuro | Evidencia mínima previa | Lo que NO concede |
|---|---|---|---|
| AUT-CODE | Código descartable en rama y ruta expresamente identificadas | DEC-08, autoridad, revisión de riesgos, límites, duración, dependencias y revocación | Compilar, ejecutar, red, secretos, CI, merge |
| AUT-EXEC | Compilar y ejecutar únicamente en entorno offline delimitado | AUT-CODE si hay código nuevo, oráculos versionados, seguridad del entorno, datos sintéticos, política de residuos y parada | Merge, despliegue, efectos externos, datos reales |
| AUT-MERGE | Fusionar código revisado en rama objetivo | Evidencia de revisión competente, controles de protección, licencia resuelta y autorización expresa | Despliegue, operación ni cambio de gates por implicación |

La tabla **no sustituye** las reglas históricas de G3. Hasta que exista acta de precedencia y definición de gates, cualquier colisión se resuelve manteniendo HOLD / NO-GO.

## Anexo: comprobación de coherencia de autorizaciones y orden de decisión

**Regla de seguridad:** un permiso tiene alcance por **actividad y entorno**, no por el nombre del gate. El hecho de que AUT-CODE esté aprobado para una rama no concede AUT-EXEC; AUT-EXEC para un entorno no permite ejecutar en otro. AUT-MERGE no implica AUT-EXEC ni despliegue. Los tres son candidatos no vigentes.

| Caso límite | Interpretación candidata | Estado mientras falte acta |
|---|---|---|
| Se aprueba delegación técnica general, pero no el significado de G3 | El delegado coordina; no puede conceder excepciones ni reinterpretar gates | HOLD / NO-GO |
| Se aprueba DEC-01 offline, sin DEC-05 ni DEC-08 | Hay alcance conceptual, pero faltan oráculos y excepción de código | Sin creación ni ejecución |
| Se autoriza AUT-CODE sin AUT-EXEC | Se permitiría solo editar código dentro del alcance futuro expresamente ratificado | Compilación, tests, scripts y CI prohibidos |
| Se autoriza AUT-EXEC sin autorizar red ni secretos | Únicamente entorno y entradas aprobados, sin expansión por conveniencia | Red y secretos excluidos |
| GitHub informa `mergeable=true` | Señal técnica sobre conflictos, no aprobación normativa | No autoriza merge |
| La PR documental #25 recibe aprobación | Puede habilitar merge documental si se cumplen políticas y autoridad | No altera ADR, gates ni permisos de software |
| Un cotitular revoca o impugna delegación | Suspender decisiones nuevas en el ámbito controvertido hasta aclaración documentada; registrar efectos y decisiones ya tomadas | Sin aprobación por silencio |
| La GPL candidata se elige sin resolver derechos de terceros | Preferencia insuficiente para licenciar materiales ajenos o dependencias incompatibles | GAP-001 sigue abierto |

**Orden mínimo recomendado:** (1) revisión competente de este texto y registro de consentimiento de ambos cotitulares; (2) acta de delegación con límites; (3) acta de precedencia y definición de G3; (4) resolución de derechos/licencia y contratos del laboratorio; (5) solicitudes independientes de permisos, si se desean. Los puntos 1–4 son trabajo documental y **no autorizan** el punto 5.

## Criterios operativos por defecto — selección editorial, NO ratificación

**Alcance de esta sección:** el solicitante pide tomar decisiones sobre la marcha «en nombre de» ambos cotitulares. Esa petición no acredita por sí sola la identidad, representación ni aceptación de @Axlfc y @TopperH4rley. Por ello se fijan **opciones editoriales recomendadas y reversibles**, no decisiones conjuntas ni autorización ejecutiva. La atribución de aprobación a ambos permanece **PENDIENTE**.

| Tema | Opción editorial recomendada | Razón y condición de revisión |
|---|---|---|
| GAP-010 | Delegación técnica limitada y revocable a @Axlfc, excluyendo materias reservadas | Reduce bloqueos ordinarios sin convertir un rol propuesto en autoridad vigente; requiere acta conjunta |
| G3 | AUT-CODE / AUT-EXEC / AUT-MERGE separados, con G3 histórico pendiente de reconciliación | Evita que un permiso se convierta tácitamente en otro; no crea gates activos |
| GPL | **GPL-3.0-or-later** como variante preferente para análisis, **no licencia aplicada** | Permite evaluar continuidad de versiones futuras; revisar compatibilidad, copyleft, derechos y preferencia de ambos antes de elegir frente a GPL-3.0-only |
| Alcance | Laboratorio sintético local/offline, sin red, secretos, datos reales, persistencia duradera ni efectos externos | Menor superficie de riesgo para un primer experimento eventual; DEC-01..06 y DEC-08 pendientes |
| Arquitectura | Comparación neutral R1/R2/Híbrida C/Baseline D, con segundo dominio y sin ganador previo | La arquitectura debe depender de oráculos y criterios aprobados, no de una etiqueta «Opción A» |
| Privacidad | Datos reales fuera del alcance; F-10/E-10 original bloqueado | No se ha demostrado borrado físico ni gestión de backups/réplicas |
| Validación | Controles positivos y negativos, oráculos independientes, abstención y registro de no evaluables | Impide elevar propuestas o simulaciones a pruebas ejecutadas |

**Regla de actuación:** se permiten correcciones documentales reversibles en la PR en borrador; no se permite cambiar estados de aprobación, atribuir firmas, crear/compilar/ejecutar código, introducir dependencias, abrir CI experimental, fusionar PR ni modificar licencias vigentes mediante esta tabla. Cualquier decisión reservada requiere consentimiento verificable de ambos cotitulares según el procedimiento que se ratifique.

## Acta candidata de consentimiento conjunto — plantilla sin firmas

**Identificador propuesto:** ACT-GOV-001. **Versión a aprobar:** referenciar SHA exacto del documento y de `GOVERNANCE.md` al momento de deliberar; no basta con «la última versión». **Estado:** SIN EMITIR / SIN RATIFICAR.

> **Texto para deliberación, no declaración atribuida a ninguna persona:** «Las personas que consten identificadas como cotitulares acuerdan —solo tras manifestar cada una aceptación expresa y verificable— adoptar la delegación limitada descrita en P-01, sin incluir las materias reservadas. La vigencia comenzará únicamente en la fecha de eficacia consignada en el acta aprobada. La delegación será revocable mediante el procedimiento aprobado y su impugnación suspenderá provisionalmente las decisiones nuevas controvertidas. El presente acuerdo no autoriza crear, compilar, ejecutar ni fusionar código; las propuestas G3, GPL y laboratorio offline requieren decisiones independientes.»

| Campo obligatorio | Valor actual |
|---|---|
| Identidad y medio de acreditación de @Axlfc | **PENDIENTE** |
| Aceptación expresa de @Axlfc (como cotitular y delegado propuesto) | **PENDIENTE** |
| Identidad y medio de acreditación de @TopperH4rley | **PENDIENTE** |
| Aceptación expresa de @TopperH4rley | **PENDIENTE** |
| SHA exacto de texto sometido a aprobación | **PENDIENTE** |
| Fecha de eficacia, plazo/revisión y mecanismo de revocación | **PENDIENTE** |
| Alcance positivo, exclusiones y tratamiento de conflictos | **PENDIENTE** |
| Revisión independiente y conflicto de interés | **PENDIENTE** |
| Resultado | **NO RATIFICADO** |

**Criterio de cierre de GAP-010:** todas las aceptaciones y campos esenciales completos, ausencia de objeciones abiertas de autoridad y reconciliación documentada con `GOVERNANCE.md` y los gates. Un comentario de PR, una petición de un usuario o una capacidad técnica de merge no sustituyen esta evidencia. No se ha pedido ni obtenido ninguna firma mediante esta plantilla.

## Conciliación textual de GOVERNANCE.md y security-gates.md (21-10-2026)

**Comprobación documental, no ratificación:** `GOVERNANCE.md` identifica a ambos cotitulares y propone a @Axlfc como mantenedor con desempate técnico ordinario **solo tras aceptación verificable**. Reserva licencias, precedencia, gates, excepciones, privacidad y cambios de autoridad. Por tanto, la preferencia de delegación delimitada **es compatible como propuesta**, pero no prueba que la delegación ya exista. La revisión de PR por persona distinta del autor tampoco prueba independencia institucional ni aprobación normativa.

`docs/02-diseno/security/security-gates.md` mantiene la definición histórica de **G3 como control antes de fusionar código ejecutable**, mientras `staged-authorization-protocol-v1.md` propone G3 antes de iniciar implementación. No se debe sustituir una definición por otra silenciosamente. La separación candidata AUT-CODE/AUT-EXEC/AUT-MERGE evita mezclar actividades, pero **no resuelve por sí sola** qué número de gate corresponde a cada autorización. Las opciones de conciliación que deberán ratificarse son:

| Opción | Tratamiento de G3 histórico | Tratamiento de permisos | Riesgo principal |
|---|---|---|---|
| **S1 (preferencia editorial)** | Conservar G3 como control pre-merge hasta acta de reforma | AUT-CODE y AUT-EXEC como controles previos explícitos y separados, sujetos a DEC-08; AUT-MERGE exige además G3 | Exige actualizar de forma coordinada documentos que describen G3 como inicio de código |
| S2 | Renumerar formalmente G3 como puerta pre-código | Crear gate nuevo para pre-merge y migrar todas las referencias | Alta carga de migración y riesgo de enlaces/afirmaciones históricas engañosas |
| S3 | Mantener ambas acepciones con nombres cualificados | Autorizar únicamente con referencias inequívocas a versión de protocolo | Ambigüedad persistente y errores operativos de interpretación |

**Recomendación editorial S1:** minimiza reinterpretaciones retrospectivas y conserva el control pre-merge. **No está adoptada normativamente**: el texto de `security-gates.md` y los estados de G3 siguen intactos. La selección futura deberá indicar alcance, precedencia, versiones afectadas, migración de referencias y aprobaciones verificables de los cotitulares.
