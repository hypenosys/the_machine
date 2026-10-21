# Contrato Comparativo Neutro para Evaluación Arquitectónica — THE MACHINE (v1)

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Ubicación:** `docs/03-preimplementacion/comparative-contract-v1.md`
**Carácter:** **CANDIDATO NO NORMATIVO / MARCO CANDIDATO INCOMPLETO** (Especificación de pautas pre-código; no autoriza implementación, no contiene cargas fijadas ni elige arquitectura ganadora).
**Estado del proyecto:** **HOLD / NO-GO (Cero código ejecutable, cero manifiestos Cargo)**

---

## 1. Propósito y Carácter Incompleto del Marco

El propósito de este contrato es establecer pautas neutras e imparciales para comparar experimentalmente cuatro alternativas de representación de evidencia y atestación en el primer laboratorio sintético offline:

1. **Opción R1 (6 Entidades Unificadas):** `Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`.
2. **Opción R2 (Artifact + Attestation Minimalist):** `Artifact` opaco + `Attestation` de metadatos y firma.
3. **Opción Híbrida (C):** Núcleo minimalista `Artifact` + `Attestation` con perfil de extensión de grafos tipados bajo demanda.
4. **Opción Baseline D (Control Específico de Dominio):** Representación ad-hoc estructurada directamente sobre el dominio de telemetría sin capa genérica.

### 1.1 Declaración Explícita de Incompletitud Pre-código
Se declara formalmente que este documento **es un marco candidato incompleto** (*incomplete candidate framework*). Establece los principios de comparación pero **NO fija todavía**:
- Ficheros payload concretos con datos sintéticos finales.
- Umbrales y tolerancias numéricas explícitas de comparación.
- Conjuntos de reglas versionadas del oráculo.
- Esquema de serialización normalizado de salida.

### 1.2 Precondiciones Obligatorias para una Comparación Reproducible
Antes de ejecutar cualquier prueba experimental comparativa en el laboratorio sintético, se requiere satisfacer las siguientes precondiciones:
1. **Fixtures sintéticos normalizados:** Definición de ficheros de entrada sintéticos idénticos en formato neutro (ej. JSON sintético).
2. **Oráculo de reglas versionado:** Especificación previa e inmutable de la lógica de evaluación del perfil.
3. **Criterios de tolerancia formalizados:** Definición exacta de límites de diferencia aceptable para datos continuos.
4. **Esquema de salida unificado:** Formato de reporte estandarizado para registrar veredictos y tiempos.

---

## 2. Separación entre Resultado Observable, Mecanismo Interno y Errores del Sistema

### 2.1 Principio del Oráculo Independiente
Un error metodológico frecuente consiste en presuponer que la propia estructura interna de datos constituye el oráculo de verificación. Se establece formalmente que:
- **Un Grafo de Conocimiento (R1)** no es el oráculo; es una estructura interna de representación.
- **Una Firma Criptográfica o Hash SHA-256** no constituyen por sí mismos el oráculo epistemológico; son mecanismos de integridad de transporte y atestación.
- **El Oráculo Común** es la función de evaluación pura definida por las reglas del perfil de dominio, la cual examina las entradas visibles y emite un veredicto observable.

### 2.2 Vocabulario Epistémico y Distinción de Fallos de Ejecución
Toda arquitectura bajo prueba debe producir un resultado interpretable por el Harness en los siguientes términos de dictamen epistemológico estandarizados:
- `SUPPORTED`: La evidencia sintética respalda la afirmación según las reglas y tolerancias del perfil.
- `REFUTED`: La evidencia sintética contradice o refuta explícitamente la afirmación.
- `CONFLICTED`: Existen dos o más evidencias sintéticas incompatibles en el mismo ámbito y ventana temporal; ambas evidencias son preservadas sin elegir una «verdad» arbitraria.
- `INSUFFICIENT`: La evidencia es incompleta, carece de atestación requerida o proviene de dependencias no independientes.
- `NOT_COMPARABLE`: Las entradas corresponden a unidades, ámbitos, versiones o escalas no comparables sin un convertidor autorizado.

**Distinción de Fallos Internos:** Se distingue estrictamente el juicio epistemológico (`INSUFFICIENT`, `NOT_COMPARABLE`) de las condiciones de error del sistema o del harness:
- `MALFORMED`: Entrada estructuralmente inválida que viola el esquema de serialización.
- `INTERNAL_FAILURE`: Error inesperado de ejecución en el arnés de prueba.

