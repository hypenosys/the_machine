# Mapa de autoridad documental — propuesta de consolidación

**Estado: PROPUESTO / NO-GO para código.** Este documento no acepta ADR ni aprueba implementación.

> **Delimitación de autoridad (23-10-2026, PR #33):** la «jerarquía de lectura» de este mapa ordena **contratos conceptuales y documentos técnicos candidatos** para facilitar su interpretación; **no** determina quién puede ratificar, qué decisión prevalece jurídicamente, ni qué gates quedan aprobados. El [paquete Finch DEC-GOV-010 / DEC-GATE-003](finch-gap010-g3-ratification-package-candidate-2026-10-23.md) propone una jerarquía **distinta**, basada en competencia, alcance y estado de ratificación, y separa las autorizaciones de código/ejecución/merge. Ambas jerarquías tienen objetos diferentes: ninguna está ratificada y no se permite inferir que el contrato conceptual prevalezca sobre una decisión competente. Ante colisión material, registrar discrepancia y mantener HOLD para la actividad afectada.

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
