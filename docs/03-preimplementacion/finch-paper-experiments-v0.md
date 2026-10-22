# Cuaderno Finch — experimentos de pensamiento y selección documental (v0)

**Fecha:** 22-10-2026 · **Estado:** HIPÓTESIS / SIMULACIÓN EN PAPEL, NO EJECUTADO · **HOLD / NO-GO**.
**Alcance:** solo teoría, diseño, evaluación lógica manual y propuestas de decisiones. Sin código, Cargo, scripts, CI, experimentos físicos, red, datos reales ni firmas atribuidas a cotitulares. Los ejemplos son **inventados**; los «resultados» indican consecuencias deducidas de premisas, no observaciones empíricas ni tests.

## Método de trabajo

1. Formular hipótesis que pueda refutarse.
2. Fijar entradas sintéticas, supuestos, reglas y respuesta esperada **antes** de comparar arquitecturas.
3. Separar **deducción conceptual**, **laguna de especificación** y **evidencia no disponible**.
4. Buscar contraejemplos y el coste de introducir entidades/relaciones auxiliares.
5. Seleccionar el **siguiente documento que reduzca incertidumbre**, nunca declarar un ganador arquitectónico por intuición.

Referencias: [contrato comparativo](comparative-contract-v1.md), [falsación en papel](architecture-paper-falsification-v0.md), [matriz de trazabilidad](traceability-matrix-v1.md) y [decisiones pendientes](decision-preferences-proposal-2026-10-21.md).

## EXP-P01 — Autenticidad declarada frente a autenticidad demostrada

**Hipótesis a falsar:** un `hash`, una firma o un campo `VERIFIED` bastan para probar origen y veracidad.

**Escenario imaginario:** dos artefactos sintéticos idénticos; el primero incluye `VERIFIED` autodeclarado, el segundo `UNVERIFIED`. Un tercero tiene una firma criptográfica cuya clave pertenece a un actor desconocido. El contenido puede ser falso en los tres.

**Deducción conceptual:** igualdad de hash solo indica igualdad del contenido bajo el algoritmo usado; una firma correctamente verificada puede vincular el contenido a una clave, **no** establecer por sí misma identidad civil, procedencia física, verdad de la afirmación o fecha de emisión. La etiqueta autodeclarada no aumenta la confianza.

**Resultado documental:** refuta la **suficiencia lógica** de la hipótesis, no demuestra comportamiento de ninguna implementación. **Decisión de diseño recomendada:** separar `claimed_source`, `verified_key_binding`, `provenance_assessment` y `claim_truth_assessment` conceptualmente; el vocabulario final queda por definir.

**Siguiente documento:** matriz de afirmaciones de procedencia y evidencia exigida para cada una.

## EXP-P02 — Dependencias ocultas y retractación

**Hipótesis a falsar:** dos evidencias que coinciden son independientes.

**Escenario imaginario:** B y C repiten el mismo documento A sin declararlo; una afirmación recibe dos apoyos aparentes. Después A se retracta.

**Deducción conceptual:** dos referencias no implican dos orígenes independientes. Si se descubre el origen común, la evaluación debe poder registrar la corrección de dependencia y conservar el historial de evaluaciones sin reescritura silenciosa.

**Resultado documental:** la independencia no es deducible del número de evidencias; queda sin resolver cómo detectar dependencias **desconocidas**. **Decisión recomendada:** `independence=UNKNOWN` como valor explícito y referencias versionadas para retractación; no multiplicar confianza por recuento bruto.

**Siguiente documento:** contrato de dependencia, retractación y re-evaluación.

## EXP-P03 — Falsa contradicción por ámbito o tiempo

**Hipótesis a falsar:** dos valores distintos para una propiedad implican contradicción.

**Escenario imaginario:** el manual v2.1 dice «módulo sin acceso de red»; el manual v2.3 dice «módulo con acceso de red». Otro par de lecturas de temperatura difiere pero corresponde a máquinas o instantes distintos.

**Deducción conceptual:** sin normalizar versión, modalidad, ámbito, unidad y tiempo válido no se puede afirmar contradicción. `recorded_time` no equivale a `valid_time` ni acredita orden de ocurrencia real.

**Resultado documental:** la regla ingenua «valores distintos = conflicto» produce falsos positivos en estos contraejemplos. **Decisión recomendada:** priorizar un contrato de comparabilidad con abstención explícita, sin extrapolar tolerancias del perfil sensor a otros dominios.

