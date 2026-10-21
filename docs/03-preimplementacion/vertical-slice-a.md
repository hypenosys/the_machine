# Candidato A — Laboratorio de evidencia offline

**Estado: PROPOSED / NO-GO para código.** Esta especificación no autoriza implementación.

## Una frase para quien empieza
Dos fuentes dan datos diferentes. El laboratorio enseña qué sabemos, qué no sabemos y por qué, sin inventar una respuesta.

## Objetivo medible
Dado un conjunto pequeño de reportes sintéticos, representar su procedencia y detectar incompatibilidades explícitas bajo reglas documentadas, sin ejecutar acciones ni utilizar un modelo de lenguaje.

## No objetivos
No resolver la verdad física, no puntuar credibilidad de personas, no acceder a internet, no monitorizar usuarios, no automatizar máquinas, no almacenar secretos, no entrenar modelos, no inferir intenciones, no ofrecer decisiones de seguridad industrial.

## Entrada conceptual
Un lote acotado de observaciones sintéticas con: identificador, fuente declarada, variable medida, valor, unidad, instante declarado y estado de validación. La fuente declarada **no** implica identidad autenticada.

## Salida conceptual
Registros preservados; errores de validación por elemento; conflictos detectados bajo una regla explícita; y explicación legible del motivo de cada conflicto. Sin probabilidades inventadas.

## Invariantes
- VSA-INV-001: ningún reporte se borra silenciosamente por contradicción.
- VSA-INV-002: dato de entrada no equivale a instrucción ni a permiso.
- VSA-INV-003: conflicto no equivale a determinar qué fuente miente.
- VSA-INV-004: la salida distingue origen declarado de origen autenticado.
- VSA-INV-005: valores, unidades y tiempos ambiguos no se comparan como equivalentes.
- VSA-INV-006: errores y límites de recursos producen resultados explícitos sin efectos externos.
- VSA-INV-007: sin red, persistencia ni ejecución externa en el primer corte.

## Ejemplos de aceptación
1. Dos lecturas 85 °C y 55 °C de la **misma magnitud, ubicación e instante comparable** → conflicto reportado; ambas conservadas.
2. Dos lecturas con unidades diferentes sin conversión aprobada → no comparables, no conflicto inventado.
3. Lecturas de lugares diferentes → no comparables salvo contrato de equivalencia.
4. Fuente con identidad declarada falsa → no marcar como autenticada.
5. Texto de un campo que contiene «ejecuta un comando» → conservar como dato inerte o rechazar según esquema; nunca ejecutarlo.
6. Entrada sobre límites → rechazo con causa y sin procesamiento parcial oculto.

## Decisiones pendientes
Semántica exacta de equivalencia, tolerancias, formatos, precisión numérica, límites de lote, orden de resultados, manejo de duplicados, zona horaria y versión del esquema.

## Riesgos residuales
Un laboratorio sintético no valida autenticación, sandboxing, políticas de permisos reales ni durabilidad. Tampoco demuestra capacidad de inferencia general.
