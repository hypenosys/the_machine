# Contrato de tareas y tablero de The Machine

## Fuente canónica

Las tareas de trabajo de THE MACHINE se registran como **GitHub Issues** en este repositorio. Una issue es la unidad de trabajo canónica: su número, URL, estado, personas asignadas, etiquetas y fecha de actualización son la evidencia operativa.

El dashboard de `dev.hypenosys.com` consume esas issues como una proyección de solo lectura:

- issue abierta → tarea activa;
- issue cerrada → tarea archivada;
- pull requests no se convierten en tareas;
- los cambios de estado, asignación o contenido se realizan en la issue, nunca en una copia del dashboard.

## Trazabilidad

Cada tarjeta proyectada conserva el repositorio `hypenosys/the_machine`, el número y enlace de la issue, sus etiquetas, responsables y última actualización. Cuando una issue contiene una checklist Markdown, el dashboard la muestra como subtareas; su avance se calcula a partir de esas casillas, sin declarar verificación adicional.

Esta integración no modifica el estado de gobernanza del proyecto ni autoriza código, ejecución, despliegue, CI ni permisos reservados. Es una vista de coordinación documental compatible con el estado HOLD / NO-GO.

## Operación

1. Crear o actualizar una issue en este repositorio.
2. Etiquetarla y asignarla cuando corresponda.
3. Abrir el espacio **The Machine** en `dev.hypenosys.com`.
4. Seguir el enlace de la tarjeta para cualquier edición o decisión con efecto operativo.

Si la lectura de GitHub falla, el dashboard debe mostrar el error y no sustituir las issues por tareas locales.