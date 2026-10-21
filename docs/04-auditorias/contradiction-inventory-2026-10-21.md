# Inventario transversal de contradicciones — revisión documental de PR #25

**Corte:** 21-10-2026. **Alcance:** árbol de la rama `docs/independent-review-remediation-20261021`, 87 archivos Markdown inventariados mediante GitHub Tree API (no truncado) en el corte inicial; este número **no es** el recuento de archivos modificados de la PR y revisados por patrones de autoridad, licencia, estado de ejecución, gates y evidencia. La búsqueda por patrones **no constituye una prueba exhaustiva de equivalencia semántica** ni inspección de todas las ramas, enlaces, cifras y fórmulas. **Estado:** registro de auditoría documental, NO RATIFICADO; HOLD / NO-GO.

## Método y regla de clasificación

1. Distinguir **contradicción factual actual** (dos afirmaciones incompatibles sobre el mismo corte), **hallazgo histórico** (verdadero o reportado para un corte anterior), **colisión normativa** (dos reglas propuestas incompatibles), **diferencia de ámbito** (p. ej., comparador de sensores frente a epistemología general) y **decisión pendiente**.
2. Conservar fuentes originales históricas y añadir notas de actualización en vez de reescribir retrospectivamente evidencia; una fecha y rama deben acompañar cualquier afirmación de estado.
3. `RESUELTO DOCUMENTALMENTE` significa que se corrigió la redacción concreta; **no** significa cierre de GAP, aprobación de gate, pruebas PASS ni certificación global. Las colisiones que dependen de una autoridad externa siguen abiertas.

## Registro de hallazgos

| ID | Tipo | Fuentes y discrepancia | Disposición documental | Estado residual |
|---|---|---|---|---|
| D-01 | Factual temporal | `README.md`, `docs/03-preimplementacion/uncertainty-register-v1.md` y `docs/04-auditorias/gap-register.md`: ausencia de licencia frente a `LICENSE.md` CC BY 4.0 en esta rama | Corregidas las afirmaciones actuales; el registro GAP conserva evidencia anterior y una nota posterior | **ABIERTO** GAP-001: derechos de terceros, software y cierre competente |
| D-02 | Autoridad | Referencias a «el titular» en protocolos de experimento, matrices, revisiones y paquetes; cotitularidad declarada @Axlfc / @TopperH4rley | Actualizadas las referencias operativas identificadas; `GOVERNANCE.md` designa @Axlfc **propuesto**, sin voto de calidad activado | **ABIERTO** GAP-010 / REV-16: mecanismo conjunto, identidad y ratificación |
| D-03 | Factual temporal | `CONTRIBUTING.md`, guías de inicio y `precode-review-checklist.md`: «privado» frente a visibilidad pública observada 21-10-2026 | Corregidas guías y checklist; no se presume visibilidad permanente | Verificar cambios de visibilidad en cada corte |
| D-04 | Exceso de alcance | `README.md`, `comparative-contract-v1.md`, auditorías: «cero código» puede interpretarse universalmente | El estado de gobernanza es NO-GO; la ausencia de archivos solo es afirmable para el árbol inspeccionado | Historial y entornos externos no verificados |
| D-05 | Colisión normativa | `docs/02-diseno/security/security-gates.md` define G3 como control antes del **merge**; `staged-authorization-protocol-v1.md` propone G3 como permiso antes de **empezar código** | Se declara expresamente la colisión en ambos contextos; no se impone jerarquía inventada | **ABIERTO** GAP-010 / REV-05: definición única y precedencia |
| D-06 | Estado frente a recomendación | `docs/04-auditorias/readiness-assessment.md`: `CONDITIONAL GO` del auditor frente a HOLD / NO-GO del proyecto | Diferenciados veredicto técnico y autorización efectiva | **NO-GO** vigente; sin permiso de implementación |
| D-07 | Histórico frente a actual | `gap-register.md` GAP-001; `security/traceability.md` añade SEC-015..017 propuestos, no ejecutados | Mantener cronología y separar cobertura documental de validación real | GAP-001, GAP-002 y otras brechas pendientes de cierre formal |
| D-08 | Cobertura epistemológica | `traceability-matrix-v1.md` R-04, R-06 y R-08: cobertura parcial o temática; F-10/E-10 original bloqueado | Mantener oráculos pendientes, sin elevar `DESIGNED` a `TESTED` | **ABIERTO**: oráculos independientes, segundo dominio y autorización |
| D-09 | Taxonomía | `contract-authority-map.md`: `CONFLICTO` del comparador de sensores frente a `CONFLICTED` del núcleo general | Ámbitos explícitamente distintos, sin conversión automática | Perfil de dominio pendiente de ratificación |
| D-10 | Privacidad | `evidence-lifecycle-privacy-candidate-v0.md` frente a F-10/E-10: trazabilidad histórica y supresión física | Se reconoce degradación de reproducibilidad y ausencia de garantía de borrado físico | **BLOQUEADO** para datos reales |
| D-11 | Atribución de autoridad | Instrucción conversacional de CC BY 4.0 y propuesta de @Axlfc como Mantenedor Principal frente a aprobación conjunta no acreditada | Registrado como instrucción recibida/propuesta; no se inventan firmas | Ratificación conjunta y derechos pendientes |

