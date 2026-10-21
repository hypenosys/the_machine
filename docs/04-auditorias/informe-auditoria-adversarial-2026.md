# Informe de Auditoría Adversarial y Troubleshooting Preimplementación — THE MACHINE

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad / Auditor Técnico Independiente (@Jules)
**Repositorio:** `hypenosys/the_machine`
**Rama de trabajo:** `audit/adversarial-troubleshooting-2026-10`
**Rama base:** `master` (Commit de referencia: `de545ad47e5b17179ee1e5e6fcdd0e425f09b677`)
**Estado del proyecto:** **HOLD / NO-GO (Cero código ejecutable, cero manifiestos de Cargo)**
**Veredicto de la Auditoría:** **REVISE** (Se identifican ambigüedades documentales y tensiones pre-código que requieren corrección y clarificación previa a la deliberación formal de las decisiones de gobernanza `DEC-01..DEC-08`. **NO AUTORIZA** la implementación de código).

---

## 1. Resumen Ejecutivo y Veredicto

### 1.1 Contexto y Objetivo
Se ha realizado una revisión adversarial y técnica exhaustiva sobre el estado documental y arquitectónico del repositorio **THE MACHINE**. El proyecto se concibe como un sistema *local-first*, *Rust-first* y *security-first* inspirado conceptualmente en *Person of Interest*, orientado a separar el registro epistemológico, la evaluación especializada, la gobernanza de reglas y la autoridad operativa.

Esta auditoría revisa la autoridad de los documentos, evalúa las tensiones/contradicciones C-01 a C-04, audita las prohibiciones P-01 a P-06 y los criterios de falsación R-01 a R-08, contrasta las amenazas TH-001..TH-020 (con foco en TH-012, TH-016 y TH-019), analiza los registros de brechas GAP-001..GAP-010 y evalúa objetivamente las alternativas arquitectónicas (R1 de seis entidades, R2 Artifact+Attestation, alternativa híbrida y control específico de dominio), sin validar complacientemente ninguna propuesta ni presuponer vencedores.

### 1.2 Veredicto Global: `REVISE`
- **Veredicto:** **REVISE**
- **Justificación (OBSERVADO):** Existen incoherencias, especificaciones de prueba faltantes en el plan de seguridad global (`GAP-002`), decisiones de arquitectura en estado borrador/propuesto (`GAP-005`, ADR-0001..0005) y contradicciones conceptuales pendientes de resolución formal (`C-01..C-04`). Se requieren correcciones y precisiones documentales explícitas antes de someter `DEC-01..DEC-08` a deliberación definitiva.
- **Alcance estricto del veredicto:** El veredicto `REVISE` **NO constituye una autorización para escribir código, añadir dependencias, aprobar ADRs ni pasar a la fase de implementación (G3)**. El proyecto permanece estrictamente bajo el estado de **HOLD / NO-GO**.

---

## 2. Mapa Propuesto de Precedencia y Jerarquía Documental

### 2.1 Reconstrucción de Autoridad (PROPUESTO / INFERIDO)
Para evitar la presuposición de que el documento con fecha más reciente invalida a los precedentes sin justificación formal, se propone el siguiente mapa de precedencia documental:

