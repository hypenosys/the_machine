# PR #33 — contrato de contraste independiente con parser Markdown (candidato)

**Estado:** especificación documental y casos de prueba, no implementación ni ejecución del software de THE MACHINE. **HOLD / NO-GO**. No modifica decisiones de autoridad, licencia o autorizaciones.

## 1. Problema y línea base reproducible

El corpus fuente congelado es `3ff2f14fbc96c3f73768f1e870491155f36144b6` (103 archivos `.md`). Los nueve manifiestos `pr33-reference-manifest-regex-batch-01` a `09` contienen **162 observaciones regex**, reproducidas campo a campo. De ellas, **158 destinos locales** existen en el árbol de ese commit y **4 apariciones externas** corresponden a tres URL distintas. El recuento **no es una verdad de referencia semántica**: el extractor original elimina aproximadamente bloques de código y fragmentos entre backticks simples y aplica patrones de una sola línea.

El objetivo del contraste es descubrir falsos positivos y falsos negativos **sin convertir la concordancia de dos expresiones regulares en una falsa prueba de exhaustividad**.

## 2. Requisitos del contraste

1. **Identidad:** fijar `source_commit`, inventario ordenado `(path, blob_sha)`, versión del parser, extensiones y configuración. Nunca mezclar el árbol congelado con el HEAD mutable.
2. **Motor independiente:** utilizar un parser de Markdown de estructura/AST compatible con CommonMark y documentar explícitamente las diferencias con GitHub Flavored Markdown (GFM), incluyendo tablas, autolinks y HTML. No reutilizar el regex de producción como fuente de verdad.
3. **Extracción:** reconocer enlaces inline, imágenes, enlaces por referencia, definiciones y usos, autolinks, HTML `a[href]` / `img[src]` cuando aplique; clasificar lo no soportado como `UNSUPPORTED`, no como ausente. Una definición sin uso no se debe confundir con un enlace renderizado.
4. **Procedencia:** conservar `source_path`, `blob_sha`, `line`, `column` (si el parser la expone), `syntax_kind`, `raw_target`, `normalized_target`, `parser_version` y `status`. Si no hay posición exacta, declarar `position_unavailable`; no inventarla.
5. **Normalización:** resolver rutas relativas desde el archivo de origen; separar ruta, query y fragmento; aplicar percent-decoding con tratamiento explícito de errores; impedir que `..` fuera del repositorio se convierta en una ruta válida por truncamiento silencioso; distinguir archivos, directorios, esquemas y enlaces `#fragment`.
6. **Fragmentos:** para destinos Markdown, derivar anclas según la política GitHub aplicable (Unicode, duplicados, signos y encabezados explícitos) y registrar `UNVERIFIED` cuando no se pueda demostrar equivalencia con GitHub. Para fragmentos de comentarios de GitHub, comprobar el identificador de comentario, no solamente la página de PR.
7. **Conjuntos comparables:** contrastar los enlaces **renderizados** del parser con los `LINK_INLINE` del inventario, identificando duplicados por `(path, position, target, occurrence)`. Las definiciones se registran aparte. Clasificar cada diferencia como `REGEX_FALSE_POSITIVE`, `REGEX_MISSED_LINK`, `PARSER_UNSUPPORTED`, `AMBIGUOUS` o `INTENTIONAL_NON_RENDERED`.
8. **Reproducción independiente:** dos ejecuciones sobre el mismo commit deben producir manifiestos canónicos idénticos (o hashes idénticos), con los comandos, entorno y versiones consignados. No afirmar `PASS` sin artefactos y evidencia revisable.

## 3. Casos mínimos de falsación (fixtures conceptuales)

| ID | Markdown de entrada | Resultado que debe distinguir el parser |
|---|---|---|
| F-01 | `[texto](destino.md)` | Un enlace renderizado a `destino.md` |
| F-02 | `![alt](imagen.png)` | Una imagen, no un enlace de texto |
| F-03 | `[texto][id]` + definición `[id]: destino.md` | Un uso renderizado y una definición; no contarlos dos veces |
| F-04 | `[texto](archivo.md "Título")` | Destino `archivo.md`; título separado |
| F-05 | `[texto](directorio/archivo%20con%20espacio.md)` | Decodificación controlada y existencia comprobada |
| F-06 | `[texto](doc.md#seccion)` | Comprobar archivo **y** ancla |
| F-07 | `[texto](#seccion)` | Ancla en el documento actual |
| F-08 | `<https://example.org/ruta>` | Autolink renderizado |
| F-09 | `<a href="destino.md">texto</a>` | Enlace HTML, según modo GFM |
| F-10 | Un código inline delimitado por backticks que contiene `[texto](falso.md)` | No hay enlace renderizado dentro del código inline |
| F-11 | Bloque de código con `[texto](falso.md)` | No hay enlace renderizado |
| F-12 | `[texto](ruta(uno).md)` | Interpretar correctamente paréntesis equilibrados |
| F-13 | `[texto](../../../../fuera.md)` | `OUTSIDE_REPOSITORY`, nunca válido por truncamiento |
| F-14 | Dos encabezados `## Igual` y enlace `#igual-1` | Resolver duplicados de ancla con política declarada |
| F-15 | `[texto][no-definido]` | No inventar destino ni enlace |
| F-16 | `[texto](a%ZZ.md)` con secuencia porcentual inválida | Conservar el destino literal y registrar `INVALID_PERCENT_ENCODING` en la capa de normalización; no atribuir al parser un rechazo que CommonMark/GFM no exijan |
| F-17 | Tabla GFM con `[texto](destino.md)` | Detectar enlace renderizado dentro de tabla |
| F-18 | Enlace en varias líneas o con destino entre `<...>` | Procesar conforme a gramática; no suponer que una línea equivale a un nodo |

Las fixtures deben convertirse en pruebas automatizadas **solo tras autorización específica de implementación**; este documento únicamente establece el oráculo de aceptación.

## 4. Evidencia de cierre requerida

Un expediente de contraste deberá incluir: (a) SHA del commit fuente; (b) versión/configuración del parser; (c) manifiesto AST íntegro; (d) diferencias contra las 162 observaciones, una a una; (e) adjudicación manual de las diferencias; (f) resultado de destinos y anclas; (g) lista de URL externas verificadas/no verificadas; (h) revisión independiente y decisión explícita.

**No basta** con `162 == 162`, con `0 rutas locales inexistentes` ni con `0 coincidencias de patrones secundarios`. Si el parser detecta una omisión, el inventario previo se conserva como evidencia histórica y se publica un nuevo manifiesto versionado; no se reescribe el corte congelado.

## 5. Puertas de decisión

- `PARSER_CONTRAST_NOT_RUN` — estado actual.
- `PARSER_CONTRAST_IN_PROGRESS` — parser y corpus identificados, evidencias incompletas.
- `PARSER_CONTRAST_ADJUDICATED` — diferencias documentadas, cobertura definida.
- `LINKS_READY_FOR_REVIEW` — solo si la evidencia satisface el protocolo de integridad y un revisor independiente la acepta.
- `HOLD/NO-GO` de THE MACHINE **permanece independiente** de cualquiera de estos estados.
