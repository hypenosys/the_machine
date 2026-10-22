# Evaluación de arquitectura y alternativas — THE MACHINE

**Fecha de auditoría:** Octubre de 2026
**Auditor independiente:** Jules — Principal Software Architect
**Estado:** Informe de auditoría / Propuestas de arquitectura para decisión de gobernanza

---

## 1. Contexto y objeto de evaluación

El presente documento evalúa el modelo ontológico y arquitectónico candidato de **THE MACHINE** expuesto en la especificación candidata (`docs/03-preimplementacion/unified-specification-candidate-v0.md` y `general-epistemic-contract-v0.md`).

La arquitectura candidata (denominada en este informe **Opción A**) propone un núcleo ontológico para la representación del conocimiento y la evidencia, estructurado en seis entidades principales:
1. `Source`: Identificador y procedencia declarada o autenticada.
2. `Artifact`: Datos primarios inmutables.
3. `Claim`: Proposición o afirmación atómica atribuida.
4. `EvidenceLink`: Vínculo explícito entre afirmaciones y artefactos/fuentes.
5. `Assessment`: Evaluación de validez o confianza sobre una `Claim` o `EvidenceLink`.
6. `Relation`: Vínculos semánticos (causalidad, contradicción, equivalencia, superposición).

---

## 2. Análisis del modelo de seis entidades (Opción A - Candidata vigente)

### 2.1. Capacidades proyectadas de la Opción A
- **Estructuración semántica explícita**: Diseñada para proporcionar primitivas explícitas para representar atribuciones, evaluaciones separadas de afirmaciones, enlaces de evidencia e inferencias.
- **Trazabilidad de razonamiento**: Busca permitir auditar el proceso mediante el cual una conclusión fue construida a partir de afirmaciones primarias y evaluaciones.
- **Separación entre afirmación y evaluación**: Al tratar `Assessment` y `Relation` como entidades de primer nivel, pretende permitir que dos agentes sostengan evaluaciones opuestas sobre una misma `Claim` sin alterar la proposición original.

### 2.2. Riesgos e hipótesis de fricción técnica identificados por el auditor
- **Hipótesis de sobrecarga semántica en casos atómicos**:
  Para registrar datos simples (por ejemplo, mediciones de sensores o entradas de logs atómicas), instanciar la estructura completa de seis entidades exige definir identidades, hashes y enlaces de evidencia intermedios. Esto constituye una *hipótesis de complejidad accidental* que deberá ser evaluada experimentalmente mediante prototipos.
- **Serialización e índice de grafos**:
  Representar cada proposición como un nodo en un grafo con seis tipos de bordes y entidades puede incrementar la sobrecarga de serialización, consumo de memoria y complejidad de índices en reposo si se implementa sin optimizaciones de dominio.
- **Incertidumbre en la verificación formal bitemporal**:
  Aunque `unified-specification-candidate-v0.md` (línea 35) menciona explícitamente la distinción entre `valid_time`, `recorded_time` y `assessed_time`, la Opción A carece aún de un esquema formalizado de consulta bitemporal (*time-travel queries*) que defina cómo se comportan las retractaciones históricas en el grafo de persistencia inmutable.

---

## 3. Estudio comparativo de alternativas arquitectónicas

A continuación se comparan cuatro enfoques arquitectónicos **de este informe histórico**, no cuatro identificadores intercambiables con el contrato comparativo posterior. La **Opción A** se conserva como especificación de referencia para la comparación, **no como arquitectura seleccionada o ratificada**; la **Opción B** es una **propuesta alternativa redactada por el auditor**. En el contrato comparativo posterior, estas opciones se denominan R1 (seis entidades) y R2 (dos entidades); las opciones C y D de este informe son **conceptos históricos distintos** de «Híbrida C» y «Baseline D» del contrato comparativo, por lo que no debe presumirse equivalencia sin mapeo explícito.

