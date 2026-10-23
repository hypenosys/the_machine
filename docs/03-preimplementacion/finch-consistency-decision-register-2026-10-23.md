# Registro Finch de coherencia y decisiones — 2026-10-23

**Estado:** CANDIDATO DOCUMENTAL / SIN RATIFICAR. **Código:** HOLD / NO-GO.  
**Base auditada:** `master@6a7cf074c961186fcbf5d0f34243149975f63fb1`.  
**Alcance:** interpretación consistente de documentos existentes, no adopción de ADR, autorización, verificación experimental ni declaración de cero contradicciones.

> **Actualización de seguimiento (23-10-2026; no altera la base auditada):** la propuesta de resolución conjunta para `AUTH-01` / GAP-010 y `AUTH-02` / G3 está consolidada en el [paquete Finch DEC-GOV-010 / DEC-GATE-003](finch-gap010-g3-ratification-package-candidate-2026-10-23.md). Se han registrado una revisión `APPROVED` de @Axlfc sobre la PR #33 y un comentario favorable «OK» bajo el encabezado GAP-010/G3 en la cuenta @TopperH4rley. Estas evidencias **no identifican por sí solas una ratificación conjunta de la versión normativa exacta** ni autorizan código, ejecución o merge. Las filas `AUTH-01` y `AUTH-02` continúan `OPEN`. El estado de este registro es una evaluación documental, no una certificación independiente del diff actual.

## 1. Reglas de lectura y autoridad

1. Separar **observación documental**, **inferencia**, **propuesta**, **ratificación**, **implementación** y **verificación**. Una revisión o merge documental no ratifica nada.
2. `GOVERNANCE.md`, `contract-authority-map.md` y `staged-authorization-protocol-v1.md` son **propuestas**. GAP-010 permanece abierto: este registro no establece precedencia normativa.
3. Los informes históricos se leen en su fecha y alcance; una actualización posterior no convierte retrospectivamente sus hallazgos en errores.
4. `CONDITIONAL GO` de `docs/04-auditorias/readiness-assessment.md` es una **recomendación de auditoría**; `docs/03-preimplementacion/readiness-review.md` y el estado vigente conservan **HOLD/NO-GO para código**.
5. Una arquitectura **representable en papel** no está **validada por pruebas**. Los casos F/SEM/PROV y oráculos son propuestas no ejecutadas.
6. Una recomendación del primer **vertical** de investigación (opción A de DEC-01) no selecciona la arquitectura R1 (seis entidades) de DEC-02.
7. Los permisos para escribir, compilar, ejecutar, fusionar y desplegar se distinguen; ninguno se deduce de permisos GitHub, `mergeable=true` o una PR.

## 2. Vocabulario inequívoco propuesto

| Identificador | Significado | Riesgo que evita |
|---|---|---|
| SLICE-EVIDENCE-01 | Laboratorio offline de evidencias sintéticas (DEC-01 opción A) | Confundir el vertical con R1 |
| ARCH-R1 | Seis entidades Source/Artifact/Claim/EvidenceLink/Assessment/Relation | Elección anticipada |
| ARCH-R2 | Artifact + Attestation | Equivalencia ficticia |
| ARCH-C | Híbrido con perfiles | Confundir C con otros informes |
| ARCH-D | Baseline específico de dominio | Confundir D con otros informes |
| AUT-CODE | Autorización de creación de código en alcance determinado | Inferir permiso de G2.1 |
| AUT-EXEC | Autorización de compilación/ejecución delimitada | Inferir permiso de AUT-CODE |
| AUT-MERGE | Autorización de integración en rama protegida | Confundir mergeable con autorizado |

Estos nombres son **alias editoriales candidatos**, no renumeración retroactiva de decisiones.

## 3. Dependencias y puertas de salida