```
[NIVEL 0: Principios Fundacionales y Mantenimiento]
   ├── AGENTS.md (Reglas metodológicas para agentes)
   ├── PHILOSOPHY.md (Principios epistemológicos e ideológicos)
   └── CONTRIBUTING.md / GLOSSARY.md / README.md (Gobernanza general)

[NIVEL 1: Marco de Seguridad Normativo y Requisitos]
   ├── docs/02-diseno/security/requirements.md (SEC-REQ-001..017)
   ├── docs/02-diseno/security/threat-model-v0.md (TH-001..020)
   ├── docs/02-diseno/security/traceability.md
   └── docs/03-preimplementacion/precode-decision-protocol-v0.md (Protocolo de decisión candidato)

[NIVEL 2: Especificaciones Técnicas Pre-código / Candidatas]
   ├── docs/03-preimplementacion/unified-specification-candidate-v0.md
   ├── docs/03-preimplementacion/general-epistemic-contract-v0.md
   ├── docs/03-preimplementacion/evidence-lifecycle-privacy-candidate-v0.md
   └── docs/03-preimplementacion/offline-experiment-contract-candidate-v0.md

[NIVEL 3: Consolidaciones y Análisis Pre-código (Propuestas/Revisiones)]
   ├── docs/03-preimplementacion/finch-consolidation-troubleshooting-candidate-v0.md
   └── docs/03-preimplementacion/precode-consistency-decision-review-v0.md

[NIVEL 4: Auditorías Independientes e Informes Históricos]
   ├── docs/04-auditorias/gap-register.md (GAP-001..GAP-010)
   ├── docs/04-auditorias/security-review.md / architecture-review.md / auditoria-integral-2026-10.md
   └── docs/04-auditorias/informe-auditoria-adversarial-2026.md (Este documento)
```

### 2.2 Evidencia de Estado Real (OBSERVADO)
- **ADRs `0001` a `0005` (`docs/02-diseno/adr/`):** Todos se encuentran en estado `Proposed` (**OBSERVADO**). Ninguno ha sido aceptado (`Accepted`).
- **Protocolo de Decisión (`precode-decision-protocol-v0.md`):** Es un protocolo candidato no ratificado (**OBSERVADO**).
- **Consolidación Finch (`finch-consolidation-troubleshooting-candidate-v0.md`, §1):** Declara explícitamente ser un documento de análisis **no normativo** que no sustituye las especificaciones originales ni autoriza código (**OBSERVADO**).

---

## 3. Auditoría Adversarial de Tensiones C-01 a C-04

### C-01: Registro Histórico e Inmutabilidad vs. Privacidad y Supresión Legítima
- **OBSERVADO:** `docs/03-preimplementacion/evidence-lifecycle-privacy-candidate-v0.md` (§3) describe el ciclo de vida de la evidencia y mecanismos de supresión de contenido, mientras que `PHILOSOPHY.md` señala principios de reproducibilidad e inmutabilidad. `docs/03-preimplementacion/finch-consolidation-troubleshooting-candidate-v0.md` (§4) indica que la privacidad real fuera de la simulación lógica `E-10` se mantiene como una cuestión abierta.
- **INFERIDO:** Existe una tensión de garantías entre prometer supresión física completa de datos y mantener la capacidad de reproducir determinísticamente un dictamen previo. Sin embargo, un diseño arquitectónico compatible podría admitir la separación entre el contenido primario sujeto a políticas de supresión/privacidad y los registros de atestación auditables. La supresión del contenido primario puede degradar la reproducibilidad plena a verificación parcial, lo cual constituye un límite de diseño a documentar y no una imposibilidad absoluta insuperable.
- **PROPUESTO:** Tratar C-01 como una tensión de garantías a definir en `DEC-04`: especificar el alcance del laboratorio sintético respecto a la gestión del ciclo de vida de evidencia (L-01..L-10), clarificando el efecto de la supresión de contenido sobre las atestaciones y dictámenes históricos sin prometer soluciones definitivas fuera del entorno sintético.
- **NO VERIFICADO:** No existen pruebas de supresión física o borrado criptográfico en tiempo de ejecución (**NO VERIFICADO**).

