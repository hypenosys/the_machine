# Punto de parada deliberado — decisión antes de Rust

**Estado: NO-GO.**

## Qué puede considerarse cerrado documentalmente
- La hipótesis de un núcleo epistemológico común y perfiles de dominio.
- Separación de atribución, afirmación, evidencia y evaluación.
- Abstención explícita ante ausencia de comparabilidad o información.
- Distinción entre verificación de formato, autenticación y verdad.
- Reglas de retractación y dependencia como requisitos, no garantías demostradas.

## Qué no está demostrado
Que el modelo sea suficientemente expresivo, seguro, eficiente, portable, libre de contradicciones o capaz de sustentar una plataforma general. No hay tests ejecutados ni revisión externa certificadora.

## Dos alternativas para el siguiente hito
**Opción 1 — Experimento desechable:** aprobar un pequeño prototipo Rust de un solo perfil, sin declarar que implementa el núcleo general; medir coste y detectar fallos conceptuales. Requiere autorización explícita para cruzar la puerta de código.

**Opción 2 — Revisión independiente:** someter la especificación unificada a crítica externa y casos adversariales adicionales antes de prototipar. Menor riesgo de sesgo de diseño, mayor coste temporal.

## Recomendación
Preparar el experimento desechable como hipótesis, no como compromiso arquitectónico irreversible. Antes de codificar, acordar alcance, entorno, dependencia de parser, licencia y criterios de descarte.

## Puerta
No crear Rust, Cargo.toml, CI ni ejecutables sin aprobación expresa posterior.
