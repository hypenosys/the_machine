# Registro de riesgos v0

**Escalas propuestas:** Probabilidad (P) 1–5; Impacto (I) 1–5; exposición preliminar P×I. **No es una medición empírica** ni una clasificación CVSS. Recalibrar con contexto y evidencia. Propietarios pendientes de designar.

| ID | Escenario | P | I | Score | Mitigación propuesta | Estado |
|---|---|---:|---:|---:|---|---|
| R-01 | Prompt injection provoca ejecución | 4 | 5 | 20 | modelo sin autoridad; gateway | Abierto |
| R-02 | Conector extrae datos sensibles | 3 | 5 | 15 | capacidades y egress limitado | Abierto |
| R-03 | Dependencia maliciosa compromete build | 3 | 5 | 15 | revisión transitiva y builds aislados | Abierto |
| R-04 | Falsificación contamina memoria | 4 | 4 | 16 | procedencia, cuarentena, corrección | Abierto |
| R-05 | Replay duplica acción externa | 3 | 5 | 15 | idempotencia, caducidad, journal | Abierto |
| R-06 | Fallo de energía corrompe eventos | 3 | 4 | 12 | atomicidad y recuperación | Abierto |
| R-07 | Auditoría filtra secretos | 3 | 5 | 15 | redacción, control de acceso | Abierto |
| R-08 | Borrado incompleto retiene datos | 3 | 4 | 12 | ciclo de vida y pruebas de supresión | Abierto |
| R-09 | Entrada enorme agota recursos | 4 | 4 | 16 | límites y cancelación | Abierto |
| R-10 | Error de política eleva privilegios | 3 | 5 | 15 | pruebas negativas y revisión independiente | Abierto |

## Tratamiento
Cada riesgo debe tener propietario, escenario de abuso reproducible, requisito de control, test, evidencia, riesgo residual y fecha de revisión. El riesgo no se cierra solo por aprobar un ADR.

## Criterio de bloqueo propuesto
Ningún conector con efectos externos se habilita si quedan riesgos críticos o altos sin mitigación verificada o aceptación explícita y justificada por responsable autorizado. La aceptación nunca sustituye obligaciones legales.
