# Investigación de seguridad — decisiones basadas en evidencia

**Estado: investigación documental preliminar. No se han ejecutado experimentos.**

Este capítulo traduce las amenazas y requisitos en preguntas técnicas que puedan responderse con experimentos. Ninguna herramienta queda aprobada por aparecer en una tabla.

## Estudios
1. [Aislamiento y sandboxes](isolation.md)
2. [Autorización y capacidades](authorization.md)
3. [Persistencia y recuperación](persistence.md)
4. [Cadena de suministro](supply-chain.md)
5. [Diseño de experimentos](experiments.md)

## Reglas de investigación
- Fuentes primarias, preferentemente documentación de mantenedores y estándares.
- Separar propiedades documentadas de garantías demostradas en THE MACHINE.
- Registrar alternativa mínima, fallos conocidos, coste operativo y posibilidad de revertir.
- No confundir sandbox, contenedor, VM y sistema de permisos.
- Revisar compatibilidad y comportamiento de cada plataforma objetivo antes de aprobar arquitectura.

[Requisitos](../../02-diseno/security/requirements.md) · [ADR](../../02-diseno/adr/README.md)
