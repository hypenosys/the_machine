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
- **OBSERVADO:** `docs/03-preimplementacion/evidence-lifecycle-privacy-candidate-v0.md` (§3) describe el ciclo de vida de la evidencia y mecanismos de retracción/supresión lógica, mientras que `PHILOSOPHY.md` exige reproducibilidad e inmutabilidad del registro. `docs/03-preimplementacion/finch-consolidation-troubleshooting-candidate-v0.md` (§4) señala que la privacidad real fuera del laboratorio simulación lógica `E-10` está fuera de alcance en la fase actual.
- **INFERIDO:** Prometer "borrado físico/privacidad real" en un soporte inmutable genera una contradicción insuperable. La eliminación de activos primarios impide reproducir evaluaciones históricas de forma determinista.
- **PROPUESTO:** No declarar una solución técnica única. Tratar C-01 como una decisión abierta (`DEC-04`): definir si el laboratorio sintético adopta retracción lógica bitemporal y documentar explícitamente que la garantía de borrado físico real requerirá investigación posterior antes de cualquier despliegue fuera del laboratorio.
- **NO VERIFICADO:** No existen pruebas de borrado físico o borrado criptográfico en tiempo de ejecución (**NO VERIFICADO**).

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
Se aclara que los criterios R-01..R-08 son **escenarios candidatos para el arnés de prueba pre-código**, no experimentos ejecutados ni pruebas pasadas:

- **R-01 (Coincidencia Identificador vs. Identidad Real):**
  *Aclaración de Oráculo:* La coincidencia de una URI, cadena de texto o identificador criptográfico entre dos fuentes **no demuestra por sí sola** que provengan de la misma entidad física real (**OBSERVADO**). El harness debe verificar que la igualdad de identificador sólo sea interpretada como hipótesis de identidad hasta que exista atestación correspondiente.
- **R-02 (Autoverificación de Fuente):**
  *Aclaración de Oráculo:* Si una declaración incluye una auto-atestación de validez sin firma/atestación de una tercera entidad o clave autorizada, la expectativa observable es que el evaluador devuelva estado `UNAUTHENTICATED` o abstención (`ABSTAIN`).
- **R-03 (Corroboración con Dependencias Conocidas):**
  *Aclaración de Oráculo:* Se refiere estrictamente a fuentes que comparten una dependencia **conocida y declarada** en el registro. Si la dependencia común no está declarada en el registro, el sistema local no puede adivinar la relación oculta. La expectativa es que el algoritmo de grafo descuente la independencia solo sobre el subgrafo de dependencias conocidas.
- **R-04 (Temporalidad y Registro de Conocimiento):**
  *Aclaración de Oráculo:* Un `recorded_time` anterior al evento alegado (`valid_time`) no implica automáticamente fraude o malicia: puede obedecer a desincronización de relojes, error de estimación o predicción. La expectativa del harness es que la anomalía sea detectada y clasificada como `TIMESTAMPS_INCONSISTENT` o abstención, sin asumir intención maliciosa.
- **R-05 (Sobrescritura Ciega de Historial):**
  *Expectativa:* Intentar actualizar un dictamen mediante la mutación del registro previo en lugar de crear un nuevo nodo append-only debe resultar en rechazo `MUTATION_DISALLOWED`.
- **R-06 (Evaluación Fuera de Alcance de Perfil):**
  *Expectativa:* Someter datos de un dominio no compatible al perfil especializado debe resultar en `DOMAIN_NOT_APPLICABLE` o abstención.
- **R-07 (Evaluación Convertida en Comando Operativo):**
  *Expectativa:* La emisión de un `Assessment` positivo no debe producir ningún evento de ejecución en el Action Gateway sin una orden explícita de la Autoridad Operativa.
- **R-08 (Supresión Lógica como Destrucción Física):**
  *Expectativa:* La supresión lógica debe cambiar el estado del registro a `RETRACTED`, sin simular o prometer la destrucción física de los bits en medios inmutables.

*Nota:* La **abstención justificada** (`ABSTAIN` / `INSUFFICIENT_EVIDENCE` / `NON_COMPARABLE`) es un resultado válido e intencional en todos los oráculos epistemológicos.

---

## 5. Auditoría del Modelo de Amenazas: Análisis de TH-012, TH-016 y TH-019

