# Modelo de amenazas v0 — STRIDE + abuso de IA

**Estado: Proposed; revisión independiente pendiente.**

## Activos
Credenciales, datos, procedencia, integridad de memoria, autoridad de herramientas, modelos, auditoría, dispositivos y disponibilidad.

## Límites de confianza
TB-01 usuario → interfaz; TB-02 fuentes externas → ingestión; TB-03 modelos → propuestas; TB-04 propuesta → política; TB-05 política → ejecutor; TB-06 núcleo → persistencia; TB-07 nodo → nodo (futuro); TB-08 cadena de suministro → binario.

## Amenazas priorizadas
| ID | Amenaza | Impacto | Control inicial |
|---|---|---|---|
| TH-001 | Prompt injection | Alto | Datos no conceden autoridad |
| TH-002 | Escalada de privilegios | Crítico | Capabilities, deny-by-default |
| TH-003 | Abuso de herramientas | Alto | Gateway tipado, allowlist |
| TH-004 | Exfiltración | Crítico | Red desactivada, egress restringido |
| TH-005 | DoS / consumo ilimitado | Alto | Límites de tiempo y tamaño |
| TH-006 | Memory poisoning | Alto | Procedencia, revisión de confianza |
| TH-007 | Suplantación de fuente | Alto | Autenticación de origen donde proceda |
| TH-008 | Contradicción oculta | Medio | Eventos inmutables y vistas revisables |
| TH-009 | Retención indebida | Alto | Minimización, borrado, caducidad |
| TH-010 | TOCTOU | Alto | Revalidación previa al efecto |
| TH-011 | Replay | Alto | Nonce/idempotency y caducidad |
| TH-012 | Confused deputy | Alto | Permisos vinculados a actor y recurso |
| TH-013 | Corrupción de almacenamiento | Alto | Checks, snapshots, recuperación |
| TH-014 | Pérdida de energía | Alto | Crash-consistency y pruebas |
| TH-015 | Logs sensibles | Alto | Redacción y control de acceso |
| TH-016 | Backup irrecuperable | Alto | Ensayos periódicos de restauración |
| TH-017 | Retención fuera de plazo | Alto | Política y propagación de borrado |
| TH-018 | Dependencia comprometida | Crítico | Auditoría transitiva y builds offline |
| TH-019 | Insider abuse | Alto | Separación de deberes y auditoría |
| TH-020 | Modelo comprometido | Alto | Sandbox y salida no confiable |

## Pendientes antes de implementar conectores
Diagramas de flujo de datos, matriz de permisos, severidad con escenarios concretos, propietario de cada riesgo, mitigaciones verificables, pruebas negativas, respuesta a incidentes y revisión legal. La tabla es un punto de partida, **no una certificación**.

## Referencias de partida
NIST AI RMF https://www.nist.gov/itl/ai-risk-management-framework
OWASP GenAI Security https://genai.owasp.org/
MITRE ATLAS https://atlas.mitre.org/
