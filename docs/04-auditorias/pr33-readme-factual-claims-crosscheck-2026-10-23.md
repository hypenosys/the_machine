# PR #33 — contraste factual del README contra fuentes primarias del repositorio

**Corte:** `3269ddc5d1bd4753008260c71f7c972ce49f47fe`. **Método:** inspección de árbol Git recursivo y lectura de tres documentos fuente mediante API GitHub. **No** es un pase AST ni ejecución de THE MACHINE. `HOLD / NO-GO`.

## Evidencia obtenida

| Afirmación del `README.md` | Fuente comprobada | Observación | Alcance |
|---|---|---|---|
| No hay código Rust `.rs` | Árbol Git recursivo del corte | **0** rutas de blob terminadas en `.rs` | Solo el árbol de este commit, no ramas ni entornos externos |
| No hay workflows | Árbol Git recursivo | **0** rutas bajo `.github/workflows/` | No prueba ausencia de CI externa |
| Existe licencia documental | Árbol Git recursivo | `LICENSE.md` presente | No ratifica licencia de software ni titularidad de terceros |
| Modelo STRIDE con 20 amenazas | `docs/02-diseno/security/threat-model-v0.md` | **20 IDs distintos** `TH-001`…`TH-020` | Presencia textual de IDs; no mitigaciones verificadas |
| Requisitos de seguridad 17 | `docs/02-diseno/security/requirements.md` | **17 IDs distintos** `SEC-REQ-001`…`SEC-REQ-017` | Presencia textual de IDs; no tests superados |
| GAP-001 a GAP-010 | `docs/04-auditorias/gap-register.md` | **10 IDs distintos** `GAP-001`…`GAP-010` | Presencia textual; no cierre de brechas |

**Contexto de inventario:** el árbol consultado contiene **120 blobs**, **119** de ellos `.md`. El recuento es propio de este SHA y no se proyecta al commit generado por este informe.

## Límites y próximos falsadores

La extracción de IDs se hizo por coincidencias textuales deduplicadas, no por interpretación de tablas ni por comprobación de unicidad de definiciones. Un mismo identificador podría repetirse en el documento; la presencia de los 20/17/10 identificadores no demuestra que todos tengan una definición sustantiva independiente. Para ese nivel de conclusión hace falta contrastar estructura y relaciones. Tampoco se verificó en esta pasada la precisión de las afirmaciones normativas o temporales del README.

**Resultado:** seis afirmaciones concretas corroboradas en el corte; **cero discrepancias en esas seis comprobaciones**, sin extrapolar a `PASS_GLOBAL`, `LINKS_READY_FOR_REVIEW` o autorización de código/ejecución/merge.
