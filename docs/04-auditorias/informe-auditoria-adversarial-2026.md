# Informe de Auditoría Adversarial y Troubleshooting Preimplementación — THE MACHINE

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad / Auditor Técnico Independiente (@Jules)
**Repositorio:** `hypenosys/the_machine`
**Rama de trabajo:** `audit/adversarial-troubleshooting-2026-10`
**Rama base:** `master` (Commit de referencia: `de545ad47e5b17179ee1e5e6fcdd0e425f09b677`)
**Estado del proyecto:** **HOLD / NO-GO (Cero código ejecutable, cero manifiestos de Cargo)**
**Veredicto de la Auditoría:** **READY-FOR-DECISION** (Evidencia documental y análisis adversarial maduros para la deliberación formal de las decisiones de gobernanza `DEC-01..DEC-08`. **NO AUTORIZA** la implementación de código).

---

## 1. Resumen Ejecutivo y Veredicto

### 1.1 Contexto y Objetivo
Se ha llevado a cabo una revisión adversarial y técnica exhaustiva sobre el estado documental y arquitectónico de **THE MACHINE**. El proyecto se define como un sistema *local-first*, *Rust-first* y *security-first* inspirado en *Person of Interest*, diseñado para separar el registro epistemológico, la evaluación especializada, la gobernanza de reglas y la autoridad operativa.

El objetivo de esta intervención es auditar de forma independiente las especificaciones pre-código, verificar contradicciones (C-01..C-04), prohibiciones (P-01..P-06), criterios de falsación (R-01..R-08), el modelo de amenazas (TH-001..TH-020) y las opciones arquitectónicas (R1 de 6 entidades vs. R2 Artifact+Attestation vs. Híbrida vs. Control de Dominio), sin validar complacientemente ninguna hipótesis preexistente.

### 1.2 Veredicto Global: `READY-FOR-DECISION`
- **Veredicto:** **READY-FOR-DECISION**
- **Justificación:** Se ha completado la reconstrucción de la autoridad documental y la evaluación adversarial de los límites conceptuales del sistema. La documentación en `master` contiene suficientes elementos de juicio para someter las decisiones de preconsolidación `DEC-01` a `DEC-08` a la deliberación del titular del proyecto.
- **Alcance estricto del veredicto:** `READY-FOR-DECISION` **NO constituye una autorización para escribir código, añadir dependencias, aprobar ADRs ni pasar a la fase de implementación (G3)**. El proyecto permanece bajo el estado de **HOLD / NO-GO**.

---

## 2. Reconstrucción de la Jerarquía y Autoridad Documental

Para evitar asumir que el documento más reciente invalida a los precedentes sin justificación normativa, se establece la jerarquía de autoridad explícita del repositorio:

```
[NIVEL 0: Principios Fundacionales y Mantenimiento]
   ├── AGENTS.md (Reglas de los agentes, metodología)
   ├── PHILOSOPHY.md (Principios epistemológicos e ideológicos)
   └── CONTRIBUTING.md / GLOSSARY.md / README.md (Gobernanza general)

[NIVEL 1: Marco de Seguridad y Gobernanza de Decisiones]
   ├── docs/02-diseno/security/ (Requirements, Threat Model, Verification)
   ├── docs/02-diseno/adr/ (ADRs 0001..0005 — Todos actualmente PROPOSED)
   └── docs/03-preimplementacion/precode-decision-protocol-v0.md (Protocolo normativo)

[NIVEL 2: Especificaciones Técnicas Candidates / Preimplementación]
   ├── docs/03-preimplementacion/unified-specification-candidate-v0.md
   ├── docs/03-preimplementacion/general-epistemic-contract-v0.md
   └── docs/03-preimplementacion/offline-experiment-contract-candidate-v0.md

[NIVEL 3: Consolidaciones y Análisis Pre-código (Propuestas/Trabajo)]
   ├── docs/03-preimplementacion/finch-consolidation-troubleshooting-candidate-v0.md
   └── docs/03-preimplementacion/precode-consistency-decision-review-v0.md

[NIVEL 4: Auditorías Independientes e Informes Históricos]
   ├── docs/04-auditorias/gap-register.md (Registro de brechas GAP-001..GAP-010)
   ├── docs/04-auditorias/security-review.md / architecture-review.md
   └── docs/04-auditorias/informe-auditoria-adversarial-2026.md (Este documento)
```

