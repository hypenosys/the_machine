# Hoja de decisiones de los titulares — candidata v1

**Cotitularidad declarada:** @Axlfc y @TopperH4rley. La presente corrección identifica a ambos como titulares del proyecto; **no presume** que cualquiera pueda ratificar unilateralmente, que se exija unanimidad ni que exista delegación. La regla de decisión conjunta, acreditación de identidad y mecanismo de resolución de desacuerdos quedan pendientes de acuerdo explícito de ambos (GAP-010 / REV-16). Hasta entonces, una firma o instrucción aislada no debe interpretarse como ratificación conjunta de gates.

**Estado:** PROPUESTA / SIN RATIFICAR · **HOLD / NO-GO** · 21-10-2026

Esta hoja reúne decisiones pendientes; **ninguna casilla se considera marcada**, y ni un commit, ni un comentario, ni un merge constituyen aceptación. La aprobación exige registro explícito de los titulares, alcance, fecha, revisión de los documentos afectados y mecanismo de revocación. No se presupone firma criptográfica.

| ID | Pregunta para los titulares | Alternativas que deben deliberarse | Efecto si no hay decisión |
|---|---|---|---|
| DEC-01 | ¿Limitar el primer corte a datos sintéticos, offline, sin efectos externos? | Sí / cambiar alcance documentando nuevos riesgos | Sin autorización de experimento |
| DEC-02 | ¿Comparar R1, R2, C y D, con segundo dominio y sin ganador previo? | Comparación completa / reducir con justificación | G2.2 bloqueado |
| DEC-03 | ¿Se delimita el núcleo puro sin E/S ni acceso al reloj, con E/S sintética en el harness? | Núcleo funcional y harness delimitado / abstracciones de E/S con riesgos explícitos | Frontera núcleo–harness pendiente; determinismo no demostrado |
| DEC-04 | ¿Qué política de retención, supresión y restauración aplica? | Política concreta / excluir por completo | F-10/E-10 original BLOQUEADO |
| DEC-05 | ¿Qué fixtures y oráculos versionados se autorizan? | F-01..09 y negativos aprobados / revisar alcance | Ninguna ejecución |
| DEC-06 | ¿Qué intercambio sintético, formato, E/S y dependencias se permiten? | Especificación limitada / no laboratorio | No hay permiso implícito para persistencia duradera |
| DEC-07 | **Instrucción recibida:** CC BY 4.0 para la documentación original; ¿qué materiales y titulares tienen derechos suficientes y qué licencia se aplicaría al software futuro? | Mantener la licencia documental incorporada en `LICENSE.md`, inventariar excepciones/terceros y decidir por separado sobre software y visibilidad | Licencia documental incorporada en la PR; `GAP-001` pendiente de revisión de alcance y cierre formal |
| DEC-08 | ¿Se autoriza una excepción temporal para código de laboratorio? | Excepción con lenguaje, límites, duración y revocación / no excepción | Prohibición total de código sigue vigente |
| GAP-010 | ¿Cuál es la precedencia normativa de documentos y quién ratifica gates? | Acta explícita de autoridad / mantener HOLD | G2.1 pendiente |
| G3 | ¿G3 regula iniciar código o fusionarlo? | Definición ratificada y relación con excepciones / sin cambio | Interpretaciones históricas en conflicto |
| REV-13 / tiempo | ¿Cómo distinguir orden de registro real de un `recorded_time` inyectado? | Testigo independiente / limitar las afirmaciones temporales | R-04 y resistencia a retrodatación no demostrados |
| REV-16 | ¿Cómo se acredita independencia de autoría, revisión y aprobación? | Revisores distintos con evidencia / declarar revisión no independiente | No atribuir revisión independiente |
| REV-17 | ¿Se versiona por separado perfil sensor y contrato genérico? | Adaptador, UTC, tolerancias y estados ratificados / diferir | No comparar semánticas incompatibles |
| REV-18 | ¿Se excluyen efectos remotos o se diseñan estados UNKNOWN y reconciliación? | Fuera del laboratorio / contrato remoto futuro separado | No afirmar exactly-once |
| REV-20 | ¿Qué versiones normativas se emplearán? | Referencias fechadas verificadas / referencias orientativas sin mapeos estables | No afirmar cobertura normativa específica |


## Preferencias registradas para deliberación (21-10-2026; no ratificadas)

