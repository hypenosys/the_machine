# Revisión arquitectónica: ¿qué es común y qué es especializado?

**Estado: deliberación, NO-GO para código.**

## Candidato recomendado
Un **núcleo de representación epistemológica** con Source, Artifact, Claim, EvidenceLink, Assessment y Relation. Los dominios aportan vocabulario, validación y reglas de comparación; no obtienen autoridad sobre acciones externas.

## Alternativas
1. **Modelo universal único:** expresivo en teoría, pero corre riesgo de ontología prematura y falsa equivalencia.
2. **Tres modelos aislados:** simple por caso, pero duplica procedencia y dificulta análisis cruzado.
3. **Núcleo común mínimo + adaptadores de dominio (recomendado):** comparte trazabilidad sin imponer comparadores universales.

## Riesgos del candidato
- Claims demasiado genéricos para representar negación, cuantificadores o tiempo.
- Proveniencia circular o manipulada.
- Doble contabilización de evidencia dependiente.
- Confusión entre soporte de una cita y validez de una conclusión.
- Explicaciones convincentes que omiten supuestos.
- Coste de versionar ontologías y migrar evaluaciones.

## Requisitos antes de implementación
- Definir semántica mínima de Claim: negación, alcance, tiempo, sujeto, predicado y objeto.
- Definir identidad y versionado de Source, Artifact y Assessment.
- Definir dependencia entre evidencias y tratamiento de retractaciones.
- Definir semántica de evaluación, abstención y errores.
- Elegir **un** caso vertical para ejecutar primero sin convertirlo en el esquema raíz.
- Decidir formatos, límites, plataforma y licencia.
- Registrar revisión crítica y autorización explícita de inicio.

## Veredicto
**NO-GO.** Se propone el contrato, pero no se aprueba una arquitectura ejecutable. No generar Rust ni dependencias.
