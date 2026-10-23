# Puerta de reflexión previa al código — THE MACHINE

**Estado: HOLD / NO-GO para implementar.** Documentos candidatos de análisis y deliberación; **sin autorización de escribir, compilar o ejecutar código**. La ausencia de código o de `Cargo.toml` en todas las ramas no queda certificada por este documento.


## Registro transversal de coherencia (propuesta, no ratificada)

- [Registro Finch de coherencia y dependencias — 23-10-2026](finch-consistency-decision-register-2026-10-23.md): distingue verticales de arquitecturas, reconcilia estados de readiness, explicita dependencias de G3/DEC-08 y enumera bloqueos sin declarar cero contradicciones ni permisos.
- [Contrato candidato de coherencia global determinista](deterministic-global-coherence-contract-candidate-v0.md): fija invariantes, disposiciones, oráculos en papel y condiciones necesarias para un cierre reproducible; estado actual NOT_READY, sin ratificación.

## Contratos conceptuales derivados (sin ejecución)

- [Matriz de garantías de procedencia](provenance-assurance-matrix-v0.md): separa integridad, clave, identidad, origen y verdad; casos de falsación en papel.
- [Linaje, retractación y reevaluación](lineage-retraction-paper-contract-v0.md): dependencias desconocidas, versiones y conservación de historial.
- [Comparabilidad entre dominios](cross-domain-comparability-paper-v0.md): telemetría y documentación técnica; abstenciones y presupuesto conceptual de complejidad para R1/R2/C/D.

Estos documentos **no son pruebas ejecutadas, selección arquitectónica ni aprobación de gates**. Las conclusiones son condicionales a ejemplos hipotéticos y deben revisarse por persona distinta del autor antes de atribuirles revisión independiente.

## Investigación conceptual — Cuaderno Finch

El [cuaderno de experimentos en papel](finch-paper-experiments-v0.md) reúne seis escenarios hipotéticos sobre autenticidad, dependencia de evidencias, comparabilidad, complejidad arquitectónica, borrado y autoridad. Cada uno distingue deducción conceptual de evidencia experimental y propone el siguiente documento que reduciría incertidumbre. **No contiene pruebas ejecutadas, mediciones ni decisiones ratificadas.**

## Preferencias operativas recientes (no ratificadas)

La [propuesta de decisiones y matriz de dependencias del 21-10-2026](decision-preferences-proposal-2026-10-21.md) registra las preferencias de delegación técnica delimitada a @Axlfc (GAP-010), separación de permisos de código/ejecución/merge (G3), evaluación de GPL para software futuro y primer alcance offline sintético. Incluye una **preferencia editorial reversible** por estudiar GPL-3.0-or-later, sin aplicarla ni alterar CC BY 4.0 para documentación original cubierta. No consta ratificación conjunta de @Axlfc y @TopperH4rley, ni se autoriza código, CI, pruebas o merge por estas preferencias. La [hoja candidata de ratificación](owner-ratification-sheet-candidate-v1.md) conserva pendientes las aceptaciones.

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

**Recomendación provisional de alcance: corte A (laboratorio de evidencia offline)**, con entrada estrictamente sintética, sin red, sin secretos, sin efectos externos y sin almacenamiento persistente en la primera prueba. **Esta letra A identifica un corte funcional, no la selección de la arquitectura R1 / «Opción A» de seis entidades** descrita en otros informes; R1, R2, C y D siguen sin ganador ratificado. Esto **no** autoriza implementarlo: primero decidir contratos, criterios y licencia.

---


**Paquete de ratificación pendiente (GAP-010 / G3):** [Decisión Finch sobre autoridad documental, delegación y permisos separados](finch-gap010-g3-ratification-package-candidate-2026-10-23.md). Es una propuesta para deliberación conjunta, **no un acta aprobada**; conserva HOLD / NO-GO, no concede AUT-CODE, AUT-EXEC ni AUT-MERGE y no reemplaza los gates históricos.

## Regla de Parada y Prohibiciones
No abrir PR de código, no crear crates, no añadir dependencias, no ejecutar pruebas invasivas y no aceptar ADR por inercia. La siguiente intervención debe ser una revisión consciente por parte de los cotitulares del paquete de decisión v1.