### Opción A: Núcleo de representación epistemológica (Candidata vigente)
- **Descripción**: Núcleo ontológico con 6 entidades (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`).
- **Ventajas**: Expresividad semántica proyectada, auditoría detallada de razonamiento, desacoplamiento de la evaluación respecto a la afirmación.
- **Inconvenientes / Costes**: Mayor coste de implementación inicial, potencial sobrecarga de serialización y necesidad de gestionar un grafo ontológico complejo.

### Opción B: Núcleo mínimo de procedencia y evaluación delegada (PROPUESTA DEL AUDITOR)
- **Descripción**: Reducir el núcleo inmutable a dos primitivas básicas: `Artifact` (datos con hash, usando algoritmos como BLAKE3 o SHA-256 según se defina) y `Attestation` (afirmaciones firmadas de procedencia/evaluación con marcas temporal bitemporales). La semántica detallada de proposiciones, contradicciones y relaciones se delega a módulos de dominio o motores de reglas externos.
- **Diferenciación técnica**:
  - *Hash de datos*: Garantiza exclusivamente la integridad del contenido (*data integrity*).
  - *Firma de fuente (Attestation)*: Puede acreditar control de una clave sobre el contenido firmado **si se valida criptográficamente**; no garantiza por sí sola identidad civil, veracidad, procedencia física, integridad de una cadena de custodia ni tiempo real de emisión. Requiere política de identidad, confianza y revocación.
- **Ventajas proyectadas**: Mayor simplicidad teórica de implementación en Rust, menor superficie de código en el núcleo y facilidad para evaluar un primer experimento offline.
- **Inconvenientes y Pérdidas Semánticas respecto a la Opción A**:
  - *Pérdida de granularidad en la atribución*: Las afirmaciones individuales dentro de un documento o respuesta de modelo quedan empaquetadas en un único `Artifact`/`Attestation`, dificultando referenciar o retractar una sola frase sin re-evaluar todo el bloque.
  - *Detección de contradicciones diferida*: El núcleo pierde la capacidad de detectar contradicciones de forma estructural o declarativa; toda detección de inconsistencias requiere ejecutar lógica de dominio externa.
  - *Composición de evaluaciones compleja*: Evaluar la validez de una evaluación previa (*meta-assessment*) requiere encadenar atestaciones compuestas, perdiendo la claridad de la entidad nativa `Assessment`.

### Opción C: Arquitectura modular basada en microkernel y capacidades
- **Descripción**: Un microkernel en Rust que solo gestiona el paso de mensajes y el cumplimiento de políticas de seguridad (Action Gateway); las abstracciones epistemológicas se empaquetan como componentes intercambiables.
- **Ventajas**: Aislamiento de componentes; permite reemplazar el modelo de evidencia sin alterar la pasarela de seguridad.
- **Inconvenientes**: Incremento de la complejidad de comunicación inter-proceso (IPC) y sobrecarga en ejecuciones locales desconectadas.

### Opción D: Registro inmutable de eventos criptográficos (Append-Only Ledger)
- **Descripción**: Modelo inspirado en sistemas de Event-Sourcing / Merkle Trees donde cada cambio o evaluación se representa como un evento encadenado inmutable.
- **Ventajas proyectadas**: Trazabilidad secuencial clara y modelo mental de persistencia append-only sencillo.
- **Inconvenientes**: La reconstrucción de vistas o estados actuales requiere proyecciones secundarias obligatorias.

---

## 4. Matriz comparativa de alternativas

| Criterio | Opción A (Candidata) | Opción B (Propuesta Auditor) | Opción C (Microkernel) | Opción D (Merkle Ledger) |
|---|---|---|---|---|
| **Expresividad semántica** | **Alta (Diseño)** | Media / Delegada | Depende del módulo | Basada en eventos |
| **Simplicidad de implementación en Rust** | Moderada | **Alta (Proyectada)** | Baja | Alta |
| **Detección nativa de contradicciones** | **Representación estructural; detección pendiente de reglas y oráculo** | Externa | Externa | Externa |
| **Superficie de código en el núcleo** | Mayor | **Mínima** | Media | Mínima |
| **Facilidad para primer prototipo offline** | Requiere más código | **Más rápida** | Requiere IPC mock | Rápida |

---

## 5. Recomendación y decisión de gobernanza

1. **Mantener la Opción A como referencia documental candidata, sin selección vigente de arquitectura**, hasta que los cotitulares del proyecto, mediante un proceso de gobernanza ratificado, adopten una decisión formal. El «corte A» del README de preimplementación es un alcance funcional, no una decisión sobre R1.
2. **Considerar la Opción B como alternativa de simplificación para una eventual evaluación documental o experimental autorizada** del corte funcional A. El contrato posterior propone R2 (Artifact + Attestation) como alternativa de dos entidades; no se ha autorizado construir el laboratorio ni la pasarela de seguridad, ni se ha demostrado que esta última sea necesaria para el corte offline sin efectos externos.
3. **Aclaración de algoritmos y firmas**: La mención de algoritmos de hash (como BLAKE3 o SHA-256) en este informe se ofrece a título de ejemplo de diseño y no constituye una ratificación oficial de elecciones criptográficas.
4. **No alterar el estado de ningún ADR a `Accepted`** mediante este informe de auditoría: las decisiones de arquitectura deberán formalizarse mediante solicitudes de cambio de ADR independientes acompañadas de evidencia experimental en código.
