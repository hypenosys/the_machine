# PR #33 — continuación de auditoría de rutas (lotes D–F)

**Fecha:** 2026-10-23. **Carácter:** registro parcial reproducible por archivos, sin ejecución de software ni ratificación.

## Alcance exacto

Se inspeccionaron **37 archivos Markdown adicionales**, distribuidos en tres lotes, mediante lectura de contenido de la rama y cotejo de rutas Markdown inline locales contra el árbol Git recursivo de **97 documentos Markdown** (antes de incorporar este registro). Se normalizaron rutas relativas y fragmentos para comprobar existencia del archivo destino. No se comprobaron anclas, URLs externas, enlaces Markdown por referencia, enlaces HTML, ni consistencia semántica.

| Lote | Archivos | Archivos incluidos | Enlaces locales comprobados | Destinos inexistentes detectados |
|---|---:|---|---:|---:|
| D | 12 | `consistency-resolution-v0.md`, `consolidation-decision-gate.md`, `cross-domain-comparability-paper-v0.md`, `decision-matrix.md`, `decision-preferences-proposal-2026-10-21.md`, `decision-request.md`, `decision-review-v0.md`, `design-freeze-candidate-v0.md`, `epistemic-review-decision.md`, `evidence-contract-v0.md`, `evidence-lifecycle-privacy-candidate-v0.md`, `executive-summary-v1.md` (todos en `docs/03-preimplementacion/`) | 0 | 0 |
| E | 12 | `final-reflection-before-code.md`, `finch-consolidation-troubleshooting-candidate-v0.md`, `finch-paper-experiments-v0.md`, `heterogeneous-cases.md`, `lineage-retraction-paper-contract-v0.md`, `offline-experiment-contract-candidate-v0.md`, `precode-consistency-decision-review-v0.md`, `precode-decision-protocol-v0.md`, `precode-review-checklist.md`, `readiness-review.md`, `reflection-questions.md`, `semantic-falsification-cases.md` (todos en `docs/03-preimplementacion/`) | 4 | 0 |
| F | 13 | `uncertainty-register-v1.md`, `unified-specification-candidate-v0.md`, `vertical-slice-a.md` (en `docs/03-preimplementacion/`); `architecture-review.md`, `auditoria-integral-2026-10.md`, `contradiction-inventory-2026-10-21.md`, `gap-register.md`, `independent-review-remediation-triage-2026-10-21.md`, `informe-auditoria-adversarial-2026.md`, `pr25-documentary-merge-readiness-2026-10-22.md`, `readiness-assessment.md`, `research-evidence.md`, `security-review.md` (en `docs/04-auditorias/`) | 7 | 0 |
| **Total D–F** | **37** | | **11** | **0** |

**Importante:** «0 enlaces locales» en muchos documentos indica que el detector no encontró enlaces inline de esa sintaxis, no que haya comprobado sus referencias textuales o citas en backticks.

## Lectura de resultados

- Los lotes A–C previos comprobaron 45 archivos y 81 enlaces locales; D–F añaden 37 archivos y 11 enlaces locales. Las muestras anteriores al lote A incluyen archivos que pueden solaparse con otros lotes, por lo que **no se declara aquí un porcentaje global deduplicado** sin reconstruir una matriz de rutas verificadas.
- No se detectaron destinos inexistentes entre los 11 enlaces locales de D–F. Esto **no prueba** que todos los enlaces o afirmaciones del repositorio sean correctos.
- Los informes creados durante la auditoría modifican el denominador del inventario. El total de 97 corresponde al corte previo a este commit.
- Los conflictos de autoridad/G3, derechos, privacidad, evidencia experimental y ratificación siguen abiertos. La PR documental no cambia HOLD/NO-GO.

## Próxima puerta de calidad

Construir una matriz deduplicada por ruta y commit, verificar enlaces de referencia y anclas, y auditar afirmaciones normativas con cita literal y disposición (compatible, contradicción abierta, propuesta o resuelta). No declarar «cero contradicciones» sin esos resultados.