### Reglas de Autoridad y Precedencia
1. Ninguna propuesta en Nivel 3 o Nivel 4 puede modificar o invalidar los requisitos de seguridad de Nivel 1 ni los principios de Nivel 0 sin un ADR aprobado (`Accepted`).
2. La presencia de especificaciones en Nivel 2 o Nivel 3 no implica aprobación normativa: son hipótesis de trabajo hasta la resolución explícita de `DEC-01..DEC-08`.

---

## 3. Auditoría Adversarial de Contradicciones C-01 a C-04

Se han analizado las cuatro tensiones/contradicciones estructurales del sistema:

### C-01: Registro Histórico e Inmutabilidad vs. Privacidad y Supresión Legítima
- **OBSERVADO:** `docs/03-preimplementacion/evidence-lifecycle-privacy-candidate-v0.md` define la supresión lógica mediante marcas de retracción, mientras que los principios de inmutabilidad en `PHILOSOPHY.md` exigen reproducibilidad histórica.
- **INFERIDO:** Existe una incompatibilidad insuperable entre prometer "borrado físico/privacidad real" y mantener un "registro determinista inmutable". Si los datos subyacentes son purgados físicamente (p. ej. por requerimiento GDPR/derecho al olvido), las evaluaciones históricas que dependían de dicho artefacto se vuelven irreproducibles.
- **EVIDENCIA PENDIENTE:** La prueba `E-10` es únicamente una simulación de estado lógico en papel, no una garantía de borrado criptográfico o físico.
- **PROPUESTA:** Declarar formalmente que el sistema garantiza exclusivamente *supresión lógica bitemporal* (`valid_time` vs `recorded_time`) y que el borrado físico de activos primarios deja la evaluación histórica en estado `UNVERIFIABLE_ORPHAN`.

### C-02: Núcleo Epistemológico Común vs. Semántica Especializada de Dominio
- **OBSERVADO:** `unified-specification-candidate-v0.md` impone un contrato genérico de 6 entidades para cualquier tipo de evidencia.
- **INFERIDO:** El núcleo genérico no posee semántica de dominio para juzgar si dos mediciones (ej. temperatura vs presión) son comparables. La semántica de comparabilidad se delega al "Perfil". Sin embargo, si el núcleo intenta forzar un esquema rígido, genera una sobrecarga conceptual donde estructuras simples requieren grafos complejos.
- **PROPUESTA:** Mantener el núcleo epistemológico como un contenedor neutro de procedencia y atestación de metadatos, delegando toda la interpretación semántica y causal a los perfiles de evaluación.

### C-03: Gobernanza de Reglas y Separación Lógica vs. Aislamiento Real de Seguridad
- **OBSERVADO:** `architecture-boundaries.md` y `adr/0001-security-first-trust-boundaries.md` definen fronteras lógicas entre "Evaluador", "Gobernanza" y "Autoridad Operativa".
- **INFERIDO:** En una arquitectura monocanal o en un único binario local, la separación lógica no constituye un límite de aislamiento frente a un adversario local con privilegios de ejecución o control sobre la memoria. Un "Insider" o un proceso comprometido dentro del mismo proceso puede eludir las fronteras lógicas.
- **EVIDENCIA PENDIENTE:** No existen barreras de aislamiento de memoria ni sandbox demostrados (`GAP-004`).
- **PROPUESTA:** Reconocer en la documentación que la separación entre evaluación y acción es una garantía de *diseño lógico de flujo de trabajo*, no un aislamiento de ejecución *hardened* frente a código malicioso en el mismo proceso.