### C-02: Núcleo Epistemológico Común vs. Semántica Especializada de Dominio
- **OBSERVADO:** `docs/03-preimplementacion/unified-specification-candidate-v0.md` propone un contrato unificado de 6 entidades (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`), mientras que `docs/03-preimplementacion/heterogeneous-cases.md` analiza casos de dominio con requerimientos de comparabilidad específicos.
- **INFERIDO:** Un núcleo genérico sin semántica de dominio no puede determinar si dos afirmaciones de dominios distintos son comparables. Forzar a que todo dato pase por las 6 entidades sin evaluar el volumen o la frecuencia podría generar sobrecarga conceptual en dominios simples de telemetría.
- **PROPUESTO:** Someter a experimentación comparativa (fase pre-código) la hipótesis de si un contrato de 6 entidades (R1) aporta ventajas demostrables de trazabilidad frente a un contrato minimalista de 2 abstracciones (R2: Artifact + Attestation) o una alternativa híbrida, antes de adoptar cualquier esquema en `DEC-02`.

### C-03: Gobernanza de Reglas y Separación Lógica vs. Aislamiento Real de Seguridad
- **OBSERVADO:** `docs/03-preimplementacion/architecture-boundaries.md` (§2) y `docs/02-diseno/adr/0001-security-first-trust-boundaries.md` definen fronteras lógicas entre Evaluadores, Gobernanza y Autoridad Operativa.
- **INFERIDO:** La separación lógica de responsabilidades dentro de un mismo proceso local o binario monolítico no equivale a un aislamiento de seguridad o sandbox de proceso/memoria. Un adversario con ejecución de código dentro del host puede eludir fronteras lógicas.
- **PROPUESTO:** Precisar en la documentación que la separación entre evaluación y acción es una garantía lógica de flujo de trabajo (*workflow rule*), no una barrera defensiva contra código malicioso residente en el mismo espacio de memoria (`GAP-004`).

### C-04: Harness de Experimentación con E/S vs. Núcleo Offline / Puramente Funcional
- **OBSERVADO:** `docs/03-preimplementacion/offline-experiment-contract-candidate-v0.md` (§2) plantea un contrato de experimento offline con entradas/salidas sintéticas controladas.
- **INFERIDO:** Si la E/S o el tiempo del sistema se introducen directamente dentro de las funciones de evaluación, se pierde el determinismo y la reproducibilidad de las pruebas.
- **PROPUESTO:** Evaluar la adopción de `DEC-03`: el núcleo computable de evaluación debe diseñarse como funciones puras sin efectos secundarios de E/S ni acceso al reloj del sistema, confinando la entrada/salida y generación de estímulos exclusivamente en el Harness de experimentación sintética.

---

## 4. Auditoría de Prohibiciones P-01..P-06 y Criterios R-01..R-08

### 4.1 Matriz de Prohibiciones P-01..P-06 (OBSERVADO / INFERIDO / PROPUESTO)
| ID | Prohibición | Referencia Documental | Estado Observado en Especificaciones | Análisis y Propuesta |
|---|---|---|---|---|
| **P-01** | Evaluación no autoriza ejecución | `docs/02-diseno/security/requirements.md` (SEC-REQ-002, SEC-REQ-003); `adr/0004` | **OBSERVADO:** Mapeado en diseño. Evaluación y Acción separadas. | **PROPUESTO:** Mantener estricto. Un `Assessment` es un dictamen, no un comando. |
| **P-02** | Fuente no se autentica a sí misma | `docs/02-diseno/security/requirements.md` (SEC-REQ-007) | **OBSERVADO:** Requiere atestación/firma provista por autoridad o canal externo. | **PROPUESTO:** Reutilizar garantía; no permitir auto-declaraciones de confianza. |
| **P-03** | Corrección no retrodata conocimiento | `docs/03-preimplementacion/claim-semantics-v0.md` | **OBSERVADO:** Requiere distinción temporal explícita (`valid_time`, `recorded_time`, `assessed_time`). | **PROPUESTO:** Precisar que las correcciones generan nuevos registros sin alterar la marca `recorded_time` original. |
| **P-04** | Evaluador no activa reglas unilateralmente | `docs/02-diseno/security/threat-model-v0.md` (TH-019); `gap-register.md` (GAP-002, GAP-010) | **OBSERVADO:** Trazabilidad parcial. El evaluador no posee autoridad sobre políticas de gobernanza. | **PROPUESTO:** Completar especificación de autoridad normativa en el protocolo pre-código. |
| **P-05** | Dependencia conocida no cuenta como soporte independiente | `docs/03-preimplementacion/general-epistemic-contract-v0.md` | **OBSERVADO:** Grafo de corroboración debe descontar nodos con ancestros comunes declarados. | **PROPUESTO:** Limitar la verificación a dependencias *conocidas/declaradas*; no prometer descubrimiento de dependencias ocultas. |
| **P-06** | Perfil no redefine garantías del núcleo | `docs/03-preimplementacion/precode-consistency-decision-review-v0.md` (DEC-02) | **OBSERVADO:** El núcleo impone denegaciones de seguridad que ningún perfil de dominio puede relajar. | **PROPUESTO:** Definir la interfaz del perfil como extensión estricta, sin capacidad de *override* sobre denegaciones del núcleo. |

### 4.2 Criterios de Falsación Candidates R-01..R-08 (Oráculos de Prueba Sintéticos)
Se aclara que los criterios R-01..R-08 son **escenarios candidatos para el arnés de prueba pre-código**, alineados con las dimensiones de procedencia (`UNVERIFIED` / `VERIFIED`) y la taxonomía candidata preexistente de juicio epistemológico (`SUPPORTED`, `REFUTED`, `CONFLICTED`, `INSUFFICIENT`, `NOT_COMPARABLE`):

- **R-01 (Coincidencia Identificador vs. Identidad Real):**
  *Aclaración de Oráculo:* Se debe distinguir la dimensión de procedencia de la evaluación epistemológica. La coincidencia de una URI o identificador entre dos fuentes **no demuestra por sí sola** la autenticidad del origen (**OBSERVADO**). En la dimensión de procedencia, el estado debe ser `UNVERIFIED` (conforme al contrato sintético E-03). En la dimensión del juicio del evaluador, esto se refleja como evidencia `INSUFFICIENT` para certificar procedencia auténtica.
- **R-02 (Autoverificación de Fuente):**
  *Aclaración de Oráculo:* Si una declaración incluye una auto-atestación sin firma/atestación externa autorizada, la procedencia se marca como `UNVERIFIED`, conduciendo en el juicio del evaluador al estado `INSUFFICIENT` o a la abstención justificada.
- **R-03 (Corroboración con Dependencias Conocidas):**
  *Aclaración de Oráculo:* Aplica a dependencias **conocidas y declaradas** en el registro. Invariante esencial de no amplificación: la ausencia de una arista de dependencia no demuestra independencia (**independencia no demostrada**). El sistema debe evitar inflar la certeza de soporte y clasificar el estado de soporte independiente como `INSUFFICIENT`.
- **R-04 (Anomalía Bitemporal / Inconsistencia):**
  *Aclaración de Oráculo:* Una diferencia o discrepancia entre `recorded_time` y `valid_time` no implica automáticamente que los datos no sean comparables (`NOT_COMPARABLE`), ya que el modelo admite predicciones o registros diferidos. Si existe una inconsistencia temporal no justificada, la anomalía debe registrarse explícitamente con su causa, conduciendo a la abstención o a un dictamen `INSUFFICIENT` según la política del perfil.
- **R-05 (Intento de Mutación Histórica):**
  *Expectativa Observable:* Someter una instrucción que intente modificar directamente un registro previo debe ser rechazada por la interfaz del harness, manteniendo inalterado el historial observable.
- **R-06 (Evaluación Fuera de Alcance de Perfil):**
  *Expectativa Observable:* Someter un contenido fuera del dominio aplicable del perfil debe devolver `NOT_COMPARABLE` o `INSUFFICIENT`.
- **R-07 (Evaluación Convertida en Comando Operativo):**
  *Expectativa Observable:* La emisión de un `Assessment` con valor `SUPPORTED` no debe generar ningún evento de ejecución en la frontera operativa sin una orden explícita de la Autoridad Operativa.
- **R-08 (Gestión de Supresión de Contenido) — EXPERIMENTO E-10 BLOQUEADO:**
  *Estado Observado:* El experimento E-10 se encuentra **expresamente BLOQUEADO** en las especificaciones preexistentes (`offline-experiment-contract-candidate-v0.md` §4 y §6) hasta que se defina la política de retención/supresión.
  *Expectativa Observable:* La gestión de supresión sintética en el laboratorio debe resolverse mediante una de las dos vías permitidas por el contrato candidato: (a) definir formalmente la política de retención/supresión previo al experimento, o (b) excluir justificadamente E-10 del primer corte vertical sintético, sin prometer ni proclamar privacidad garantizada.

*Nota:* La **abstención o la respuesta `INSUFFICIENT` / `NOT_COMPARABLE`** son resultados epistemológicos válidos y previstos en la taxonomía candidata preexistente del proyecto.

---

## 5. Auditoría del Modelo de Amenazas: Análisis de TH-012, TH-016 y TH-019

### 5.1 Estado Actual en la Documentación (OBSERVADO)
- En `docs/02-diseno/security/threat-model-v0.md`, las amenazas `TH-012` (Confused Deputy), `TH-016` (Backup irrecuperable) y `TH-019` (Insider Abuse) están categorizadas con impacto Alto.
- En `docs/02-diseno/security/traceability.md` y `docs/04-auditorias/gap-register.md` (`GAP-002`), se constata que **ninguna de las tres amenazas posee una prueba asignada (`SEC-XXX`) en la matriz de verificaciones ejecutables** (**OBSERVADO**).

### 5.2 Propuesta de Escenarios Negativos Condicionados (PROPUESTO / NO EJECUTADO)
Para avanzar en la resolución de `GAP-002` mediante **propuestas pendientes de aprobación** (que no cierran el gap hasta ser ejecutadas y verificadas), se proponen los siguientes escenarios de prueba conceptuales condicionados a la política vigente:

1. **Escenario Negativo para TH-012 (Confused Deputy) — Propuesta de Test `SEC-015`:**
   - *Condición de Política:* Reglas de autorización del Action Gateway en `SEC-REQ-017`.
   - *Escenario Negativo Sintético:* Un actor A sin privilegio suficiente solicita una acción a través de un intermediario B. Si la solicitud delegada no satisface la política de autorización del originador A según la política vigente, la acción debe ser rechazada.

2. **Escenario Negativo para TH-016 (Persistencia Inconsistente) — Propuesta de Test `SEC-016`:**
   - *Condición de Política:* Verificación de integridad estructural descrita en `SEC-REQ-011`.
   - *Escenario Negativo Sintético:* Presentar un estado de almacenamiento sintético con registros truncados o punteros corruptos. El arnés de prueba debe detectar la inconsistencia estructural en la inicialización y rechazar la carga del estado corrupto.

3. **Escenario Negativo para TH-019 (Insider Abuse / Alteración de Reglas sin Autorización) — Propuesta de Test `SEC-017`:**
   - *Condición de Política:* Verificación de autorización de cambio de política descrita en `SEC-REQ-016`.
   - *Escenario Negativo Sintético:* Intento de cambiar las reglas de evaluación o perfiles activos mediante un comando que no satisfaga los requisitos de autorización establecidos por la política vigente (ej. autoaprobación o cambio no autorizado). El sistema debe denegar la modificación de reglas.
   - *Aclaración de Alcance:* La amenaza de un *insider* con control total e irrestricto sobre el sistema operativo host se considera **fuera del alcance del laboratorio sintético local**, pues sobrepasa las defensas a nivel de software.

*Aclaración:* `TH-012`, `TH-016` y `TH-019` **no cuentan con tests globales ejecutados** en el repositorio actual (**OBSERVADO**). Las propuestas `SEC-015..017` constituyen la vía trazable para definir dichas pruebas, pero `GAP-002` permanece abierto hasta su inclusión formal y verificación.

---

## 6. Análisis Adversarial: Hipótesis de Estrés y Contraejemplos Documentales

Se plantean tres hipótesis de estrés pre-código para evaluar posibles límites o puntos débiles en las especificaciones candidatas. Se enfatiza que son **argumentos de análisis documental y no resultados experimentales o de rendimiento ejecutados**:

### Hipótesis de Estrés 1: Evaluación de la Estructura de Tipos R1 frente a Dominios Simples
- **Ubicación Documental:** `docs/03-preimplementacion/unified-specification-candidate-v0.md` (§3).
- **Hipótesis de Estrés (INFERIDO):** Si un dominio de prueba requiere procesar eventos simples (ej. telemetría de sensores), la especificación de 6 tipos de entidades de R1 (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`) añade mayor número de relaciones conceptuales en comparación con estructuras reducidas.
- **Aclaración Importante:** Se aclara que contar con 6 tipos en la especificación no permite inferir directamente menor auditabilidad ni peor rendimiento sin pruebas empíricas. La evaluación de auditabilidad y adecuación de R1 debe medirse de forma neutral frente a R2, la opción Híbrida y el Control Específico de Dominio (Opción D) en el laboratorio sintético pre-código.

