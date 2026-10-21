# Contrato Comparativo Neutro para Evaluación Arquitectónica — THE MACHINE (v1)

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Ubicación:** `docs/03-preimplementacion/comparative-contract-v1.md`
**Carácter:** **CANDIDATO NO NORMATIVO** (Especificación técnica de arnés de prueba pre-código; no autoriza implementación ni elige arquitectura ganadora).
**Estado del proyecto:** **HOLD / NO-GO (Cero código ejecutable, cero manifiestos Cargo)**

---

## 1. Propósito e Igualdad de Entradas (Harmonized Harness)

El propósito de este contrato es establecer un marco de pruebas totalmente **neutro, simétrico e imparcial** para comparar experimentalmente cuatro alternativas de representación de evidencia y atestación en el primer laboratorio sintético offline:

1. **Opción R1 (6 Entidades Unificadas):** `Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`.
2. **Opción R2 (Artifact + Attestation Minimalist):** `Artifact` opaco + `Attestation` de metadatos y firma.
3. **Opción Híbrida (C):** Núcleo minimalista `Artifact` + `Attestation` con perfil de extensión de grafos tipados bajo demanda.
4. **Opción Baseline D (Control Específico de Dominio):** Representación ad-hoc estructurada directamente sobre el dominio de telemetría sin capa genérica.

### 1.1 Invariante de Simetría de Entradas
Todas las arquitecturas bajo prueba (R1, R2, Híbrida C, Baseline D) recibirán **exactamente los mismos estímulos de entrada sintéticos**, empaquetados en un formato neutro visible para el Harness (ej. estructuras JSON sintéticas). Ninguna arquitectura recibirá información previa privilegiada ni formatos adaptados a su estructura interna.

---

## 2. Separación entre Resultado Observable y Mecanismo Interno

### 2.1 Principio del Oráculo Independiente
Un error metodológico frecuente consiste en presuponer que la propia estructura interna de datos constituye el oráculo de verificación. Se establece formalmente que:
- **Un Grafo de Conocimiento (R1)** no es el oráculo; es una estructura interna de representación.
- **Una Firma Criptográfica o Hash SHA-256** no constituyen por sí mismos el oráculo epistemológico; son mecanismos de integridad de transporte y atestación.
- **El Oráculo Común** es la función de evaluación pura definida por las reglas del perfil de dominio, la cual examina las entradas visibles y emite un veredicto observable.

### 2.2 Vocabulario de Resultados Observables
Toda arquitectura bajo prueba debe producir un resultado interpretable por el Harness en los siguientes términos de dictamen epistemológico:
- `SUPPORTED`: La evidencia sintética respalda la afirmación según las reglas y tolerancias del perfil.
- `REFUTED`: La evidencia sintética contradice o refuta explícitamente la afirmación.
- `CONFLICTED`: Existen dos o más evidencias sintéticas incompatibles en el mismo ámbito y ventana temporal; ambas evidencias son preservadas sin elegir una «verdad» arbitraria.
- `INSUFFICIENT`: La evidencia es incompleta, carece de atestación requerida o proviene de dependencias no independientes.
- `NOT_COMPARABLE`: Las entradas corresponden a unidades, ámbitos, versiones o escalas no comparables sin un convertidor autorizado.

---

## 3. Semántica Temporal e Independencia de Tiempos

### 3.1 Las Tres Dimensiones Temporales
Conforme a `claim-semantics-v0.md` y en subsanación del Defecto B-04, se definen y preservan tres dimensiones temporales completamente independientes:
1. `valid_time`: Timestamp o intervalo opcional de validez del hecho en el mundo real.
2. `recorded_time`: Timestamp opcional de ingreso o registro de la atestación en la memoria del sistema.
3. `assessed_time`: Timestamp opcional en que la regla del evaluador emitió el juicio.

```
+-----------------------------------------------------------------------------------+
| DIMENSIONES TEMPORALES INDEPENDIENTES                                            |
|                                                                                   |
|  [valid_time]    ---> ¿Cuándo ocurrió el hecho sintético? (Opcional)            |
|  [recorded_time] ---> ¿Cuándo fue ingerida la atestación? (Opcional)             |
|  [assessed_time] ---> ¿Cuándo se emitió el dictamen del evaluador? (Opcional)     |
+-----------------------------------------------------------------------------------+
```

### 3.2 Opcionalidad y Ausencia de Timestamps
La ausencia de cualquiera de las tres marcas temporales **NO constituye un error de sintaxis o esquema (`MALFORMED`)**. Una lectura de sensor sin `valid_time` es una entrada válida cuyos efectos de comparabilidad temporal serán resueltos por las reglas del perfil de dominio (ej. emitiendo `NOT_COMPARABLE` o `INSUFFICIENT` si la regla exige coincidencia temporal explícita).

---

## 4. Criterios Comparativos, Condiciones de Refutación y Abstención

### 4.1 Criterios Comparativos Objetivos
Las cuatro alternativas (R1, R2, Híbrida C, Baseline D) serán evaluadas en el laboratorio pre-código bajo los siguientes criterios sin asignación arbitraria de puntuaciones previas:
1. **Fidelidad de Representación:** Capacidad de expresar todos los fixtures (F-01..F-10) sin perder contexto, marcas de tiempo ni procedencia.
2. **Sobrecarga de Tipos (Complejidad Accidental):** Número de entidades y relaciones requeridas por cada fixture.
3. **Auditabilidad y Trazabilidad:** Facilidad para rastrear el origen de una contradicción o la retractación de un dato.
4. **Resiliencia ante Insumos Incompletos:** Comportamiento frente a ausencias de atestación, unidades desconocidas o marcas temporales omitidas.

### 4.2 Condiciones de Refutación de un Modelo
Se considerará que una arquitectura (R1, R2, Híbrida C o D) **ha sido refutada por un fixture** si incurre en alguno de los siguientes fallos observables:
- **Elegir una «verdad» arbitraria** ante datos contradictorios en lugar de emitir `CONFLICTED` (Fallo en F-01).
- **Convertir unidades incompatibles** sin una regla explícita de normalización en lugar de emitir `NOT_COMPARABLE` (Fallo en F-02).
- **Ascender una fuente no autenticada** a estado `VERIFIED` basándose únicamente en el contenido textual de la declaración (Fallo en F-03).
- **Contar una dependencia compartida conocida** como corroboración independiente (Fallo en F-04).
- **Sobrescribir o borrar silenciosamente** el historial ante una corrección o retractación (Fallo en F-05 / L-01).
- **Colapsar o inferir simultaneidad** ante marcas temporales distintas o ausentes (Fallo en F-06).

### 4.3 Condiciones de Abstención Justificada
El arnés de prueba aceptará como respuesta válida y correcta la **abstención justificada** (`NOT_COMPARABLE` o `INSUFFICIENT_EVIDENCE`) cuando los insumos sintéticos carezcan de la información mínima requerida por las reglas del perfil para emitir un juicio definitivo. La abstención justificada se distingue explícitamente de un fallo de ejecución o error interno del sistema (`INTERNAL_FAILURE`).
