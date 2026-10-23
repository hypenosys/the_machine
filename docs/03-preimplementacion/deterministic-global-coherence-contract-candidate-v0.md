# Contrato de coherencia global determinista — candidato v0

**Fecha:** 2026-10-23. **Estado:** PROPUESTA DOCUMENTAL, SIN RATIFICAR. **Ámbito:** auditoría de documentos de THE MACHINE; no certifica código, experimentos, gates, permisos ni inexistencia de contradicciones.

## 1. Principio de determinismo

Dos auditores que utilicen el **mismo commit**, el **mismo conjunto de fuentes**, la **misma versión del extractor**, las **mismas reglas de normalización** y la **misma tabla de autoridad ratificada** deben producir un manifiesto canónico con idénticos identificadores, disposiciones y digest. Si cualquiera de esos insumos falta, el resultado es `INDETERMINATE` o `BLOCKED_BY_DECISION`, **nunca PASS por defecto**.

**No confundir:** reproducibilidad de una clasificación con verdad de sus premisas; determinismo no prueba corrección semántica ni validez jurídica.

## 2. Modelo mínimo de afirmación

Cada afirmación auditable debe registrar:

| Campo | Obligación |
|---|---|
| `claim_id` | Identificador estable y único, independiente de número de línea |
| `source_path`, `source_commit`, `source_span` | Evidencia verificable y versión |
| `literal` y `literal_digest` | Texto exacto y hash para detectar deriva |
| `subject`, `predicate`, `object` | Proposición normalizada, sin inferir equivalencias no declaradas |
| `modality` | `DESCRIPTIVE`, `PROPOSED`, `NORMATIVE`, `HISTORICAL`, `AUDIT_RECOMMENDATION` |
| `authority_status` | `RATIFIED`, `CANDIDATE`, `UNKNOWN`, `NOT_APPLICABLE` |
| `scope`, `valid_from`, `valid_to` | Alcance y temporalidad explícitos; `UNKNOWN` si no consta |
| `evidence_status` | `PAPER_ONLY`, `PROPOSED_UNEXECUTED`, `EXECUTED_UNVERIFIED`, `VERIFIED_FOR_SCOPE`, `UNKNOWN` |
| `dependencies` | Referencias a decisiones, gates y otras afirmaciones |
| `disposition` | Clasificación final con justificación y fuentes |

Las modalidades no son intercambiables. Una recomendación `CONDITIONAL GO` no equivale a una autorización `GO`. `VERIFIED_FOR_SCOPE` de procedencia no significa verdad epistemológica ni permiso operativo.

## 3. Disposiciones permitidas

- `CONSISTENT`: afirmaciones compatibles dentro de un alcance común probado.
- `DISTINCT_SCOPE`: aparentemente divergentes, pero con alcance, modalidad o fecha distintos documentados.
- `CONTRADICTION_OPEN`: afirmaciones incompatibles dentro del mismo alcance y autoridad, sin resolución válida.
- `BLOCKED_BY_DECISION`: conflicto cuya resolución exige una decisión reservada, como GAP-010/G3.
- `INSUFFICIENT_EVIDENCE`: faltan fuentes, autoridad, alcance, definición o prueba.
- `SUPERSEDED_RATIFIED`: una decisión acreditada sustituye otra **prospectivamente**, sin reescribir el historial.
- `NOT_EVALUATED`: afirmación aún no examinada.

`PASS_GLOBAL` no es una disposición individual: es un resultado agregado que solo puede emitirse si se cumplen todas las condiciones de la sección 5.

## 3.1. Orden de decisión y no determinismo encubierto

Para un mismo par de afirmaciones, aplicar **en este orden** las siguientes reglas candidatas, conservando todas las evidencias y sin permitir que una categoría posterior borre un bloqueo anterior:

1. **Cobertura:** si una fuente requerida no se ha examinado, marcar su afirmación `NOT_EVALUATED`; no clasificarla como consistente.
2. **Identidad, versión y alcance:** si falta una correspondencia verificable entre sujeto, predicado, ámbito o vigencia, clasificar el par `INSUFFICIENT_EVIDENCE`; no inventar equivalencias.
3. **Autoridad reservada:** si el resultado depende de precedencia, ratificación o delegación sin resolver (por ejemplo GAP-010/G3), clasificar `BLOCKED_BY_DECISION`, aun cuando las redacciones sean materialmente distintas.
4. **Sustitución acreditada:** solo un acto ratificado y verificable puede producir `SUPERSEDED_RATIFIED`, conservando el estado histórico anterior.
5. **Alcance o modalidad distintos:** si están documentados y son compatibles, clasificar `DISTINCT_SCOPE`.
6. **Incompatibilidad:** si ambas proposiciones verificablemente comparten sujeto, alcance, vigencia y autoridad y son incompatibles, clasificar `CONTRADICTION_OPEN`.
7. **Compatibilidad:** solo después de descartar los casos anteriores clasificar `CONSISTENT`.

**Agregación:** un corpus con al menos un `BLOCKED_BY_DECISION` o `CONTRADICTION_OPEN` es `NOT_READY`; también lo es si contiene `NOT_EVALUATED` o `INSUFFICIENT_EVIDENCE`. `INDETERMINATE` se reserva para imposibilidad de calcular el estado por falta del manifiesto, reglas o fuentes mínimas, y nunca se convierte automáticamente en PASS. Las disposiciones de distintos pares coexisten; el orden anterior solo decide el tratamiento **de un mismo par**.

**Límite epistemológico:** estas reglas son un **algoritmo candidato**; no existe todavía extractor implementado, evaluación completa ni ratificación. Un ejemplo que ofrece salidas alternativas sin condiciones de desempate viola el determinismo y debe corregirse antes de adoptar la especificación.

## 4. Reglas invariantes

**INV-01 — Identidad:** coincidencia textual no demuestra identidad de sujetos externos.

**INV-02 — Autoridad:** documento candidato, PR, permiso de escritura GitHub o `mergeable=true` no constituyen ratificación.

**INV-03 — Temporalidad:** un documento posterior no altera retrospectivamente el estado histórico de un documento anterior.

**INV-04 — Gates:** G2.1, G2.2, G2.3, G2.4 y G3 son transiciones diferenciadas; ninguna concede permisos implícitos. AUT-CODE, AUT-EXEC, AUT-MERGE y despliegue no se infieren entre sí.

**INV-05 — Evidencia:** fixtures propuestos F-11/E-11 y F-12/E-12 no cuentan como casos aprobados, ejecutados ni PASS. No confundir las series originales F-01..F-10 y E-01..E-10 con extensiones propuestas.

**INV-06 — Epistemología:** `CONFLICTO` sensorial, `CONFLICTED` epistemológico y `VERIFIED_FOR_SCOPE` de procedencia no tienen mapeo automático.

**INV-07 — Licencias:** preferencia GPL para software futuro no reemplaza el estado de licencia vigente ni resuelve derechos de terceros.

**INV-08 — Cierre:** ausencia de hallazgos detectados no equivale a ausencia de contradicciones; las fuentes no examinadas permanecen `NOT_EVALUATED`.

## 5. Predicado de cierre global

`PASS_GLOBAL(commit, ruleset, corpus)` requiere conjuntamente:

1. Manifiesto congelado del corpus con rutas, blobs/digests, fecha de corte y versión del extractor.
2. Cobertura completa de afirmaciones relevantes de ese corpus, no solo archivos abiertos ni enlaces Markdown inline.
3. Todas las rutas locales, anclas y referencias exigidas comprobadas; incidencias registradas con disposición reproducible.
4. Ninguna afirmación relevante `NOT_EVALUATED`, `INSUFFICIENT_EVIDENCE`, `CONTRADICTION_OPEN` ni `BLOCKED_BY_DECISION` para el alcance declarado.
5. Precedencia y autoridad ratificadas y verificables, con evidencia de identidad y alcance de la ratificación.
6. Decisiones de arquitectura, licencias, privacidad y gates trazadas a sus dependencias; ninguna autorización inferida.
7. Revisión independiente y reproducción del manifiesto con el mismo digest.
8. Cualquier cambio de commit, fuente, regla o decisión **invalida el PASS anterior para el nuevo corte** y exige revalidación.

