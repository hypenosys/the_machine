# ADR-0004 — Pasarela de acciones autorizadas

**Estado: Proposed · Fecha: 2026-10-21**

## Explicación sencilla
Que una IA recomiende apagar una máquina no significa que tenga permiso para apagarla.

## Decisión propuesta
Separar `ActionProposal` de `AuthorizationDecision` y de `ExecutionReceipt`. Una propuesta del modelo es dato no confiable. El gateway valida identidad del solicitante, permiso, objetivo, parámetros, expiración, contexto, presupuesto y aprobación adicional si procede. Los efectos se ejecutan solo tras una decisión válida.

## Invariantes
INV-012 el modelo no puede concederse permisos.
INV-013 el permiso se verifica inmediatamente antes del efecto.
INV-014 acciones repetidas no duplican efectos irreversibles; exigir idempotencia o intervención humana.
INV-015 revocación y expiración impiden nuevas ejecuciones.
INV-016 ante caída del motor de políticas, denegar.

## Amenazas
TH-002 escalada; TH-003 abuso; TH-010 TOCTOU; TH-011 replay; TH-012 confused deputy.

## Alternativas
Autorización en prompt (rechazada); comprobaciones dispersas por herramienta (difícil auditar); pasarela central de políticas con contratos tipados (propuesta).

## Verificación
Pruebas negativas por cada permiso, expiración, revocación, replay, reinicio, error de herramienta, doble solicitud y política inaccesible. Ninguna acción física de riesgo en pruebas iniciales.
