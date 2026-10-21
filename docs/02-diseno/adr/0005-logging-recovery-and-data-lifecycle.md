# ADR-0005 — Auditoría, recuperación y ciclo de vida

**Estado: Proposed · Fecha: 2026-10-21**

## Explicación sencilla
Después de un apagón necesitamos saber qué se guardó, qué quedó a medias y qué nunca llegó a ejecutarse.

## Decisión propuesta
Evaluar event log tipado y versionado, snapshots consistentes, backups cifrados y pruebas de restauración. Separar eventos de auditoría de datos sensibles. Definir retención, rectificación, supresión y minimización antes de persistir información. No afirmar resistencia a manipulación hasta implementar integridad criptográfica y validar la gestión de claves.

## Invariantes
INV-017 reiniciar no debe repetir efectos externos.
INV-018 no declarar éxito sin recibo verificable.
INV-019 las operaciones de borrado autorizadas se propagan a índices, caches y copias conforme a política.
INV-020 las migraciones permiten recuperar o abortar sin corrupción silenciosa.

## Amenazas
TH-013 corrupción parcial; TH-014 pérdida de energía; TH-015 filtración de logs; TH-016 backup no restaurable; TH-017 retención indebida.

## Alternativas
Archivos planos sin journal (insuficientes para durabilidad avanzada); SQLite/PostgreSQL (dependencias y operación); log propio (requiere exhaustiva validación). Ninguna opción seleccionada aún.

## Verificación
Inyección de fallos, escritura interrumpida, restauración, replay, retención y borrado, rotación de claves y revisión de permisos de backup. Pendiente.
