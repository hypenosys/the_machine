# Matriz de Trazabilidad y Correspondencia Falsable — THE MACHINE (v1)

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Ubicación:** `docs/03-preimplementacion/traceability-matrix-v1.md`
**Carácter:** **CANDIDATO NO NORMATIVO** (Matriz de trazabilidad y correspondencia de pruebas sintéticas pre-código).
**Estado del proyecto:** **HOLD / NO-GO (Cero código ejecutable, cero manifiestos Cargo)**

---

## 1. Metodología de Correspondencia Reconstruida

En estricta atención al **Defecto B-02**, la presente matriz reconstruye de manera rigurosa la trazabilidad entre:
- **Criterios de Falsación R-01..R-08** (definidos en `finch-consolidation-troubleshooting-candidate-v0.md` §5).
- **Fixtures Sintéticos F-01..F-10** (definidos en `precode-decision-protocol-v0.md`).
- **Oráculos de Aceptación E-01..E-10** (definidos en `offline-experiment-contract-candidate-v0.md` §4).
- **Escenarios de Ciclo de Vida y Privacidad L-01..L-10** (definidos en `evidence-lifecycle-privacy-candidate-v0.md`).

### Reglas Metodológicas de Mapeo
1. **Verificación de Definiciones Literales:** Ninguna correspondencia se asigna por mera asociación temática superficial. Cada vínculo exige una justificación conceptual directa y verificable basada en el texto literal de la especificación original.
2. **Tratamiento de Ausencia de Fixtures ("SIN FIXTURE DIRECTO"):** Cuando un criterio R carece de un fixture directo en la serie F-01..F-10 o E-01..E-10, se registra explícitamente el texto **"SIN FIXTURE DIRECTO"** y se propone formalmente un nuevo caso sintético (ej. F-11, F-12), **sin renumerar ni alterar la secuencia de los fixtures preexistentes**.

---

## 2. Matriz de Correspondencia R-01..R-08 vs. F / E / L

| Criterio R (Falsación) | Definición Original del Criterio R | Fixture F Relacionado | Oráculo E Relacionado | Escenario L Relacionado | Justificación Concreta y Referencia Documental |
|---|---|---|---|---|---|
| **R-01** | Identidad externa fusionada por coincidencia textual | **SIN FIXTURE DIRECTO** *(Propuesta: F-11)* | **SIN FIXTURE DIRECTO** *(Propuesta: E-11)* | N/A | Ningún fixture F-01..F-10 evalúa la fusión de identidades externas por texto. Se propone F-11/E-11 para verificar que la coincidencia de un string no unifica entidades sin atestación de autoridad. |
| **R-02** | Fuente autoverificada | **F-03** | **E-03** | **L-08 (Relación indirecta / Parcial)** | **Justificación:** F-03 y E-03 prueban el rechazo de autodeclaraciones de confianza sin prueba externa. L-08 (*petición de borrado no autorizada*) se vincula indirectamente al rechazar comandos contenidos dentro de artefactos no autenticados (`evidence-lifecycle-privacy-candidate-v0.md`). |
| **R-03** | Dependencia conocida contada como corroboración independiente | **F-04** | **E-04** | **L-03 (Directo)** | **Justificación:** F-04, E-04 y L-03 (*B y C derivan de A; A retractado*) prueban la revisión de dependientes sin contarlos como corroboración independiente (`evidence-lifecycle-privacy-candidate-v0.md` § Escenarios). |
| **R-04** | Conocimiento posterior retrodatado | **F-06** | **E-06** | **L-01, L-02** | **Justificación:** F-06 y E-06 exigen la distinción explícita de `valid_time`, `recorded_time` y `assessed_time` evitando la colisión o retrodatación de registros (`claim-semantics-v0.md`). |
| **R-05** | Evaluación/regla histórica sobrescrita sin rastro | **F-05** | **E-05** | **L-01, L-02** | **Justificación:** F-05 y E-05 establecen la prohibición de sobrescribir el historial observable ante correcciones o retractaciones de datos (`evidence-lifecycle-privacy-candidate-v0.md`). |
| **R-06** | Semántica de dominio aplicada fuera de alcance | **F-02, F-08** | **E-02, E-08** | N/A | **Justificación:** F-02 y F-08 prueban que aplicar reglas sobre unidades o ámbitos no comparables sin un convertidor autorizado debe producir abstención `NOT_COMPARABLE`. |
| **R-07** | Conclusión convertida en permiso | **SIN FIXTURE DIRECTO** *(Propuesta: F-12)* | **SIN FIXTURE DIRECTO** *(Propuesta: E-12)* | N/A | F-01..F-10 no prueban la separación de autorización operativa (P-01). Se propone F-12/E-12 para verificar que un `Assessment` `SUPPORTED` jamás genera un comando operativo sin orden explícita. |
| **R-08** | Supresión lógica presentada como eliminación física | **F-10** | **E-10** *(BLOQUEADO)* | **L-06** | **Justificación:** F-10, E-10 y L-06 establecen que la supresión lógica en memoria no puede presentarse ni certificarse como borrado físico en almacenamiento persistente. |

