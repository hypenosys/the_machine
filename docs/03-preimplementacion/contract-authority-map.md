# Mapa de autoridad documental — propuesta de consolidación

**Estado: PROPUESTO / NO-GO para código.** Este documento no acepta ADR ni aprueba implementación.

## Jerarquía de lectura propuesta
1. **Gobernanza y seguridad:** los ADR conservan estado PROPOSED y sus controles son objetivos, no garantías implementadas.
2. **Contrato conceptual del núcleo:** `general-epistemic-contract-v0.md` más `claim-semantics-v0.md` y `evidence-dependencies-and-retractions.md`, como conjunto candidato de referencia. **Todavía no hay especificación normativa aprobada.**
3. **Casos de falsación transversal:** `heterogeneous-cases.md` y `semantic-falsification-cases.md`.
4. **Adaptador experimental de temperatura:** `evidence-contract-v0.md`, `design-freeze-candidate-v0.md` y `acceptance-cases-v0.md`. Son un caso de dominio, no el esquema raíz.
5. **Histórico de deliberación:** `decision-review-v0.md`, `decision-matrix.md` y documentos previos siguen accesibles como decisiones no ratificadas.

## Reglas de precedencia propuestas
- El contrato general **no hereda** el requisito de usar JSON, temperatura, enteros escalados o instantes exactos del experimento de sensores.
- Los estados COMPATIBLE/CONFLICTO/NO_COMPARABLE/INVALIDO pertenecen al comparador de sensores; SUPPORTED/REFUTED/CONFLICTED/INSUFFICIENT/NOT_COMPARABLE/INVALID son categorías candidatas de evaluación general. **No hay correspondencia automática**.
- Un EvidenceLink describe la relación declarada con un artefacto; no certifica que ese artefacto pruebe una proposición.
- Un Assessment puede abstenerse; una Claim no se convierte en verdad al almacenarse.
- Las fuentes pueden tener atribución declarada, pero autenticación requiere un mecanismo externo verificable.
- Un contrato de dominio puede imponer restricciones más estrictas, sin redefinir el significado de los conceptos comunes.

## Resultado de la auditoría
No existe todavía un único esquema normativo implementable. Se recomienda un contrato conceptual de referencia y perfiles de dominio versionados, sujetos a revisión independiente.
