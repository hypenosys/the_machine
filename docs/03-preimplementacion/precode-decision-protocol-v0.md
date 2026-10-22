# Protocolo de decisión antes de código — v0

**Estado:** PROPUESTO / NO-GO. **Naturaleza:** instrumento de deliberación, no ADR aceptado, autorización, resultado experimental ni contrato implementado.

## Propósito y autoridad
Preparar una decisión falsable sobre el primer experimento offline de THE MACHINE. La auditoría integrada en PR #15 no aprobó la opción B, ninguna licencia ni la fase de código **en aquel corte**. Posteriormente se incorporó `LICENSE.md` con CC BY 4.0 para documentación original; ello no licencia software futuro ni autoriza código. Solo los cotitulares, conforme a un procedimiento de autoridad ratificado, podrán autorizar expresamente un experimento delimitado. La comparación descrita aquí es una **prueba diseñada, no ejecutada**.

## Pregunta a resolver
¿Cuál es el modelo conceptual mínimo que conserva atribución, evidencia versionada, contradicción, incertidumbre y retractación sin complejidad innecesaria?

- **A — candidata vigente:** `Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`. Fuente: `docs/03-preimplementacion/unified-specification-candidate-v0.md`.
- **B — propuesta del auditor:** `Artifact` + `Attestation`; las relaciones y evaluaciones semánticas se delegan a perfiles. Fuente: `docs/04-auditorias/architecture-review.md`.
- **C — híbrida a evaluar:** envoltorio de procedencia sencillo, con afirmaciones, evaluaciones y relaciones tipadas en un perfil explícito, sin imponer las seis entidades a todo artefacto. **Nueva hipótesis**, no decisión.
- **D — control mínimo:** representación directa del caso de sensores sin núcleo genérico, para estimar la complejidad base. No se promociona como arquitectura general.

## Fixtures sintéticos propuestos (ninguno ejecutado)
| ID | Entrada y expectativa observable | Error que falsaría el modelo |
|---|---|---|
| F-01 | Dos sensores, mismo alcance/instante, valores incompatibles; preservar ambas lecturas y declarar conflicto relativo a tolerancia explícita | Elegir una lectura como verdad sin justificación |
| F-02 | Dos valores diferentes con unidades o alcances no comparables; abstención `NOT_COMPARABLE` | Declarar conflicto por desigualdad numérica |
| F-03 | Una fuente sin autenticar declara un hecho; procedencia `UNVERIFIED` | Ascender a `VERIFIED` por texto |
| F-04 | Dos informes derivados de una sola fuente; dependencia compartida | Contarlos como corroboración independiente |
| F-05 | Corrección/retractación de lectura anterior; conservar versión, vínculo y evaluación histórica sin presentar como vigente la evaluación retractada | Borrar silenciosamente la historia o mantener evaluación obsoleta como actual |
| F-06 | `valid_time`, `recorded_time` y `assessed_time` diferentes; no inferir simultaneidad | Colapsar los tres tiempos |
| F-07 | «No se observó P» frente a «No P»; mantener polaridad/modalidad | Inferir negación por ausencia |
| F-08 | Una afirmación contradictoria bajo versiones o ámbitos diferentes | Falso conflicto sin comparar ámbito/versión |
| F-09 | Evidencia ausente o insuficiente; abstenerse `INSUFFICIENT` | Inventar evidencia o certeza |
| F-10 | Datos marcados para supresión; diseñar privacidad compatible con referencias históricas | Prometer inmutabilidad incompatible con borrado |

**Criterios comparativos predefinidos:** capacidad de expresar cada fixture sin pérdida de información; número de tipos y relaciones *realmente necesarios* por fixture; complejidad de serialización y versionado; trazabilidad de evaluaciones; extensibilidad a otro dominio no sensorial; riesgo de acoplamiento; posibilidad de auditar y rectificar. **No asignar puntuaciones, rendimiento ni ganadores antes de ejecutar pruebas.**

## Seguridad y alcance del posible corte
Solo datos sintéticos, ejecución local, sin conectores de red, sin acciones sobre host, sin LLM, sin persistencia duradera, sin credenciales ni datos personales. Las amenazas de persistencia, copias de seguridad, delegación y operación siguen en el backlog global; no se simula su mitigación por exclusión de alcance. La restricción «sin red» requerirá prueba negativa al ejecutar, no basta con declararla.

## Matriz de decisiones pendientes
| Decisión | Evidencia requerida | Autoridad | Estado |
|---|---|---|---|
| Alcance exacto y no objetivos del experimento | Una página con activos, límites y casos negativos | Cotitulares | ABIERTA |
| Arquitectura A/B/C/D | Comparación falsable con F-01..F-10 y un segundo dominio | Cotitulares tras revisión | ABIERTA |
| Formato de datos, identificadores y semántica temporal | Contrato versionado, errores y límites explícitos | Cotitulares / ADR pertinente | ABIERTA |
| Plataforma, toolchain, dependencias y reproducción | Procedimiento fijado antes de ejecución | Cotitulares / ADR pertinente | ABIERTA |
| Licencia y política de contribuciones | CC BY 4.0 documental ya incorporada; revisar derechos de terceros, aportaciones y licencia de código antes de distribuir software | Cotitulares | ABIERTA (residual) |
| Riesgos residuales y excepciones de gates | Amenazas específicas, pruebas negativas, responsable y vencimiento de excepciones | Cotitulares | ABIERTA |
| Permiso para escribir código | GO expreso, acotado y registrado | Cotitulares | **NO-GO** |

## Condición de salida
Una decisión `GO` solo puede registrarse tras satisfacer las condiciones de `docs/03-preimplementacion/readiness-review.md` o aprobar excepciones expresas, limitadas y justificadas. `CONDITIONAL GO` en `docs/04-auditorias/readiness-assessment.md` es recomendación del auditor, **no permiso**.

**Siguiente trabajo permitido sin código:** revisar adversarialmente esta matriz, completar los fixtures conceptuales y documentar los riesgos de cada alternativa. No convertir propuestas en ADR `Accepted`, no iniciar crates ni CI.
