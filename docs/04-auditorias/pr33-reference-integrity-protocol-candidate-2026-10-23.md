# Protocolo de cierre de enlaces y referencias — candidato documental

**Fecha:** 2026-10-23. **Estado:** propuesta de auditoría, sin ejecución de verificador de software ni certificación de resultados. **Corte de referencia:** `96dddefa060c64c4329a22d9f26e2aef2327c910` (101 archivos Markdown según árbol consultado). La adición de este documento crea un corte nuevo; no se declara cobertura de ese nuevo corte.

## Problema observado

Los informes anteriores comprueban principalmente enlaces Markdown inline con expresiones regulares, en lotes y cortes distintos. El informe `pr33-inline-link-coverage-reconciliation-2026-10-23.md` reconstruye 100 rutas de un corte anterior, pero declara explícitamente que **no son verificaciones homogéneas**. La detección inicial trató ejemplos entre backticks como `[texto](ruta)` y `[texto](destino)` como si fueran enlaces: falsos positivos. Por tanto, ni «cero rotos» ni «100 rutas contabilizadas» prueban cierre de todas las referencias.

## Taxonomía de referencia y oráculo propuesto

| ID | Tipo | Regla de comprobación | Posibles resultados |
|---|---|---|---|
| LNK-01 | Markdown inline `[x](archivo.md)` e imágenes `![x](img.png)` | Resolver destino local y su existencia en árbol del mismo commit | `VALID`, `MISSING_TARGET`, `NOT_EVALUATED` |
| LNK-02 | Referencias `[x][id]`, `[id]: destino` | Resolver identificador normalizado, definición y destino | `VALID`, `UNDEFINED_REFERENCE`, `MISSING_TARGET` |
| LNK-03 | Anclas `#titulo` y `archivo.md#titulo` | Comparar contra IDs de encabezados calculados con reglas de renderizador fijadas | `VALID`, `MISSING_ANCHOR`, `RENDERER_UNKNOWN` |
| LNK-04 | Enlaces HTML `<a href="...">` e imágenes HTML | Parsear atributo real fuera de código y resolver | `VALID`, `MISSING_TARGET`, `EXTERNAL_UNCHECKED` |
| LNK-05 | Enlaces absolutos externos | Comprobación de red **solo con autorización expresa**, política de redirects y fecha | `VALID_AT_TIME`, `EXTERNAL_UNCHECKED`, `ERROR_AT_TIME` |
| LNK-06 | Referencias textuales en backticks | No tratarlas como enlaces navegables; registrar como mención si la trazabilidad lo exige | `LITERAL_REFERENCE` |
| LNK-07 | Rutas relativas a directorios | Definir resolución por archivo índice permitido; no inventar index por defecto | `VALID`, `MISSING_TARGET`, `POLICY_UNKNOWN` |
| LNK-08 | Destinos con percent-encoding, espacios, paréntesis, escapes y query | Parsear según sintaxis del formato; resolver solo tras normalización definida | `VALID`, `MALFORMED`, `POLICY_UNKNOWN` |

**No equiparar** enlace válido con contenido correcto. Un enlace puede existir y citar una fuente semánticamente incompatible.

## Requisitos de reproducibilidad

1. Congelar commit SHA completo y árbol; guardar cada ruta Markdown y blob SHA; no evaluar por nombre de rama mutable.
2. Seleccionar y fijar un parser compatible con la sintaxis Markdown realmente utilizada y una política concreta de generación de anchors. Sin esas versiones, clasificar `POLICY_UNKNOWN` o `RENDERER_UNKNOWN`, no PASS.
3. Separar el texto literal, el código delimitado, los bloques indentados, las definiciones de referencias y los nodos de enlace del árbol sintáctico.
4. Conservar para cada incidencia `source_path`, `source_blob`, `source_span`, `target_raw`, `target_normalized`, `reference_kind`, `rule_id` y `result`.
5. Guardar denominadores por tipo de referencia: `detected`, `evaluated`, `valid`, `invalid`, `unknown`; nunca convertir `unknown` en cero.
6. Excluir red del alcance offline; no inferir estado de URL externa sin solicitud autorizada. El corpus puede auditarse documentalmente sin efectuar peticiones HTTP.
7. Reproducir de forma independiente el manifiesto en el mismo commit y comprobar diferencias de resultados, no solo de recuentos.

