# Paquete de Decisión Preimplementación y Protocolo de Deliberación — THE MACHINE (v0)

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Repositorio:** `hypenosys/the_machine`
**Ubicación:** `docs/03-preimplementacion/decision-package-v0.md`
**Estado del proyecto:** **HOLD / NO-GO (Cero código ejecutable, cero manifiestos Cargo)**
**Propósito:** Proveer al titular del proyecto un paquete de decisión normativo, falsable y estructurado para la deliberación formal de las decisiones de gobernanza `DEC-01..DEC-08`, sin autorizar código ni alterar el estado HOLD.

---

## 1. Contexto y Principios de Deliberación

### 1.1 Naturaleza del Entregable
El presente documento constituye un **paquete de decisión preimplementación** de carácter exclusivamente documental. No aprueba ADRs, no modifica el estado de investigación ni autoriza la transición a la fase de código (G3).

### 1.2 Taxonomía de Evidencia Obligatoria
Toda afirmación contenida en este paquete utiliza estrictamente la taxonomía metodológica establecida en `AGENTS.md` y `PHILOSOPHY.md`:
- **OBSERVADO:** Hecho verificado directamente en los documentos existentes de `master`.
- **INFERIDO:** Deducción lógica a partir de las especificaciones observadas.
- **PROPUESTO:** Opción o recomendación sometida a la deliberación del titular.
- **NO VERIFICADO:** Propiedad o afirmación que no cuenta con prueba empírica en la fase actual.

### 1.3 Dimensiones Temporales
Conforme a `docs/03-preimplementacion/claim-semantics-v0.md` (§3) y `docs/03-preimplementacion/evidence-lifecycle-privacy-candidate-v0.md` (§2), se preservan explícitamente tres dimensiones temporales distintas e independientes:
1. `valid_time`: Intervalo o instante en que el hecho ocurrió o es válido en el dominio externo.
2. `recorded_time`: Momento en que la atestación o artefacto fue registrado en la memoria/persistencia.
3. `assessed_time`: Momento en que el evaluador emitió el dictamen o juicio epistemológico.

---

## 2. Matriz Exhaustiva de Decisiones DEC-01 a DEC-08

A continuación se detallan las decisiones de gobernanza pre-código establecidas en `docs/03-preimplementacion/precode-decision-protocol-v0.md` (§3) y `docs/03-preimplementacion/precode-consistency-decision-review-v0.md` (§4):

