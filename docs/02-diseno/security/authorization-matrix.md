# Matriz de autorización v0

**Estado: propuesta; denegar por defecto.** Un rol describe un contexto de autorización, no un privilegio automático.

| Operación | Lector sin sesión | Usuario autenticado | Operador autorizado | Modelo IA | Conector |
|---|---|---|---|---|---|
| Leer documentación pública | Permitir | Permitir | Permitir | Datos | Datos |
| Leer datos privados propios | Denegar | Condicional: dueño + finalidad | Condicional: alcance | Denegar | Denegar salvo capacidad delegada |
| Ingerir fuente externa | Denegar | Condicional: cuota + procedencia | Condicional | Proponer solamente | Condicional: capacidad limitada |
| Modificar conocimiento | Denegar | Proponer/corregir | Condicional: revisión | Proponer solamente | Proponer solamente |
| Ejecutar acción externa | Denegar | Condicional: permiso específico | Condicional: aprobación y política | Denegar | Solo token de capacidad de corto alcance |
| Leer secretos | Denegar | Denegar | Solo función autorizada | Denegar | Denegar |
| Cambiar políticas | Denegar | Denegar | Separación de deberes | Denegar | Denegar |
| Borrar datos | Denegar | Condicional: titular + verificación | Condicional: obligación y auditoría | Denegar | Denegar |

## Contrato de decisión
Actor autenticado, recurso, operación, propósito, alcance, caducidad, condiciones, identificador de solicitud, versión de política, decisión y motivo. No confiar en roles declarados por texto.

## Fallos
Política no disponible, identidad ambigua, permiso caducado, petición duplicada o recurso distinto → **DENY**. Las acciones sensibles requieren verificación adicional según el riesgo.

## No resuelto
Modelo concreto de identidad, autenticación, delegación, separación de deberes y gestión de claves. No implementar permisos con una lista textual de roles.

## Aclaración de alcance — idempotencia y separación de deberes (propuesta, 23-10-2026)

La fila «Cambiar políticas → Separación de deberes» expresa un **requisito de diseño**, no un control operativo ya implantado ni una autorización a un operador para cambiar políticas. La identidad efectiva del proponente y del aprobador, su independencia, el inventario de operaciones sensibles, la vigencia y el alcance de la aprobación permanecen **sin resolver**. Una misma persona con dos cuentas o una delegación que no preserve independencia no satisface automáticamente la separación. La falta de identidad verificable o de aprobación válida se trata como denegación por defecto; el detalle del oráculo sigue propuesto.

La fila «Ejecutar acción externa → Condicional» **no** implica ejecución exactamente una vez, idempotencia remota ni permiso para experimentar. La deduplicación por identificador de solicitud solo puede evaluarse en un alcance explícito; un resultado remoto incierto no autoriza reintentos ciegos. La condición de autorización y la condición de no duplicación de efectos son independientes y ambas deben cumplirse cuando proceda.

Los criterios falsables candidatos se desarrollan en [el análisis de idempotencia y separación de deberes](../../04-auditorias/pr33-falsifiable-idempotency-and-separation-contracts-2026-10-23.md). Este enlace es **informativo y no normativo**: ni los oráculos propuestos ni esta aclaración alteran los ADR `Proposed`, ratifican `SEC-REQ-010/016` o conceden `AUT-CODE`, `AUT-EXEC` o `AUT-MERGE`. Sigue **HOLD / NO-GO**.
