# Límites de arquitectura para el primer corte

**Estado: PROPUESTO; sin componentes implementados.**

## Separación conceptual
1. **Entrada:** recibe registros sintéticos; no interpreta órdenes.
2. **Validación:** comprueba esquema, límites y unidades.
3. **Comparación:** aplica reglas explícitas y deterministas a registros comparables.
4. **Explicación:** genera una traza legible de reglas y entradas utilizadas.
5. **Presentación:** explica resultados y limitaciones a personas sin experiencia.

El modelo generativo, si llega a existir, será un adaptador posterior y no una fuente de autoridad.

## Fronteras de confianza
- TB-A: usuario/archivo sintético → validador; todos los campos son no confiables.
- TB-B: registros validados → motor de reglas; validez estructural no significa veracidad.
- TB-C: resultados → explicación; la explicación no puede añadir hechos ausentes.
- TB-D: salida → persona; no debe presentarse como diagnóstico físico certificado.

## Contratos que deben fijarse antes de código
- Esquema versionado y límites.
- Reglas de comparabilidad: magnitud, unidad, lugar, instante y tolerancia.
- Semántica de error, duplicados y rechazo.
- Determinismo y trazabilidad de resultados.
- Estrategia de pruebas con fixtures sintéticos.
- Matriz de amenazas reducida al alcance real.

## Trade-offs
Un solo proceso offline reduce superficie de ataque, pero no elimina errores de parser, agotamiento de recursos o ambigüedad semántica. Mantener el núcleo independiente de una interfaz específica facilita reutilización, aunque añade contratos que deben permanecer simples.

## Exclusiones explícitas
No introducir sistema de plugins, orquestador distribuido, almacenamiento de larga duración, identidad federada o permisos de ejecución por anticipación.
