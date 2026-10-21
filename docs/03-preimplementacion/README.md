# Puerta de reflexión previa al código — THE MACHINE

**Estado: HOLD / NO-GO para implementar.** Documentos candidatos de análisis y deliberación; **sin autorización de escribir, compilar o ejecutar código**. La ausencia de código o de `Cargo.toml` en todas las ramas no queda certificada por este documento.

## Por qué detenernos aquí
El repositorio contiene documentación educativa, ADR propuestos, un modelo de amenazas inicial, requisitos y contratos de prueba pre-código. **No contiene todavía evidencia suficiente para afirmar que el diseño del núcleo es correcto o seguro.** Producir código Rust ahora cristalizaría decisiones no tomadas ni ratificadas.

---

## Entregables Principales de Preimplementación (Versión v1 — Candidatos No Normativos)

Para orientar la deliberación formal de los cotitulares (@Axlfc y @TopperH4rley) sin violar la prohibición de código, la carpeta `docs/03-preimplementacion/` dispone de los siguientes seis entregables estructurados v1:

1. **[Resumen Ejecutivo para los Cotitulares](executive-summary-v1.md):**
   Síntesis concisa (máximo 2 páginas) sobre la corrección de defectos B-01..B-08, matriz de decisiones DEC-01..DEC-08 y opciones de deliberación inmediata.
2. **[Paquete de Decisión v1](decision-package-v1.md):**
   Matriz exhaustiva `DEC-01..DEC-08` con opciones, costes, riesgos, evidencia requerida, dependencias, autoridad e idoneidad provisional.
3. **[Contrato Comparativo v1](comparative-contract-v1.md):**
   Especificación neutra e imparcial (marco candidato incompleto) para comparar R1 (6 entidades), R2 (2 entidades), Híbrida C y Baseline D bajo un arnés común, oráculo independiente e independencia de marcas temporales (`valid_time`, `recorded_time`, `assessed_time`).
4. **[Matriz de Trazabilidad v1](traceability-matrix-v1.md):**
   Correspondencia documental candidata, con cobertura directa, parcial o temática, entre criterios `R-01..R-08`, fixtures `F-01..F-10`, oráculos `E-01..E-10` y escenarios `L-01..L-10`, identificando huecos explícitos (**"SIN FIXTURE DIRECTO"**) y proponiendo los fixtures F-11 y F-12 sin renumerar.
5. **[Protocolo de Autorización por Etapas v1](staged-authorization-protocol-v1.md):**
   Desacoplamiento estricto de las puertas de autorización (Gates G0 a G5) y subgates de laboratorio (Subgates G2.1 a G2.4), estableciendo como regla candidata que la aprobación documental (Subgate G2.1) o la ejecución de laboratorio (Subgate G2.2) no concedan autorización automática para la fase de código (Gate G3).
6. **[Registro de Incertidumbres v1](uncertainty-register-v1.md):**
   Catálogo activo de bloqueos reales (E-10 en estado **BLOQUEADO**), estado real de brechas (`GAP-001..GAP-010`), falta de tests ejecutados para amenazas `TH-012/016/019` (`GAP-002`) e hipótesis sin demostrar.

---

## Qué sabemos
- Objetivo: sistema local-first, auditable, generalista, explicable y útil a principiantes.
- Hipótesis arquitectónicas: Rust, núcleo pequeño, datos tipados, fuentes no confiables, autorización fuera del modelo.
- Hay 5 ADR en Proposed, 17 requisitos de seguridad propuestos y experimentos sintéticos diseñados pero no ejecutados.
- La investigación publicada es preliminar; citar documentación oficial no equivale a haber contrastado sus afirmaciones con pruebas empíricas.

## Qué no sabemos todavía
- **Alcance del primer producto**: ¿biblioteca de evidencia, simulador educativo, herramienta de investigación o agente ejecutor? (Sometido a deliberación en `DEC-01`).
- **Modelo de amenaza real**: actores, activos y plataformas para la primera entrega.
- **Modelo de datos y privacidad**: identidad, retención, borrado, formato y evolución de esquemas (`E-10 BLOQUEADO`).
- **Autorización**: permisos, delegación, revocación y efecto exactamente una vez frente a servicios externos.
- **Aislamiento**: límites demostrables por SO, no promesas de sandbox universal.
- **Persistencia**: garantías de durabilidad frente a coste operativo y dependencias (Diferido en `DEC-06`).
- **Licencia**: `LICENSE.md` incorpora CC BY 4.0 para documentación original y materiales no software con derechos suficientes; siguen pendientes revisión de terceros, cierre formal de `GAP-001` y licencia de software futuro. No debe presentarse como licencia general del eventual código.
- **Reproducibilidad**: entorno y criterios de prueba aún no establecidos.

---

## Tres posibles primeros cortes (NO decididos)
| Opción | Qué entrega | Ventaja | Riesgo |
|---|---|---|---|
| A — Laboratorio de evidencia offline | Ingerir dos observaciones sintéticas, detectar conflicto y mostrar procedencia | Alineado con enseñanza y mínimo privilegio | No prueba conectores ni aislamiento |
| B — Pasarela de acciones simuladas | Políticas y decisiones sobre acciones sin efectos externos | Ataca riesgos de autoridad | Obliga a definir identidad y semántica pronto |
| C — Investigación de aislamiento | Harness para comparar sandboxes en SO concretos | Valida una frontera crítica | Dependencia del entorno y portabilidad |

**Recomendación provisional: A**, con entrada estrictamente sintética, sin red, sin secretos, sin efectos externos y sin almacenamiento persistente en la primera prueba. Esto **no** autoriza implementarlo: primero decidir contratos, criterios y licencia.

---

## Regla de Parada y Prohibiciones
No abrir PR de código, no crear crates, no añadir dependencias, no ejecutar pruebas invasivas y no aceptar ADR por inercia. La siguiente intervención debe ser una revisión consciente por parte del titular del paquete de decisión v1.
