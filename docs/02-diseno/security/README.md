# Seguridad desde el minuto cero

**Estado:** arquitectura y controles propuestos, sin certificación.

## Empieza aquí
¿Puede un documento ordenar a la IA que envíe información privada? **No debería.** Un documento es dato, no autoridad. Esta diferencia es una **frontera de confianza**.

## Documentos
1. [Modelo de amenazas](threat-model-v0.md)
2. [Flujos de datos y fronteras](data-flow-diagrams.md)
3. [Matriz de permisos](authorization-matrix.md)
4. [Registro de riesgos](risk-register.md)
5. [Plan de verificación adversarial](verification-plan.md)
6. [Respuesta a incidentes](incident-response.md)
7. [Criterios de aceptación de seguridad](security-gates.md)

## Reglas
- Una descripción de un control no equivale a su implementación.
- No llamar «seguro» a un sistema sin definir alcance, amenaza y evidencia.
- Una salida de IA jamás autoriza por sí misma un efecto externo.
- Minimizar datos y permisos desde el diseño.
- Mantener los hallazgos negativos y riesgos residuales visibles.