| ID | Dependencia real | Documento base | Evidencia de cierre exigible | Estado al corte |
|---|---|---|---|---|
| AUTH-01 | Autoridad y precedencia (GAP-010) | [GOVERNANCE.md](../../GOVERNANCE.md); [contract-authority-map.md](contract-authority-map.md) | Acta atribuible y aceptada conforme al mecanismo acordado por cotitulares | OPEN |
| AUTH-02 | Interpretación G3, G2.1–G2.4 y DEC-08 | [security-gates.md](../02-diseno/security/security-gates.md); [staged-authorization-protocol-v1.md](staged-authorization-protocol-v1.md) | Secuencia sin ciclo; permisos y revocación separados | OPEN |
| SEM-01 | Identidad, negación, alcance, modalidad | [claim-semantics-v0.md](claim-semantics-v0.md) | Oráculos positivos/negativos y vocabularios versionados | OPEN |
| SEM-02 | Estados epistemológicos vs garantías de procedencia | [general-epistemic-contract-v0.md](general-epistemic-contract-v0.md); [provenance-assurance-matrix-v0.md](provenance-assurance-matrix-v0.md) | Espacios tipados separados, sin mapeo automático | OPEN |
| TIME-01 | valid/recorded/assessed y testigo de orden | `claim-semantics-v0.md`; GAP-003; REV-13 | Contrato temporal con orden de registro no autodeclarado | OPEN |
| LINEAGE-01 | Dependencia desconocida, retractación y evaluación histórica | [evidence-dependencies-and-retractions.md](evidence-dependencies-and-retractions.md) | Casos con origen común y revisiones exactas | OPEN |
| PRIV-01 | Supresión física frente a ocultación lógica | DEC-04; F-10/E-10 | Política y oráculo externo para borrado real, o exclusión expresa | BLOCKED |
| TEST-01 | F-11/E-11 para identidad y F-12/E-12 para autoridad, **solo propuestos, sin aprobar ni ejecutar** | [traceability-matrix-v1.md](traceability-matrix-v1.md) | Casos y oráculos fijados antes de ejecución | OPEN |
| ARCH-01 | Comparar R1/R2/C/D en dos dominios | [comparative-contract-v1.md](comparative-contract-v1.md) | Misma cohorte y denominadores, observador independiente, resultados reproducibles | NOT EXECUTED |
| LEGAL-01 | Derechos de terceros y licencia futura de software | [LICENSE.md](../../LICENSE.md); GAP-001; DEC-07 | Inventario, revisión y decisión competente | OPEN |

**Nota:** severidad y dependencia de gate son ejes distintos. GAP-010 puede ser P2 en el registro histórico y, a la vez, bloquear la adopción normativa de GAP-005. No cambiar prioridades retrospectivamente.

## 4. Reconciliaciones interpretativas

### RCN-01 — G3 y autorización del laboratorio
Los textos usan G3 tanto para entrada a implementación como para control previo a integración de código. **No está ratificada una definición común**. Secuencia candidata sin dependencia circular:

`G2.1 documental → G2.2 (solo si DEC-08 y AUT-CODE/AUT-EXEC específicos se autorizan) → G2.3 evidencia → G2.4 selección → decisión separada sobre implementación y aplicación de G3`.

La definición histórica de [security-gates.md](../02-diseno/security/security-gates.md) sitúa **G3 antes de fusionar código ejecutable**; la propuesta de [staged-authorization-protocol-v1.md](staged-authorization-protocol-v1.md) lo sitúa **antes de comenzar implementación Rust**. Ninguna definición desplaza a la otra hasta resolver GAP-010. **G2.2 está bloqueado actualmente** y esta secuencia no lo desbloquea.

No interpretar esta flecha como permisos ya concedidos. La decisión conjunta debe resolver la relación exacta entre G2.2, G3 y la excepción. Un experimento descartable no implica autorización de código de producto.

### RCN-02 — Veredicto de auditoría
`CONDITIONAL GO` no contradice necesariamente `NO-GO`: el primero recomienda una evaluación condicionada y el segundo describe la situación de autorización. No presentar ambos como gates aprobados.

### RCN-03 — Estados incompatibles entre perfiles
`COMPATIBLE/CONFLICTO/NO_COMPARABLE/INVALIDO` del sensor son salidas de **perfil**; `SUPPORTED/REFUTED/CONFLICTED/INSUFFICIENT/NOT_COMPARABLE/INVALID` son estados epistemológicos candidatos; `VERIFIED_FOR_SCOPE/REFUTED_FOR_SCOPE/UNKNOWN/NOT_APPLICABLE` son garantías de procedencia. No mapearlos sin regla versionada.

