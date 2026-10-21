# Backlog de investigación de seguridad — Prioridad por exposición

**Estado: propuesta.** Antes de elegir bibliotecas o escribir conectores:

## P0 — Bloqueantes
1. **SEC-RSCH-001:** comparar mecanismos de aislamiento local de procesos y capacidades para Linux/Windows/macOS; límites y bypass conocidos.
2. **SEC-RSCH-002:** estudiar identidad, autenticación, autorización y delegación; comparar modelos RBAC/ABAC/capabilities.
3. **SEC-RSCH-003:** evaluar el ciclo completo de una acción externa: TOCTOU, idempotencia, reintentos, revocación, journal.
4. **SEC-RSCH-004:** estudiar prompt injection y abuso de herramientas; evaluar defensa determinista fuera del modelo.
5. **SEC-RSCH-005:** revisar seguridad de parsers y límites de recursos ante documentos no confiables.

## P1 — Antes de persistir datos reales
6. **SEC-RSCH-006:** evaluar persistencia transaccional, recuperación, snapshots y pruebas de crash.
7. **SEC-RSCH-007:** estudiar cifrado y gestión de claves con implementaciones auditadas.
8. **SEC-RSCH-008:** diseñar minimización, retención, supresión y auditoría sin filtraciones.
9. **SEC-RSCH-009:** definir supply-chain: pinning, lockfile, advisories, licencias, SBOM y reproducibilidad.
10. **SEC-RSCH-010:** threat modeling de modelos locales, artefactos y conectores.

## P2 — Antes de distribución o federación
11. **SEC-RSCH-011:** identidad entre nodos, autenticación mutua, replay y particiones.
12. **SEC-RSCH-012:** actualizaciones firmadas, rollback y rotación de confianza.
13. **SEC-RSCH-013:** ensayos de respuesta a incidentes y recuperación operacional.

## Método
Cada investigación entregará fuentes primarias, alternativas, experimento mínimo, resultados negativos, implicaciones de licencias y una recomendación que pueda refutarse.
