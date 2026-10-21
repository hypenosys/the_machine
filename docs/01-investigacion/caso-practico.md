# Caso práctico: ¿podemos confiar en una medición?

**Ejercicio didáctico con datos inventados.**

Un sensor A registra 85 °C y un sensor B registra 55 °C. Ambos indican la misma hora.

## Paso 1 — Documentar
Pregunta: «¿Cuál era la temperatura real del motor a las 10:00?».
Sabemos que hay dos reportes; no sabemos cuál representa mejor la temperatura.

## Paso 2 — Investigar
Hipótesis H1: un sensor está mal calibrado.
Hipótesis H2: los sensores miden puntos diferentes.
Hipótesis H3: sus relojes están desincronizados.

¿Qué información permitiría descartar cada hipótesis? Una tercera medición, la ubicación de los sensores, su historial de calibración y los relojes originales.

## Paso 3 — Diseñar
Guardar ambos reportes por separado, con origen, hora, unidad, identificador del sensor y posibles correcciones. No sobrescribir uno con otro.

## Paso 4 — Implementar
**Pendiente.** Un programa Rust podría validar estos registros y detectar contradicciones.

## Paso 5 — Verificar
**Pendiente.** Las pruebas comprobarían que ningún reporte desaparece y que el sistema no afirma una temperatura definitiva sin evidencia.

## Resultado de aprendizaje
La transparencia no consiste en mostrar una conclusión con confianza aparente, sino en permitir reconstruir de dónde salió y cómo podría cambiar.
