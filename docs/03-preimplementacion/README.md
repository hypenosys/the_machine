# Puerta de reflexión previa al código — THE MACHINE

**Estado: HOLD / NO-GO para implementar.** Documento de decisión, no código ni resultado experimental.

## Por qué detenernos aquí
El repositorio contiene documentación educativa, ADR propuestos, un modelo de amenazas inicial, requisitos y planes de experimentos. **No contiene todavía evidencia suficiente para afirmar que el diseño del núcleo es correcto o seguro.** Producir Rust ahora cristalizaría decisiones no tomadas.

## Qué sabemos
- Objetivo: sistema local-first, auditable, generalista, explicable y útil a principiantes.
- Hipótesis arquitectónicas: Rust, núcleo pequeño, datos tipados, fuentes no confiables, autorización fuera del modelo.
- Hay 5 ADR en Proposed, 17 requisitos de seguridad propuestos y experimentos definidos pero no ejecutados.
- La investigación publicada es preliminar; citar documentación oficial no equivale a haber contrastado sus afirmaciones con pruebas.

## Qué no sabemos todavía
- **Alcance del primer producto**: ¿biblioteca de evidencia, simulador educativo, herramienta de investigación o agente ejecutor?
- **Modelo de amenaza real**: actores, activos y plataformas para la primera entrega.
- **Modelo de datos y privacidad**: identidad, retención, borrado, formato y evolución de esquemas.
- **Autorización**: permisos, delegación, revocación y efecto exactamente una vez frente a servicios externos.
- **Aislamiento**: límites demostrables por SO, no promesas de sandbox universal.
- **Persistencia**: garantías de durabilidad frente a coste operativo y dependencias.
- **Licencia**: sin decisión explícita no podemos prometer software libre.
- **Reproducibilidad**: entorno y criterios de prueba aún no establecidos.

## Tres posibles primeros cortes (NO decididos)
| Opción | Qué entrega | Ventaja | Riesgo |
|---|---|---|---|
| A — Laboratorio de evidencia offline | Ingerir dos observaciones sintéticas, detectar conflicto y mostrar procedencia | Alineado con enseñanza y mínimo privilegio | No prueba conectores ni aislamiento |
| B — Pasarela de acciones simuladas | Políticas y decisiones sobre acciones sin efectos externos | Ataca riesgos de autoridad | Obliga a definir identidad y semántica pronto |
| C — Investigación de aislamiento | Harness para comparar sandboxes en SO concretos | Valida una frontera crítica | Dependencia del entorno y portabilidad |

**Recomendación provisional: A**, con entrada estrictamente sintética, sin red, sin secretos, sin efectos externos y sin almacenamiento persistente en la primera prueba. Esto **no** autoriza implementarlo: primero decidir contratos, criterios y licencia.

## Regla de parada
No abrir PR de código, no crear crates, no añadir dependencias, no ejecutar pruebas invasivas y no aceptar ADR por inercia. La siguiente intervención debe ser una revisión consciente del alcance, amenazas, opciones y costes.
