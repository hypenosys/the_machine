# Matriz de Trazabilidad y Correspondencia Falsable — THE MACHINE (v1)

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Ubicación:** `docs/03-preimplementacion/traceability-matrix-v1.md`
**Carácter:** **CANDIDATO NO NORMATIVO** (Matriz de trazabilidad y correspondencia de pruebas sintéticas pre-código).
**Estado de gobernanza:** **HOLD / NO-GO** (sin autorización para escribir, compilar o ejecutar código; esta matriz no acredita la ausencia de código o manifiestos Cargo en todas las ramas del repositorio)

---

## 1. Metodología de Correspondencia Reconstruida

En atención al **Defecto B-02**, la presente matriz propone correspondencias documentales de distinta solidez —directas, parciales o temáticas— entre:
- **Criterios de Falsación R-01..R-08** (definidos en `finch-consolidation-troubleshooting-candidate-v0.md` §5).
- **Fixtures Sintéticos F-01..F-10** (definidos en `precode-decision-protocol-v0.md`).
- **Oráculos de Aceptación E-01..E-10** (definidos en `offline-experiment-contract-candidate-v0.md` §4).
- **Escenarios de Ciclo de Vida y Privacidad L-01..L-10** (definidos en `evidence-lifecycle-privacy-candidate-v0.md`).

### Espacios de nombres de identificadores (aclaración no normativa)
- `F-xx`: fixtures del protocolo de decisión pre-código; `E-xx`: oráculos del contrato offline; `L-xx`: escenarios de ciclo de vida.
- `R-FALS-xx`: alias documental para los criterios R-01..R-08 de Finch §5. No renombra los originales.
- `R-RISK-xx`: alias documental para los riesgos R-01..R-10 del registro de riesgos de seguridad; **no equivalen** a `R-FALS-xx`.
- `ARCH-R1`, `ARCH-R2`, `ARCH-C`, `ARCH-D`: alternativas de arquitectura, distintas de las letras A/B/C/D empleadas en categorías de decisión y de otras taxonomías históricas.
- `CONFLICTED` es un dictamen epistemológico; `CONFLICTO` puede ser un estado del perfil de sensores. No existe equivalencia automática.
- `UNVERIFIED`/`VERIFIED` califican procedencia; `SUPPORTED`/`REFUTED`/`CONFLICTED`/`INSUFFICIENT`/`NOT_COMPARABLE` califican evaluación. No se sustituyen entre sí.

### Advertencia sobre cobertura R-08 (privacidad)

La fila R-08 es una **correspondencia temática**, no un test aprobado ni un oráculo suficiente. F-10/E-10 original permanece BLOQUEADO. Para probar que el sistema no declara borrado físico a partir de ocultación lógica haría falta un caso independiente, con observables y criterio de fallo propios, además de autorización expresa. Ningún test en memoria certifica destrucción física de copias, backups o réplicas.

### Reglas Metodológicas de Mapeo
1. **Verificación de Definiciones Literales:** Ninguna correspondencia se asigna por mera asociación temática superficial. Cada vínculo exige una justificación conceptual directa y verificable basada en el texto literal de la especificación original.
2. **Tratamiento de Ausencia de Fixtures ("SIN FIXTURE DIRECTO"):** Cuando un criterio R carece de un fixture directo en la serie F-01..F-10 o E-01..E-10, se registra explícitamente el texto **"SIN FIXTURE DIRECTO"** y se propone formalmente un nuevo caso sintético (ej. F-11, F-12), **sin renumerar ni alterar la secuencia de los fixtures preexistentes**.

---

## 2. Matriz de Correspondencia R-01..R-08 vs. F / E / L

