# Hallazgos de coherencia transversal — revisión documental v0

**Método:** contraste textual de cinco documentos de preimplementación: `README.md`, `decision-review-v0.md`, `design-freeze-candidate-v0.md`, `general-epistemic-contract-v0.md` y `claim-semantics-v0.md`. Revisión parcial; **no** auditoría exhaustiva del repositorio, ejecución ni validación externa.

| ID | Hallazgo | Resolución propuesta | Estado |
|---|---|---|---|
| CONS-001 | El diseño de temperatura usa `evidence.v0` y valores numéricos; el núcleo general requiere Claims heterogéneas | Degradar temperatura a perfil experimental | PROPUESTO |
| CONS-002 | El contrato de sensor expresa COMPATIBLE; el general usa SUPPORTED | No equiparar compatibilidad de valores con soporte epistemológico | PROPUESTO |
| CONS-003 | `design-freeze-candidate-v0.md` menciona salida local mientras otros documentos excluyen efectos externos | Delimitar salida controlada de prueba; no declarar ausencia absoluta de efectos | ABIERTO |
| CONS-004 | La fuente se denomina declarada/autenticada pero no hay autenticador | Exigir campo de estado de verificación, sin inferir autenticidad | PROPUESTO |
| CONS-005 | Tiempo de observación, registro y evaluación aparecen con semánticas distintas | Separar tiempos y definir política de normalización por perfil | ABIERTO |
| CONS-006 | Dos fuentes pueden compartir origen sin declararlo | Registrar dependencia desconocida; no multiplicar corroboración | PROPUESTO |
| CONS-007 | SUPPORTED podría interpretarse como verdad universal | Obligar a identificar regla, alcance y evidencia | PROPUESTO |
| CONS-008 | El conjunto de conceptos no define cuantificadores ni negación compuesta | Limitar semántica v0 y abstenerse cuando no se pueda representar | ABIERTO |
| CONS-009 | Reglas de rechazo atómico del sensor podrían generalizarse indebidamente | Restringir atomicidad a lote del perfil, no a todas las evaluaciones | PROPUESTO |
| CONS-010 | «Design freeze» sugiere cierre, pero hay decisiones abiertas | Tratarlo explícitamente como candidato no congelado | PROPUESTO |

## Bloqueos para un contrato implementable
Definir identidad y versionado, representación exacta de proposición y alcance, evaluación y abstención, referencias a evidencia, errores, privacidad y formato del primer perfil. Revisar también amenazas del alcance real.

## Advertencia
Los hallazgos son observaciones de documentos consultados; no prueban ausencia de otros conflictos en documentos no inspeccionados.
