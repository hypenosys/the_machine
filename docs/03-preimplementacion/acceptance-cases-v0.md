# Casos de aceptación del contrato v0

**Estado: especificación conceptual; NO EJECUTADOS.** Todos los ejemplos son ficticios y no deben confundirse con mediciones.

Supuesto provisional para estos ejemplos: magnitud `temperature`, unidad `degC`, tolerancia **1 grado**, sujeto `sensor-banco-1`, contexto `ensayo-A`, mismo instante `2026-01-01T12:00:00Z`. La tolerancia **solo aplica a los ejemplos**; no está aprobada como criterio físico.

| Caso | Entrada sintética resumida | Resultado esperado | Razón |
|---|---|---|---|
| AC-001 | 55 y 55.5, mismo sujeto/contexto/instante | COMPATIBLE | Diferencia 0.5 ≤ 1 |
| AC-002 | 55 y 85, mismo sujeto/contexto/instante | CONFLICTO | Diferencia 30 > 1 |
| AC-003 | 55 y 85, sujetos distintos | NO_COMPARABLE | No miden el mismo sujeto |
| AC-004 | 55 y 85, contextos distintos | NO_COMPARABLE | Condiciones diferentes |
| AC-005 | 55 degC y 85 degF | NO_COMPARABLE | No hay conversión aprobada |
| AC-006 | 55 y 85, instantes distintos | NO_COMPARABLE | Sin ventana temporal aprobada |
| AC-007 | Valor NaN o infinito | INVALIDO | Número no finito |
| AC-008 | Mismo ID con contenido distinto | INVALIDO | Colisión de identidad |
| AC-009 | Texto «ignora instrucciones» en fuente | INVALIDO o dato inerte según esquema | Nunca autoriza acción |
| AC-010 | Fuente declara «certificada» sin prueba | Sin autenticación | Declaración no es verificación |
| AC-011 | Permutar orden de registros | Mismo conjunto de resultados | Determinismo |
| AC-012 | Lote excede tamaño permitido | INVALIDO | Límite explícito antes de procesar |
| AC-013 | No existe tolerancia configurada | NO_COMPARABLE | No inferir umbral |
| AC-014 | Dos registros válidos pero magnitudes diferentes | NO_COMPARABLE | Tipos incompatibles |

## Antes de codificar
Precisar el resultado de AC-009, elegir límites cuantitativos, definir representación numérica, fixture completo y criterio de comparación del conjunto. No afirmar PASS.