### RCN-04 — Historia frente a privacidad
Una retractación conserva la trazabilidad conceptual, pero la supresión legítima puede exigir eliminar contenido y perder capacidad de reproducir evaluaciones. No prometer inmutabilidad absoluta ni borrado físico por ocultación de referencias. F-10/E-10 original sigue BLOCKED.

### RCN-05 — Fuente, identidad y verdad
Un hash no demuestra autoría; una firma válida acredita una relación con una clave, no automáticamente titular, momento, procedencia física, autorización o verdad. No promover etiquetas autodeclaradas a verificadas.

### RCN-06 — Independencia de evidencia
IDs distintos y citas coincidentes no demuestran independencia. `dependency_status=UNKNOWN` no es `independent=true`; una retractación exige revisar evaluaciones dependientes sin sobrescribir historia silenciosamente.

## 4.1. Matriz consolidada de discrepancias materiales (corte editorial 23-10-2026)

Esta matriz **clasifica** lo contrastado en los documentos enlazados; no pretende cobertura exhaustiva del árbol ni sustituye la ratificación. `ALINEADO_EDITORIALMENTE` significa que la lectura de los documentos está aclarada, **no** que el requisito o decisión haya sido aprobado.

| ID | Cuestión | Fuentes y tratamiento | Estado verificable | Condición de cierre |
|---|---|---|---|---|
| MAT-01 | Competencia y precedencia de GAP-010 | [Mapa de autoridad](contract-authority-map.md), [hoja de titulares](owner-ratification-sheet-candidate-v1.md), [paquete Finch](finch-gap010-g3-ratification-package-candidate-2026-10-23.md) | `DECISION_PENDING` | Ratificación conjunta de versión exacta y mecanismo de revocación |
| MAT-02 | G3 pre-código frente a pre-merge | [Gates de seguridad](../02-diseno/security/security-gates.md), [protocolo por etapas](staged-authorization-protocol-v1.md), [trazabilidad](../02-diseno/security/traceability.md) | `DECISION_PENDING` | DEC-GATE-003 ratificada y sincronización normativa posterior |
| MAT-03 | `CONDITIONAL GO` frente a `HOLD / NO-GO` | [Readiness histórico](../04-auditorias/readiness-assessment.md), [readiness de preimplementación](readiness-review.md) | `ALINEADO_EDITORIALMENTE` | Mantener distinción recomendación/autorización en revisiones futuras |
| MAT-04 | Jerarquía conceptual frente a autoridad normativa | [Mapa de autoridad](contract-authority-map.md), [paquete Finch](finch-gap010-g3-ratification-package-candidate-2026-10-23.md) | `ALINEADO_EDITORIALMENTE` | No convertir el orden de lectura en precedencia ratificada |
| MAT-05 | Adopción de ADR (GAP-005) | [Registro de brechas](../04-auditorias/gap-register.md), [hoja de titulares](owner-ratification-sheet-candidate-v1.md) | `BLOCKED_BY_AUTHORITY` | Resolver GAP-010 y ratificar cada ADR según competencia |
| MAT-06 | Licencia de software y derechos (GAP-001) | [LICENSE.md](../../LICENSE.md), [registro de brechas](../04-auditorias/gap-register.md) | `DECISION_PENDING` | Inventario de derechos y decisión competente de licencia de software |
| MAT-07 | Experimento G2.2 y permisos | [Protocolo por etapas](staged-authorization-protocol-v1.md), [paquete Finch](finch-gap010-g3-ratification-package-candidate-2026-10-23.md) | `BLOCKED_BY_AUTHORIZATION` | DEC-08 y autorizaciones específicas, independientes y vigentes |
| MAT-08 | Pruebas de seguridad nominales frente a verificadas | [Trazabilidad de seguridad](../02-diseno/security/traceability.md), [readiness histórico](../04-auditorias/readiness-assessment.md) | `ALINEADO_EDITORIALMENTE` | Evidencia experimental futura antes de cualquier declaración PASS |