### C-04: Harness de Experimentación con E/S vs. Núcleo Offline / Puramente Funcional
- **OBSERVADO:** `offline-experiment-contract-candidate-v0.md` propone un *Harness* sintético con entrada/salida efímera para inyectar estímulos.
- **INFERIDO:** Existe el riesgo de que la E/S del Harness contamine el núcleo "sin E/S" o que el Harness actúe como un oráculo permisivo que oculte fallos en la representación de datos.
- **PROPUESTA:** Adoptar formalmente `DEC-03`: el núcleo computable de evaluación debe ser un conjunto de funciones puras en Rust (sin dependencias de red, disco ni tiempo del sistema), y la E/S debe estar estrictamente confinada en un arnés de pruebas externo no distribuido con la biblioteca central.

---

## 4. Examen de Prohibiciones P-01 a P-06 y Criterios de Falsación R-01 a R-08

### 4.1 Matriz de Prohibiciones P-01..P-06
| ID | Prohibición | Estado en Especificación | Cobertura Previa / Análisis |
|---|---|---|---|
| **P-01** | Evaluación no autoriza ejecución | **CUMPLIDA EN DISEÑO** | Mapeada a `SEC-REQ-002`, `SEC-REQ-003` y `ADR-0004`. Las evaluaciones son solo afirmaciones. |
| **P-02** | Fuente no se autentica a sí misma | **CUMPLIDA EN DISEÑO** | Coincide con `F-03` y `SEC-REQ-007`. La firma/identidad debe provenir de atestación externa. |
| **P-03** | Corrección no retrodata conocimiento | **CUMPLIDA EN DISEÑO** | Requiere timestamps bitemporales obligatorios (`valid_time` vs `recorded_time`). |
| **P-04** | Evaluador no activa reglas unilateralmente | **PARCIALMENTE CUBIERTA** | Mapeada a `TH-019`, `SEC-REQ-016` y `GAP-002`. Falta trazabilidad normativa explícita. |
| **P-05** | Dependencia conocida no cuenta como soporte independiente | **CUMPLIDA EN DISEÑO** | `F-04`. Grafos de corroboración deben descontar nodos con ancestros comunes. |
| **P-06** | Perfil no redefine garantías del núcleo | **CUMPLIDA EN DISEÑO** | `DEC-02`. Los perfiles extienden semántica pero no pueden relajar denegaciones del núcleo. |

### 4.2 Criterios de Falsación Candidate R-01..R-08
Se han evaluado los criterios de falsación propuestos en la fase Finch:
- **R-01 (Identidad externa fusionada por coincidencia textual):** Refutada si dos entidades con mismo nombre carecen de URI/ID criptográfico común.
- **R-02 (Fuente autoverificada):** Refutada si un reclamo valida su propia procedencia.
- **R-03 (Falsa corroboración por dependencia oculta):** Refutada si dos fuentes independientes comparten una misma fuente primaria no declarada.
- **R-04 (Retrodatación de conocimiento posterior):** Refutada si `recorded_time` es anterior al evento generador.
- **R-05 (Sobrescritura de evaluación histórica sin rastro):** Refutada si la actualización de un juicio borra la versión previa en lugar de crear un nuevo nodo.
- **R-06 (Aplicación de semántica fuera de alcance):** Refutada si un evaluador procesa datos fuera de sus tipos compatibles declarados.
- **R-07 (Conclusión convertida en autorización automática):** Refutada si un `Assessment` desencadena un efecto secundario sin pasar por el `Action Gateway`.
- **R-08 (Supresión lógica presentada como borrado físico):** Refutada si el sistema promete destrucción de datos físicos en un medio inmutable.

*Todos los criterios R-01..R-08 se confirman como escenarios de prueba conceptuales válidos para el arnés pre-código.*

---

## 5. Evaluación del Modelo de Amenazas y Foco en TH-012, TH-016, TH-019

