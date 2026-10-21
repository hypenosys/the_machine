# Diseñar antes de programar

Una decisión de arquitectura necesita problema, evidencia, alternativas, riesgos, contrato, criterios de aceptación y plan de recuperación.

**Hipótesis, no decisión definitiva:** Rust local-first, núcleo pequeño, conocimiento tipado, permisos independientes de modelos, cero dependencias en el bootstrap y adaptadores opcionales.

## Por dónde seguir

- [Registro de decisiones de arquitectura (ADR)](adr/README.md): decisiones propuestas, alternativas y criterios para aprobarlas.
- [Modelo de amenazas](security/threat-model-v0.md): qué podría fallar o ser atacado desde el primer día.
- [Contrato de evidencia](contrato-evidencia.md): ejemplo de diseño didáctico.

**Importante:** los ADR están en estado Proposed y no autorizan todavía una implementación. La complejidad se introduce solo cuando un experimento demuestra que hace falta.