| ID | Título de la Decisión | Opciones Reales | Ventajas y Oportunidades | Inconvenientes y Costes | Riesgos Asociados | Evidencia Disponible (OBSERVADO) | Evidencia Faltante (NO VERIFICADO) | Dependencias Directas | Autoridad Competente |
|---|---|---|---|---|---|---|---|---|---|
| **DEC-01** | **Producto v0 / Alcance** | **Opción A:** Laboratorio sintético offline de afirmaciones.<br>**Opción B:** Producto autónomo distribuido con persis. y red. | **A:** Cero superficie de ataque externa, iteración rápida.<br>**B:** Producto final funcional. | **A:** No prueba rendimiento en red.<br>**B:** Gran complejidad inicial y brechas de seguridad. | **A:** Sesgo de laboratorio sintético.<br>**B:** Incumplimiento de G0-G2. | `offline-experiment-contract-candidate-v0.md` (§1). | Ninguna en laboratorio offline. | Ninguna. | **Titular del Proyecto** |
| **DEC-02** | **Modelo Causal y de Evidencia** | **Opción R1:** 6 entidades unificadas.<br>**Opción R2:** Artifact + Attestation.<br>**Opción Híbrida:** R2 núcleo + Grafos R1.<br>**Opción D:** Baseline específico de dominio. | **R1:** Expresividad completa.<br>**R2:** Mínima complejidad.<br>**Híbrida:** Modularidad.<br>**D:** Optimización de dominio. | **R1:** Estructura compleja.<br>**R2:** Requiere extensiones.<br>**Híbrida:** Capa intermedia.<br>**D:** Nula interoperabilidad. | **R1:** Sobrecarga conceptual.<br>**R2:** Pérdida de semántica.<br>**Híbrida:** Falsa abstracción.<br>**D:** Fragmentación. | `unified-specification-candidate-v0.md`; `heterogeneous-cases.md`. | Pruebas comparativas sintéticas en memoria. | DEC-01 | **Titular del Proyecto** |
| **DEC-03** | **Frontera del Núcleo y E/S** | **Opción A:** Núcleo puro funcional (sin E/S) + Harness externo.<br>**Opción B:** Núcleo con E/S y reloj integrado. | **A:** Determinismo 100%, testabilidad limpia.<br>**B:** Menor boilerplate de interfaz. | **A:** Exige adaptar datos sintéticos en arnés.<br>**B:** Pierde determinismo. | **A:** Acoplamiento al arnés sintético.<br>**B:** Contaminación de estado y efectos secundarios. | `offline-experiment-contract-candidate-v0.md` (§2). | Comprobación de determinismo sintético. | DEC-01 | **Titular del Proyecto** |
| **DEC-04** | **Lifecycle de Datos y Privacidad (E-10)** | **Opción A:** Excluir E-10 del primer laboratorio sintético.<br>**Opción B:** Definir política formal de retención/supresión antes del lab. | **A:** Desbloquea el laboratorio sin falsas promesas.<br>**B:** Aborda la privacidad desde el inicio. | **A:** Poscompone la privacidad.<br>**B:** Bloquea la fase pre-código hasta redactar política. | **A:** Deuda técnica de privacidad.<br>**B:** Parálisis por especificación. | `evidence-lifecycle-privacy-candidate-v0.md` (**BLOQUEADO** en §3). | Política formal de retención/supresión ratificada. | DEC-01 | **Titular del Proyecto** |
| **DEC-05** | **Oráculos de Falsación (R-01..08)** | **Opción A:** Adoptar R-01..R-08 mapeados a fixtures F/E/L.<br>**Opción B:** Definir nuevos tests ad-hoc. | **A:** Evita duplicación y reutiliza especificaciones.<br>**B:** Cobertura ad-hoc personalizada. | **A:** Requiere mapeo riguroso de taxonomía.<br>**B:** Riesgo de tests redundantes. | **A:** Ambigüedad si no se alinean la procedencia y el juicio.<br>**B:** Fragmentación de oráculos. | `semantic-falsification-cases.md`; `acceptance-cases-v0.md`. | Fixtures sintéticas codificadas en el arnés. | DEC-02, DEC-03 | **Titular del Proyecto** |
| **DEC-06** | **Tecnología de Persistencia** | **Opción A:** Diferir persis. física y usar memoria volátil.<br>**Opción B:** Seleccionar motor (SQLite/Sled/RocksDB) ya. | **A:** Aisla lógica de atestación del soporte de disco.<br>**B:** Prematuro. | **A:** No prueba escrituras en disco.<br>**B:** Decisión rígida sin contrato probado. | **A:** Acoplamiento a estructuras en memoria.<br>**B:** Incompatibilidad con esquema final. | `docs/01-investigacion/security/persistence.md`. | Benchmarks de rendimiento en disco. | DEC-01, DEC-02 | **Titular del Proyecto** |
| **DEC-07** | **Licencia Legal** | **Opción A:** Asignar licencia (e.g., MIT, Apache-2.0, BUSL).<br>**Opción B:** Mantener "Todos los derechos reservados". | **A:** Claridad jurídica para contribuciones.<br>**B:** Protección total en fase privada. | **A:** Exposición legal si no se revisa.<br>**B:** Impide apertura pública (GAP-001). | **A:** Licenciamiento incompatible.<br>**B:** Ambigüedad de propiedad intelectual. | `CONTRIBUTING.md`; `gap-register.md` (`GAP-001`). | Dictamen de idoneidad de licencia. | Ninguna. | **Titular del Proyecto** |
| **DEC-08** | **Autorización de Transición (G2->G3)** | **Opción A:** Mantener HOLD / NO-GO estricto.<br>**Opción B:** Autorizar GO a código Rust tras votar DEC-01..07. | **A:** Cero riesgo de código prematuro.<br>**B:** Permite iniciar implementación. | **A:** No se escribe código.<br>**B:** Exige cumplir todos los gates G0-G2. | **A:** Estancamiento si no se delibera.<br>**B:** Paso a código con brechas P1 abiertas. | `readiness-assessment.md`; `auditoria-integral-2026-10.md` (§4). | Verificación completa de Gates G0-G2. | DEC-01 a DEC-07 | **Titular del Proyecto** |

