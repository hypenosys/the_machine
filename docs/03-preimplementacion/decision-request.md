# Solicitud de decisión arquitectónica — Gate previo a implementación

**Estado: PENDIENTE.**

## Recomendación del diseño
Aceptar el **alcance conceptual** del laboratorio offline de evidencia como primer corte, con entrada exclusivamente sintética y sin efectos externos. Mantener el diseño modular y reversible.

## Qué se está solicitando aprobar
- Que el primer objetivo sea comprobar procedencia declarada, comparabilidad y detección de contradicciones bajo reglas explícitas y versionadas; el determinismo del núcleo sigue siendo una hipótesis por verificar.
- Que no se incluya modelo generativo, red, plugins, acciones externas ni almacenamiento duradero.
- Que las garantías de autorización, sandboxing y recuperación queden explícitamente **fuera del alcance demostrado** de este corte.
- Que se resuelvan los bloqueos de `precode-review-checklist.md` antes de autorizar implementación.

## Qué NO se está solicitando aprobar
- No se solicita todavía escribir código.
- No se solicita aceptar los cinco ADR generales.
- No se solicita cambiar la visibilidad del repositorio ni decidir una licencia para software futuro. El repositorio ya era público en la comprobación del 21-10-2026 y esta PR incorpora `LICENSE.md` con CC BY 4.0 para documentación original; ambos hechos son independientes de la autorización para código.
- No se solicita certificar seguridad ni declarar tests superados.

## Alternativas rechazables
- B: pasarela de acciones simuladas, si la prioridad real es autorización.
- C: laboratorio de aislamiento, si la prioridad real es control de ejecución.
- Ninguna: más investigación si la semántica de observación sigue siendo ambigua.

## Resultado formal
**NO-GO para código** hasta una decisión explícita posterior. Registrar fecha, responsable, objeciones y cambios aceptados al tomarla.
