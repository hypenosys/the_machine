# Checklist de revisión profesional de seguridad

**Para revisores humanos o agentes. No sustituye revisión independiente.**

## Documentación
- [ ] Problema, activos y objetivos explicados para no especialistas.
- [ ] ADR y requisitos enlazados; alternativas y supuestos visibles.
- [ ] Se distinguen fuentes, inferencias, propuestas y pruebas.
- [ ] Cada frontera de confianza tiene propietario.

## Amenazas y controles
- [ ] Entradas no confiables tipadas y limitadas.
- [ ] Política deny-by-default, sin autorización desde el LLM.
- [ ] Revalidación antes de efectos externos y protección contra replay.
- [ ] Cuotas de CPU, memoria, tiempo, tamaño y red documentadas.
- [ ] No se exponen secretos a prompts, logs ni fixtures.
- [ ] Ciclo de vida, borrado y backups definidos.
- [ ] Dependencias, scripts de build y licencias revisados.
- [ ] Plan de rollback y respuesta a incidentes.

## Verificación
- [ ] Pruebas negativas asociadas a requisitos.
- [ ] Resultados reales asociados a commit y entorno.
- [ ] Fallos y bloqueos visibles, sin pruebas inventadas.
- [ ] Riesgos residuales explícitos.
- [ ] Revisión por persona distinta cuando exista capacidad.

## Decisión
- [ ] ACCEPT / REJECT / BLOCKED con motivos, autor, fecha y enlaces.