### 5.1 Estado Actual en la Documentación (OBSERVADO)
- En `docs/02-diseno/security/threat-model-v0.md`, las amenazas `TH-012` (Confused Deputy), `TH-016` (Backup irrecuperable) y `TH-019` (Insider Abuse) están categorizadas con impacto Alto.
- En `docs/02-diseno/security/traceability.md` y `docs/04-auditorias/gap-register.md` (`GAP-002`), se constata que **ninguna de las tres amenazas posee una prueba asignada (`SEC-XXX`) en la matriz de verificaciones ejecutables** (**OBSERVADO**).

### 5.2 Propuesta de Escenarios Negativos Condicionados (PROPUESTO / NO EJECUTADO)
Para cerrar `GAP-002` sin imponer mecanismos de implementación prematuros (como exigir multisig o sandbox específicos cuando las políticas aún no están definidas), se proponen los siguientes escenarios de prueba conceptuales condicionados a las políticas de seguridad:

1. **Escenario Negativo para TH-012 (Confused Deputy) — Propuesta de Test `SEC-015`:**
   - *Condición de Política:* Vinculación explícita de `[Actor + Recurso + Operación + Contexto Temporal]`.
   - *Escenario Negativo Sintético:* Un actor A sin permiso sobre el recurso R delega una solicitud al servicio B (que sí tiene acceso a R). Si el token o credencial presentado por B no incluye la prueba de autorización originada por A para esa operación específica sobre R, el Action Gateway debe rechazar la acción (`DELEGATION_NOT_AUTHORIZED`).

2. **Escenario Negativo para TH-016 (Backup/Persistencia Inconsistente) — Propuesta de Test `SEC-016`:**
   - *Condición de Política:* Verificación de integridad estructural en el arranque/restauración de estado.
   - *Escenario Negativo Sintético:* Inyección de una imagen de persistencia sintética truncada o con punteros de evidencia rotos (`EvidenceLink` huérfano). El sistema en arranque debe detectar la incoherencia y abortar o entrar en modo degradado seguro (`CORRUPTED_STATE_REJECTED`), impidiendo la emisión de evaluaciones sobre datos inconsistentes.

3. **Escenario Negativo para TH-019 (Insider Abuse / Alteración Unilateral) — Propuesta de Test `SEC-017`:**
   - *Condición de Política:* La política de gobernanza aplicable determine el nivel de autorización necesario para modificar la vigencia o reglas de un perfil.
   - *Escenario Negativo Sintético:* Intento de cambiar la versión activa de un perfil de reglas enviando una instrucción firmada por una sola identidad cuando la política configurada requiere doble autorización o validación de quórum. El sistema debe denegar la actualización (`UNAUTHORIZED_POLICY_MUTATION`).

*Aclaración:* `TH-012`, `TH-016` y `TH-019` **no cuentan con tests globales ejecutados** en el repositorio actual (**OBSERVADO**).

---

## 6. Análisis Adversarial: Hipótesis de Estrés y Contraejemplos Documentales

Se plantean tres hipótesis de estrés pre-código para evaluar posibles límites o puntos débiles en las especificaciones candidatas. Se enfatiza que son **argumentos de análisis documental y no resultados experimentales o de rendimiento ejecutados**:

