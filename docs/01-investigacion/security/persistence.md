# SEC-RSCH-006 — Persistencia, integridad y recuperación

**Estado: investigación preliminar; sin benchmark.**

## Pregunta
¿Cómo almacenar evidencia y acciones sin perder integridad tras un crash, sin bloquear borrados legítimos y sin duplicar efectos externos?

## Alternativas
| Enfoque | Ventaja | Riesgo o coste |
|---|---|---|
| Archivos con escritura atómica | Bootstrap simple | Transacciones y recuperación complejas |
| SQLite | Transacciones embebidas y WAL | Dependencia y configuración de durabilidad |
| PostgreSQL | Concurrencia, transacciones y operación madura | Servicio adicional y mantenimiento |
| Event log propio | Control del formato | Alto riesgo de bugs de durabilidad; no recomendado sin pruebas exhaustivas |

## Experimentos propuestos
Cortar el proceso durante escrituras, repetir eventos, restaurar snapshot, migrar esquema y solicitar borrado de registros con índices derivados. Medir consistencia, pérdida y tiempo de recuperación. Probar en filesystem real y configuración documentada.

## Precauciones
WAL no equivale a backups; un commit local no asegura exactamente una ejecución remota; el cifrado de datos en reposo exige resolver claves y rotación.

## Referencias
- SQLite atomic commit: https://www.sqlite.org/atomiccommit.html
- SQLite WAL: https://www.sqlite.org/wal.html
- PostgreSQL WAL: https://www.postgresql.org/docs/current/wal-intro.html

**Decisión:** pendiente; no inventar un motor de almacenamiento propio para evitar dependencias.
