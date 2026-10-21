# THE MACHINE

**Plataforma local de investigación, evaluación de evidencia e ingeniería asistida por inteligencia artificial.**

---

## 1. Identidad y propósito

### ¿Qué es THE MACHINE?
**THE MACHINE** es un proyecto de software libre en fase de **diseño y preimplementación** concebido para construir un laboratorio local (*Local-First*), seguro y determinista para el análisis de información, la verificación de procedencia y la automatización asistida por modelos de lenguaje (LLM/IA).

### ¿Qué problema pretende resolver?
Los sistemas actuales de inteligencia artificial operan frecuentemente como "cajas negras" opacas:
- Combinan en un mismo flujo datos no confiables con capacidad de ejecución de herramientas (*Excessive Agency*).
- Presentan alucinaciones o afirmaciones sin respaldo como certezas verificadas.
- Carecen de un registro inmutable de procedencia y trazabilidad que permita auditar por qué se tomó una decisión.

THE MACHINE aborda este problema separando de forma estricta la **propuesta de un modelo** de la **autorización de una acción**, y exigiendo que todo conocimiento almacenado esté vinculado a datos primarios inmutables (*Evidence-First*).

### Principios operativos
1. **Evidence-First**: Ninguna afirmación sin evidencia verificable y rastreable.
2. **Zero Fabrication**: Prohibido inventar datos, pruebas, fuentes o certificaciones.
3. **Security by Design**: Límites de confianza estrictos y denegación por defecto (*deny-by-default*).
4. **Local-First**: Operabilidad completa sin conexión a red, garantizando privacidad y soberanía de datos.
5. **Rust-First, no dogmático**: Uso de Rust para garantizar seguridad de memoria, rendimiento y minimización paranoica de dependencias.

### ¿Qué NO es y qué todavía NO hace?
- **NO es un producto en producción**: Se encuentra en fase de preimplementación teórica.
- **NO contiene código ejecutable en Rust**: No existen archivos `.rs` compilados ni binarios distribuidos.
- **NO ejecuta acciones autónomas en el sistema operativo**: El pasarela de acciones (*Action Gateway*) está diseñada pero no codificada.
- **NO reemplaza la revisión humana**: Asiste en la estructuración de evidencia, no sustituye la responsabilidad del usuario.

---

## 2. Estado real del proyecto (Cuatro Dimensiones)

El estado del proyecto se evalúa con rigor mediante la auditoría integral de octubre de 2026 (`docs/04-auditorias/`):

| Dimensión / Área | Estado Documentado | Estado Implementado | Estado Verificado | Estado Real / Dictamen |
|---|---|---|---|---|
| **Investigación** | Completo | N/A (Teórico) | Verificado (Red aislada) | **Sólido / Fundamentado** |
| **Arquitectura** | Candidato v0 | 0% (Sin código) | 0% (Sin prototipo) | **En Rediseño (Opción B)** |
| **Seguridad** | Modelo STRIDE v0 | 0% (Sin código) | 0% (Sin ejecutable) | **Diseñado / 3 Brechas en P1** |
| **Gobernanza / Licencia** | Incompleto | N/A | 0% (Falta LICENSE) | **Bloqueante P0 (GAP-001)** |
| **Código Rust** | No iniciado | 0% (Zero `.rs`) | 0% (Zero tests) | **No Iniciado (Deliberado)** |
| **CI / CD** | Inexistente | 0% (Sin workflows) | 0% (Sin runner) | **Pendiente de Infraestructura** |
| **Preparación Prototipo**| Evaluado | N/A | Evaluado en Gates | **CONDITIONAL GO (Offline)** |

---

## 3. Arquitectura candidata

La arquitectura de THE MACHINE se estructura en tres capas principales:

```
+-------------------------------------------------------------------+
|                        Entorno del Usuario                        |
|                  Interfaz CLI / Visualización                     |
+-------------------------------------------------------------------+
                                  | (TB-01)
                                  v
+-------------------------------------------------------------------+
|               Núcleo Epistemológico de Procedencia                |
|  Primitivas: Artifact (Datos Hash) + Attestation (Firmas/Tiempo)  |
+-------------------------------------------------------------------+
                                  | (TB-03/TB-04)
                                  v
+-------------------------------------------------------------------+
|            Pasarela de Acciones (Action Gateway)                  |
|     Verificación de Capacidades / Evaluador de Políticas          |
+-------------------------------------------------------------------+
```

- **Núcleo de Procedencia (Rediseño Opción B)**: Abstracción mínima inmutable que registra *Artifacts* (archivos con hash BLAKE3) y *Attestations* (afirmaciones firmadas con marcas bitemporales: *Valid Time* vs. *Transaction Time*).
- **Pasarela de Acciones (Action Gateway - ADR-0004)**: Componente que intercepta cualquier petición de ejecución de herramientas emitida por un modelo o script, aplicando políticas de seguridad *deny-by-default*.

*Nota de transparencia*: Las 6 abstracciones ontológicas complejas (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`) están siendo simplificadas tras la auditoría técnica para evitar sobreingeniería.

---

## 4. Cómo empezar y rutas de lectura

El repositorio ofrece itinerarios adaptados al perfil del lector:

### Ruta 1: Para personas interesadas en filosofía y concepto (Sin código)
1. Lee [`PHILOSOPHY.md`](PHILOSOPHY.md) para comprender la visión y valores del proyecto.
2. Explora [`docs/00-empezar/itinerario.md`](docs/00-empezar/itinerario.md) para una introducción paso a paso.
3. Consulta [`GLOSSARY.md`](GLOSSARY.md) para familiarizarte con los términos técnicos.

### Ruta 2: Para investigadores y arquitectos de software
1. Examina el informe ejecutivo de auditoría en [`docs/04-auditorias/auditoria-integral-2026-10.md`](docs/04-auditorias/auditoria-integral-2026-10.md).
2. Lee la evaluación de arquitectura y alternativas en [`docs/04-auditorias/architecture-review.md`](docs/04-auditorias/architecture-review.md).
3. Revisa los Registros de Decisiones de Arquitectura en [`docs/02-diseno/adr/`](docs/02-diseno/adr/).

### Ruta 3: Para especialistas en ciberseguridad
1. Consulta la matriz de seguridad y amenazas en [`docs/04-auditorias/security-review.md`](docs/04-auditorias/security-review.md).
2. Analiza el Modelo de Amenazas STRIDE en [`docs/02-diseno/security/threat-model-v0.md`](docs/02-diseno/security/threat-model-v0.md).
3. Revisa los Requisitos Verificables en [`docs/02-diseno/security/requirements.md`](docs/02-diseno/security/requirements.md).

---

## 5. Índice de documentación vigente y auditorías

Toda la documentación técnica está organizada en el directorio `docs/`:

- **`docs/00-empezar/`**: Guías de inicio, conceptos pedagógicos e itinerarios de lectura.
- **`docs/01-investigacion/`**: Estudios preliminares de aislamiento, autorización, persistencia y cadena de suministro en Rust.
- **`docs/02-diseno/`**: Modelo de amenazas, diagramas de flujo de datos (DFD), requisitos de seguridad y registros ADR-0001 a ADR-0005.
- **`docs/03-preimplementacion/`**: Especificaciones candidatas, análisis de consistencia, casos de aceptación y reflexiones previas a la fase de código.
- **`docs/04-auditorias/`**: **Informes de auditoría integral de octubre de 2026**:
  - `auditoria-integral-2026-10.md`: Informe ejecutivo consolidado.
  - `gap-register.md`: Registro de las 10 brechas priorizadas (GAP-001 a GAP-010).
  - `architecture-review.md`: Evaluación de alternativas (A, B, C, D) y simplificación del núcleo.
  - `security-review.md`: Matriz de trazabilidad de seguridad y estado en 4 dimensiones.
  - `research-evidence.md`: Fuentes y evidencias de estándares (NIST, OWASP, MITRE, SLSA, W3C).
  - `readiness-assessment.md`: Evaluación de Readiness Gates (G0-G5) y veredicto CONDITIONAL GO.

---

## 6. Estado de seguridad y modelo de amenazas

La seguridad en THE MACHINE no es una capa posterior, sino el requisito de diseño primario (`ADR-0001`):

- **Modelado de amenazas**: 20 amenazas catalogadas (`TH-001` a `TH-020`) abarcando prompt injection, confused deputy, exfiltración, escalada de privilegios y corrupción de almacenamiento.
- **Requisitos de seguridad**: 17 requisitos verificables (`SEC-REQ-001` a `SEC-REQ-017`).
- **Límites de red**: Sockets de red totalmente desactivados por defecto (`Local-First`).
- **Cadena de suministro**: Política de minimización paranoica de dependencias en Rust (`ADR-0002`).

*Estado real de verificación*: Todos los controles se encuentran actualmente en estado **Diseñado** (0% implementado / 0% verificado en binarios), pendiente del inicio de la fase de código.

---

## 7. Principales limitaciones y brechas identificadas (Gap Analysis)

La auditoría independiente ha identificado 10 brechas principales que deben ser resueltas antes del prototipo:

1. **GAP-001 (P0 - Critical)**: Ausencia del archivo de licencia legal (`LICENSE`) en la raíz del repositorio.
2. **GAP-002 (P1 - High)**: Faltan especificaciones de prueba asignadas para las amenazas TH-012, TH-016 y TH-019.
3. **GAP-003 (P1 - High)**: Falta de semántica bitemporal (*Valid Time* vs *Transaction Time*) en el registro de evidencias.
4. **GAP-004 (P1 - High)**: Indefinición del mecanismo de firma/integridad para las capacidades almacenadas en la base de datos local.
5. **GAP-005 (P1 - High)**: Los 5 ADRs permanecen en estado `Proposed` sin procedimiento formal de aprobación.

El registro completo con los 10 hallazgos y sus criterios de cierre se encuentra en [`docs/04-auditorias/gap-register.md`](docs/04-auditorias/gap-register.md).

---

## 8. Próximos hitos y hoja de ruta

El desarrollo avanza según la siguiente secuencia condicionada:

1. **Hito 1: Gobernanza y Licencia (P0)**: Incorporar el archivo `LICENSE` (Dual MIT / Apache-2.0) y formalizar la adopción de los ADRs principales.
2. **Hito 2: Simplificación Arquitectónica (P1)**: Aprobar el rediseño del núcleo mínimo de procedencia (Opción B) e incorporar la especificación bitemporal.
3. **Hito 3: Cierre de Brechas de Seguridad (P1)**: Completar la asignación de pruebas en la matriz de seguridad.
4. **Hito 4: Primer Prototipo Offline (Vertical Slice A)**: Implementar en Rust el experimento de prueba de concepto desconectado (dos sensores contradictorios) cumpliendo el veredicto CONDITIONAL GO.

---

## 9. Contribución y gobernanza

Agradecemos las contribuciones de la comunidad en forma de revisión crítica de arquitectura, modelos de seguridad y documentación.

- Para conocer las pautas de participación, lee [`CONTRIBUTING.md`](CONTRIBUTING.md).
- Toda propuesta de cambio arquitectónico debe presentarse en formato ADR siguiendo la plantilla [`docs/02-diseno/adr/TEMPLATE.md`](docs/02-diseno/adr/TEMPLATE.md).
- No se aceptarán PRs de código funcional en Rust hasta superar formalmente las condiciones del gate G2 de diseño.

---

## 10. Licencia

**Estado actual**: Pendiente de incorporación formal del archivo `LICENSE` en el repositorio (**GAP-001**).
Se propone la adopción de una **Doble Licencia MIT / Apache-2.0**, estándar en el ecosistema de software libre en Rust. Hasta que dicho archivo sea integrado en la raíz del repositorio, el contenido se presenta para revisión y auditoría pública.