La propuesta detallada está en [decision-preferences-proposal-2026-10-21.md](decision-preferences-proposal-2026-10-21.md). Se recibieron preferencias por **delegación formal revocable a @Axlfc**, **separación de permisos para escribir/ejecutar/fusionar código**, **evaluación de GPL-3.0 para software futuro** y **primer corte offline con datos sintéticos**. No constituyen acta de ambos cotitulares, aceptación del delegado ni aprobación de DEC-01/02/07, GAP-010 o G3. La variante GPL-3.0-only frente a GPL-3.0-or-later queda pendiente; CC BY 4.0 documental no cambia. AUT-CODE, AUT-EXEC y AUT-MERGE son etiquetas candidatas, **ninguna concedida**.

## Evidencia exigible por decisión

Registrar: identificador, opción elegida, razonamiento, riesgos residuales, documentos/versión exactos, autoridad del decisor, fecha, alcance temporal, condiciones de revocación y contradicciones aceptadas o resueltas. Si faltan, el estado es **PENDIENTE**, no `ACCEPTED`.

## Criterios de aceptación documental para DEC-02 y DEC-05 (propuesta, sin ejecución)

Antes de solicitar una ratificación de comparación, los titulares deben poder identificar la **revisión exacta** del contrato `comparative-contract-v1.md` y de la matriz `traceability-matrix-v1.md`. Los criterios añadidos en la PR #25 sobre controles positivos, oráculo independiente, abstención, denominadores, cohorte fija, repeticiones y segundo dominio **son candidatos**: no se convierten en reglas aprobadas por aparecer en un commit.

- **DEC-02 — comparabilidad:** confirmar R1, R2, C y D bajo las mismas entradas y perfiles, incluir un segundo dominio no sensor, fijar la unidad `(case_id, architecture_id)`, distinguir repeticiones de nuevos casos y prohibir un ganador previo. Si se reduce el alcance, documentar qué conclusión deja de ser legítima.
- **DEC-05 — oráculos:** fijar antes de cualquier observación el inventario y revisión de casos, expectativas, abstenciones admisibles, controles positivos y negativos, y clasificación de resultados. Registrar casos no evaluables y enmiendas sin borrarlos del denominador. F-11/F-12 siguen propuestos y no ejecutados; F-10/E-10 original sigue bloqueado.
- **Evidencia y autoridad:** documentar por separado quién propone, quién revisa y quién ratifica; si no hay independencia comprobable, declararlo. La revisión documental de la PR no equivale a aprobación del protocolo ni a autorización de pruebas.

**Resultado de la comprobación documental actual:** faltan ratificación de los titulares, oráculos y perfiles normalizados, controles observables, autorización del laboratorio y evidencia experimental. **DEC-02/05 PENDIENTES; G2.1 PENDIENTE; G2.2 BLOQUEADO.**

## Matriz de dependencias para deliberación (no equivale a autorización)

| Dependencia | Evidencia o decisión mínima pendiente | Consecuencia mientras falte |
|---|---|---|
| Autoridad documental | GAP-010: precedencia de fuentes, titular competente, acta explícita y alcance | Ningún documento candidato desplaza a los originales ni ratifica gates |
| Alcance y permisos | DEC-01 y DEC-08 separados: delimitar laboratorio, excepción de código y su revocación | Aprobar alcance conceptual no autoriza construir ni ejecutar |
| Comparación | DEC-02, DEC-05 y REV-17: segundo dominio, perfiles, oráculos y controles versionados | No existe comparación ejecutable ni ganador legítimo |
| Tiempo y atribución | DEC-03 y REV-13: frontera E/S, reloj inyectado y eventual testigo independiente | Determinismo y resistencia a retrodatación no demostrados |
| Intercambio y privacidad | DEC-04/06: formato sintético, límites de E/S, retención y supresión | F-10/E-10 original BLOQUEADO; simulación de memoria no prueba borrado físico |
| Seguridad y acción | REV-18 y verificaciones SEC-015..017 aún no ejecutadas | No afirmar exactly-once, aislamiento ni separación de acción comprobados |
| Independencia y referencias | REV-16/20: revisor acreditado y referencias normativas fechadas | No atribuir validación independiente o cumplimiento normativo |
| Distribución | DEC-07 / GAP-001: CC BY 4.0 documental incorporada por instrucción recibida, inventario de derechos y licencia de software pendiente | El aviso `LICENSE.md` permite reutilizar **solo** materiales cubiertos; visibilidad pública no licencia contenidos de terceros ni código futuro |