| Criterio R (Falsación) | Definición Original del Criterio R | Fixture F Relacionado | Oráculo E Relacionado | Escenario L Relacionado | Justificación Concreta y Referencia Documental |
|---|---|---|---|---|---|
| **R-01** | Identidad externa fusionada por coincidencia textual | **SIN FIXTURE DIRECTO** *(Propuesta: F-11)* | **SIN FIXTURE DIRECTO** *(Propuesta: E-11)* | N/A | Ningún fixture F-01..F-10 evalúa la fusión de identidades externas por texto. Se propone F-11/E-11 para verificar que la coincidencia de un string no unifica entidades sin atestación de autoridad. |
| **R-02** | Fuente autoverificada | **F-03 (diseño directo)** | **E-03 (no ejecutado)** | **L-08 (relación indirecta)** | **Expectativa candidata:** F-03/E-03 exigen no elevar procedencia `UNVERIFIED` a `VERIFIED` por autodeclaración. La mera etiqueta del fixture no verifica criptográficamente a la fuente; L-08 trata autorización de borrado y no es un oráculo directo de autenticidad. No hay prueba ejecutada. |
| **R-03** | Dependencia conocida contada como corroboración independiente | **F-04 (diseño directo)** | **E-04 (no ejecutado)** | **L-03 (contexto de retractación)** | **Expectativa candidata:** preservar el ancestro común y no contar dos derivados de A como corroboración independiente. L-03 introduce además retractación y propagación histórica, que F-04/E-04 no verifican por sí solos. Sin oráculo versionado y ejecución no hay prueba de independencia de fuentes. |
| **R-04** | Conocimiento posterior retrodatado | **F-06 (cobertura parcial)** | **E-06 (cobertura parcial)** | **L-01, L-02 (contexto)** | **Cobertura PARCIAL:** F-06/E-06 permiten distinguir `valid_time`, `recorded_time` y `assessed_time`, pero no demuestran que un actor no pueda suministrar retrospectivamente un `recorded_time` falso. Para falsar R-04 se necesita un testigo de orden de registro independiente del dato y un oráculo previo; propuesta no ratificada (REV-13). |
| **R-05** | Evaluación/regla histórica sobrescrita sin rastro | **F-05 (cobertura parcial)** | **E-05 (cobertura parcial)** | **L-01, L-02 (contexto)** | **Cobertura PARCIAL:** F-05/E-05 observan conservación de versiones en el escenario sintético; no prueban inmutabilidad, resistencia a manipulación o recuperación tras reinicio en almacenamiento persistente. Se requiere un oráculo de historial y alcance de amenaza explícitos antes de afirmar protección contra sobrescritura. |
| **R-06** | Semántica de dominio aplicada fuera de alcance | **F-02, F-08 (cobertura parcial)** | **E-02, E-08 (no ejecutados)** | N/A | **Cobertura PARCIAL:** F-02/E-02 tratan unidades/ámbitos no comparables y F-08/E-08 versiones distintas; no demuestran que un perfil de dominio no pueda aplicar reglas fuera de su alcance a otros perfiles. Hace falta control cruzado con segundo dominio, versión de reglas y oráculo negativo específico; no aprobado (REV-09/17). |
| **R-07** | Conclusión convertida en permiso | **SIN FIXTURE DIRECTO** *(Propuesta: F-12)* | **SIN FIXTURE DIRECTO** *(Propuesta: E-12)* | N/A | **Cobertura NO DEMOSTRADA:** F-12/E-12 son propuestas sin ejecutar. Un Action Gateway real está fuera de alcance; solo un observador independiente con control positivo permitiría valorar la frontera sintética. Ausencia de eventos sin observador funcional = NO EVALUABLE, no PASS. |
| **R-08** | Supresión lógica presentada como eliminación física | **F-10 (relación temática; BLOQUEADO)** | **E-10 (BLOQUEADO; no es oráculo ejecutable de R-08)** | **L-06 (relación temática)** | **Cobertura NO DEMOSTRADA:** F-10 exige tratamiento de privacidad y referencias históricas, no constituye por sí solo un control directo de falsación de afirmaciones de borrado físico. R-08 requiere un oráculo distinto, identificador nuevo y autorización del titular; ninguna ocultación en memoria demuestra supresión física. |

---

### Contraste literal con fuentes originales y falsadores candidatos (sin ejecución)

Fuentes contrastadas en `master`: `finch-consolidation-troubleshooting-candidate-v0.md` §5 (R-01..R-08) y `precode-decision-protocol-v0.md` (F-01..F-10). Finch define **criterios**, no tests ejecutados. La columna «fallo observable» es una **propuesta de oráculo futuro**, no un resultado medido ni una ampliación aprobada de alcance.

| Criterio | Observación que lo falsaría en un ensayo autorizado | Límite de la evidencia existente |
|---|---|---|
| R-01 | Dos identidades externas con igual texto quedan fusionadas sin autoridad común | F-11/E-11 propuestos, no ejecutados |
| R-02 | Una fuente pasa de `UNVERIFIED` a `VERIFIED` solo por su declaración | F-03/E-03 prueban una regla declarativa, no autenticación criptográfica |
| R-03 | Dos derivados de una fuente única se cuentan como dos apoyos independientes | F-04/E-04 no demuestran descubrir dependencias ocultas ni retractaciones completas |
| R-04 | Una evaluación posterior aparece registrada como conocida antes de su ingreso real | F-06/E-06 separan campos; falta testigo independiente del orden de registro |
| R-05 | Una corrección elimina o hace vigente sin rastro una evaluación anterior | F-05/E-05 solo contemplan historial sintético, no resistencia a manipulación |
| R-06 | Un perfil aplica una regla a un dominio/versión fuera de su alcance sin abstención | F-02/F-08 no bastan para demostrar aislamiento entre perfiles |
| R-07 | Un dictamen `SUPPORTED` dispara una solicitud operativa sin orden autorizada | F-12/E-12 requieren observador independiente y control positivo; gateway real fuera de alcance |
| R-08 | El sistema afirma eliminación física tras ocultación lógica sin evidencia de supresión | F-10/E-10 BLOQUEADO; falta oráculo independiente y política de retención |

