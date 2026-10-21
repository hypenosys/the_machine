# SEC-RSCH-002/003 — Identidad, capacidades y acciones

**Estado: investigación preliminar; sin implementación.**

## Pregunta
¿Cómo impedir que un modelo, documento o conector convierta una sugerencia en autoridad?

## Alternativas
- RBAC: roles definidos; simple, pero insuficiente para permisos contextuales muy finos.
- ABAC: atributos de actor, recurso y contexto; flexible, con riesgo de políticas difíciles de auditar.
- Capacidades: autorización explícita ligada a recurso y operación; requiere emisión, delegación, expiración y revocación bien diseñadas.
- Mezcla de políticas y capacidades: propuesta para comparar, no aprobada.

## Contrato experimental
Una solicitud incluye identidad verificada, recurso, operación, finalidad, contexto, versión de política y un identificador de intento. El modelo solo produce una **propuesta**, nunca una decisión vinculante.

## Pruebas a diseñar
Revocación entre autorización y ejecución, suplantación de rol, recurso distinto, token caducado, doble ejecución, política inaccesible y operación no autorizada.

## Problema importante
Un token de capacidad no evita por sí solo TOCTOU ni garantiza exactamente una ejecución. La idempotencia requiere coordinación con el ejecutor y persistencia apropiada.

## Fuentes de referencia
- NIST SP 800-162 (ABAC): https://csrc.nist.gov/pubs/sp/800/162/upd2/final
- NIST SP 800-53 (controles): https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- OWASP GenAI: https://genai.owasp.org/

**Decisión:** pendiente de análisis de casos de uso y tests.