**Distinción de hitos:** la corrección documental puede preparar una decisión sobre G2.1, pero no sustituye su ratificación. Una eventual ratificación de G2.1 tampoco autoriza por sí sola G2.2, G2.3, G2.4 o G3. La excepción de código DEC-08, si alguna vez se concede, debe enumerar actividades permitidas y prohibidas; no se infiere de la aprobación de fixtures o de una PR.

## Revocación y cambios de alcance (protocolo candidato)

Una futura decisión expresa de los titulares no debe entenderse como permiso permanente o transferible. Cada autorización, si llegase a existir, tendría que especificar **objeto, revisión exacta, actividades permitidas, exclusiones, vigencia, autoridad y procedimiento de suspensión**. Una excepción para diseñar un fixture no habilita ejecutarlo; una excepción para un harness no habilita conectores, acciones remotas, persistencia duradera ni pruebas con datos reales.

**Reglas candidatas ante cambios:**

1. Si cambia la autoridad documental (GAP-010), el alcance (DEC-01), el oráculo (DEC-05), la frontera E/S (DEC-03/06) o el perfil (REV-17), revisar la validez de cualquier aprobación dependiente **antes de reutilizarla**; el cambio no hereda automáticamente permisos anteriores.
2. Si aparece una contradicción material, una evidencia de observador inválido o una violación de límites, suspender la **actividad afectada** y registrar causa, alcance, revisión y quién puede decidir su reanudación. No presentar esa suspensión como fallo probado del núcleo.
3. Si se revoca una excepción de código (DEC-08), cesa la autorización de nuevas actividades cubiertas por ella; documentar el tratamiento de artefactos ya producidos sin inferir permiso para retenerlos, publicarlos o destruirlos.
4. Las decisiones sobre privacidad, retención, publicación y licencia (DEC-04/07) requieren su propio tratamiento de obligaciones y derechos; la revocación no garantiza por sí sola eliminación física de copias ni reversión de distribuciones previas.

**Estado actual:** no hay permisos ni gates ratificados que revocar. Este texto describe únicamente cómo deberían delimitarse decisiones futuras; no crea un mecanismo operativo, una política legal ni autoridad nueva. **HOLD / NO-GO**.

## Acta de ratificación futura: campos mínimos sin cumplimentar

La siguiente plantilla **no es un acta emitida**. No contiene firma, fecha de aprobación ni identidad verificada del decisor. Sirve para evitar que un comentario, una aprobación de PR o un silencio se interpreten como autorización.

| Campo obligatorio | Valor actual |
|---|---|
| Identificador de decisión o gate | **PENDIENTE** |
| Autoridad y competencia acreditadas | **PENDIENTE** |
| Opción aprobada y alternativas descartadas | **PENDIENTE** |
| Revisión exacta de documentos, casos y perfiles afectados | **PENDIENTE** |
| Actividades permitidas y prohibidas; entorno y datos autorizados | **PENDIENTE** |
| Riesgos residuales y contradicciones expresamente aceptadas | **PENDIENTE** |
| Revisión independiente y conflictos de interés declarados | **PENDIENTE** |
| Vigencia, caducidad y condiciones de suspensión o revocación | **PENDIENTE** |
| Fecha, medio de constancia y referencia al registro de decisión | **PENDIENTE** |
| Efecto sobre G2.1/G2.2/G2.3/G2.4/G3, especificado uno por uno | **NINGUNO — SIN RATIFICAR** |

**Regla de interpretación:** no inferir consentimiento de una casilla vacía, del transcurso del tiempo, de un merge, de una revisión favorable o de la aprobación de otro gate. Un acta futura deberá enlazar la evidencia concreta que sustenta cada afirmación y declarar expresamente qué permanece bloqueado. La presencia de esta plantilla no constituye evidencia de aprobación.

## Secuencia de desbloqueo propuesta

1. Registrar el alcance de CC BY 4.0 documental ya incorporado en esta PR, revisar derechos de terceros y licencia de futuro software (DEC-07 / GAP-001); resolver por separado GAP-010/G3 sin alterar unilateralmente la visibilidad.
2. Definir DEC-01..06, REV-13, REV-17 y REV-18; preservar E-10 bloqueado.
3. Deliberar DEC-08 de forma **separada**: una decisión documental no autoriza construir o ejecutar harness.
4. Revisar de manera independiente las evidencias y decidir explícitamente sobre G2.1; G2.2..G2.4 siguen bloqueados hasta sus propias condiciones.

**No autoriza Rust, Cargo, CI, scripts ejecutables, pruebas, aceptación de ADR, GO o merge.**
