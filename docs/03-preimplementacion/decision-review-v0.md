# Revisión de decisión v0 — antes del primer archivo Rust

**Estado: DELIBERATION / NO-GO.** No se ha realizado una revisión independiente ni ejecutado experimentos.

## Recomendación
Elegir provisionalmente el **candidato A** para el primer corte educativo y epistemológico. La recomendación no aprueba su implementación.

## Por qué A
- Ofrece una propiedad observable y falsable sin dependencias de servicios.
- Permite enseñar incertidumbre, procedencia y contradicción.
- Reduce superficie de ataque al excluir red, secretos y efectos externos.
- Conserva espacio para evaluar B (autorización) y C (aislamiento) posteriormente, sin fingir que A los demuestra.

## Argumento contrario
Podríamos dedicar demasiado tiempo a un motor de evidencias que no prueba la seguridad de acciones reales. Si el objetivo prioritario fuese controlar herramientas externas, B podría generar aprendizaje técnico antes. No resolver este desacuerdo mediante preferencia estética.

## Umbral para reconsiderar
Si las reglas de comparabilidad requieren un sistema ontológico complejo, reducir el caso de uso. Si los criterios de éxito no se pueden escribir sin código, el contrato sigue inmaduro. Si el primer producto necesita fuentes reales, rehacer el modelo de amenazas.

## Condiciones de GO propuestas
- [ ] Definir una sola historia de usuario y un caso de éxito mínimo.
- [ ] Aprobar esquema, equivalencia y límites.
- [ ] Documentar fallos y fixtures negativos.
- [ ] Revisar amenazas y privacidad para el alcance exacto.
- [ ] Fijar entornos y herramienta de compilación.
- [ ] Resolver licencia y política de publicación.
- [ ] Registrar revisión de arquitectura con responsable y objeciones.
- [ ] Obtener autorización explícita para comenzar código.

## Decisión actual
**NO-GO.** La siguiente actividad es revisar estas decisiones y aceptar o rechazar la propuesta; no iniciar la implementación.
