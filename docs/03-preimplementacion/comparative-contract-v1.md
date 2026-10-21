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
2. **Opción R2 (Artifact + Attestation Minimalist):** `Artifact` opaco + `Attestation` de metadatos y procedencia; cualquier firma criptográfica es una capacidad futura no evaluada en este laboratorio.
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

**Distinción de Fallos Internos:** Se distingue estrictamente el juicio epistemológico (`INSUFFICIENT`, `NOT_COMPARABLE`) de las condiciones de error del sistema o del harness. Se conserva el vocabulario candidato completo del contrato offline original, sin asumir que todas las etiquetas se ejecutarán en el primer corte:
- `MALFORMED`: Entrada estructuralmente inválida que viola el esquema de serialización.
- `UNSUPPORTED_PROFILE`: Perfil no reconocido.
- `UNRESOLVED_REFERENCE`: Referencia no resoluble.
- `LIMIT_EXCEEDED`: Se excede un límite de recursos declarado.
- `INTERNAL_FAILURE`: Error inesperado de ejecución en el arnés de prueba.

**Estado de procedencia declarado en el laboratorio:** `VERIFIED`/`UNVERIFIED` son atributos de entrada del fixture, definidos por el oráculo externo, no el resultado de una firma generada o validada por R1/R2/C/D. Ninguna arquitectura puede autoconcederse autenticidad por texto, hash o estructura. La comparación no mide criptografía ni gestión de claves.

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
1. **Fidelidad de Representación:** Capacidad de expresar F-01..F-09 y los casos adicionales expresamente autorizados sin perder contexto, marcas de tiempo ni procedencia; F-10/E-10 original permanece BLOQUEADO.
2. **Sobrecarga de Tipos (Complejidad Accidental):** Número de entidades y relaciones requeridas por cada fixture.
3. **Auditabilidad y Trazabilidad:** Facilidad para rastrear el origen de una contradicción o la retractación de un dato.
4. **Resiliencia ante Insumos Incompletos:** Comportamiento frente a ausencias de atestación, unidades desconocidas o marcas temporales omitidas.
5. **Transferencia a Segundo Dominio:** Evaluación con al menos un segundo perfil sintético no basado en sensores, con oráculos específicos previamente definidos. No se podrá declarar generalidad del núcleo con un único dominio.
6. **Coste de Serialización y Versionado:** Cambios de formato, migración de perfiles, compatibilidad de versiones y esfuerzo de mantenimiento comparados con el mismo criterio para las cuatro alternativas.
7. **Acoplamiento Núcleo–Perfil:** Identificar modificaciones del núcleo necesarias al introducir el segundo dominio y distinguir complejidad desplazada a perfiles de complejidad eliminada.
8. **Complejidad Semántica y Operativa:** No reducir la comparación al número de tipos; documentar transformaciones auxiliares, excepciones, reglas y cambios requeridos para conservar la misma semántica.

**Límite de ejecución:** F-10/E-10 original está BLOQUEADO; su inclusión en una lista de cobertura documental no lo habilita para ejecución. El primer laboratorio, si se autoriza, cubrirá F-01..F-09 y casos adicionales aprobados de forma expresa.

### 4.3 Segundo dominio: casos documentales de referencia (sin oráculo ratificado)

El segundo dominio no se inventa desde la telemetría: los ejemplos `A6` y `A7` de `architecture-paper-falsification-v0.md` afirman respectivamente uso y ausencia de red en versiones **2.1 y 2.3** del módulo X. El caso `HET-002` de `heterogeneous-cases.md` compara afirmaciones sobre versiones de documentación; `HET-003` contrasta afirmaciones sobre comportamiento de software y la diferencia entre ausencia observada y ausencia universal.