### Hipótesis de Estrés 2: Conservación de Independencia Desconocida en Grafos de Procedencia
- **Ubicación Documental:** `docs/03-preimplementacion/general-epistemic-contract-v0.md` (§4).
- **Hipótesis de Estrés (INFERIDO):** Si dos fuentes externas A y B emiten afirmaciones idénticas, pero ambas se basan internamente en una fuente primaria común C no declarada en sus metadatos visibles, la ausencia de una arista de dependencia en el grafo no demuestra que A y B sean independientes.
- **Invariante de No Amplificación:** La ausencia de relación conocida en el registro equivale a **independencia desconocida o no demostrada**. Por ello, el sistema no debe inflar la certeza epistemológica y debe mantener la clasificación de soporte restringida al subgrafo de dependencias explícitamente verificadas (`INSUFFICIENT` para soporte independiente global).

### Hipótesis de Estrés 3: Inefectividad de Fronteras Lógicas frente a Procesos en la Misma Memoria
- **Ubicación Documental:** `docs/03-preimplementacion/architecture-boundaries.md` (§2).
- **Hipótesis de Estrés (INFERIDO):** Definir interfaces separadas entre "Evaluación", "Gobernanza" y "Acción" dentro del mismo binario o espacio de direcciones de memoria proporciona una excelente estructura de código, pero no protege el sistema si la amenaza es un componente comprometido con capacidad de sobrescribir memoria en el host.
- **Límite Identificado:** La separación lógica de responsabilidades es un control de calidad de software y flujo de trabajo, no un mecanismo de aislamiento defensivo contra exploits de memoria o insiders con privilegios en el sistema operativo.

