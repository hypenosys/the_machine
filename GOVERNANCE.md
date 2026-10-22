# Gobernanza de THE MACHINE

**Estado:** propuesta documental para revisión de los cotitulares. Este documento no ratifica por sí mismo ADR, gates, permisos de ejecución ni el proceso normativo (GAP-010).

## 1. Roles

- **Cotitulares:** [@Axlfc](https://github.com/Axlfc) y [@TopperH4rley](https://github.com/TopperH4rley). Conservan la responsabilidad sobre identidad del proyecto, titularidad, licencias, autoridad y decisiones reservadas.
- **Mantenedor Principal propuesto: @Axlfc.** Responsable operativo de clasificar propuestas, facilitar la discusión, solicitar revisiones y decidir desacuerdos **técnicos ordinarios** tras escuchar a las partes. La designación ha sido indicada en la conversación por el solicitante, pero **no consta todavía aceptación o ratificación verificable de ambos cotitulares**; hasta que se documente, la facultad de desempate no se considera activada.
- **Mantenedores de área:** colaboradores designados para revisar componentes concretos; su nombramiento y alcance se registrarán en una PR. No adquieren facultades reservadas por revisar o fusionar cambios.
- **Colaboradores y revisores:** proponen cambios mediante issues/PRs y documentan observaciones, evidencias, riesgos y límites de sus revisiones.

La identidad de los roles, las delegaciones y las sustituciones deben quedar registradas de forma verificable; no se infieren de permisos técnicos de GitHub.

## 2. Flujo de propuestas y PRs

1. Abrir issue o PR con objetivo, alcance, archivos afectados, alternativas, riesgos y evidencias disponibles. Para cambios sustanciales, utilizar **draft PR** durante la elaboración.
2. Solicitar revisión de al menos una persona distinta de quien redacta. La autoevaluación no sustituye revisión independiente; la revisión documental no demuestra ejecución de pruebas.
3. Responder observaciones, resolver o dejar explícitos los desacuerdos y registrar decisiones y condiciones pendientes. Los comentarios no equivalen a aprobación normativa.
4. Una vez satisfechos los controles aplicables y la autorización competente, un mantenedor habilitado podrá fusionar. **Que GitHub muestre `mergeable=true` no equivale a autorización.** La mera fusión no ratifica ADR, gates ni decisiones reservadas.

**Situación actual:** mientras siga vigente el estado documental HOLD / NO-GO, este flujo permite preparar y revisar documentación, pero **no** autoriza por sí solo crear, compilar, ejecutar o desplegar código, dependencias, harness ni CI experimental. Cualquier excepción requiere decisión expresa, delimitada y trazable conforme a DEC-08 y los gates que correspondan.

## 3. Escalada en dos pasos

1. **Discusión:** las partes exponen opciones, fundamentos, objeciones y propuesta de resolución en el issue/PR. Se procura consenso y se deja un registro legible.
2. **Decisión del Mantenedor Principal:** si persiste un desacuerdo **técnico ordinario**, el Mantenedor Principal designado puede resolverlo motivadamente, citando alternativas y riesgos. La decisión se registra en el issue/PR y admite revisión posterior.

**Límite de autoridad:** este segundo paso no se aplica a licencias, derechos de terceros, cambios de titularidad, visibilidad, normas de precedencia (GAP-010), ratificación de ADR/gates, excepciones de ejecución (DEC-08), privacidad/retención o cambios de este reparto de autoridad. Tales asuntos se elevan a **ambos cotitulares**, quienes deberán acordar y documentar el mecanismo de aprobación. **Mientras no conste ese acuerdo, el asunto queda pendiente; no hay aprobación por silencio ni por decisión unilateral.** La designación propuesta de @Axlfc como Mantenedor Principal no activa la potestad de desempate hasta que quede registrada su ratificación por ambos cotitulares.

## 4. Registro y evolución

Cada decisión relevante debe identificar: asunto, alcance, alternativas, responsables, revisiones, objeciones, decisión, autoridad que la adoptó, fecha y referencia a issue/PR. Diferenciar **propuesto**, **aprobado**, **implementado** y **verificado**.

Si el proyecto crece, los cotitulares podrán proponer `.github/CODEOWNERS` para solicitar revisiones por áreas, siempre que los usuarios/equipos tengan los permisos exigidos por GitHub. CODEOWNERS **no reemplaza** las decisiones reservadas. Votaciones, quórums y delegaciones formales solo se introducirán mediante una revisión explícita de este documento.

## 5. Relación con documentos anteriores

Este archivo es una **propuesta de procedimiento**, no una solución automática a las discrepancias históricas sobre G0–G5, G2.1–G2.4 o GAP-010. Hasta su ratificación por la autoridad competente, las reglas de precedencia, aprobación conjunta y excepciones siguen pendientes. La licencia documental CC BY 4.0 se trata separadamente en `LICENSE.md`; no constituye autorización de desarrollo experimental.