## Controles positivos y negativos propuestos, no ejecutados

| Caso | Entrada de papel | Esperado |
|---|---|---|
| REF-01 | `[ejemplo](no-existe.md)` dentro de backticks | `LITERAL_REFERENCE`, no `MISSING_TARGET` |
| REF-02 | Enlace real a archivo inexistente | `MISSING_TARGET` |
| REF-03 | Referencia `[texto][clave]` sin definición | `UNDEFINED_REFERENCE` |
| REF-04 | Archivo existente con fragmento inexistente | `MISSING_ANCHOR` si la política de anchors está fijada |
| REF-05 | URL HTTPS no comprobada en modo offline | `EXTERNAL_UNCHECKED` |
| REF-06 | Destino local válido cuyo texto contradice el claim citado | `VALID` como enlace; discrepancia se deriva a auditoría semántica |
| REF-07 | Archivo nuevo después del commit auditado | No entra en el corte anterior; exige nuevo inventario |
| REF-08 | Enlace HTML dentro de un bloque de código | No es enlace navegable |

## Política de estados y precedencia para referencias

Para impedir que un mismo enlace obtenga resultados diferentes según el auditor, las categorías de la tabla inicial se aplican a **dimensiones separadas**:

1. **Naturaleza sintáctica:** `LINK_NODE`, `IMAGE_NODE`, `REFERENCE_DEFINITION`, `LITERAL_REFERENCE`, `NOT_PARSED`.
2. **Ubicación del destino:** `LOCAL_PATH`, `LOCAL_FRAGMENT`, `EXTERNAL_URL`, `UNKNOWN_LOCATION`.
3. **Evaluación:** `VALID`, `MISSING_TARGET`, `MISSING_ANCHOR`, `UNDEFINED_REFERENCE`, `MALFORMED`, `EXTERNAL_UNCHECKED`, `RENDERER_UNKNOWN`, `POLICY_UNKNOWN`, `NOT_EVALUATED`.

**Reglas de desempate:** un tramo dentro de código es `LITERAL_REFERENCE` y no genera evaluación de destino; una referencia sin definición es `UNDEFINED_REFERENCE` antes de comprobar rutas; un destino local inexistente es `MISSING_TARGET` antes de comprobar anclas; un archivo existente con fragmento solo puede clasificarse `MISSING_ANCHOR` si la política del renderizador está fijada; si no, `RENDERER_UNKNOWN`. Los enlaces externos en modo offline son `EXTERNAL_UNCHECKED`, no `VALID`. Si el parser no interpreta inequívocamente el nodo, prevalece `NOT_EVALUATED` y debe registrarse la causa.

**Corrección de ambigüedad:** `LITERAL_REFERENCE` es una clasificación sintáctica, no un resultado de integridad; `VALID_AT_TIME` y `ERROR_AT_TIME` son resultados temporales de red fuera del alcance offline. Nunca deben sumarse con `VALID` local como si midieran el mismo criterio.

**Identidad del hallazgo:** registrar un identificador derivado de `source_blob`, posición del nodo, tipo de referencia y destino literal. Un cambio de blob exige reconciliar el hallazgo con su antecesor; no asumir que conservar la misma línea garantiza identidad.

## Puerta de cierre

**`LINKS_READY_FOR_REVIEW`** requiere un manifiesto del corte completo, política de parser y anchors fijada, todas las referencias locales del alcance evaluadas, cero destinos o anclas inexistentes sin disposición, y reproducción independiente. Las externas pueden quedar `EXTERNAL_UNCHECKED` **solo si** el alcance excluye expresamente su validación. Esta puerta **no** concede `PASS_GLOBAL` semántico ni altera HOLD/NO-GO.

**Estado presente:** `NOT_READY`. No se ha ejecutado una validación uniforme de LNK-01..08 en los 101 documentos del corte. No se ha autorizado implementar ni ejecutar un verificador de software.