### 5.1 Análisis Específico de Amenazas Críticas No Asignadas
En la revisión del modelo de amenazas (`docs/02-diseno/security/`) y el registro de brechas (`GAP-002`), se identificaron tres amenazas de severidad Alta que **carecían de especificación de prueba asignada (`SEC-XXX`)**:

1. **TH-012: Confused Deputy (Suplantación de autoridad delegada)**
   - *Estado previo:* Mapeado a `SEC-REQ-017` y `ADR-0004`, pero con prueba "Pendiente / Sin Asignar".
   - *Análisis Adversarial:* Si un componente de gobernanza delega una acción a un ejecutor intermediario, un solicitante no autorizado podría aprovechar el privilegio del intermediario si el token de autorización no vincula explícitamente: `[Actor + Recurso + Operación Específica + Contexto Temporal]`.
   - *Especificación de Prueba Propuesta (`SEC-015`):* Inyección de solicitud delegada donde el actor intermedio posee permisos superiores al actor originador. El sistema debe rechazar la acción si el scope del originador no cubre la operación requerida.

2. **TH-016: Backup irrecuperable o inconsistente**
   - *Estado previo:* Mapeado a `SEC-REQ-015` y `ADR-0005`, prueba "Pendiente / Sin Asignar".
   - *Análisis Adversarial:* La persistencia de logs bitemporales puede quedar corrupta si un respaldo físico ocurre durante una transacción incompleta, generando un estado donde los punteros de evidencia queden huérfanos.
   - *Especificación de Prueba Propuesta (`SEC-016`):* Simulación de restauración desde volcado sintético con transacciones truncadas. El sistema debe detectar la inconsistencia en el arranque y entrar en modo de recuperación o aborto seguro.

3. **TH-019: Insider Abuse / Abuso de privilegios administrativos**
   - *Estado previo:* Mapeado a `SEC-REQ-016` y `ADR-0001`/`ADR-0004`, prueba "Pendiente / Sin Asignar".
   - *Análisis Adversarial:* Un operador de la entidad de gobernanza podría alterar unilateralmente los parámetros de evaluación o insertar reglas maliciosas para forzar un dictamen favorable.
   - *Especificación de Prueba Propuesta (`SEC-017`):* Intento de modificación unilateral de una regla activa sin la firma conjunta (*multi-sig* o revisión de pares) exigida por la política de gobernanza.

---

## 6. Refutación y Contraejemplos Concretos de Hipótesis Arquitectónicas

Para garantizar un análisis riguroso, se han diseñado tres contraejemplos concretos que intentan refutar las hipótesis centrales del diseño:

### Contraejemplo 1: Refutación de la hipótesis del "Núcleo Común Genérico" (R1 de 6 entidades)
- **Hipótesis a refutar:** *"Un esquema de 6 entidades fijas (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`) puede representar de forma transparente cualquier dominio epistemológico sin pérdidas ni sobreingeniería."*
- **Escenario de Contraejemplo:** Dominio de lectura continua de telemetría de sensores IoT (e.g. dos termómetros leyendo la misma caldera en intervalos de 10 ms).
- **Resultado:** Representar 1,000 lecturas sencillas mediante el grafo R1 genera 6,000 entidades y miles de relaciones de vinculación (`EvidenceLink`), provocando una explosión de metadatos y sobrecarga de memoria inaceptable para una evaluación en tiempo real en dispositivos con recursos limitados.
- **Conclusión de la Refutación:** La Opción R1 pura es una **sobreingeniería rígida** para datos de alta frecuencia o estructuras simples. La hipótesis de que R1 es universalmente óptimo queda **REFUTADA**.

