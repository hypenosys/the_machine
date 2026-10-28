# Matriz de adjudicación semántica — corte PR #33

**Estado:** EVIDENCIA DOCUMENTAL PARCIAL / SIN RATIFICAR. **Fecha:** 2026-10-23. **Corte base:** rama `docs/finch-consistency-consolidation-20261023` leída antes de añadir esta matriz. Esta matriz no certifica el repositorio completo y no autoriza código, pruebas, merge ni despliegue.

## Método

Se compararon seis documentos mediante lectura directa de sus blobs Git y posiciones de línea. Cada fila distingue lo que **dice la fuente** de la **disposición analítica**. Los rangos de línea se refieren al blob SHA indicado, no a una línea flotante de una rama mutable. No se ha realizado reproducción independiente ni extracción semántica integral.

## Fuentes congeladas por blob

| ID | Ruta | Blob SHA |
|---|---|---|
| S1 | `docs/02-diseno/security/security-gates.md` | `ea793356a3b134fd02149c20735f0afae0cb9044` |
| S2 | `docs/03-preimplementacion/staged-authorization-protocol-v1.md` | `f1000aadf0d52d92f670629226ee2c1a2f2697ba` |
| S3 | `docs/04-auditorias/readiness-assessment.md` | `098770844007013e87dea815f845e10e40af856d` |
| S4 | `docs/03-preimplementacion/readiness-review.md` | `e940e8bd05c7c3ea248e7160f3194ced338def80` |
| S5 | `docs/03-preimplementacion/owner-ratification-sheet-candidate-v1.md` | `9e973b5b0a995ec6e01358233c4e36556d6c63fb` |
| S6 | `docs/03-preimplementacion/traceability-matrix-v1.md` | `a3741495b9c0a62ce73959f0ebc09cf30dd9746d` |

## Adjudicaciones trazables

| ID | Afirmaciones contrastadas | Disposición | Justificación / salida |
|---|---|---|---|
| ADJ-01 | S1:12,23 sitúa G3 antes de fusionar código ejecutable; S2:33,41,90 propone G3 antes de iniciar implementación Rust | `BLOCKED_BY_DECISION` | Los dos hitos no son equivalentes. S1 y S2 reconocen la divergencia. Requiere decisión competente sobre precedencia y definición; GAP-010 abierto. |
| ADJ-02 | S3:9,34–35 presenta `CONDITIONAL GO` como recomendación de auditoría y HOLD como estado vigente; S4:27 declara NO-GO para código | `DISTINCT_SCOPE` | Una recomendación condicionada de auditor no constituye autorización operativa. No cambiar HOLD. |
| ADJ-03 | S5:3,19–20,30 registra cotitularidad, preferencias no ratificadas y autoridad pendiente; S2:3,35 exige acuerdo explícito para transición | `BLOCKED_BY_DECISION` | No hay mecanismo de ratificación conjunta acreditado por estas fuentes; no inferir delegación ni permiso unilateral. |
| ADJ-04 | S6:33,41,47,90–101 separa fixtures F-01..10/E-01..10 de F-11/E-11 y F-12/E-12 propuestos; S5:41 reitera su estado | `CONSISTENT` **solo respecto del estado documental de las propuestas** | Los casos 11/12 no son cobertura ejecutada. No hay evidencia de PASS, fixture aprobado ni prueba independiente. |
| ADJ-05 | S3:26 contiene afirmación histórica sobre inexistencia de archivos Rust; S3:9 restringe expresamente ese dato al corte original | `DISTINCT_SCOPE` | No extrapolar la ausencia de código a todas las ramas o fechas. No se ha inspeccionado aquí cada rama ni el sistema de archivos externo. |
| ADJ-06 | S5:30 indica preferencia por GPL-3.0 para software futuro y distingue la licencia documental CC BY 4.0 | `INSUFFICIENT_EVIDENCE` **para declarar licencia de software adoptada** | La preferencia no selecciona variante ni demuestra derechos de terceros. La afirmación documental sobre preferencia es verificable; su transformación en licencia efectiva no. |

