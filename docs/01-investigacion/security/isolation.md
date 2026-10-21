# SEC-RSCH-001 — Aislamiento local y límites de confianza

**Estado: investigación preliminar; sin pruebas.**

## Pregunta
¿Cómo ejecutar parsers, modelos y conectores no confiables minimizando acceso a archivos, red, procesos y secretos?

## Opciones a comparar
| Opción | Ventaja potencial | Límite o riesgo |
|---|---|---|
| Proceso sin privilegios | Bajo coste | Comparte kernel y permisos del usuario |
| Linux namespaces + seccomp + LSM | Restricciones por recurso y syscall | Configuración compleja; soporte según host |
| Landlock (Linux) | Restricciones de acceso a recursos del proceso | Disponibilidad por versión de kernel y cobertura variable |
| Sandbox del SO (Windows/macOS) | Integración nativa | Semánticas y APIs distintas |
| VM aislada | Límite de aislamiento más fuerte en muchos escenarios | Mayor consumo y operación |

**Advertencia:** contenedores no son automáticamente fronteras equivalentes a VM; seccomp no sustituye control de acceso a archivos ni red.

## Diseño experimental propuesto
Ejecutar un adaptador sintético que intente: leer un archivo no autorizado, abrir un socket, crear procesos, agotar memoria y escapar de su directorio. Registrar qué operaciones deniega cada configuración y en qué plataforma. Nunca realizar estas pruebas contra terceros.

## Criterios
Permisos efectivos, recuperación, latencia, memoria, portabilidad, mantenimiento, superficie de escape y compatibilidad con Rust.

## Fuentes primarias para contrastar
- Linux seccomp: https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html
- Linux Landlock: https://docs.kernel.org/userspace-api/landlock.html
- Microsoft AppContainer: https://learn.microsoft.com/en-us/windows/win32/secauthz/appcontainer-isolation
- Apple App Sandbox: https://developer.apple.com/documentation/security/app-sandbox

**Decisión:** pendiente de resultados y matriz por sistema operativo.