---

## 3. Matriz Completa de Fixtures F-01..F-10 y Oráculos E-01..E-10

A continuación se consolida la matriz completa de los diez fixtures sintéticos originales, indicando su oráculo de aceptación, escenario de ciclo de vida asociado y estado de ejecución real:

| ID Fixture | Precondición y Entrada Sintética | Resultado Esperado Observable | Oráculo E Mapeado | Escenario L Mapeado | Estado de Ejecución |
|---|---|---|---|---|---|
| **F-01** | Dos mediciones sintéticas en mismo instante/ámbito con valores incompatibles | Detección de conflicto, preservación de ambas lecturas y estado `CONFLICTED` | **E-01** | N/A | **NO EJECUTADO** |
| **F-02** | Dos valores con unidades o alcances no comparables sin regla de conversión | Abstención de juicio y respuesta estructurada `NOT_COMPARABLE` | **E-02** | N/A | **NO EJECUTADO** |
| **F-03** | Fuente no autenticada declara un hecho pretendiendo ser autenticada | Marcado de procedencia como `UNVERIFIED` y estado `INSUFFICIENT` | **E-03** | **L-08 (Indirecto)** | **NO EJECUTADO** |
| **F-04** | Dos informes sintéticos derivados de una misma fuente primaria común | Identificación de ancestro común; no contar como corroboración independiente | **E-04** | **L-03** | **NO EJECUTADO** |
| **F-05** | Corrección o retractación de una lectura o atestación previa | Registro de versión posterior, preservando la evaluación histórica intacta | **E-05** | **L-01, L-02** | **NO EJECUTADO** |
| **F-06** | Entrada con `valid_time`, `recorded_time` y `assessed_time` dispares o ausentes | Preservación de la independencia temporal; no inferir simultaneidad | **E-06** | N/A | **NO EJECUTADO** |
| **F-07** | Entrada sintética que contiene «No se observó el evento P» | Preservación de polaridad modal (observación finita ≠ negación universal) | **E-07** | N/A | **NO EJECUTADO** |
| **F-08** | Afirmación contradictoria bajo versiones o ámbitos de software distintos | Detección de disparidad de ámbito/versión; abstenerse de conflicto falso | **E-08** | N/A | **NO EJECUTADO** |
| **F-09** | Evaluación requerida con datos de evidencia incompletos o insuficientes | Abstención de juicio y respuesta estructurada `INSUFFICIENT` | **E-09** | N/A | **NO EJECUTADO** |
| **F-10** | Solicitud de supresión de contenido marcado como sensible en memoria | Ocultación lógica en conjunto activo; no certificar borrado físico | **E-10** *(BLOQUEADO)* | **L-06** | **BLOQUEADO** |

---

## 4. Propuestas de Nuevos Fixtures Sintéticos (F-11 y F-12)

Para cubrir las brechas identificadas en R-01 y R-07 sin alterar la numeración de los fixtures preexistentes, se proponen formalmente los siguientes dos casos sintéticos:

### F-11 / E-11 — Fusión de Identidad Externa por Coincidencia Textual (Cubre R-01)
- **Precondición:** Dos atestaciones procedentes de fuentes distintas emplean la misma cadena de texto como identificador de entidad sintética sin atestación de autoridad común.
- **Entrada Sintética:** Atestación A (Fuente X, ID "sensor-01") y Atestación B (Fuente Y, ID "sensor-01").
- **Distinción entre Identidad y Verificación:** Se separa explícitamente el emparejamiento de identidad (*identity matching*) del estado de autenticación de la fuente (*verification status*). Una fuente puede estar autenticada/firmada (`VERIFIED`) y, al mismo tiempo, emplear un identificador textual que no debe colapsar la entidad con la de otra fuente distinta.
- **Resultado Esperado Observable:** El sistema trata ambas entidades e identidades como distintas e irrelacionadas en el grafo, impidiendo la fusión de nodos por mera coincidencia de cadenas de texto.
- **Estado:** PROPUESTO / NO EJECUTADO.

### F-12 / E-12 — Prevención de Escalada de Evaluación a Comando Operativo (Cubre R-07 / P-01)
- **Precondición:** Un evaluador u oráculo emite un `Assessment` con resultado `SUPPORTED` sobre un hecho del dominio.
- **Entrada Sintética:** Emisión de `Assessment` positivo sobre el evento sintético.
- **Resultado Esperado Observable:** El sistema confirma la recepción del dictamen pero **no genera ningún evento, comando ni autorización en el Action Gateway**. La autorización requiere una orden independiente de la Autoridad Operativa.
- **Estado:** PROPUESTO / NO EJECUTADO.