Si falla cualquier requisito, producir `NOT_READY` con los bloqueos y su procedencia. Si falta información esencial para determinarlo, producir `INDETERMINATE`. No se permite un `PASS_GLOBAL` condicionado implícito.

## 6. Casos de control para el evaluador

| Caso | Fuentes / condición | Salida esperada |
|---|---|---|
| COH-01 | G3 previo a merge vs G3 previo a implementación; GAP-010 abierto | `BLOCKED_BY_DECISION` |
| COH-02 | `CONDITIONAL GO` de auditoría vs HOLD operativo | `DISTINCT_SCOPE` si las modalidades se conservan |
| COH-03 | F-11/E-11 descritos como tests ejecutados sin acta ni evidencia; el registro vigente indica propuestos/no ejecutados y coincide alcance temporal | `CONTRADICTION_OPEN` por incompatibilidad explícita de estados; si no se puede establecer identidad/alcance de las afirmaciones, `INSUFFICIENT_EVIDENCE` |
| COH-04 | PR `mergeable=true` presentada como autorización conjunta | `CONTRADICTION_OPEN` con INV-02 |
| COH-05 | Procedencia verificada presentada como verdad del claim | `CONTRADICTION_OPEN` con INV-06 |
| COH-06 | Licencia futura GPL tratada como licencia ya efectiva | `CONTRADICTION_OPEN` con INV-07 |
| COH-07 | 0 enlaces rotos en muestra presentado como auditoría completa | `INSUFFICIENT_EVIDENCE` con INV-08 |
| COH-08 | Cambio en el corpus tras obtener PASS | `NOT_READY` hasta nueva evaluación |

**Todos estos casos son oráculos de papel propuestos, no pruebas ejecutadas.**

## 7. Estado actual del proyecto

- `GAP-010`: **OPEN**; la autoridad y precedencia requieren decisión competente.
- `G3`: **BLOCKED_BY_DECISION**; dos usos documentados, sin definición ratificada común.
- `DEC-08 / G2.2`: **NO AUTORIZADOS**; la secuencia candidata no los activa.
- `F-11/E-11; F-12/E-12`: **PROPOSED_UNEXECUTED**.
- Auditoría de enlaces previa: **parcial y limitada a sintaxis inline**; no sustituye la cobertura de afirmaciones.
- Resultado global **actual**: `NOT_READY` por bloqueos y cobertura incompleta. No equivale a fallo experimental ni a autorización para modificar software.

## 8. Requisitos para una implementación futura del verificador

Esta especificación **no autoriza implementarla**. Una vez habilitado el código mediante las decisiones correspondientes, el verificador deberá leer el árbol Git por commit, no la rama mutable; producir JSON canónico con orden estable y hash reproducible; conservar todos los `NOT_EVALUATED`; ejecutar controles positivos y negativos; emitir un reporte humano con enlaces a fuente y diff entre cortes; y fallar en modo cerrado cuando una regla o fuente carezca de definición. El parser de Markdown debe distinguir texto literal y bloques de código de enlaces reales, evitando falsos positivos como `[texto](ruta)` usado como ejemplo.

**Fuentes base para contrastar:** `GOVERNANCE.md`, `docs/02-diseno/security/security-gates.md`, `docs/03-preimplementacion/staged-authorization-protocol-v1.md`, `docs/03-preimplementacion/traceability-matrix-v1.md`, `docs/03-preimplementacion/owner-ratification-sheet-candidate-v1.md`, `docs/03-preimplementacion/finch-consistency-decision-register-2026-10-23.md`, `docs/04-auditorias/gap-register.md`.