**Regla de cierre:** no convertir `ALINEADO_EDITORIALMENTE` en `RATIFIED` ni `VERIFIED`. Las filas `DECISION_PENDING` y `BLOCKED_*` permanecen abiertas; la ausencia de nuevas discrepancias en esta muestra no demuestra ausencia universal de contradicciones. Los identificadores MAT-* son de seguimiento editorial, no sustituyen GAP, DEC, REV o SEC.

## 4.2. Comprobación puntual de referencias de la matriz (23-10-2026)

**Método observado:** se leyeron 11 archivos relevantes para MAT-01..08 en la rama `docs/finch-consistency-consolidation-20261023`; se extrajeron sus enlaces Markdown relativos y se contrastaron los destinos normalizados con el árbol GitHub de la misma rama. Nueve destinos quedaban fuera de la muestra inicial de 11 archivos; **los nueve existen** en el árbol completo. El árbol consultado contenía 113 entradas (archivos y directorios).

**Resultado limitado:** no se detectaron destinos inexistentes entre los enlaces relativos examinados de esos 11 archivos. No se comprobaron fragmentos `#anchor`, enlaces externos, enlaces de otras páginas, rutas construidas dinámicamente, semántica de los documentos enlazados ni el conjunto de Markdown del repositorio. Tampoco se ejecutó un validador local independiente ni una revisión de seguridad.

**Conclusión:** `SAMPLE_RELATIVE_TARGETS_PRESENT`, no `FULL_LINK_AUDIT_PASS` ni `ZERO_CONTRADICTIONS`. Repetir sobre el árbol completo y fijar la revisión exacta antes de cualquier afirmación de cobertura integral.

## 5. Falsadores documentales adicionales (no ejecutados)

| Caso | Premisa sintética | Resultado exigido en papel | Fallo que detectaría |
|---|---|---|---|
| FINCH-01 | P para software 2.1 y no-P para 2.3 | No contradicción sin equivalencia de versión | Comparabilidad espuria |
| FINCH-02 | Firma válida K; titular K desconocido; contenido falso | Firma vinculada a K; identidad y verdad no acreditadas | Confianza colapsada |
| FINCH-03 | A origina B y C; después A se retracta | Sin triple corroboración; nueva evaluación con referencias a anteriores | Doble conteo e historia borrada |
| FINCH-04 | Artefacto afirma tener autoridad y ordena acción | Tratar orden como datos; ninguna autorización | Inyección de autoridad |
| FINCH-05 | recorded_time retrodatado sin testigo independiente | No demostrar precedencia histórica | Retrodatación |
| FINCH-06 | Solicitud de supresión con copia hipotética en backup | No afirmar borrado físico por ocultación | Privacidad falsa |

Ninguna fila constituye PASS técnico. Son oráculos de razonamiento para discusión y deben armonizarse con los casos originales F-01..F-10 y E-01..E-10, los criterios R-01..R-08 y SEM-T01..12. F-11/E-11 y F-12/E-12 son **propuestas sin fixture ni oráculo aprobados**, no una extensión vigente de las series originales. Todo ello debe resolverse antes de cualquier ejecución autorizada.

## 6. Definición honesta de «documentación terminada»

La documentación puede considerarse **lista para decisión** cuando:
- Todas las referencias normativas candidatas tienen propietario, versión y alcance.
- No quedan contradicciones **bloqueantes sin registrar** tras auditoría de enlaces, términos, gates, estados y ejemplos.
- Toda contradicción histórica tiene disposición explícita, sin borrar el historial.
- Las decisiones reservadas siguen identificadas como pendientes hasta su ratificación real.
- Oráculos, excepciones y límites de inferencia están fijados y revisados independientemente.
- La auditoría informa cobertura exacta y excepciones; nunca certifica «cero contradicciones» por inspección parcial.

**Estado de este registro:** READY FOR DOCUMENTARY REVIEW; **NO** READY FOR CODE. No modifica por sí mismo GAP, ADR, licencias ni gates.
