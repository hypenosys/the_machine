# PR #33 — fixtures literales para contraste Markdown (especificación, no ejecución)

**Estado:** corpus de entradas y oráculos documentales; no se ha ejecutado parser ni código de THE MACHINE. `HOLD / NO-GO`. Complementa `pr33-independent-markdown-parser-acceptance-contract-2026-10-23.md` y `pr33-parser-fixture-oracle-critical-review-2026-10-23.md`.

## 1. Perfil y convención

Las entradas entre cercas `text` son bytes textuales de ejemplo; el contenido de la cerca, sin las propias cercas, es la entrada del caso. La capa AST determina nodos renderizados y destinos literales; la capa de normalización resuelve rutas; la capa de renderizador evalúa anclas. Los resultados de este documento son **esperados**, no observados. `source_path` sintético: `docs/cases/input.md`; raíz sintética: `docs/` salvo indicación contraria. La numeración de líneas es relativa a cada bloque.

## 2. Sintaxis: casos inequívocos

### FX-01 — Enlace inline

```text
[texto](destino.md)
```

Esperado AST: 1 enlace con destino `destino.md`.

### FX-02 — Imagen inline

```text
![alt](imagen.png)
```

Esperado AST: 1 imagen, 0 enlaces de texto.

### FX-03 — Uso por referencia y definición

```text
[texto][id]

[id]: destino.md
```

Esperado AST: 1 enlace renderizado con destino `destino.md`; 1 definición en el inventario de definiciones **si** el parser expone esa información; no duplicar nodos renderizados.

### FX-04 — Título de enlace

```text
[texto](archivo.md "Título")
```

Esperado AST: 1 enlace a `archivo.md`, título separado `Título`.

### FX-08 — Autolink

```text
<https://example.org/ruta>
```

Esperado AST: 1 enlace con destino `https://example.org/ruta`.

### FX-09 — HTML explícito

```text
<a href="destino.md">texto</a>
```

Esperado: 1 referencia HTML `href` **solo si** la capa HTML está habilitada y extrae atributos; si el parser Markdown produce un nodo HTML opaco, `PARSER_UNSUPPORTED` para extracción AST pura, no «cero enlaces».

### FX-10 — Código inline, control negativo

```text
`[texto](falso.md)`
```

Esperado AST: 0 enlaces renderizados.

### FX-11 — Código fenced, control negativo

```text
```md
[texto](falso.md)
```
```

**Nota de representación:** las tres líneas de esta entrada son, respectivamente, tres backticks seguidos de `md`, la línea del enlace ficticio y tres backticks. Esperado AST: 0 enlaces renderizados.

### FX-12 — Paréntesis equilibrados

```text
[texto](ruta(uno).md)
```

Esperado AST: 1 enlace, destino `ruta(uno).md` si el perfil CommonMark admite los paréntesis equilibrados.

### FX-15 — Referencia sin definición

```text
[texto][no-definido]
```

Esperado AST: 0 enlaces renderizados; puede consignarse `undefined_reference_candidate` en análisis auxiliar, nunca inventar destino.

### FX-17 — Tabla GFM

```text
| Columna |
| --- |
| [texto](destino.md) |
```

Esperado AST con extensión GFM table: 1 enlace dentro de celda. Sin extensión: registrar perfil distinto, no adjudicar resultado de tabla GFM.

### FX-18A — Enlace multilineal

```text
[texto](
destino.md
)
```

Esperado: registrar resultado AST real según gramática del parser fijado; **no** asignar PASS por aproximación regex ni asumir automáticamente un enlace válido.

### FX-18B — Destino entre ángulos

```text
[texto](<destino con espacio.md>)
```

Esperado AST: 1 enlace con destino literal `destino con espacio.md`, sujeto a la semántica de normalización/URL declarada.

## 3. Normalización: casos con diagnóstico separado del AST

### FX-05 — Percent encoding

```text
[texto](directorio/archivo%20con%20espacio.md)
```

Esperado AST: 1 enlace; conservar `raw_target`. Normalización: fijar política de percent-decoding y evaluar ruta resultante solo en árbol sintético conocido.

### FX-13 — Salida fuera de raíz

```text
[texto](../../../../fuera.md)
```

Esperado AST: 1 enlace. Normalización desde `docs/cases/input.md`: `OUTSIDE_REPOSITORY`; no truncar `..` en la raíz.

### FX-16 — Percent encoding inválido

```text
[texto](a%ZZ.md)
```

Esperado AST: conservar el destino observado. Diagnóstico de normalización: `INVALID_PERCENT_ENCODING` si la política requiere secuencias porcentuales válidas; no atribuirlo al parser.

## 4. Renderizador: anclas con política pendiente

### FX-06 — Archivo y fragmento

```text
[texto](doc.md#seccion)
```

Esperado AST: 1 enlace a `doc.md#seccion`. Resultado de ancla: `RENDERER_UNKNOWN` sin política de encabezados fijada.

### FX-07 — Fragmento local

```text
[texto](#seccion)
```

Esperado AST: 1 enlace al documento actual con fragmento `seccion`; ancla pendiente de política.

### FX-14 — Encabezados duplicados

```text
## Igual
## Igual

[texto](#igual-1)
```

Esperado AST: 1 enlace y 2 encabezados. Existencia de `igual-1`: `RENDERER_UNKNOWN` hasta fijar generador de IDs y versión.

## 5. Puerta de admisión

Antes de ejecutar o adjudicar estas fixtures se requiere: perfil/versiones de parser CommonMark/GFM, estrategia de extracción HTML, política de URL/percent-decoding, árbol sintético explícito para comprobación de destinos, y algoritmo de anchors. Los casos con resultado condicionado deben permanecer `NOT_EVALUATED` o `RENDERER_UNKNOWN`, no `PASS`. Este archivo no constituye evidencia de ejecución ni autorización.