**Nota de clasificación:** ADJ-04 se refiere a la compatibilidad de dos fuentes sobre el estado de las propuestas, **no** a una declaración de que el sistema haya pasado las pruebas. ADJ-06 no afirma una contradicción entre licencias de objetos distintos.

## Segunda pasada: autoridad y precedencia (cuatro fuentes adicionales)

Se añadieron las siguientes fuentes, leídas directamente en la misma rama antes de este cambio. **Esta pasada no vuelve a inspeccionar los otros 90 documentos** ni acredita cobertura global.

| ID | Ruta | Blob SHA |
|---|---|---|
| S7 | `docs/03-preimplementacion/contract-authority-map.md` | `21f27cfa28b2a9738a583031f7fa3cca8ad51609` |
| S8 | `docs/04-auditorias/gap-register.md` | `091df5171589b1978afe9f55349df37003ed5afb` |
| S9 | `docs/03-preimplementacion/decision-preferences-proposal-2026-10-21.md` | `1ee7d2484662c4cd5dfb9b1014d5b980d603be5d` |
| S10 | `GOVERNANCE.md` | `bb5781b8820cc687ae2ae71598a846bb31a43125` |

| ID | Evidencia | Disposición | Efecto |
|---|---|---|---|
| ADJ-07 | S7:3–6,12–20 declara mapa y precedencia propuestos; S8:164–174 mantiene GAP-010 abierto | `CONSISTENT` en estado documental | El mapa **no** resuelve por sí mismo autoridad normativa. |
| ADJ-08 | S9:9–14 propone delegación revocable a @Axlfc; S10:8,28 niega activación de desempate sin ratificación | `CONSISTENT` en estado documental | Delegación propuesta, **no concedida**; sigue `BLOCKED_BY_DECISION` la facultad de ratificar. |
| ADJ-09 | S9:17–21 separa AUT-CODE, AUT-EXEC y AUT-MERGE; S10:19,21 rechaza inferir permisos del merge técnico | `CONSISTENT` en la prohibición de inferencia | Ninguna autorización AUT-* activa; etiquetas candidatas. |
| ADJ-10 | S9:23–28 propone evaluar GPL-3.0-only u or-later; S8:40 mantiene GAP-001 abierto y CC BY 4.0 documental | `DISTINCT_SCOPE` | Licencia documental actual y preferencia de software futuro son objetos distintos; decisión sobre software pendiente. |

**Hallazgo editorial puntual:** S8:167 utiliza `kandidatos` en vez de `candidatos`. No afecta al estado normativo, pero debe corregirse sin modificar la evidencia histórica de GAP-010. Esta matriz preserva la grafía observada en el blob fuente y no interpreta el error tipográfico como discrepancia de fondo.

**Cobertura de esta matriz:** diez documentos fuente únicos, diez adjudicaciones registradas, **no** diez documentos íntegramente auditados. Las adjudicaciones son muestreo dirigido de afirmaciones; denominador global de claims **UNKNOWN**. El estado `NOT_READY` permanece.

## Bloqueos y cobertura

- `ADJ-01` y `ADJ-03` requieren acto competente y no pueden cerrarse mediante edición interpretativa.
- Seis documentos examinados en esta matriz; **no** se han extraído todas sus afirmaciones ni las de los demás documentos. Por tanto, cobertura de afirmaciones global: **UNKNOWN**, no 100 %.
- Resultado para `PASS_GLOBAL`: **NOT_READY** por decisiones abiertas, evidencia incompleta y ausencia de reproducción independiente.
- Este informe es un **análisis documental con seis fuentes**, no una revisión de seguridad ejecutada ni una autorización para alterar software.

## Siguiente verificación reproducible

Fijar un commit de corte y un inventario de todas las fuentes, enumerar afirmaciones normativas y candidatas sin omitir las negativas, verificar rangos y hashes, construir un grafo de dependencias, realizar segunda clasificación independiente y registrar desacuerdos. Solo después evaluar el predicado de cierre definido en `docs/03-preimplementacion/deterministic-global-coherence-contract-candidate-v0.md`. Hasta entonces: HOLD / NO-GO.