---

## 3. Alcance y Especificación del Primer Laboratorio Sintético Offline

### 3.1 Activos Sintéticos y Dominio de Prueba
Conforme a `docs/03-preimplementacion/offline-experiment-contract-candidate-v0.md` (§2) y `docs/03-preimplementacion/vertical-slice-a.md`, el primer laboratorio se limita a:
- **Dominio de Prueba:** Evaluación de consistencia bitemporal entre dos sensores de lectura ambiental sintéticos (Sensor A y Sensor B) leyendo un mismo parámetro físico.
- **Volumen de Datos:** Estímulos sintéticos predefinidos en archivos de datos planos o memoria (no streams continuos).

### 3.2 Fronteras de Confianza y Aislamiento Lógico
Conforme a `docs/03-preimplementacion/architecture-boundaries.md` (§2) y `docs/02-diseno/adr/0001-security-first-trust-boundaries.md`:
- **Frontera de Entrada:** Datos inyectados desde el Harness de pruebas externas (**OBSERVADO**).
- **Núcleo Evaluador:** Funciones puras que reciben estructuras en memoria y devuelven dictámenes epistemológicos (**PROPUESTO**).
- **Frontera Operativa:** Denegación por defecto (*deny-by-default*). Ningún dictamen autoriza la ejecución de acciones (**OBSERVADO**).
- **Límite de Aislamiento:** Se explicita que las fronteras son lógicas (*workflow rules*) y no constituyen un Sandbox de sistema operativo contra código malicioso en el mismo proceso (**INFERIDO**).

### 3.3 Entradas, Salidas y Prohibiciones
- **Entradas Sintéticas Permitidas:**
  1. Artefactos sintéticos con identificador, contenido opaco y marcas de tiempo (`valid_time`, `recorded_time`).
  2. Atestaciones de origen emitidas por autoridades sintéticas.
  3. Políticas/Reglas de evaluación cargadas explícitamente en la inicialización del arnés.
- **Salidas Permitidas:**
  1. Dictámenes epistemológicos expresados exclusivamente en la taxonomía candidata preexistente: `SUPPORTED`, `REFUTED`, `CONFLICTED`, `INSUFFICIENT`, `NOT_COMPARABLE`.
  2. Estado de procedencia: `VERIFIED` o `UNVERIFIED`.
  3. Marcas de auditoría sintética con timestamp `assessed_time`.
- **Prohibiciones Estrictas del Laboratorio Sintético:**
  1. **Sin Red:** Prohibida cualquier llamada a sockets, HTTP, DNS o servicios remotos (**OBSERVADO**).
  2. **Sin Persistencia Duradera:** Prohibida la escritura en base de datos o almacenamiento físico continuo (**OBSERVADO**).
  3. **Sin Acceso al Reloj del Sistema:** Las funciones del núcleo deben recibir la marca de tiempo de evaluación como argumento puro, sin invocar funciones de hora del SO (**PROPUESTO**).
  4. **Sin Acciones Operativas:** Cero integración con actuadores, APIs externas o comandos del sistema operativo (**OBSERVADO**).

### 3.4 Condiciones Negativas Verificables (Condiciones de Rechazo)
1. Rechazar cualquier entrada que carezca de la distinción bitemporal `valid_time` y `recorded_time`.
2. Devuelve procedencia `UNVERIFIED` y dictamen `INSUFFICIENT` si una fuente intenta autoverificar su propia autenticidad sin atestación externa.
3. Denegar cualquier intento de mutación directa sobre un artefacto previamente registrado en memoria.
4. Responder `NOT_COMPARABLE` ante la comparación de datos pertenecientes a esquemas o dominios incompatibles sin perfil de mapeo.

---

## 4. Comparación Arquitectónica Neutra (R1 vs. R2 vs. Híbrida vs. Baseline D)

