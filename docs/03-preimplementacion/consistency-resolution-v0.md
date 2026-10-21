# Resolución propuesta de hallazgos CONS-001..010

**Estado: revisión documental; sin validación experimental.**

| Hallazgo | Resolución de diseño | Estado |
|---|---|---|
| CONS-001 | Temperatura pasa a perfil; Claim es entidad del núcleo | RESUELTO EN PROPUESTA |
| CONS-002 | Compatibilidad numérica y soporte epistemológico tienen resultados separados | RESUELTO EN PROPUESTA |
| CONS-003 | Lectura de entrada y salida de prueba son E/S locales; prohibidos red y acciones externas, no se promete ausencia total de efectos | RESUELTO EN PROPUESTA |
| CONS-004 | Procedencia declarada y autenticación verificable son campos y procesos distintos | RESUELTO EN PROPUESTA |
| CONS-005 | Separar valid_time, recorded_time y assessed_time; formato exacto pendiente | PARCIAL |
| CONS-006 | Dependencia desconocida no equivale a independencia | RESUELTO EN PROPUESTA |
| CONS-007 | SUPPORTED solo tiene sentido relativo a regla, evidencia y alcance | RESUELTO EN PROPUESTA |
| CONS-008 | Cuantificadores complejos fuera del v0; abstención si no representable | RESUELTO EN PROPUESTA |
| CONS-009 | Rechazo atómico se limita al perfil que lo especifique | RESUELTO EN PROPUESTA |
| CONS-010 | «Design freeze» es candidato histórico, no congelación aprobada | RESUELTO EN PROPUESTA |

**Interpretación:** RESUELTO EN PROPUESTA no equivale a aceptación independiente ni a verificación. Se revisaron los diez hallazgos registrados, no se afirma cobertura exhaustiva del repositorio.

## Riesgo abierto relevante
La estructura conceptual todavía no define la forma serializada, la semántica formal de los predicados ni los límites de memoria/CPU. El primer experimento debe probar un subconjunto, no fingir soporte general.
