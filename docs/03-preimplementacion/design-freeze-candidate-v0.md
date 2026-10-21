# Design freeze candidato — laboratorio de evidencia v0

**Estado: CANDIDATE / NO-GO.** Ninguna decisión se considera aprobada ni implementada.

## Contrato mínimo propuesto
- Un lote de **2 a 100** observaciones sintéticas; tamaño máximo de entrada **64 KiB**; superar límites rechaza el lote completo.
- Esquema explícitamente versionado `evidence.v0`; formato de intercambio **JSON UTF-8**, sin extensiones, comentarios ni campos desconocidos.
- Identificadores ASCII limitados a 64 caracteres, con conjunto permitido `[A-Za-z0-9_-]`; campos textuales libres excluidos del primer corte.
- Magnitud inicial única: `temperature`; unidad única `milli_degC`; valor entero con signo que representa milésimas de grado Celsius, sin floats.
- Rango didáctico permitido de **-100000 a 200000** milésimas de °C. Es un límite de prototipo, **no** certificación de rango físico.
- Instante: cadena RFC 3339 con offset explícito; equivalencia de instantes normalizados a UTC. Antes de codificar, definir comportamiento de segundos intercalares y precisión subsegundo.
- Contexto y sujeto obligatorios, sin inferir identidad ni ubicación física.
- Tolerancia ilustrativa fija de **1000 milli_degC** para `temperature`, pendiente de aprobación; no equivale a especificación de sensor.
- Orden de salida canónico por identificadores; cada pareja no ordenada se compara una sola vez.
- No hay persistencia, red, plugins, llamadas a LLM, permisos externos ni efectos sobre el sistema más allá de lectura de fixture y escritura de salida local de prueba.
- No se aceptan credenciales ni datos reales; entrada sintética exclusivamente.

## Comparabilidad
Dos registros estructuralmente válidos se comparan solo si coinciden `subject_id`, `quantity_id`, `unit_id`, `context_id` y el instante UTC. Diferencia absoluta calculada sin overflow; si supera tolerancia → CONFLICTO; si no → COMPATIBLE. Si difieren las condiciones → NO_COMPARABLE.

## Rechazos
- Campos ausentes, extraños o duplicados; versión desconocida; ID repetido; valor fuera de rango; tiempo ambiguo o inválido; JSON malformado; lote fuera de límites.
- **Política propuesta:** validación completa y rechazo atómico del lote; sin resultados parciales disfrazados de éxito.
- La procedencia es siempre **declarada**, nunca autenticada.

## Lo que sigue abierto
Elección exacta de biblioteca JSON mantenida y sus riesgos, semántica temporal y segundos intercalares, límites de memoria/tiempo, formato preciso de errores, plataforma mínima y licencia. La política de salida local también debe fijarse antes de implementar.

## Principio
Estos números son decisiones de diseño candidatas y modificables, no valores deducidos de mediciones reales.
