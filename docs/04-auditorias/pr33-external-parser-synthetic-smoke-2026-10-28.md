# PR #33 — contraste ejecutado de fixtures Markdown (28-10-2026)

**Naturaleza:** evidencia de experimento externo sobre entradas sintéticas documentadas; no es ejecución de THE MACHINE ni auditoría AST del repositorio. **HOLD / NO-GO** permanece.

**Fuente de casos:** `docs/04-auditorias/pr33-parser-literal-fixtures-candidate-2026-10-23.md` en `420a9844e1ac27d1b27c49f43def17320aafbed3`. **Motor:** Python `markdown-it-py 4.2.0`, `MarkdownIt('commonmark')`; parseo de cadenas sintéticas en entorno externo. Se inspeccionaron tokens `link_open`, `image`, `html_inline` y `html_block`. **Sin extensión de tabla GFM, sin extractor HTML href, sin política de anchors ni árbol de archivos sintético.**

## Observaciones reproducibles

| Caso | Links (destinos de tokens) | Imágenes | Notas |
|---|---|---|---|
| FX-01 | `destino.md` | 0 | inline |
| FX-02 | 0 | `imagen.png` | imagen diferenciada |
| FX-03 | `destino.md` | 0 | referencia resuelta |
| FX-04 | `archivo.md` | 0 | título no incluido en destino |
| FX-05 | `directorio/archivo%20con%20espacio.md` | 0 | sin validación de ruta |
| FX-06 | `doc.md#seccion` | 0 | anchor no validado |
| FX-07 | `#seccion` | 0 | anchor no validado |
| FX-08 | `https://example.org/ruta` | 0 | autolink |
| FX-09 | 0 | 0 | 2 tokens HTML inline; no extracción de href |
| FX-10 | 0 | 0 | código inline ignorado |
| FX-11 | 0 | 0 | bloque fenced ignorado |
| FX-12 | `ruta(uno).md` | 0 | paréntesis equilibrados |
| FX-13 | `../../../../fuera.md` | 0 | salida de raíz aún no clasificada |
| FX-14 | `#igual-1` | 0 | encabezados duplicados; anchor no validado |
| FX-15 | 0 | 0 | referencia indefinida |
| FX-16 | `a%25ZZ.md` | 0 | **el parser normaliza `%` inválido**; conservar raw source aparte |
| FX-17 | `destino.md` | 0 | enlace detectado en texto de tabla, **sin parseo de estructura de tabla GFM** |
| FX-18A | `destino.md` | 0 | multilineal reconocido |
| FX-18B | `destino%20con%20espacio.md` | 0 | destino angular normalizado |
| FX-19 | `../02-diseno/adr/` | 0 | destino directorio conservado; no verificado |

**Importante:** las entradas se reconstruyeron manualmente a partir de los bloques conceptuales, no se extrajeron automáticamente de los archivos del repositorio. Por tanto, estos resultados **no acreditan cobertura exacta de bytes, líneas o escapes** de fixtures publicadas.

## Diferencias relevantes para el contrato

1. La extracción de `link_open` **no basta para HTML**: FX-09 requiere una segunda capa para atributos `href`.
2. FX-17 requiere habilitar y verificar el plugin GFM de tablas para atribuir estructura de celda, aunque el enlace aparezca en CommonMark como texto de párrafo.
3. FX-16 y FX-18B demuestran que el `href` expuesto por el parser puede diferir del destino escrito; el manifiesto debe preservar `raw_target` y `parsed_target` separados.
4. FX-13, FX-14 y FX-19 **no son PASS de integridad**: faltan normalización de raíz, algoritmo de anchors y semántica de directorios.
5. No se hicieron dos ejecuciones canónicas ni se compararon hashes; **reproducibilidad independiente: NOT_VERIFIED**.

**Resultado:** `SYNTHETIC_PARSER_SMOKE_OBSERVED`; `REPOSITORY_AST_AUDIT_NOT_RUN`; `LINKS_READY_FOR_REVIEW=NO`. La evidencia no sustituye la revisión independiente requerida por la PR.