### Hipótesis de Estrés 1: Evaluación del Esquema R1 (6 Entidades) frente a Estructuras Simples de Alta Frecuencia
- **Ubicación Documental:** `docs/03-preimplementacion/unified-specification-candidate-v0.md` (§3).
- **Hipótesis de Estrés (INFERIDO):** Si un dominio de prueba requiere procesar grandes volúmenes de eventos simples (ej. telemetría o lecturas consecutivas de sensores), obligar a que cada evento individual instancie las 6 entidades de R1 (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`) podría multiplicar los metadatos y la complejidad de navegación del grafo.
- **Aclaración Importante:** Se aclara que tener 6 *tipos* de entidades en la especificación no implica que cada lectura instancie necesariamente 6 *objetos nuevos* (los nodos de `Source` o `Assessment` pueden reutilizarse). Por lo tanto, el argumento no debe presentarse como un hecho verificado de "explosión de memoria" ni proclamar a R1 como "REFUTADA". Se debe tratar como una **hipótesis de estrés de diseño que deberá medirse objetivamente frente a R2 y la opción Híbrida en el primer laboratorio sintético**.

### Hipótesis de Estrés 2: Falsa Presunción de Independencia en Fuentes con Ancestros Comunes No Declarados
- **Ubicación Documental:** `docs/03-preimplementacion/general-epistemic-contract-v0.md` (§4).
- **Hipótesis de Estrés (INFERIDO):** Si dos fuentes externas A y B emiten afirmaciones idénticas, pero ambas se basan internamente en una fuente primaria común C no declarada en sus metadatos visibles, el algoritmo de evaluación local procesará A y B como corroboraciones independientes.
- **Límite Identificado:** Ningún contrato epistemológico local puede descubrir dependencias no declaradas ni invisibles en la procedencia. Por ello, la regla de deduplicación de soporte en P-05 aplica exclusivamente sobre el *subgrafo de dependencias conocidas y declaradas*. La certidumbre resultante debe calificarse como `PROVISIONAL_SUPPORT_KNOWN_GRAPH` y no como "independencia absoluta".

### Hipótesis de Estrés 3: Inefectividad de Fronteras Lógicas frente a Procesos en la Misma Memoria
- **Ubicación Documental:** `docs/03-preimplementacion/architecture-boundaries.md` (§2).
- **Hipótesis de Estrés (INFERIDO):** Definir interfaces separadas entre "Evaluación", "Gobernanza" y "Acción" dentro del mismo binario o espacio de direcciones de memoria proporciona una excelente estructura de código, pero no protege el sistema si la amenaza es un componente comprometido con capacidad de sobrescribir memoria en el host.
- **Límite Identificado:** La separación lógica de responsabilidades es un control de calidad de software y flujo de trabajo, no un mecanismo de aislamiento defensivo contra exploits de memoria o insiders con privilegios en el sistema operativo.

---

## 7. Comparación Neutra de Opciones Arquitectónicas (DEC-02)

Se presenta la comparación objetiva de las cuatro opciones arquitectónicas bajo criterios comunes, **sin proclamar un ganador ni inventar métricas de rendimiento**:

| Criterio de Comparación | Opción R1 (6 Entidades Unificadas) | Opción R2 (Artifact + Attestation Minimal) | Opción Híbrida (R2 en Núcleo + Grafos Extendidos) | Control Específico de Dominio |
|---|---|---|---|---|
| **Estructura Representacional** | 6 tipos explicitados (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`). | 2 tipos base (`Artifact` opaco + `Attestation` de metadatos/firma). | `Artifact` + `Attestation` en el núcleo; grafos R1 construidos bajo demanda por el evaluador. | Definiciones ad-hoc especificadas individualmente por cada perfil de dominio. |
| **Complejidad del Esquema Base** | Mayor número de tipos e interconexiones en el contrato inicial. | Mínima superficie de tipos en el núcleo computable. | Modular: núcleo simple con capacidad de extensión en capa superior. | Inexistencia de contrato común unificado. |
| **Interoperabilidad entre Dominios** | Unificada a través del esquema común de 6 tipos. | Basada en atestaciones estándar sobre artefactos tipados. | Unificada en metadatos primarios; especializada en la extensión. | Nula o dependiente de mapeadores ad-hoc entre dominios. |
| **Auditabilidad de Código** | Requiere auditar la correcta gestión de grafos y relaciones complejas. | Facilita la auditoría del núcleo por su reducida superficie de estado. | Permite auditar el núcleo de atestación de forma aislada a los grafos. | Compleja por la dispersión de contratos de dominio. |
| **Estado en la Deliberación Pre-código** | Opción candidata en `unified-specification-candidate-v0.md`. | Opción propuesta en revisiones y evaluaciones de auditoría. | Opción de consenso propuesta para el primer laboratorio sintético. | Descartada como contrato global por no aportar abstracción común. |

*Conclusión de Comparación:* La elección entre R1, R2 o la opción Híbrida debe realizarse en la deliberación de `DEC-02` mediante la ejecución previa de oráculos sintéticos en el primer laboratorio pre-código, sin seleccionar ganador prematuramente en este informe.

---

## 8. Matriz Consolidada y Priorizada de Hallazgos

A continuación se detallan los hallazgos documentales y de diseño identificados, especificando archivo/sección, evidencia, consecuencia y propuesta mínima:

| ID Hallazgo | Gravedad Justificada | Categoría | Archivo y Sección de Referencia | Evidencia (OBSERVADO) | Consecuencia (INFERIDO) | Propuesta Mínima de Resolución (PROPUESTO) | Estado |
|---|---|---|---|---|---|---|---|
| **AUD-2026-01** | **Medium (P2 Interno / P1 Pre-publicación)** | Gobernanza / Legal | Root directory; `CONTRIBUTING.md`, `README.md` | Inexistencia de archivo `LICENSE` en el repositorio (**OBSERVADO**). | El código y docs permanecen "Todos los derechos reservados", impidiendo contribuciones/distribución pública. | Incorporar el archivo `LICENSE` con la licencia decidida por el titular antes de la apertura pública (`GAP-001`). | **OPEN** |
| **AUD-2026-02** | **High** | Seguridad / Cobertura | `docs/02-diseno/security/traceability.md`; `gap-register.md` | `TH-012`, `TH-016` y `TH-019` carecen de prueba asignada (`SEC-XXX`) (**OBSERVADO**). | Brecha en el plan global de verificación de seguridad (`GAP-002`). | Incorporar la especificación de escenarios de prueba condicionados `SEC-015`, `SEC-016` y `SEC-017`. | **OPEN** |
| **AUD-2026-03** | **Medium** | Arquitectura | `docs/03-preimplementacion/unified-specification-candidate-v0.md` (§3) | Especificación R1 unificada no ha sido comparada experimentalmente frente a R2 o Híbrida (**OBSERVADO**). | Riesgo de adoptar un contrato de datos rígido antes de probar su adecuación en el laboratorio. | Tratar la elección R1/R2/Híbrida como hipótesis abierta a evaluar en `DEC-02` (`GAP-006`). | **OPEN** |
| **AUD-2026-04** | **Medium** | Especificación | `docs/03-preimplementacion/claim-semantics-v0.md` | Falta especificación formal de serialización y precisión de tipos bitemporales (**OBSERVADO**). | Posible ambigüedad en la interpretación y parsing de `valid_time`, `recorded_time` y `assessed_time` (`GAP-003`). | Especificar tipos concretos (e.g. ISO-8601/RFC-3339 UTC) en el borrador de contrato de datos. | **OPEN** |
| **AUD-2026-05** | **Medium** | Seguridad / Aislamiento | `docs/03-preimplementacion/architecture-boundaries.md` (§2) | Inexistencia de especificación de aislamiento de memoria/proceso entre componentes localmente residentes (**OBSERVADO**). | Falsa presuposición de que las fronteras lógicas ofrecen protección contra malware local (`GAP-004`). | Documentar explícitamente que los límites son de flujo de trabajo (*workflow*) y no un Sandbox de SO. | **OPEN** |
| **AUD-2026-06** | **Medium** | Gobernanza | `docs/02-diseno/adr/` (0001 a 0005) | Los 5 ADRs centrales están en estado `Proposed` (**OBSERVADO**). | Ambigüedad sobre cuáles decisiones de arquitectura son definitivas (`GAP-005`). | Revisar y votar el cambio de estado de los ADRs a `Accepted` / `Rejected` tras resolver `DEC-01..08`. | **OPEN** |
| **AUD-2026-07** | **Low** | Mantenimiento | `.github/workflows/` | Inexistencia de directorio de CI/CD para automatizar chequeos documentales (**OBSERVADO**). | Verificación manual propensa a errores en enlaces o formato Markdown (`GAP-007`). | Añadir un workflow básico de linter/validación de enlaces Markdown cuando se autorice la fase de herramientas. | **OPEN** |

---

## 9. Cuestiones Abiertas para la Deliberación de Gobernanza (DEC-01 a DEC-08)

Para avanzar ordenadamente en la fase de pre-diseño sin romper el estado **HOLD / NO-GO**, se someten a la consideración del titular las siguientes decisiones clave:

1. **`DEC-01` (Alcance del Producto v0):**
   - *Cuestión:* ¿Se ratifica que la versión inicial es exclusivamente un *Laboratorio de Afirmaciones/Evidencias Offline* sintético, sin red, sin persistencia física duradera y sin ejecución de acciones reales?
2. **`DEC-02` (Elección de Representación de Evidencia):**
   - *Cuestión:* ¿Se aprueba someter a comparación experimental las opciones R1, R2 y Híbrida mediante oráculos de prueba pre-código antes de formalizar el esquema final?
3. **`DEC-03` (Frontera del Núcleo y Harness):**
   - *Cuestión:* ¿Se ratifica que el núcleo computable debe consistir en funciones puras sin E/S ni acceso al reloj, restringiendo la E/S al Harness de pruebas?
4. **`DEC-04` (Gestión de Privacidad y Lifecycle):**
   - *Cuestión:* ¿Se acuerda que el laboratorio sintético gestionará la privacidad mediante marcas de retracción lógica bitemporal, difiriendo las garantías de borrado físico hasta fases posteriores?
5. **`DEC-05` (Oráculos de Falsación Negativos):**
   - *Cuestión:* ¿Se aprueba la incorporación formal de los escenarios R-01 a R-08 como oráculos de prueba negativos obligatorios para el arnés sintético?
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

Se emite el veredicto **REVISE**. El proyecto se mantiene estrictamente en estado **HOLD / NO-GO**.
