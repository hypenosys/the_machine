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