A continuación se establece la matriz de evaluación comparativa bajo criterios y oráculos comunes, **utilizando la Opción D (Control Específico de Dominio) como línea base de comparación (*baseline*), sin declarar ganadores ni presuponer consensos no verificados**:

| Criterio de Comparación | Opción R1 (6 Entidades Unificadas) | Opción R2 (Artifact + Attestation Minimal) | Opción Híbrida (R2 en Núcleo + Grafos Extendidos) | Opción D (Control Específico de Dominio - Baseline) |
|---|---|---|---|---|
| **Estructura Representacional** | 6 tipos explicitados (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`). | 2 tipos base (`Artifact` opaco + `Attestation` de metadatos/firma). | `Artifact` + `Attestation` en el núcleo; grafos R1 construidos bajo demanda por el evaluador. | Definiciones ad-hoc especificadas individualmente por cada perfil de dominio. |
| **Complejidad del Esquema Base** | Mayor número de tipos e interconexiones en el contrato inicial (`unified-specification-candidate-v0.md`). | Menor número de tipos base en el núcleo computable. | Modular: núcleo simple con capacidad de extensión en capa superior. | Inexistencia de contrato común unificado. |
| **Interoperabilidad entre Dominios** | Unificada a través del esquema común de 6 tipos. | Basada en atestaciones estándar sobre artefactos tipados. | Unificada en metadatos primarios; especializada en la extensión. | Nula o dependiente de mapeadores ad-hoc entre dominios (Baseline). |
| **Auditabilidad de Código** | A evaluar empíricamente según complejidad del grafo de tipos. | A evaluar empíricamente según simplicidad de los tipos base. | A evaluar empíricamente en núcleo y extensiones. | Variable y dependiente de cada implementación de dominio. |
| **Oráculo Sintético de Prueba (F-01 / E-01)** | Debe construir el grafo de 6 nodos y verificar consistencia de relaciones. | Debe verificar la firma de la atestación sobre el hash del artefacto. | Debe verificar la atestación e invocar la extensión de grafo si el perfil lo exige. | Debe ejecutar el parser y validador propio del dominio de prueba. |
| **Estado en la Deliberación Pre-código** | Opción candidata en `unified-specification-candidate-v0.md`. | Opción propuesta para evaluación pre-código. | Opción propuesta para evaluación pre-código. | Sirve como línea base (*baseline*) de comparación no estandarizada. |

*Conclusión de Comparación:* La elección entre R1, R2, Híbrida y D debe ser el resultado de medir objetivamente la claridad, determinismo y mantenibilidad durante la evaluación sintética pre-código en `DEC-02`.

---

## 5. Matriz de Falsación: Mapeo de Criterios R-01..R-08 a Fixtures F / E / L

Para evitar duplicaciones y articular los oráculos con la documentación preexistente, se relaciona cada criterio R-01..R-08 (`finch-consolidation-troubleshooting-candidate-v0.md` §5) con los casos de falsación F-01..F-10 (`architecture-paper-falsification-v0.md`), experimentos E-01..E-10 (`offline-experiment-contract-candidate-v0.md`) y ciclo de vida L-01..L-10 (`evidence-lifecycle-privacy-candidate-v0.md`), distinguiendo la dimensión de procedencia, el juicio epistemológico y los errores estructurales:

| Criterio R | Mapeo F / E / L Preexistente | Dimensión de Procedencia | Dimensión de Juicio Epistemológico | Resultado Observable / Error Estructural Esperado |
|---|---|---|---|---|
| **R-01** (Coincidencia Identificador vs Identidad) | **F-01 / F-02 / E-03** | `UNVERIFIED` | `INSUFFICIENT` | Mismo ID sin atestación externa válida no prueba identidad real de origen. |
| **R-02** (Autoverificación de Fuente) | **F-03 / E-03** | `UNVERIFIED` | `INSUFFICIENT` | Declaración que valida su propia autenticidad es rechazada en procedencia. |
| **R-03** (Falsa Corroboración por Dependencia) | **F-04 / E-04** | `VERIFIED` (si declarada) | `INSUFFICIENT` (soporte independiente) | Invariante: ausencia de arista no prueba independencia (**independencia no demostrada**). |
| **R-04** (Anomalía Bitemporal) | **F-05 / E-05** | N/A | `INSUFFICIENT` o abstención | Discrepancia no justificada entre `recorded_time` y `valid_time` registra anomalía y no infla certeza. |
| **R-05** (Mutación Histórica sin Rastro) | **F-06 / E-06 / L-03** | N/A | Error Estructural | Intento de sobrescritura directa es rechazado por la interfaz del Harness (`MUTATION_REJECTED`). |
| **R-06** (Semántica Fuera de Alcance) | **F-07 / E-07** | N/A | `NOT_COMPARABLE` | Datos que no corresponden al dominio del perfil devuelven incompatibilidad explícita. |
| **R-07** (Evaluación Convertida en Comando) | **F-08 / E-08** | N/A | `SUPPORTED` (sin efecto operativo) | Un `Assessment` no desencadena ejecución alguna en el Action Gateway. |
| **R-08** (Gestión de Supresión de Contenido) | **F-10 / E-10 (BLOQUEADO) / L-08** | N/A | N/A | **E-10 BLOQUEADO:** Supresión sintética requiere definir política previa o ser excluida de v0. |

---

## 6. Registro de Bloqueos y Alcance de Mitigación

Para clarificar el estado del proyecto, se distingue estrictamente qué elementos **bloquean la ejecución del primer laboratorio sintético** frente a cuáles constituyen brechas de cobertura global a resolver en fases posteriores:

| ID de Bloqueo / Brecha | Origen / Referencia | Descripción Sintética | Impacto en el Laboratorio Sintético | Pertenencia / Alcance Real | Estado Actual |
|---|---|---|---|---|---|
| **E-10 (Experimento de Privacidad)** | `offline-experiment-contract-candidate-v0.md` (§2) | Experimento de supresión sintética de evidencia. | **BLOQUEANTE si se incluye E-10.** No bloquea el laboratorio si E-10 se excluye explícitamente en `DEC-04`. | Pertenece a la evaluación de privacidad. Requiere política formal de retención/supresión. | **BLOQUEADO** |
| **GAP-001 (Licencia Legal)** | `gap-register.md` (`GAP-001`) | Ausencia de archivo `LICENSE` en el repositorio root. | **NO BLOQUEA** la ejecución de un laboratorio privado offline. | P2 interno / **P1 indispensable previa publicación o distribución pública**. | **OPEN** |
| **GAP-002 (Incobertura de Tests SEC)** | `gap-register.md` (`GAP-002`) | Amenazas `TH-012`, `TH-016` y `TH-019` sin prueba `SEC-XXX` asignada. | **NO BLOQUEA** el laboratorio sintético p3 si se evalúan funciones puras en memoria. | Pertenece a la cobertura global de seguridad del sistema completo. Las propuestas `SEC-015..017` son la vía de cierre. | **OPEN** |
| **GAP-003 (Serialización Bitemporal)** | `gap-register.md` (`GAP-003`) | Falta de especificación formal de tipos y formato bitemporal. | **PARCIALMENTE BLOQUEANTE.** Exige acordar el formato de fechas (ISO-8601 UTC) para las entradas sintéticas. | Pertenece al contrato de datos pre-código. Debe precisarse en el borrador de especificación. | **OPEN** |
| **GAP-004 (Aislamiento de Memoria)** | `gap-register.md` (`GAP-004`) | Ausencia de prueba de aislamiento de memoria entre componentes. | **NO BLOQUEA** el laboratorio sintético offline monolítico. | Pertenece a la seguridad del entorno de ejecución de producción. | **OPEN** |
| **GAP-005 (ADRs en Proposed)** | `gap-register.md` (`GAP-005`) | Todos los ADRs centrales (`0001..0005`) permanecen en estado borrador. | **PARCIALMENTE BLOQUEANTE.** Se requiere votar los ADRs pertinentes tras deliberar `DEC-01..08`. | Pertenece a la gobernanza de arquitectura pre-código. | **OPEN** |
| **GAP-010 (Autoridad Normativa)** | `gap-register.md` (`GAP-010`) | Inexistencia de mapa de autoridad normativa aprobado. | **BLOQUEANTE para pasar a código (G3).** No bloquea la deliberación de este paquete de decisión. | Pertenece a la gobernanza preimplementación. Se resuelve mediante la adopción de `DEC-01..08`. | **OPEN** |

---

## 7. Propuesta de Secuencia de Decisiones para el Titular

Para facilitar un proceso de deliberación ordenado y no paralizante, se clasifica la secuencia recomendada de las decisiones `DEC-01..DEC-08`:

```
[FASE I: DECISIONES INDEPENDIENTES INMEDIATAS]
   ├── DEC-01 (Aprobar alcance exclusivo de Laboratorio Sintético Offline)
   └── DEC-07 (Seleccionar modelo de licencia legal LICENSE para GAP-001)

[FASE II: DECISIONES SINTÉTICAS PRE-CÓDIGO (Requieren DEC-01)]
   ├── DEC-03 (Confirmar núcleo puro de funciones sin E/S ni reloj del SO)
   ├── DEC-04 (Resolver E-10: Excluir del v0 sintético o redactar política previa)
   └── DEC-05 (Aprobar mapeo de oráculos R-01..R-08 a fixtures F/E/L)

[FASE III: DECISIONES EXPERIMENTALES (Requieren evidencia sintética del Laboratorio)]
   ├── DEC-02 (Comparar R1, R2, Híbrida y Baseline D mediante pruebas sintéticas)
   └── DEC-06 (Mantener diferida la tecnología de persistencia física)

[FASE IV: DECISIÓN DE AUTORIZACIÓN FINAL (Puerta de Transición)]
   └── DEC-08 (Mantener HOLD / NO-GO hasta autorización expresa y separada del titular)
```

### 7.1 Decisiones que Pueden Adoptarse De Inmediato
- **`DEC-01`:** Permite fijar las reglas del juego excluyendo red, persistencia física y acciones externas.
- **`DEC-07`:** Resuelve la brecha legal `GAP-001` sin afectar la arquitectura técnica.

### 7.2 Decisiones Condicionadas a la Preparación del Laboratorio
- **`DEC-03`, `DEC-04` y `DEC-05`:** Establecen los límites del arnés sintético y la exclusión o inclusión justificada de E-10.

### 7.3 Decisiones que Deben Quedar Abiertas hasta Obtener Evidencia
- **`DEC-02`:** No debe decidirse prematuramente en papel. Debe ser el resultado de la comparación objetiva de los oráculos sintéticos sobre los borradores de datos.
- **`DEC-06`:** Debe permanecer diferida hasta validar las estructuras puras en memoria.

### 7.4 Decisión de Autorización Final (Puerta de Control)
- **`DEC-08`:** Permanece en **HOLD / NO-GO**. Ninguna votación parcial de DEC-01 a DEC-07 se interpretará como una autorización automática para pasar a la fase de implementación de software (G3).

---

## 8. Resumen para el Titular y Próximos Pasos

### 8.1 Hallazgos Principales
1. El marco preimplementación cuenta con suficiente madurez documental para que el titular pueda abordar las decisiones `DEC-01` a `DEC-07` de forma estructurada.
2. La exclusión explícita del experimento E-10 en `DEC-04` permite desbloquear la especificación del primer laboratorio sintético sin caer en falsas promesas de privacidad.
3. El modelo de amenazas `TH-012`, `TH-016` y `TH-019` dispone de propuestas de prueba trazables (`SEC-015..017`) que deberán integrarse formalmente en el plan de seguridad global.

### 8.2 Intervenciones Expresas Requeridas del Titular
Se solicita la intervención del titular exclusivamente en el plano de gobernanza documental para:
1. **Deliberar sobre `DEC-01`:** Confirmar el alcance exclusivo de laboratorio sintético offline.
2. **Deliberar sobre `DEC-04`:** Indicar si el experimento E-10 se excluye del v0 sintético o si se requiere la redacción previa de la política de retención/supresión.
3. **Deliberar sobre `DEC-07`:** Definir la licencia legal a asignar en `LICENSE` (`GAP-001`).
4. **Ratificar `DEC-08`:** Reconfirmar la continuidad del estado **HOLD / NO-GO** hasta completar la fase pre-código.

*El proyecto se mantiene estrictamente bajo el estado **HOLD / NO-GO**.*
