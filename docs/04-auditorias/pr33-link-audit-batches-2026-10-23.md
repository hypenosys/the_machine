# PR #33 — comprobación incremental de enlaces (lotes A–C)

**Estado:** comprobación parcial de rutas, no auditoría semántica ni ratificación. **Fecha:** 2026-10-23. **Rama:** `docs/finch-consistency-consolidation-20261023`.

## Método

Se extrajo el árbol Git recursivo y se cotejaron las rutas de los enlaces Markdown inline `[texto](ruta)` de los archivos indicados con las rutas del árbol. Se normalizaron segmentos `.`/`..`, fragmentos y parámetros; se aceptó `README.md` de directorios. No se comprobaron anclas, enlaces externos, referencias Markdown por definición, autolinks, HTML, contenido semántico, ni archivos no listados. Los recuentos no equivalen a cobertura total.

## Lotes comprobados

| Lote | Archivos | Rango de documentos | Enlaces inline locales examinados | Destinos locales inexistentes detectados |
|---|---:|---|---:|---:|
| A | 15 | `AGENTS.md` a `docs/01-investigacion/security/experiments.md`, según orden de árbol | 51 | 0 |
| B | 15 | `docs/01-investigacion/security/isolation.md` a `docs/02-diseno/security/data-flow-diagrams.md` | 22 | 0 |
| C | 15 | `docs/02-diseno/security/evidence-protocol.md` a `docs/03-preimplementacion/consistency-findings-v0.md` | 8 | 0 |
| **Total nuevos** | **45** | | **81** | **0** |

Se habían comprobado previamente otros **12 archivos distintos** en `pr33-incremental-documentation-audit-2026-10-23.md`, con 32 enlaces inline totales, sin destinos locales inexistentes detectados. En el corte de estos lotes el árbol contiene **96 archivos Markdown**, incluido el informe previo: **57/96 archivos distintos** tienen comprobación de rutas inline; **39 restantes** no la tienen. No sumar los 32 enlaces previos como enlaces locales sin clasificación adicional.

## Fe de erratas de cobertura (reconciliación posterior)

**Error identificado:** la afirmación «otros 12 archivos distintos» y el resultado «57/96 archivos distintos» no son correctos como unión de rutas. La muestra inicial de doce archivos incluye `GOVERNANCE.md` y `docs/02-diseno/security/security-gates.md`, ambos dentro de los primeros 45 del lote A–C. Por tanto, la unión de **12 + 45 − 2 = 55 rutas únicas**, no 57. Para el inventario histórico de 96 Markdown, la cifra corregida es **55/96** y quedan **41**, no 39, fuera de esa unión.

**Alcance de la corrección:** conserva sin alterar los recuentos históricos por lote (15/15/15 y 51/22/8 enlaces) y la muestra de 12 archivos, porque no se han reejecutado sus detectores. Corrige únicamente la aritmética de deduplicación; no prueba que las 55 rutas fueran verificadas con un parser homogéneo ni valida anclas, referencias o semántica. El informe de reconciliación posterior sobre 100 documentos utiliza una unión de 91 rutas previas y 9 adicionales; sus resultados no deben extrapolarse al corte histórico de 96.

## Advertencias

- El inventario aumenta cuando se añaden informes de auditoría. Las cifras se refieren al árbol inspeccionado **antes de crear este archivo**.
- No se han encontrado enlaces rotos **con este detector**; no es una afirmación sobre todos los tipos de enlace ni sobre el contenido de las referencias.
- G3/GAP-010, autorización, ratificación y límites de experimentación siguen abiertos. El resultado de enlaces no cambia HOLD/NO-GO.
- Para finalizar: comprobar los restantes 39 documentos del inventario de 96, incluir este informe en el siguiente inventario y realizar una auditoría semántica separada con evidencia por afirmación.