---

## 7. Comparación Neutra de Opciones Arquitectónicas (DEC-02)

Se presenta la comparación objetiva de las cuatro opciones arquitectónicas bajo criterios comunes, **utilizando la Opción D (Control Específico de Dominio) como baseline de comparación, sin proclamar ganadores ni presuponer consensos no ratificados**:

| Criterio de Comparación | Opción R1 (6 Entidades Unificadas) | Opción R2 (Artifact + Attestation Minimal) | Opción Híbrida (R2 en Núcleo + Grafos Extendidos) | Opción D (Control Específico de Dominio - Baseline) |
|---|---|---|---|---|
| **Estructura Representacional** | 6 tipos explicitados (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`). | 2 tipos base (`Artifact` opaco + `Attestation` de metadatos/firma). | `Artifact` + `Attestation` en el núcleo; grafos R1 construidos bajo demanda por el evaluador. | Definiciones ad-hoc especificadas individualmente por cada perfil de dominio. |
| **Complejidad del Esquema Base** | Mayor número de tipos e interconexiones en el contrato inicial. | Menor número de tipos base en el núcleo computable. | Modular: núcleo simple con capacidad de extensión en capa superior. | Inexistencia de contrato común unificado. |
| **Interoperabilidad entre Dominios** | Unificada a través del esquema común de 6 tipos. | Basada en atestaciones estándar sobre artefactos tipados. | Unificada en metadatos primarios; especializada en la extensión. | Nula o dependiente de mapeadores ad-hoc entre dominios (Baseline). |
| **Auditabilidad de Código** | A evaluar empíricamente según complejidad del grafo de tipos. | A evaluar empíricamente según simplicidad de los tipos base. | A evaluar empíricamente en núcleo y extensiones. | Variable y dependiente de cada implementación de dominio. |
| **Estado en la Deliberación Pre-código** | Opción candidata en `unified-specification-candidate-v0.md`. | Opción propuesta para evaluación pre-código. | Opción propuesta para evaluación pre-código. | Sirve como línea base (*baseline*) de comparación no estandarizada. |

*Conclusión de Comparación:* La decisión `DEC-02` debe tomarse mediante la evaluación objetiva de los escenarios de prueba en el laboratorio pre-código, comparando R1, R2 y la opción Híbrida frente a la línea base D, sin seleccionar ganadores de forma anticipada.

---

## 8. Matriz Consolidada y Priorizada de Hallazgos

A continuación se detallan los hallazgos documentales y de diseño identificados, especificando archivo/sección, evidencia, consecuencia y propuesta mínima:

| ID Hallazgo | Gravedad Justificada | Categoría | Archivo y Sección de Referencia | Evidencia (OBSERVADO) | Consecuencia (INFERIDO) | Propuesta Mínima de Resolución (PROPUESTO) | Estado |
|---|---|---|---|---|---|---|---|
| **AUD-2026-01** | **Medium (P2 Interno / P1 Pre-publicación)** | Gobernanza / Legal | Root directory; `CONTRIBUTING.md`, `README.md` | Inexistencia de archivo `LICENSE` en el repositorio (**OBSERVADO**). | El código y docs permanecen "Todos los derechos reservados", impidiendo contribuciones/distribución pública. | Incorporar el archivo `LICENSE` con la licencia decidida por el titular antes de la apertura pública (`GAP-001`). | **OPEN** |
| **AUD-2026-02** | **High** | Seguridad / Cobertura | `docs/02-diseno/security/traceability.md`; `gap-register.md` | `TH-012`, `TH-016` y `TH-019` carecen de prueba asignada (`SEC-XXX`) (**OBSERVADO**). | Brecha en el plan global de verificación de seguridad (`GAP-002`). | Incorporar la especificación de escenarios de prueba condicionados `SEC-015`, `SEC-016` y `SEC-017` (propuesta pendiente de ejecución). | **OPEN** |
| **AUD-2026-03** | **Medium** | Arquitectura | `docs/03-preimplementacion/unified-specification-candidate-v0.md` (§3) | Especificación R1 unificada no ha sido comparada experimentalmente frente a R2, Híbrida o Baseline D (**OBSERVADO**). | Riesgo de adoptar un contrato de datos rígido antes de probar su adecuación en el laboratorio. | Tratar la elección R1/R2/Híbrida/D como hipótesis abierta a evaluar en `DEC-02` (`GAP-006`). | **OPEN** |
| **AUD-2026-04** | **Medium** | Especificación | `docs/03-preimplementacion/claim-semantics-v0.md` | Falta especificación formal de serialización y precisión de tipos bitemporales (**OBSERVADO**). | Posible ambigüedad en la interpretación y parsing de `valid_time`, `recorded_time` y `assessed_time` (`GAP-003`). | Especificar tipos concretos (e.g. ISO-8601/RFC-3339 UTC) preservando los tres tiempos en los borradores de contrato. | **OPEN** |
| **AUD-2026-05** | **Medium** | Seguridad / Aislamiento | `docs/03-preimplementacion/architecture-boundaries.md` (§2) | Inexistencia de especificación de aislamiento de memoria/proceso entre componentes localmente residentes (**OBSERVADO**). | Falsa presuposición de que las fronteras lógicas ofrecen protección contra malware local (`GAP-004`). | Documentar explícitamente que los límites son de flujo de trabajo (*workflow*) y no un Sandbox de SO. | **OPEN** |
| **AUD-2026-06** | **Medium** | Gobernanza | `docs/02-diseno/adr/` (0001 a 0005) | Los 5 ADRs centrales están en estado `Proposed` (**OBSERVADO**). | Ambigüedad sobre cuáles decisiones de arquitectura son definitivas (`GAP-005`). | Revisar y votar el cambio de estado de los ADRs a `Accepted` / `Rejected` tras resolver `DEC-01..08`. | **OPEN** |
| **AUD-2026-07** | **Low** | Mantenimiento | `.github/workflows/` | Inexistencia de directorio de CI/CD para automatizar chequeos documentales (**OBSERVADO**). | Verificación manual propensa a errores en enlaces o formato Markdown (`GAP-007`). | Añadir un workflow básico de linter/validación de enlaces Markdown cuando se autorice la fase de herramientas. | **OPEN** |

---

## 9. Cuestiones Abiertas para la Deliberación de Gobernanza (DEC-01 a DEC-08)

Para avanzar ordenadamente en la fase de pre-diseño sin romper el estado **HOLD / NO-GO**, se someten a la consideración del titular las siguientes decisiones clave:

1. **`DEC-01` (Alcance del Producto v0):**
   - *Cuestión:* ¿Se ratifica que la versión inicial es exclusivamente un *Laboratorio de Afirmaciones/Evidencias Offline* sintético, sin red, sin persistencia física duradera y sin ejecución de acciones reales?
2. **`DEC-02` (Elección de Representación de Evidencia):**
   - *Cuestión:* ¿Se aprueba someter a comparación experimental las opciones R1, R2 y Híbrida frente al Baseline D mediante los escenarios de prueba sintéticos antes de formalizar el esquema final?
3. **`DEC-03` (Frontera del Núcleo y Harness):**
   - *Cuestión:* ¿Se ratifica que el núcleo computable debe consistir en funciones puras sin E/S ni acceso al reloj, restringiendo la E/S al Harness de pruebas?
4. **`DEC-04` (Gestión de Privacidad y Lifecycle de Datos — Experimento E-10 BLOQUEADO):**
   - *Cuestión:* Dado que el experimento E-10 sobre privacidad se encuentra **expresamente BLOQUEADO** en las especificaciones preexistentes, ¿se acuerda definir formalmente la política de retención/supresión preservando los tres tiempos (`valid_time`, `recorded_time`, `assessed_time`) antes de autorizar E-10, o se excluye E-10 del primer corte sintético sin prometer privacidad garantizada?
5. **`DEC-05` (Oráculos de Falsación Negativos):**
   - *Cuestión:* ¿Se aprueba mapear los criterios de falsación R-01 a R-08 a los fixtures existentes F/E/L para su verificación sintética en el arnés de pruebas?
6. **`DEC-06` (Postergación de Tecnología de Persistencia):**
   - *Cuestión:* ¿Se confirma que la elección de motores de almacenamiento (e.g. SQLite, Sled, RocksDB) permanece diferida hasta validar las estructuras en memoria?
7. **`DEC-07` (Modelo de Licencia Legal):**
   - *Cuestión:* ¿Qué modelo de licencia legal (`LICENSE`) asignará el titular para resolver `GAP-001` previa distribución pública?
8. **`DEC-08` (Autorización de Transición a Código - Gate G2->G3):**
   - *Cuestión:* ¿Se confirma que la eventual resolución de DEC-01 a DEC-07 **requiere una autorización expresa y separada del titular** para poder cambiar el estado del proyecto de HOLD a GO?

---

## 10. Conclusión y Recomendación

El análisis de la documentación de **THE MACHINE** refleja una arquitectura conceptual madura, bien orientada a la seguridad y con una clara separación de responsabilidades. No obstante, antes de considerar cualquier autorización para la fase de código, es necesario:

1. Resolver las ambigüedades documentales y calificar adecuadamente la precedencia normativa.
2. Formalizar la asignación de pruebas para `TH-012`, `TH-016` y `TH-019` en el plan global de seguridad (`GAP-002`).
3. Deliberar formalmente sobre las decisiones `DEC-01` a `DEC-08` tras revisar los resultados del presente informe.

Se mantiene el veredicto **REVISE**. El proyecto permanece estrictamente en estado **HOLD / NO-GO**.