**Condición metodológica:** las observaciones propuestas deben fijarse antes de cualquier ejecución, junto con precondiciones, entradas sintéticas, controles positivos/negativos, alcance de amenaza y criterio de `NO EVALUABLE`. Un resultado favorable en un fixture no acredita por sí solo seguridad general, privacidad legal ni cumplimiento de R-01..R-08.

---

## 3. Matriz Completa de Fixtures F-01..F-10 y Oráculos E-01..E-10

A continuación se consolida la matriz documental de los diez fixtures sintéticos originales, indicando su oráculo candidato, escenario de ciclo de vida asociado y estado de ejecución. **Las expectativas son interpretaciones propuestas y no sustituyen los textos originales de F/E.** En particular, F-01 no demuestra por sí mismo el dictamen epistemológico `CONFLICTED`, ni el perfil sensor convierte automáticamente su estado `CONFLICTO` en un veredicto del núcleo general:

| ID Fixture | Precondición y Entrada Sintética | Resultado Esperado Observable | Oráculo E Mapeado | Escenario L Mapeado | Estado de Ejecución |
|---|---|---|---|---|---|
| **F-01** | Dos mediciones sintéticas en mismo instante/ámbito con valores incompatibles | Preservar ambas lecturas y detectar incompatibilidad **según el oráculo del perfil**. `CONFLICTO` (sensor) y `CONFLICTED` (dictamen epistemológico) son salidas distintas: ninguna traducción entre ellas está aprobada; no exigir `CONFLICTED` por la mera diferencia numérica | **E-01** | N/A | **NO EJECUTADO** |
| **F-02** | Dos valores con unidades o alcances no comparables sin regla de conversión | Abstención de juicio y respuesta estructurada `NOT_COMPARABLE` | **E-02** | N/A | **NO EJECUTADO** |
| **F-03** | Fuente no autenticada declara un hecho pretendiendo ser autenticada | Marcado de procedencia como `UNVERIFIED`; no elevar a `VERIFIED` por autodeclaración. El fixture original no exige un dictamen epistémico `INSUFFICIENT`. | **E-03** | **L-08 (Indirecto)** | **NO EJECUTADO** |
| **F-04** | Dos informes sintéticos derivados de una misma fuente primaria común | Identificación de ancestro común; no contar como corroboración independiente | **E-04** | **L-03** | **NO EJECUTADO** |
| **F-05** | Corrección o retractación de una lectura o atestación previa | Registro de versión posterior, preservando la evaluación histórica intacta | **E-05** | **L-01, L-02** | **NO EJECUTADO** |
| **F-06** | Entrada con `valid_time`, `recorded_time` y `assessed_time` dispares o ausentes | Preservación de la independencia temporal; no inferir simultaneidad | **E-06** | N/A | **NO EJECUTADO** |
| **F-07** | Entrada sintética que contiene «No se observó el evento P» | Preservación de polaridad modal (observación finita ≠ negación universal) | **E-07** | N/A | **NO EJECUTADO** |
| **F-08** | Afirmación contradictoria bajo versiones o ámbitos de software distintos | Detección de disparidad de ámbito/versión; abstenerse de conflicto falso | **E-08** | N/A | **NO EJECUTADO** |
| **F-09** | Evaluación requerida con datos de evidencia incompletos o insuficientes | Abstención de juicio y respuesta estructurada `INSUFFICIENT` | **E-09** | N/A | **NO EJECUTADO** |
| **F-10** | Datos marcados para supresión; diseñar privacidad compatible con referencias históricas (definición original F-10) | Registrar obligaciones de minimización y efectos sobre referencias; política pendiente (E-10 original). No sustituir por ocultación lógica en memoria | **E-10** *(BLOQUEADO)* | **L-06** | **BLOQUEADO** |

---

## 4. Propuestas de Nuevos Fixtures Sintéticos (F-11 y F-12)

Para investigar las brechas identificadas en R-01 y R-07, sin afirmar cobertura ni alterar la numeración de los fixtures preexistentes, se presentan dos **casos candidatos sin aprobación ni ejecución**:

### F-11 / E-11 — Fusión de Identidad Externa por Coincidencia Textual (Propuesta para R-01; cobertura no demostrada)
- **Precondición:** Dos atestaciones procedentes de fuentes distintas emplean la misma cadena de texto como identificador de entidad sintética sin atestación de autoridad común.
- **Entrada Sintética:** Atestación A (Fuente X, ID "sensor-01") y Atestación B (Fuente Y, ID "sensor-01").
- **Distinción entre Identidad y Verificación:** Se separa explícitamente el emparejamiento de identidad (*identity matching*) del estado de autenticación de la fuente (*verification status*). Una fuente puede tener procedencia `VERIFIED` **declarada como dato sintético por un oráculo externo**, sin validación criptográfica ejecutada; ello no autoriza colapsar entidades de fuentes distintas por coincidencia textual.
- **Resultado Esperado Observable (propuesta):** El sistema conserva dos identidades externas distintas pese a compartir cadena textual, sin inferir equivalencia ni relación autorizada. Un control positivo separado, con atestación de identidad común expresamente autorizada y reglas versionadas, deberá permitir vincularlas; sin ese control no se acredita que el detector discrimine entre coincidencia textual y equivalencia legítima. Sin oráculo y controles ejecutados: NO EVALUABLE.
- **Estado:** PROPUESTO / NO EJECUTADO. No demuestra autenticación ni resolución de identidades en sistemas externos.

### F-12 / E-12 — Prevención de Escalada de Evaluación a Comando Operativo (Propuesta para R-07 / P-01; cobertura no demostrada)
- **Precondición:** Un evaluador u oráculo emite un `Assessment` con resultado `SUPPORTED` sobre un hecho del dominio.
- **Entrada Sintética:** Emisión de `Assessment` positivo sobre el evento sintético.
- **Resultado Esperado Observable (propuesta no ejecutada):** Un observador independiente de la frontera registra cero solicitudes de acción cuando la única entrada es un dictamen `SUPPORTED`. Un control positivo separado, con una orden operativa sintética explícita, debe producir una señal observable para demostrar que el observador funciona. Sin ambos controles, el caso queda NO EVALUABLE, nunca PASS. Esto no verifica un Action Gateway real, que permanece fuera del alcance del laboratorio.
- **Estado:** PROPUESTO / NO EJECUTADO.

---

## 5. Diagnóstico candidato del oráculo y observador (no autorizado ni ejecutado)

Un veredicto futuro no puede inferirse solo del valor que devuelve la arquitectura bajo prueba. Para F-11 y F-12, la revisión independiente debe disponer **antes de ejecutar** de un manifiesto de casos sintéticos, reglas versionadas, salida esperada y un canal de observación separado del componente evaluado. Esta sección define **criterios documentales de diagnóstico**, no un harness aprobado.

| Señal observada en un ensayo futuro | Clasificación candidata | Regla para evitar falsos PASS |
|---|---|---|
| El control positivo no produce la señal esperada en el observador | `NO EVALUABLE — OBSERVADOR` | No concluir que el sistema impide fusiones o acciones; reparar y recalibrar el observador bajo nueva revisión |
| La entrada sintética o el oráculo carecen de versión, autoridad o expectativa inequívoca | `NO EVALUABLE — ORÁCULO` | No atribuir el desacuerdo a R1/R2/C/D; fijar la especificación antes de repetir |
| El observador funciona y una salida contradice una regla de oráculo previamente fijada | `FALLO OBSERVADO — PENDIENTE DE ATRIBUCIÓN` | Conservar entrada, salida, versión y rastro; investigar si falló representación, perfil, adaptador o harness |
| Los controles positivos/negativos funcionan y todas las salidas coinciden con el oráculo fijado | `COINCIDENCIA EN EL CASO` | No extrapolar a cumplimiento global de R-01..R-08, aislamiento real ni seguridad de producción |
| El registro no permite distinguir ausencia de evento de ausencia de observación | `NO EVALUABLE — VISIBILIDAD` | Nunca declarar `PASS` por silencio del registro |

**Independencia exigible:** el resultado esperado no debe derivarse de la salida de la arquitectura probada; el observador no debe compartir con ella el único punto de fallo que se pretende detectar. Un control positivo debe poder activar la misma ruta de observación que el caso negativo. Documentar explícitamente cualquier dependencia compartida; si compromete la discriminación, el caso es `NO EVALUABLE`.

**Trazabilidad mínima propuesta:** identificador de caso y control, revisión exacta del oráculo, versión del perfil, entradas sintéticas, orden de observación, salida y diagnóstico con atribución pendiente. La ausencia de estos datos impide declarar un resultado reproducible. No se prescribe almacenamiento duradero, conexión de red, ejecución ni mecanismo de firmas.

**Autoridad y estado:** pendiente de DEC-05/06/08, GAP-010 y autorización de gates aplicables. F-10/E-10 sigue BLOQUEADO; ningún criterio de esta tabla sustituye decisiones sobre retención o borrado físico. **NO EJECUTADO · HOLD / NO-GO**.
