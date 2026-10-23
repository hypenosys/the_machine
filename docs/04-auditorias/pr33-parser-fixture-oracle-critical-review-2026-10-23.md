# PR #33 — revisión crítica del oráculo de parser Markdown (23-10-2026)

**Estado:** auditoría documental de las 18 fixtures F-01..F-18, **no** ejecución de parser ni del software de THE MACHINE. Corte del contrato examinado: `1cf16e779d2fa910178fe673e5099663b9cca8cb`. `HOLD / NO-GO`.

## Hallazgo: 18 identificadores, pero no 18 pruebas ejecutables independientes

Se comprobó que el contrato `pr33-independent-markdown-parser-acceptance-contract-2026-10-23.md` enumera exactamente **F-01 a F-18**, sin duplicados ni saltos de identificador. **La existencia de 18 filas no constituye 18 pruebas ejecutadas ni un oráculo determinista**. Varias filas mezclan gramática, normalización, política de navegación y comportamiento del renderizador. Se deben separar antes de admitir resultados PASS/FAIL.

| Caso | Ambigüedad comprobada en el texto del contrato | Resolución documental necesaria |
|---|---|---|
| F-03 | Combina uso y definición en una misma fila | Separar `link_node_count=1` y `definition_count=1`, con posiciones propias |
| F-05 | Mezcla percent-decoding y existencia de archivo | Exigir `raw_target` y `normalized_target` y fijar política de decodificación antes de evaluar existencia |
| F-06/F-07/F-14 | Supone una política de anchors aún no fijada | Definir versión de algoritmo y casos Unicode, duplicados y puntuación; sin política: `RENDERER_UNKNOWN` |
| F-09 | Dice «según modo GFM», sin declarar modo ni tratamiento de HTML | Fijar parser, extensión GFM y tratamiento de HTML en un perfil reproducible |
| F-10/F-11 | Describe código inline y fenced code sin bytes de entrada precisos | Añadir fixtures literales en archivo dedicado, sin que el propio Markdown de la tabla altere el ejemplo |
| F-12 | Paréntesis equilibrados: caso no parametrizado | Fijar exactamente la cadena de entrada y el destino esperado por el parser elegido |
| F-13 | Ruta que sale del repositorio: política de normalización | Evaluar `OUTSIDE_REPOSITORY` en resolución de rutas, no en sintaxis Markdown |
| F-15 | Uso de referencia sin definición: puede renderizarse como texto literal | Diferenciar `undefined_reference_candidate` de `link_node`; no inventar nodo renderizado |
| F-16 | Secuencia porcentual inválida: comportamiento del parser no necesariamente rechazo | Mantener `raw_target` y emitir diagnóstico en capa de normalización, separado del AST |
| F-17 | Una tabla GFM es un contenedor sintáctico opcional | Fijar extensión `table` y comprobar que el enlace es descendiente de una celda |
| F-18 | Une multilineal y destino entre `<...>` en una sola fila | Dividir en dos fixtures independientes y fijar saltos de línea literales |

## Perfil de evidencia requerido

Cada caso deberá contar con un identificador único, bytes UTF-8 de entrada, configuración exacta del parser, nodos esperados (tipo, destino, posición cuando esté disponible), diagnósticos de normalización esperados y una justificación de semántica CommonMark/GFM. Los casos que dependan del renderizador GitHub deben declarar `RENDERER_UNKNOWN` mientras su política no se determine. Las comprobaciones de destino deben ejecutarse en un árbol sintético de prueba o en el commit congelado y **no** inferirse del parser.

## Propuesta de descomposición, no implementación

- **P-01 — Sintaxis:** F-01, F-02, F-03, F-04, F-08, F-09, F-10, F-11, F-12, F-15, F-17 y F-18 (este último dividido).
- **P-02 — Normalización y seguridad de rutas:** F-05, F-13 y F-16.
- **P-03 — Renderizador y anclas:** F-06, F-07 y F-14.
- **P-04 — Integridad de destino:** comprobar existencia de rutas y directorios tras la extracción AST, sin utilizar el parser como prueba de existencia.
- **P-05 — Comparación de inventarios:** unir observaciones regex y nodos AST con trazabilidad; nunca comparar solo totales.

**Criterio de parada:** no declarar `PARSER_CONTRAST_ADJUDICATED` hasta tener entradas literales, resultados AST y evidencia independiente. El presente documento no eleva ninguna puerta de autorización.
