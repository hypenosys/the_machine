# PR #33 — control del denominador documental y cierre de fixtures (23-10-2026)

**Estado:** evidencia de inventario y estructura; **no** validación semántica mediante parser. `HOLD / NO-GO`.

## Corte auditado frente a rama actual

| Corte | SHA | Markdown en árbol Git | Qué se ha probado |
|---|---|---:|---|
| Fuente congelada de manifiestos regex | `3ff2f14fbc96c3f73768f1e870491155f36144b6` | 103 | Reproducción de 162 detecciones regex y existencia de 158 destinos locales; no parser independiente |
| Rama documental actual inspeccionada | `50f36e45a4aa2ab03d7aef9f2ee5fae5ee83aea1` | 116 | Solo conteo del árbol, no nueva extracción exhaustiva |

**Delta:** +13 documentos Markdown entre los cortes; este diferencial es aritmético, no un listado de archivos añadidos ni prueba de que los 103 blobs originales sigan idénticos. La adición de este informe vuelve a cambiar el HEAD y el denominador; no atribuirle automáticamente el recuento de 116.

## Control estructural de las fixtures

Archivo `docs/04-auditorias/pr33-parser-literal-fixtures-candidate-2026-10-23.md` leído en el corte `50f36e45a4aa2ab03d7aef9f2ee5fae5ee83aea1`:

- **19** encabezados `### FX-`, correspondientes a F-01..F-17 y F-18A/F-18B.
- Cercas de backticks de longitud variable comprobadas con un escáner de apertura/cierre: **0 cercas sin cerrar**. Este control es de estructura delimitadora, no de AST Markdown.
- El ejemplo FX-11 utiliza cerca externa de cuatro backticks y cerca interna de tres; ya no colisionan al representar el bloque de código ficticio.
- Los resultados esperados de FX-18A, anchors y HTML siguen condicionados al perfil de parser/renderizador: **no** son PASS.

## Implicaciones de auditoría

1. El universo de 162 referencias pertenece exclusivamente a los 103 Markdown del commit congelado; no extrapolarlo a los 116 del HEAD inspeccionado.
2. Un archivo de fixtures puede contener enlaces de ejemplo en bloques de código: un extractor regex no debe tratarlos como enlaces navegables.
3. Para evaluar la PR actual, congelar un nuevo corte y contrastar **todos** sus Markdown con parser independiente, sin alterar los manifiestos históricos.
4. La comprobación estructural de cercas no verifica gramática CommonMark/GFM, renderizado HTML, destinos ni anclas.
5. Ningún recuento de cobertura sustituye la ratificación de gobernanza, licencia o puertas de autorización.

**Estado de puertas:** `PARSER_CONTRAST_NOT_RUN`, `LINKS_READY_FOR_REVIEW = NO`, `HOLD / NO-GO`.