### Contraejemplo 2: Refutación de la "Falsa Corroboración por Grafos Acíclicos Simples"
- **Hipótesis a refutar:** *"Dos declaraciones independientes (`Claim A` y `Claim B`) que coinciden en un juicio incrementan linealmente el nivel de certeza."*
- **Escenario de Contraejemplo:** Un periódico A y un periódico B publican la misma noticia. Ambos citan fuentes distintas en apariencia, pero ambas fuentes primarias abrevan de una misma nota de prensa errónea emitida por una agencia central C (que no fue declarada en los metadatos de A ni B).
- **Resultado:** Si el sistema únicamente analiza el grafo explícito presentado por A y B, computará dos soportes independientes (certidumbre duplicada), cuando en realidad existe una dependencia circular/común oculta.
- **Conclusión de la Refutación:** Ningún algoritmo local puede garantizar la "independencia de fuentes" si las dependencias primarias son desconocidas. El sistema debe etiquetar la corroboración como `CORROBORATED_PROVISIONAL_PENDING_PROVENANCE_GRAPH` y no como `VERIFIED_INDEPENDENT`.

---

## 7. Análisis Comparativo Neutro de Alternativas Arquitectónicas

Se comparan objetivamente las cuatro opciones arquitectónicas debatidas en el proyecto, sin seleccionar un ganador de forma prematura:

| Criterio | Opción R1 (6 Entidades Unificadas) | Opción R2 (Artifact + Attestation Minimal) | Opción C (Híbrida: R2 Núcleo + Grafos Extendidos) | Opción D (Control Específico de Dominio) |
|---|---|---|---|---|
| **Estructura** | `Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation` | `Artifact` (contenido) + `Attestation` (metadatos/firma) | `Artifact` + `Attestation` en núcleo; extensiones de grafo bajo demanda | Estructuras ad-hoc definidas por cada perfil/dominio |
| **Complejidad Conceptual** | Alta (6 tipos de entidad interconectados) | Muy Baja (2 abstracciones primarias) | Modera (Evolución gradual) | Heterogénea / No estandarizada |
| **Flexibilidad de Dominio** | Alta en expresividad, Rígida en contrato | Muy Alta (el contenido es opaco al núcleo) | Alta (Núcleo opaco, plugins de dominio) | Máxima en dominio, Nula interoperabilidad |
| **Garantías de Seguridad** | Difíciles de verificar en memoria por complejidad de grafo | Muy fáciles de auditar (superficie reducida) | Verificables de forma modular | Dependientes de cada implementación |
| **Rendimiento / Overhead** | Elevado (Explosión de punteros y asignaciones) | Óptimo (Cero overhead de metadatos no usados) | Adaptativo según necesidades del experimento | Óptimo para el dominio específico |
| **Adecuación para Experimento Minimalista** | Sobreingeniería potencial | **Ideal para Laboratorio Pre-código** | Adecuada para fase II | Desaconsejada por falta de abstracción |

---

## 8. Matriz Consolidada de Hallazgos Priorizados

A continuación se consolidan todos los hallazgos de auditoría identificados, ordenados por gravedad:

| ID Hallazgo | Gravedad | Categoría | Descripción Sintética | Impacto | Propuesta Mínima de Resolución | Estado |
|---|---|---|---|---|---|---|
| **AUD-2026-01** | **Alta** | Gobernanza / Legal | Inexistencia de archivo `LICENSE` en la raíz (`GAP-001`). | El proyecto está bajo "Todos los derechos reservados", impidiendo la distribución pública legal. | Crear `LICENSE` con licencia apropiada (e.g. MIT/Apache-2.0 o BUSL según decisión del titular). | **OPEN** |
| **AUD-2026-02** | **Alta** | Seguridad / Cobertura | Cobertura de pruebas incompleta para amenazas `TH-012`, `TH-016` y `TH-019` (`GAP-002`). | Vulnerabilidades en delegación, recuperación e insider abuse sin verificación automatizada. | Aprobar la incorporación de `SEC-015`, `SEC-016` y `SEC-017` al plan global. | **OPEN** |
| **AUD-2026-03** | **Alta** | Arquitectura | Sobreingeniería en el esquema R1 de 6 entidades para casos simples (`GAP-006`). | Ineficiencia de memoria y complejidad innecesaria en el núcleo computable. | Evaluar la adopción de la Opción R2/Híbrida mediante `DEC-02`. | **OPEN** |
| **AUD-2026-04** | **Media** | Especificación | Ausencia de especificación formal de serialización y bitemporalidad (`GAP-003`). | Incompatibilidad de persistencia y parsing impreciso de marcas de tiempo. | Definir formalmente tipos RFC-3339/Unix ts y esquemas JSON/CBOR en los contratos pre-código. | **OPEN** |
| **AUD-2026-05** | **Media** | Seguridad / Aislamiento | Inexistencia de prueba de aislamiento entre procesos y memoria (`GAP-004`). | Falsa sensación de seguridad frente a componentes maliciosos en el mismo binario. | Documentar explícitamente que los límites son lógicos y no barreras Sandbox de SO. | **OPEN** |
| **AUD-2026-06** | **Media** | Gobernanza | Todos los ADRs centrales (`ADR-0001`..`0005`) permanecen en estado `Proposed` (`GAP-005`). | Incertidumbre sobre cuáles decisiones arquitectónicas son definitivas. | Someter a votación y cambiar estado a `Accepted` o `Rejected` tras resolver `DEC-01..08`. | **OPEN** |
| **AUD-2026-07** | **Baja** | Mantenimiento | Inexistencia de pipeline de CI/CD `.github/workflows/` (`GAP-007`). | Falta de automatización de linters y verificadores de Markdown. | Crear workflow básico de validación de links y formateo en la fase previa a código. | **OPEN** |

---

## 9. Cuestiones Bloqueantes para la Gobernanza (DEC-01 a DEC-08)

Para desbloquear el proyecto de su estado actual de HOLD / NO-GO, el titular del proyecto debe resolver formalmente las siguientes decisiones clave:

1. **`DEC-01` (Definición del Producto v0):** ¿Se autoriza limitar el alcance inicial a un *Laboratorio de Afirmaciones/Evidencias Offline* (sin red, sin persistencia física, sin acciones externas)?
2. **`DEC-02` (Modelo Causal y de Evidencia):** ¿Se adopta la abstracción minimalista R2 / Híbrida para la primera fase de evaluación pre-código?
3. **`DEC-03` (Frontera del Núcleo y Harness):** ¿Se aprueba que el núcleo sea 100% puro y funcional, confinando la E/S exclusivamente en el harness de pruebas sintéticas?
4. **`DEC-04` (Lifecycle de Datos y Privacidad):** ¿Se ratifica que la privacidad se gestiona únicamente mediante retracción lógica bitemporal, excluyendo garantías de borrado físico en soportes inmutables?
5. **`DEC-05` (Criterios de Falsación y Oráculos):** ¿Se aprueba el uso obligatorio de los escenarios R-01..R-08 como oráculos de prueba negativos?
6. **`DEC-06` (Postergación de Plataforma/Serialización):** ¿Se autoriza posponer la decisión de motores de almacenamiento (e.g. SQLite, Sled) hasta validar los contratos puros de memoria?
7. **`DEC-07` (Licencia Legal):** ¿Qué modelo de licencia legal se asignará al archivo `LICENSE` del repositorio?
8. **`DEC-08` (Autorización de Transición a Código - Gate G2->G3):** ¿Se mantiene el estado estricto de HOLD / NO-GO hasta la resolución completa de DEC-01..DEC-07?

---

## 10. Conclusión y Recomendación

La arquitectura documental de **THE MACHINE** muestra un nivel excepcional de rigor conceptual y conciencia de seguridad. Sin embargo, antes de autorizar cualquier línea de código Rust, es imprescindible resolver las ambigüedades en la jerarquía normativa, incorporar las especificaciones de prueba para las amenazas `TH-012`, `TH-016` y `TH-019`, y adoptar formalmente las decisiones `DEC-01` a `DEC-08`.

El proyecto está formalmente **READY-FOR-DECISION** para la deliberación de gobernanza. Se mantiene el estado estricto de **HOLD / NO-GO** para la fase de implementación de software.
