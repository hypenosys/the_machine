# Finch XXI–XXII — Consolidación preimplementación y protocolo de troubleshooting con Jules

**Estado:** PROPUESTA PARA REVISIÓN / HOLD / NO-GO. Documento de análisis, **no normativo**. No autoriza código, herramientas externas, conectores, persistencia, ADR Accepted ni merge. Fecha: 2026-10-21.

## 1. Propósito y precedencia
Consolidar la revisión adversarial de las fases conceptuales Finch XV–XXII sin introducir otra ontología ni sustituir los documentos existentes. **Preceden para la deliberación** `precode-consistency-decision-review-v0.md`, `precode-decision-protocol-v0.md`, el registro de brechas y los requisitos de seguridad. Cualquier conflicto debe escalarse a DEC-01..DEC-08, no resolverse por la autoridad de este documento.

REC (Registro Epistemológico Controlado) es **nombre de trabajo para una responsabilidad lógica**, no un servicio, un modelo físico, una fuente de verdad ni una decisión aprobada. La hipótesis existente sobre contrato común y perfiles versionados continúa abierta. R1 (seis entidades), R2 (Artifact+Attestation), híbrido y control específico siguen sin ganador. **No confundir las letras C/D del informe de auditoría con las C/D del protocolo de decisión**: son taxonomías distintas.

## 2. Frontera conceptual candidata
- **Registro:** identidad interna y ámbito externo declarado; procedencia declarada frente a autenticada; dependencias conocidas y desconocidas; revisiones y tiempos distinguidos; atribución de evaluaciones, dentro de límites de retención.
- **Evaluadores/perfiles:** semántica de dominio, comparabilidad, causalidad, aplicabilidad, independencia investigada, incertidumbre y abstención. La independencia desconocida nunca equivale a independencia verificada.
- **Gobernanza:** propuestas, aprobación, vigencia y revisión de reglas/políticas, sin que el evaluador se otorgue unilateralmente autoridad.
- **Autoridad operativa:** autorización de acciones separada de evaluaciones; deny-by-default, límites de capacidad y revalidación cuando corresponda.
Estas son responsabilidades lógicas, no cuatro procesos ni barreras de aislamiento demostradas. Un adversario con control del host/binario/llaves supera muchas garantías puramente locales.

## 3. Matriz de no duplicación P-01..P-06
| Propuesta | Cobertura previa | Resolución recomendada |
|---|---|---|
| P-01 Evaluación no autoriza ejecución | TB-03/04; SEC-REQ-002/003 | Reutilizar, no duplicar |
| P-02 Fuente no se autentica a sí misma | F-03; SEC-REQ-007 | Reutilizar |
| P-03 Corrección no retrodata conocimiento | F-05/06; GAP-003 | Precisar temporalidad y supresión legítima |
| P-04 Evaluador no activa unilateralmente reglas | TH-019; SEC-REQ-016; GAP-002/005/010 | **Brecha parcial**: trazabilidad de cambios y autoridad normativa |
| P-05 Dependencia conocida no cuenta como soporte independiente | F-04; rechazo de H | Reutilizar, sin prometer descubrir dependencias ocultas |
| P-06 Perfil no redefine garantías del núcleo | H común/perfiles; DEC-02 | Reutilizar, definir frontera verificable |

## 4. Tensiones C-01..C-04 y disposición propuesta
| ID | Tensión | Disposición no aprobada | Evidencia pendiente |
|---|---|---|---|
| C-01 | Historia vs privacidad | Supresión legítima puede hacer imposible reproducir una evaluación; no prometer retención eterna ni borrado físico | E-10 simulación lógica, privacidad real fuera de alcance |
| C-02 | Núcleo común vs semántica especializada | Registro conserva estructura; perfil justifica comparabilidad y causalidad | Segundo dominio y contraejemplos |
| C-03 | Gobernanza vs seguridad real | Separación lógica no equivale a aislamiento; adversario privilegiado explícito | TH-019, GAP-004, pruebas globales pendientes |
| C-04 | Harness con E/S vs núcleo sin E/S | Núcleo sin E/S; harness sintético con entradas/salidas efímeras solo si se autoriza | DEC-03, pruebas negativas futuras |

## 5. Criterios de falsación R-01..R-08 (NO EJECUTADOS)
R-01 identidad externa fusionada por coincidencia textual; R-02 fuente autoverificada; R-03 dependencia conocida contada como corroboración independiente; R-04 conocimiento posterior retrodatado; R-05 evaluación/regla histórica sobrescrita sin rastro; R-06 semántica de dominio aplicada fuera de alcance; R-07 conclusión convertida en permiso; R-08 supresión lógica presentada como eliminación física.

Son **criterios candidatos** que deben mapearse a F-01..F-10 / E-01..E-10 / L-01..L-10 existentes; no son tests nuevos ni PASS. No confundir fidelidad de representación con corrección de evaluación. Fijar oráculos antes de ejecutar, separar verdad del harness de entradas visibles y admitir abstención justificada.

## 6. Decisiones existentes, sin ratificar
- DEC-01 laboratorio epistemológico offline, no producto autónomo completo.
- DEC-02 comparar R1/R2 con contratos neutrales, sin representación elegida.
- DEC-03 núcleo sin E/S y harness controlado, pendiente de aprobación.
- DEC-04 E-10 como simulación lógica, no garantía física.
- DEC-05 oráculos previos, negativos y segundo dominio.
- DEC-06 diferir plataforma/serialización hasta contrato y límites.
- DEC-07 licencia expresa antes de distribución pública.
- DEC-08 **NO-GO** hasta autorización explícita del titular.

## 7. Protocolo de troubleshooting adversarial para @Jules
1. Leer este documento **junto a los originales**, no tomarlo como fuente de autoridad.
2. Construir tabla con: hallazgo, archivo y sección/linea, contradicción o duplicación, gravedad, impacto, propuesta mínima, evidencia, estado OPEN/RESOLVED/UNVERIFIED.
3. Verificar especialmente C-01..C-04, P-04, identidades y tiempos, taxonomías A/B/C/D, `CONFLICTO` vs `CONFLICTED`, y diferencias entre oráculo del harness y entrada del evaluador.
4. Buscar **contraejemplos** que refuten H del núcleo común y el límite REC/evaluadores. Comparar R1/R2 contra control de dominio, sin declarar vencedor por recuento de tipos.
5. Auditar mapeo a TH-001..020, SEC-REQ-001..017 y GAP-001..010; no crear requisitos duplicados. Identificar explícitamente TH-012/016/019 sin test global asignado.
6. Separar hallazgos DOCUMENTALES de propiedades solo verificables con código. No afirmar pruebas ejecutadas, aislamiento, ausencia de red, borrado físico, reproducibilidad ni seguridad de producción.
7. Emitir **STOP / REVISE / READY-FOR-DECISION**, con razones y preguntas bloqueantes; READY-FOR-DECISION **no** significa GO para código.
8. No modificar archivos ni crear PR sin permiso adicional del titular. No adoptar ADR, no implementar, no mergear.

## 8. Estado de salida
**HOLD / NO-GO.** Esta consolidación permite revisar contradicciones y preparar la deliberación; no acredita cumplimiento de G0–G5, no selecciona arquitectura y no demuestra controles.