- **Expectativa conceptual A6/A7:** no inferir conflicto sin equiparar versión, alcance y modalidad; conservar atribución. Una afirmación documental no autentica el comportamiento del módulo.
- **Expectativa conceptual HET-002:** preservar ambas citas y versiones; no privilegiar automáticamente la fuente más reciente.
- **Expectativa conceptual HET-003:** no inferir que una conexión es imposible por no haber sido observada en un test limitado.
- **Control metodológico:** R1, R2, C y D reciben exactamente las mismas afirmaciones sintéticas y condiciones de comparabilidad. Registrar cuándo el control D debe ampliar su esquema para representar el segundo dominio.

Estos son **oráculos conceptuales candidatos**, no fixtures normalizados ni reglas versionadas. Antes de G2.2 deberán fijarse payloads, esquema, versiones, resultados esperados y controles negativos para ambos dominios, sin ejecutar ni declarar PASS ahora.

### 4.4 Perfil de sensores y núcleo general (REV-17; contraste candidato)

`design-freeze-candidate-v0.md` define **exclusivamente para el perfil sintético de temperatura**: esquema `evidence.v0`, `temperature` en enteros `milli_degC`, tolerancia ilustrativa `1000 milli_degC`, coincidencia del instante normalizado UTC y salida de comparación `COMPATIBLE | CONFLICTO | NO_COMPARABLE`. Son propuestas sin ratificar. `precode-review-checklist.md` confirma pendientes el parser, segundos intercalares, precisión, errores y límites. **No se extrapolan al núcleo general** ni al segundo dominio.

El contrato offline genérico admite tres tiempos independientes `valid_time`, `recorded_time` y `assessed_time` con presencia opcional o determinada por perfil. Un instante obligatorio en el perfil de sensor no convierte todos los timestamps del núcleo en obligatorios. `CONFLICTO` es un resultado de **comparación de dos lecturas** del perfil; `CONFLICTED` es un **dictamen epistemológico** sobre afirmaciones y evidencia. `COMPATIBLE` no implica `SUPPORTED`, ni `NO_COMPARABLE` del perfil equivale automáticamente al dictamen `NOT_COMPARABLE` sin regla explícita de traducción.

**Obligación previa a G2.2 (no satisfecha):** versionar por separado `sensor-profile.v0` y contrato genérico, definir el adaptador y tabla de traducción de estados, precisar tolerancia, normalización UTC, precisión temporal, unidades y tratamiento de datos ausentes. Una comparación que confunda esos niveles debe declararse `NO EVALUABLE`, no `PASS`.

### 4.5 Condiciones de Abstención Justificada
En un ensayo futuro expresamente autorizado, la **abstención justificada** (`NOT_COMPARABLE` o `INSUFFICIENT`) solo será un resultado conforme **cuando el oráculo independiente y versionado la haya fijado de antemano para ese caso**. No toda abstención es correcta: si las entradas permiten un juicio y la arquitectura se abstiene indebidamente, existe una discrepancia que debe investigarse. La abstención se distingue de fallos de ejecución como `INTERNAL_FAILURE`, y de la falta de observabilidad del harness.

### 4.6 Atribución de fallos y controles de observación (propuesta no ejecutada)

La matriz `traceability-matrix-v1.md` §5 propone una clasificación de diagnóstico para F-11/F-12. Como criterio comparativo **candidato** para R1, R2, C y D, la clasificación se aplicaría de forma simétrica y previa a cualquier puntuación:

- **`NO EVALUABLE — OBSERVADOR/VISIBILIDAD`:** el control positivo no llega a la misma ruta de observación o no es posible diferenciar silencio del sistema de silencio del instrumento.
- **`NO EVALUABLE — ORÁCULO`:** faltan reglas, versión o expectativas inequívocas; no atribuir el resultado a la arquitectura.
- **`FALLO OBSERVADO — PENDIENTE DE ATRIBUCIÓN`:** el instrumento y el oráculo están controlados, pero una salida discrepa; conservar evidencia y separar fallo del núcleo, perfil, adaptador y harness.
- **`COINCIDENCIA EN EL CASO`:** las salidas coinciden con expectativas fijadas y los controles funcionan; no equivale a seguridad general, cobertura completa ni `GO`.