**Siguiente documento:** tabla de comparabilidad entre sensor y documentación técnica, con casos positivos y negativos.

## EXP-P04 — Complejidad desplazada entre R1, R2, C y D

**Hipótesis a falsar:** menos entidades del núcleo implican menor complejidad total.

**Escenario imaginario:** cada arquitectura debe explicar fuente, versión, afirmación, dependencia, retractación y evaluación de los tres casos anteriores.

| Alternativa | Posible ventaja conceptual | Coste o riesgo oculto | Veredicto en papel |
|---|---|---|---|
| R1 (6 entidades) | Vínculos explícitos de procedencia y evaluación | Ontología y cardinalidad de relaciones | **No evaluable cuantitativamente** |
| R2 (Artifact + Attestation) | Núcleo reducido | Relaciones y semántica reaparecen en atestaciones/adaptadores | **No evaluable cuantitativamente** |
| Híbrida C | Núcleo reducido con perfiles de extensión | Deriva semántica entre perfiles y migraciones | **No evaluable cuantitativamente** |
| Baseline D | Simplicidad local en dominio sensor | Ampliaciones ad-hoc para segundo dominio | **No evaluable cuantitativamente** |

**Resultado documental:** no puede deducirse ganador ni rendimiento sin implementaciones comparables y oráculos aprobados. **Decisión recomendada:** medir en el futuro complejidad **total** (núcleo + perfiles + adaptadores + reglas + migraciones), no solo entidades nominales.

**Siguiente documento:** presupuesto conceptual de complejidad y plantilla de costes por arquitectura, sin números inventados.

## EXP-P05 — Borrado lógico frente a borrado físico

**Hipótesis a falsar:** ocultar un artefacto equivale a eliminarlo.

**Escenario imaginario:** se oculta una entrada de una vista; persisten copias hipotéticas en backups, cachés y referencias derivadas.

**Deducción conceptual:** la ocultación no implica destrucción de copias ni revocación de conocimiento derivado. No hay oráculo de eliminación física.

**Resultado documental:** F-10/E-10 original **BLOQUEADO**; no se propone ejecutarlo. **Decisión recomendada:** excluir datos reales del primer corte y redactar política de retención y límites de garantías antes de cualquier prueba autorizada.

## EXP-P06 — Autoridad aparente frente a autorización real

**Hipótesis a falsar:** un rol en GitHub o `mergeable=true` basta para conceder GO.

**Escenario imaginario:** una PR documental es técnicamente fusionable y recibe comentarios favorables del autor, pero no tiene aprobación verificable de ambos cotitulares para cambiar gates.

**Deducción conceptual:** la capacidad técnica y la revisión del autor no constituyen autorización normativa. **Decisión recomendada:** mantener estados separados `proposed`, `ratified`, `implemented`, `verified` y permisos AUT-CODE/AUT-EXEC/AUT-MERGE independientes.

**Siguiente documento:** acta conjunta ACT-GOV-001 con aceptación real, nunca simulada.

## Priorización Finch: qué hacer a continuación

| Prioridad | Entregable exclusivamente documental | Incertidumbre que reduce | Criterio para considerarlo preparado |
|---|---|---|---|
| 1 | Matriz de procedencia y niveles de confianza | Confusión entre hash, firma, identidad y verdad | Cada afirmación tiene fuente de validación y limitación |
| 2 | Contrato de dependencia y retractación | Doble conteo de evidencia y pérdida de historia | Caso de origen común y retractación definido |
| 3 | Tabla de comparabilidad de dos dominios | Contradicciones falsas y abstención | Casos comparables/no comparables con reglas previas |
| 4 | Presupuesto conceptual de complejidad R1/R2/C/D | Elección sesgada por número de entidades | Misma lista de responsabilidades en cuatro opciones |
| 5 | Acta de gobernanza y conciliación S1 | Autoridad y significado de G3 | Consentimientos verificables, no presuntos |
| 6 | Contrato de retención/supresión | Garantías falsas de borrado | Límites de conservación y copias declarados |

**Criterio de continuación:** completar los documentos 1–4 como candidatos, someterlos a crítica adversarial y revisar hipótesis; no atribuir `PASS`, tasas, tiempos, eficacia, coste ni resultados medidos. Ningún ejercicio en papel desbloquea automáticamente G2.1–G3. Las decisiones reservadas requieren ratificación separada de @Axlfc y @TopperH4rley.
