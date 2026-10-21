# ADR-0001 — Seguridad desde el inicio y límites de confianza

**Estado: Proposed · Fecha: 2026-10-21**

## Explicación sencilla
Una IA puede leer un documento malicioso. Ese documento no debe convertirse en una orden para el ordenador.

## Contexto
THE MACHINE procesará fuentes, modelos y herramientas con diferentes grados de confianza. La frontera crítica separa **datos que se pueden leer** de **autoridad para actuar**.

## Decisión propuesta
- Núcleo Rust pequeño, sin red ni acciones externas por defecto.
- Tratar datos externos, salidas de modelos, documentos y sensores como no confiables.
- Validar tamaño, formato, propósito y procedencia en la entrada.
- Políticas de autorización evaluadas por código determinista separado del modelo.
- Aislamiento por capacidades, mínimos privilegios y denegación ante fallos.
- Ningún conector nuevo sin inventario de superficie de ataque y tests negativos.

## Alternativas
1. Confiar en instrucciones del modelo: rechazada como base de seguridad, susceptible a prompt injection.
2. Conceder permisos amplios al proceso: rechazada por impacto de compromiso.
3. Núcleo aislado y adaptadores restringidos: propuesta; añade complejidad de contratos.

## Invariantes
INV-001 ningún dato externo concede permisos.
INV-002 ausencia de permiso implica denegación.
INV-003 los fallos de validación no producen efectos externos.
INV-004 las acciones sensibles requieren política y aprobación independiente.

## Amenazas
TH-001 prompt injection; TH-002 escalada de privilegios; TH-003 abuso de herramientas; TH-004 exfiltración; TH-005 denegación de servicio.

## Verificación requerida
Pruebas de permisos ausentes, documento malicioso, input sobredimensionado, conector comprometido, revocación y fallo del motor de políticas. **Sin resultados aún.**

## Riesgos residuales
Bugs en parsers, kernel, sistema operativo y políticas; ataques laterales. No prometer aislamiento perfecto.
