# Cierre de cobertura de lotes Markdown inline — PR #33

**Fecha:** 2026-10-23. **Estado:** evidencia limitada al detector descrito; no certificación semántica ni de todos los formatos de enlace. **Corte inspeccionado:** `025c69eb9183d8ef96855bab184e1b4fe5193332` (100 documentos Markdown antes de añadir este informe). **Rama:** `docs/finch-consistency-consolidation-20261023`.

## Reconstrucción deduplicada

Se reconstruyó la unión de los doce archivos de la primera muestra, los lotes A–C (45 rutas) y D–F (37 rutas), utilizando el inventario de rutas del corte. La unión corresponde a **91 rutas únicas** del corte; las otras **9** se detallan a continuación. Esta reconstrucción depende de que las listas históricas de lotes correspondan exactamente a los conjuntos declarados y **no reejecuta** las verificaciones de los 91 documentos originales. No se debe interpretar como una verificación homogénea de 100 archivos con un mismo parser.

## Nueve rutas examinadas en esta pasada

| Ruta | Blob SHA | Enlaces inline detectados fuera de código | Destinos locales inexistentes |
|---|---|---:|---:|
| `docs/03-preimplementacion/architecture-paper-falsification-v0.md` | `027c77d91f285995e832836479ca990370bccba3` | 0 | 0 |
| `docs/03-preimplementacion/comparative-contract-v1.md` | `8c28d369525aa4b6787eeec8a584c35b2a5aac46` | 0 | 0 |
| `docs/03-preimplementacion/consistency-findings-v0.md` | `dc0768df3576a1f45cb082ac45e17b942b91648f` | 0 | 0 |
| `docs/03-preimplementacion/deterministic-global-coherence-contract-candidate-v0.md` | `c46be35f48315d6ee363c8aa998fa7ed255b81b8` | 0 | 0 |
| `docs/03-preimplementacion/evidence-dependencies-and-retractions.md` | `12c1dc29ca12213f6079e3843c09b2aeedd2d1d7` | 0 | 0 |
| `docs/04-auditorias/pr33-incremental-documentation-audit-2026-10-23.md` | `ad656315c12b2fb503c0434761f482715713e670` | 0 | 0 |
| `docs/04-auditorias/pr33-link-audit-batches-2026-10-23.md` | `a32645bfaf0022dbb66a19635c898a080f16079e` | 0 | 0 |
| `docs/04-auditorias/pr33-link-audit-batches-d-f-2026-10-23.md` | `ec3c20dc963ab52811504ff1e8a877fe48461d4a` | 0 | 0 |
| `docs/04-auditorias/pr33-semantic-adjudication-matrix-2026-10-23.md` | `42792b2179f7d909856dc712801910061bb52161` | 0 | 0 |

## Método y límites

1. Leer contenido por blob de Git; eliminar mediante patrones los bloques delimitados por tres backticks y los tramos inline de un backtick; extraer después enlaces `[etiqueta](destino)` con un patrón regular simple.
2. Para destinos relativos, resolver segmentos `.` y `..` contra el directorio del documento y comprobar la presencia de ruta, `README.md` o `index.md` en el árbol del corte.
3. **No cubre** sintaxis Markdown de referencias `[texto][id]`, anchors de encabezado, imágenes HTML, URLs externas, rutas complejas con paréntesis, bloques indentados, escapes Markdown ni enlaces generados dinámicamente. El borrado regex de bloques tampoco equivale a un parser CommonMark.
4. Los ejemplos `[texto](ruta)` y `[texto](destino)` escritos entre backticks no son enlaces. Su clasificación como enlaces por el patrón previo constituye **falso positivo del detector**, no defecto del documento.
5. Al añadir este informe, el corpus aumenta y exige nuevo corte para una afirmación de cobertura total. **No** declarar `PASS_GLOBAL`, ni un `100/100` verificado de manera uniforme.

## Resultado y trabajo pendiente

- **Resultado verificable de esta pasada:** nueve rutas examinadas, cero enlaces inline reales encontrados en esas rutas con este método, cero destinos locales inexistentes entre los encontrados.
- **Cobertura histórica reconstruida:** 91 rutas previas + 9 rutas de esta pasada = 100 rutas del corte **solo como inventario de comprobaciones heterogéneas**, no auditoría integral.
- **Pendiente:** inventario de referencias Markdown, anclas, enlaces HTML y validación uniforme con parser especificado; extracción y adjudicación semántica completa; revisión independiente; ratificación de GAP-010/G3.
- **Gobernanza:** HOLD / NO-GO para código, ejecución y merge de código. Este informe documental no altera permisos.
