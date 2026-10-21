# Auditoría de seguridad y matriz de amenazas — THE MACHINE

**Fecha de auditoría:** Octubre de 2026
**Auditor independiente:** Security Architect & Application Security Engineer (Jules)
**Estado:** Final / Entregable de Auditoría

---

## 1. Resumen ejecutivo

La presente auditoría de seguridad evalúa el modelo de amenazas, los requisitos de seguridad verificables, la matriz de autorización, los límites de confianza y los mecanismos de trazabilidad documentados para **THE MACHINE**.

El objetivo es determinar si las salvaguardas diseñadas son suficientes para prevenir vulnerabilidades críticas (tales como prompt injection, escalada de privilegios, ejecuciones no autorizadas, confused deputy o suplantación de procedencia) antes de iniciar la fase de código en Rust.

---

## 2. Evaluación de los límites de confianza (Trust Boundaries)

Se analizan los 8 límites de confianza definidos en `docs/02-diseno/security/data-flow-diagrams.md`:

- **TB-01 (Usuario → Interfaz CLI/Local)**:
  *Evaluación*: Correctamente identificado. Requiere sanitización de entradas de terminal para evitar inyecciones de comandos en el shell local.
- **TB-02 (Fuentes externas → Ingestión de datos)**:
  *Evaluación*: Zona de alto riesgo. Toda entrada de datos externos (archivos, APIs) debe tratarse como **no confiable por defecto**.
- **TB-03 (Modelos LLM/IA → Propuestas de acción)**:
  *Evaluación*: **Frontera Crítica**. El texto o estructuras emitidas por modelos de lenguaje NUNCA deben tener autoridad ejecutiva directa.
- **TB-04 (Propuesta → Política de seguridad / Action Gateway)**:
  *Evaluación*: El motor de políticas debe interceptar la propuesta y validar permisos mediante un esquema *deny-by-default*.
- **TB-05 (Política → Pasarela de ejecución)**:
  *Evaluación*: Incompleto. Falta especificar cómo se protege la integridad de la decisión en memoria antes de la ejecución.
- **TB-06 (Kernel → Persistencia local)**:
  *Evaluación*: Presenta la brecha **GAP-004**. Si la base de datos local es modificable por el usuario en disco, no se garantiza la autenticidad de las capacidades almacenadas.
- **TB-07 (Nodo local → Nodo remoto - Futuro)**:
  *Evaluación*: Fuera de alcance del primer prototipo offline.
- **TB-08 (Cadena de suministro Cargo → Binario compilado)**:
  *Evaluación*: Abordado formalmente en ADR-0002. Excelente enfoque de minimización estricta de dependencias.

---

## 3. Matriz integral de trazabilidad: Amenaza → Requisito → Control → Prueba → Evidencia → Brecha → Riesgo Residual

A continuación se detalla la matriz de seguridad construida durante la auditoría:

| Amenaza | Requisito Verificable | Control Propuesto | Prueba | Evidencia Disponible | Brecha Asociada | Riesgo Residual |
|---|---|---|---|---|---|---|
| **TH-001** (Prompt Injection) | `SEC-REQ-001` | Ingestión de datos sin autoridad ejecutiva; parseo estricto | `SEC-001` | Solo especificación teórica | Ninguna | Bajo en prototipo offline |
| **TH-002** (Escalada Privilegios) | `SEC-REQ-002` | Sistema de capacidades tipadas, deny-by-default | `SEC-002` | Solo especificación teórica | Ninguna | Medio (diseño no probado) |
| **TH-003** (Abuso de herramientas) | `SEC-REQ-003` | Action Gateway tipado con allowlist de herramientas | `SEC-003` | Solo especificación teórica | Ninguna | Medio |
| **TH-004** (Exfiltración de datos) | `SEC-REQ-004` | Desactivación total de sockets de red por defecto | `SEC-004` | Solo especificación teórica | Ninguna | Bajo en entorno desconectado |
| **TH-005** (DoS / Límites) | `SEC-REQ-005` | Allocators con límites de memoria y timeouts en IO | `SEC-005` | Solo especificación teórica | Ninguna | Medio |
| **TH-006** (Memory Poisoning) | `SEC-REQ-006` | Preservación de contradicciones sin resolver | `SEC-006` | Solo especificación teórica | GAP-003 | Medio |
| **TH-007** (Suplantación de fuente) | `SEC-REQ-007` | Firmas digitales / hashes verificables de origen | `SEC-007` | Solo especificación teórica | GAP-004 | Medio |
| **TH-008** (Contradicción oculta) | `SEC-REQ-006` | Registro inmutable de eventos de evaluación | `SEC-006` | Solo especificación teórica | Ninguna | Bajo |
| **TH-009** (Retención indebida) | `SEC-REQ-008` | Propagación de borrado en cascada sobre derivados | `SEC-008` | Solo especificación teórica | GAP-003 | Medio |
| **TH-010** (TOCTOU) | `SEC-REQ-009` | Revalidación de tokens/capacidades atomicamente | `SEC-009` | Solo especificación teórica | Ninguna | Medio |
| **TH-011** (Replay Attacks) | `SEC-REQ-010` | Nonces únicos e idempotencia en Action Gateway | `SEC-010` | Solo especificación teórica | Ninguna | Bajo |
| **TH-012** (Confused Deputy) | `SEC-REQ-017` | Vinculación estricta Actor + Recurso + Propósito | **Sin Asignar** | **Ninguna** | **GAP-002** | **Alto (Falta prueba)** |
| **TH-013** (Corrupción persistencia) | `SEC-REQ-011` | Transacciones ACID, checksums de bloque | `SEC-011` | Solo especificación teórica | Ninguna | Medio |
| **TH-014** (Pérdida de energía) | `SEC-REQ-011` | Crash-consistency mediante Write-Ahead Log (WAL) | `SEC-011` | Solo especificación teórica | Ninguna | Medio |
| **TH-015** (Logs con secretos) | `SEC-REQ-012` | Redacción automática e imprevistos filtrados | `SEC-012` | Solo especificación teórica | **GAP-008** | **Alto (Estructura no definida)** |
| **TH-016** (Backup irrecuperable) | `SEC-REQ-015` | Ensayos automatizados de restauración sintética | **Sin Asignar** | **Ninguna** | **GAP-002** | **Alto (Falta prueba)** |
| **TH-017** (Retención fuera plazo) | `SEC-REQ-008` | Tareas programadas de caducidad y trituración | `SEC-008` | Solo especificación teórica | Ninguna | Medio |
| **TH-018** (Dependencia comprometida)| `SEC-REQ-013` | Vendoring, cargo-audit, `#![no_std]` preferente | `SEC-013` | Solo especificación teórica | Ninguna | Bajo (por política de deps) |
| **TH-019** (Insider Abuse) | `SEC-REQ-016` | Separación de deberes y auditoría inalterable | **Sin Asignar** | **Ninguna** | **GAP-002** | **Alto (Falta prueba)** |
| **TH-020** (Modelo comprometido) | `SEC-REQ-014` | Sandbox estricto y salida tratada como propuesta | `SEC-014` | Solo especificación teórica | Ninguna | Bajo (por diseño) |

---

## 4. Estado de la seguridad: Cuatro dimensiones obligatorias

Para cumplir con la regla *Evidence-First*, la seguridad de THE MACHINE se clasifica explícitamente en cuatro estados:

1. **Seguridad Documentada**: **COMPLETA (90%)**. Existe un modelo de amenazas STRIDE exhaustivo (`TH-001` a `TH-020`), requisitos verificables (`SEC-REQ-001` a `SEC-REQ-017`) y diagramas de flujo.
2. **Seguridad Implementada**: **NULA (0%)**. No existe ningún archivo de código Rust, módulo de cifrado ni pasarela de ejecución compilada.
3. **Seguridad Comprobada**: **NULA (0%)**. No se ha ejecutado ninguna prueba negativa ni test adversarial, al no existir binarios compilados.
4. **Seguridad Pendiente**: **CRÍTICA (100%)**. Todos los controles diseñados deben codificarse, someterse a análisis estático, fuzzeo y verificaciones en el sandbox de Rust antes de declarar operativo el sistema.

---

## 5. Recomendaciones priorizadas de seguridad

1. **Resolver GAP-002 antes de codificar**: Asignar e incorporar las especificaciones de prueba `SEC-015`, `SEC-016` y `SEC-017` en el plan de verificación de seguridad.
2. **Especificar integridad en reposo (GAP-004)**: Diseñar la firma criptográfica de las tablas de capacidades almacenadas en la base de datos local para evitar la manipulación offline del Action Gateway.
3. **Definir la estructura de tipos redactados para logs (GAP-008)**: Crear un envoltorio en Rust como `Secret<T>` que impida la impresión accidental de tokens o claves en los registros de auditoría (`Display` / `Debug`).