## Invariantes editoriales de esta rama

- Ningún documento candidato ratifica ADR-0001..0005, G2.1, G2.2, G2.3, G2.4 ni G3.
- Ninguna prueba planificada o fixture en papel es prueba ejecutada, y ninguna autoatribución de procedencia equivale a autenticación.
- `valid_time`, `recorded_time` y `assessed_time` son conceptos distintos; la retrodatación no se detecta únicamente comparando campos autodeclarados.
- F-10/E-10 no se desbloquea mediante ocultación de referencias en memoria; eliminación física, backups y réplicas requieren política y evidencia independientes.
- Una PR fusionable o fusionada no implica autorización normativa. La PR #25 permanece en borrador hasta revisión competente.
- La licencia CC BY 4.0 se aplica a material documental original cubierto, no automáticamente a terceros ni a software futuro.

## Condiciones para afirmar «cero contradicciones»

**No alcanzadas.** Una declaración de cero contradicciones requiere, como mínimo: (a) definición ratificada de autoridad y precedencia de documentos; (b) resolución formal de D-05; (c) revisión semántica completa con referencias y versiones de todos los documentos, no solo patrones; (d) verificación independiente y registro reproducible de resultados; (e) ausencia de hallazgos bloqueantes para el alcance declarado. **No puede confundirse «cero contradicciones editoriales detectadas» con «cero contradicciones del diseño».**

**Próxima decisión reservada:** los cotitulares deben acordar cómo ratificar GAP-010 y qué semántica única tendrán los gates. Hasta entonces, las divergencias están **identificadas y aisladas**, no resueltas por autoridad.

## Seguimiento de correcciones posteriores al corte inicial (21-10-2026)

Este apartado actualiza el **estado editorial** sin alterar la evidencia ni el alcance del inventario original de 87 Markdown. El recuento inicial es una fotografía del árbol entonces inspeccionado, no un recuento actualizado de toda la PR.

| Hallazgo | Corrección posterior comprobable en la rama | Residuo que no se cierra |
|---|---|---|
| D-01 / D-03 | Se actualizaron `decision-review-v0.md`, `readiness-review.md`, `offline-experiment-contract-candidate-v0.md`, `architecture-objections.md` y `consolidation-decision-gate.md` para distinguir visibilidad pública, licencia documental CC BY 4.0 y derechos/software futuros. Se añadieron notas fechadas a `security-review.md`, `informe-auditoria-adversarial-2026.md` y `auditoria-integral-2026-10.md`. | GAP-001 y derechos de terceros; las auditorías históricas conservan sus afirmaciones de época, no son estado actual. |
| D-02 / D-11 | `README.md`, el registro REV-01..20 y la tabla G2.1–G5 del protocolo por etapas se refieren ahora a **cotitulares**, sin asumir ratificación ni desempate. | GAP-010 y acreditación de ratificación por ambos; una solicitud de revisión no es una aprobación. |
| D-04 | Los informes históricos incorporan notas que limitan las afirmaciones sobre ausencia de código y conteos al árbol y corte inspeccionados. | No se ha certificado la ausencia universal de código, ni en ramas adicionales ni en entornos externos. |
| D-05 | El protocolo por etapas enlaza a las fuentes canónicas `docs/02-diseno/security/security-gates.md` y `traceability.md` para facilitar contraste. | La discrepancia G3 **no está resuelta**: inicio de código frente a merge de código. |
| D-07 | El índice consolidado de REV-15 se sincronizó con la incorporación posterior de `LICENSE.md`; las observaciones `license=null` previas permanecen como evidencia histórica fechada. | Licencia de software, terceros y cierre formal de GAP-001. |

**Comprobación de integración separada:** GitHub REST reportó `mergeable=true` y `mergeable_state=clean` para el HEAD `5703ed21cea99f7aa17b56303cb6e8d1f8d33aa9`; no se extrapola ese resultado a HEAD posteriores ni a autorizaciones de gobernanza. La PR sigue DRAFT / HOLD / NO-GO. No se han ejecutado pruebas, no se ha ratificado ningún gate y no se afirma cero contradicciones.