---

## 3. Semántica Temporal e Independencia de Tiempos

### 3.1 Las Tres Dimensiones Temporales
Conforme a `claim-semantics-v0.md` y en subsanación del Defecto B-04, se definen y preservan tres dimensiones temporales completamente independientes:
1. `valid_time`: Timestamp o intervalo opcional de validez del hecho en el mundo real.
2. `recorded_time`: Timestamp opcional de ingreso o registro de la atestación en la memoria del sistema.
3. `assessed_time`: Timestamp opcional en que la regla del evaluador emitió el juicio.

### 3.2 Opcionalidad y Ausencia de Timestamps
La ausencia de cualquiera de las tres marcas temporales **NO constituye un error de sintaxis o esquema (`MALFORMED`)**. Una lectura de sensor sin `valid_time` es una entrada válida cuyos efectos de comparabilidad temporal serán resueltos por las reglas del perfil de dominio (ej. emitiendo `NOT_COMPARABLE` o `INSUFFICIENT` si la regla exige coincidencia temporal explícita).

---

## 4. Criterios Comparativos, Hipótesis de Representación y Abstención

### 4.1 Delimitación entre Hipótesis de Representación y Defectos de Implementación
Un fallo de ejecución en un test de laboratorio **no refuta automáticamente a una arquitectura completa (R1/R2/C/D)** si la causa raíz es un defecto menor de implementación del arnés o un error de código puntual.
- **Refutación por Representación:** Ocurre solo si la estructura del modelo es conceptualmente incapaz de expresar las relaciones o distinciones exigidas por un fixture (ej. imposibilidad estructural de representar bitemporalidad o procedencia).
- **Defecto de Implementación:** Error en el código de prueba que puede corregirse sin alterar la hipótesis de representación de la arquitectura.

### 4.2 Criterios Comparativos Objetivos
Las cuatro alternativas (R1, R2, Híbrida C, Baseline D) serán evaluadas en el laboratorio pre-código bajo los siguientes criterios sin asignación arbitraria de puntuaciones previas:
1. **Fidelidad de Representación:** Capacidad de expresar todos los fixtures (F-01..F-10) sin perder contexto, marcas de tiempo ni procedencia.
2. **Sobrecarga de Tipos (Complejidad Accidental):** Número de entidades y relaciones requeridas por cada fixture.
3. **Auditabilidad y Trazabilidad:** Facilidad para rastrear el origen de una contradicción o la retractación de un dato.
4. **Resiliencia ante Insumos Incompletos:** Comportamiento frente a ausencias de atestación, unidades desconocidas o marcas temporales omitidas.
5. **Transferencia a Segundo Dominio:** Evaluación con al menos un segundo perfil sintético no basado en sensores, con oráculos específicos previamente definidos. No se podrá declarar generalidad del núcleo con un único dominio.
6. **Coste de Serialización y Versionado:** Cambios de formato, migración de perfiles, compatibilidad de versiones y esfuerzo de mantenimiento comparados con el mismo criterio para las cuatro alternativas.
7. **Acoplamiento Núcleo–Perfil:** Identificar modificaciones del núcleo necesarias al introducir el segundo dominio y distinguir complejidad desplazada a perfiles de complejidad eliminada.
8. **Complejidad Semántica y Operativa:** No reducir la comparación al número de tipos; documentar transformaciones auxiliares, excepciones, reglas y cambios requeridos para conservar la misma semántica.

**Límite de ejecución:** F-10/E-10 original está BLOQUEADO; su inclusión en una lista de cobertura documental no lo habilita para ejecución. El primer laboratorio, si se autoriza, cubrirá F-01..F-09 y casos adicionales aprobados de forma expresa.

### 4.3 Condiciones de Abstención Justificada
El arnés de prueba aceptará como respuesta válida y correcta la **abstención justificada** (`NOT_COMPARABLE` o `INSUFFICIENT`) cuando los insumos sintéticos carezcan de la información mínima requerida por las reglas del perfil para emitir un juicio definitivo. La abstención justificada se distingue explícitamente de un fallo de ejecución o error interno del sistema (`INTERNAL_FAILURE`).