**Criterio de comparabilidad:** las cuatro alternativas reciben idénticas entradas, reglas y criterios de diagnóstico; un defecto del observador compartido no puede computarse como cuatro defectos de arquitectura ni como cuatro éxitos. No atribuir independencia al observador por estar descrito en otro documento: habrá que demostrar que su punto de fallo relevante es separado. No se autoriza instrumentación, código, almacenamiento persistente, pruebas ni G2.2 mediante esta sección.


### 4.7 Regla candidata de denominadores y comparaciones justas (sin resultados)

Una comparación entre arquitecturas no debe esconder los casos sin medición ni convertir errores de infraestructura en resultados epistemológicos. Se propone fijar, **antes de cualquier ensayo autorizado**, un manifiesto común de casos y un reporte con columnas separadas:

| Campo documental | Significado y restricción |
|---|---|
| `case_id`, `oracle_revision`, `profile_revision` | Identidad y versiones previas del caso; ausencia => `NO EVALUABLE — ORÁCULO` |
| `architecture_id`, `adapter_revision` | Alternativa R1/R2/C/D y traducción aplicada; no equiparar salidas semánticas por similitud de etiquetas |
| `expected`, `observed` | Resultado esperado fijado independientemente y salida registrada; no deducir `expected` de `observed` |
| `observer_control`, `visibility` | Evidencia de que los controles y el canal de observación funcionaron; silencio sin control => `NO EVALUABLE` |
| `diagnosis`, `attribution` | Distinguir coincidencia, discrepancia, error de sistema y caso no evaluable; atribución causal puede seguir pendiente |
| `scope_exclusions` | Registrar límites de laboratorio (sin red, persistencia, gateway o criptografía real), no tratarlos como controles demostrados |

**Partición de resultados y denominadores (candidata):** por cada `case_id` y arquitectura, registrar **exactamente un estado terminal** de la siguiente partición, sin contar el mismo caso en dos categorías: `NO EVALUABLE` (instrumento/oráculo/visibilidad insuficientes), `ERROR DE SISTEMA` (ejecución fallida con observación válida), `DISCREPANCIA` (salida válida pero contraria al oráculo) o `COINCIDENCIA` (salida válida conforme al oráculo). Las causas detalladas, abstenciones y atribuciones son **atributos secundarios**, no categorías adicionales que se sumen al total. Un `INTERNAL_FAILURE` observable es `ERROR DE SISTEMA`, no una abstención válida. Un `NOT_COMPARABLE` o `INSUFFICIENT` conforme al oráculo es `COINCIDENCIA`; si el oráculo exigía otro dictamen, es `DISCREPANCIA`.

**Invariantes de recuento propuestos:** `planificados = no_evaluables + errores_sistema + discrepancias + coincidencias` para cada arquitectura/dominio, incluyendo casos retirados o no intentados dentro de `NO EVALUABLE` con motivo explícito. `elegibles = errores_sistema + discrepancias + coincidencias` **solo si** «elegible» se define como caso con oráculo e instrumentación válidos; no reutilizar el término para «caso inicialmente seleccionado». Registrar ambas cifras `planificados` y `elegibles` y las razones de exclusión. Una tasa descriptiva de coincidencia, si se llegase a autorizar, deberá mostrar tanto `coincidencias/elegibles` como `coincidencias/planificados`, sin etiquetarlas como seguridad, calidad global o `PASS`. No asignar ventaja a una arquitectura por abstenerse más, omitir casos difíciles o disponer de un adaptador menos exigente.

**Criterio de bloqueo:** si faltan reglas comunes, controles válidos o equivalencia de entradas, la comparación cruzada queda `NO EVALUABLE`; no hay ganador ni `GO`. Esta sección no fija cifras, umbrales de aprobación ni autoriza ejecutar pruebas. **HOLD / NO-GO**.
