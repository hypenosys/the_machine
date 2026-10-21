# Evaluación crítica de arquitectura y alternativas — THE MACHINE

**Fecha de auditoría:** Octubre de 2026
**Auditor independiente:** Jules — Principal Software Architect & Team de Auditoría
**Estado:** Final / Entregable de Auditoría

---

## 1. Resumen ejecutivo

El presente documento constituye la evaluación crítica e independiente de la arquitectura propuesta para **THE MACHINE**. Analiza la validez, suficiencia y necesidad del núcleo epistemológico candidato (compuesto por las seis abstracciones principales: `Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`), contrasta cuatro alternativas de diseño arquitectónico y evalúa los riesgos de complejidad accidental, rendimiento y mantenibilidad antes de autorizar la escritura del primer archivo de código en Rust.

---

## 2. Evaluación crítica del núcleo epistemológico candidato

La especificación candidata propone un núcleo ontológico uniforme para la representación del conocimiento y la evidencia, estructurado en seis entidades:

1. **`Source`**: Identificador y procedencia declarada o autenticada de la información.
2. **`Artifact`**: Datos primarios inmutables (archivos, respuestas de APIs, mediciones de sensores).
3. **`Claim`**: Afirmación o proposición atómica extraída o derivada de un artefacto.
4. **`EvidenceLink`**: Enlace explícito que vincula una `Claim` con uno o más `Artifact`s o `Claim`s previas.
5. **`Assessment`**: Evaluación de validez, confianza o falsabilidad sobre una `Claim` o `EvidenceLink`.
6. **`Relation`**: Vínculos semánticos entre entidades (causalidad, contradicción, equivalencia, superposición).

### 2.1. Inconsistencias y lagunas conceptuales identificadas

Tras someter el modelo a un análisis adversarial de lógica computacional y teoría de procedencia, se observan las siguientes limitaciones fundamentales:

- **Falta de semántica bitemporal (Valid Time vs. Transaction Time)**:
  El núcleo actual registra una marca de tiempo (*timestamp*). Sin embargo, no distingue entre la fecha en que una afirmación ocurrió en el mundo real (*valid time*) y la fecha en que la afirmación fue registrada en la base de conocimientos (*transaction time*). Esta laguna impide gestionar retractaciones históricas o correcciones retroactivas de datos sin destruir la trazabilidad inmutable del registro de auditoría (*append-only log*).

- **Complejidad accidental masiva en casos simples**:
  Para registrar un dato elemental (por ejemplo, "el sensor de temperatura A midió 22.5 °C a las 10:00"), el sistema exige instanciar las 6 entidades, generar hashes criptográficos y establecer enlaces de evidencia intermedios. Esta sobrecarga conceptual y computacional puede ahogar el rendimiento de ingestión y dificultar la adopción por parte de desarrolladores de dominios específicos.

- **Falta de cuantificadores y semántica de negación**:
  Una `Claim` se define como un enunciado. El sistema no especifica cómo representar proposiciones compuestas, negaciones explícitas ("X no es la causa de Y") ni cuantificadores universales o existenciales. Si la semántica de la negación se delega totalmente al texto o al dominio, el núcleo pierde la capacidad de detectar contradicciones lógicas de forma automatizada.

- **Riesgo de explosión combinatoria de `Relation`s**:
  Al permitir relaciones arbitrarias entre entidades, el grafo de conocimiento corre el riesgo de sufrir una explosión combinatoria de bordes (*edges*), complicando las consultas de procedencia (*provenance queries*) y requiriendo algoritmos de recorrido de grafos con complejidad $O(N^2)$ o superior.

---

## 3. Análisis comparativo de alternativas arquitectónicas

Para determinar la estructura óptima de THE MACHINE, se evalúan minuciosamente cuatro alternativas arquitectónicas distintas:

### Opción A: Núcleo epistemológico general con adaptadores especializados (Propuesta actual)
- **Descripción**: Un núcleo central rígido con las 6 abstracciones epistemológicas; los dominios se adaptan mediante mapeadores.
- **Ventajas**: Uniformidad total en las consultas de auditoría y evidencia; abstracción agnóstica del dominio.
- **Inconvenientes**: Sobreingeniería prematura, alto coste de serialización, rigidez ontológica y elevada barrera de entrada.
- **Superficie de ataque**: Amplia (múltiples tipos de entidades expuestos a parsing y deserialización).
- **Complejidad de mantenimiento**: Alta.

### Opción B: Núcleo mínimo de procedencia y evaluación con semántica delegada (Recomendada)
- **Descripción**: El núcleo solo gestiona dos primitivas inmutables: `Artifact` (datos con hash SHA-256/BLAKE3) y `Attestation` (afirmaciones firmadas de procedencia/evaluación con marcas temporal bitemporales). Tontos en semántica, sabios en procedencia.
- **Ventajas**: Extrema simplicidad, máximo rendimiento, minimización de dependencias en Rust, fácil de probar y verificar formalmente.
- **Inconvenientes**: La detección de contradicciones lógicas complejas se traslada a los módulos de dominio o motores de políticas externos.
- **Superficie de ataque**: Mínima (superficie de manipulación de datos reducida a verificación de firmas e hashes).
- **Complejidad de mantenimiento**: Muy baja.

### Opción C: Arquitectura modular basada en capacidades independientes (Micro-kernel)
- **Descripción**: Un microkernel en Rust que solo expone el paso de mensajes y el cumplimiento de políticas de seguridad (Action Gateway); los módulos de evidencia y lógica son plugins independientes.
- **Ventajas**: Aislamiento de fallos estricto; permite sustituir el motor epistemológico sin tocar la seguridad.
- **Inconvenientes**: Mayor overhead de IPC (comunicación inter-proceso) y complejidad de despliegue local.
- **Superficie de ataque**: Media (requiere sandbox para los plugins).
- **Complejidad de mantenimiento**: Media-Alta.

### Opción D: Event-Sourcing Criptográfico estricto (Append-Only Provenance Ledger)
- **Descripción**: Representar toda evolución de conocimiento como un registro de eventos inmutables encadenados por hashes (similar a Git/Merkle Tree), sin abstracciones ontológicas predefinidas.
- **Ventajas**: Reproducibilidad matemática perfecta, fácil verificación de integridad, modelo mental de persistencia extremadamente claro.
- **Inconvenientes**: Las consultas ad-hoc o vistas proyectadas requieren construir índices secundarios explícitos.
- **Superficie de ataque**: Mínima.
- **Complejidad de mantenimiento**: Baja.

---

## 4. Matriz comparativa de alternativas

| Criterio | Opción A (Actual) | Opción B (Mínima - Recomendada) | Opción C (Microkernel) | Opción D (Merkle Ledger) |
|---|---|---|---|---|
| **Simplicidad de implementación** | Búscar / Baja | **Muy Alta** | Media | Alta |
| **Facilidad de verificación en Rust** | Difícil | **Excelente** | Media | Excelente |
| **Superficie de ataque de seguridad** | Grande | **Mínima** | Media | Mínima |
| **Sobrecarga de rendimiento** | Alta | **Mínima** | Media | Muy Baja |
| **Capacidad de evolución** | Rigida | **Muy Flexible** | Flexible | Flexible |
| **Riesgo de sobreingeniería** | **Crítico** | Bajo | Medio | Bajo |

---

## 5. Recomendación y dictamen arquitectónico

Se dictamina la **desestimación de la Opción A** en favor de una transición hacia la **Opción B (o una hibridación B + D)**.

### Razón del dictamen:
Iniciar la implementación de THE MACHINE en Rust utilizando las 6 entidades rígidas de la Opción A impondrá una pesada deuda técnica desde el primer día. Un sistema de evidencia confiable debe basarse ante todo en la **integridad de los datos primarios y sus firmas de procedencia** (Opción B/D), permitiendo que la interpretación semántica evolucione sin necesidad de migrar o corromper el motor de persistencia central.
