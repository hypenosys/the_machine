# Experimentos de seguridad — protocolo previo a la ejecución

**Todos los experimentos están PLANIFICADOS, ninguno ejecutado.**

| ID | Hipótesis falsable | Métrica | Bloquea |
|---|---|---|---|
| EXP-SEC-001 | El sandbox impide lectura de un archivo no autorizado | intentos permitidos/denegados | ADR-0001 |
| EXP-SEC-002 | El adaptador sin permiso no puede abrir conexión externa | intentos permitidos/denegados | ADR-0001 |
| EXP-SEC-003 | La política rechaza privilegios falsificados | decisiones erróneas | ADR-0004 |
| EXP-SEC-004 | Una revocación previa al efecto impide ejecutarlo | efectos no autorizados | ADR-0004 |
| EXP-SEC-005 | La persistencia recupera o detecta una escritura truncada | pérdida/corrupción | ADR-0005 |
| EXP-SEC-006 | Reintentos no duplican efectos con idempotencia | número de efectos | ADR-0004/0005 |
| EXP-SEC-007 | La revisión bloquea una dependencia no aprobada | entregas bloqueadas | ADR-0002 |
| EXP-SEC-008 | Los registros redactados no filtran secretos sintéticos | coincidencias en logs | ADR-0005 |

## Condiciones para ejecutar
Entorno aislado, datos sintéticos, autorización, límites de recursos, plataforma declarada, scripts reproducibles y un criterio de salida. Registrar resultados negativos y no probar contra servicios ajenos.

## Criterio de aprobación
Un experimento favorable informa una decisión, pero no demuestra ausencia de vulnerabilidades. Repetir en sistemas operativos y versiones relevantes.
