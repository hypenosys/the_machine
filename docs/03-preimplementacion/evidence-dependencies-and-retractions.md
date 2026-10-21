# Dependencia de evidencia, correcciones y retractaciones

**Estado: PROPUESTO / sin implementación.**

## Problema de independencia
Dos artículos que copian una misma nota de prensa no constituyen automáticamente dos confirmaciones independientes. La trazabilidad debe preservar relaciones como `derived_from`, `quotes`, `duplicates`, `supersedes` y `retracts` con semántica versionada.

## Reglas
- DEP-001: evidencia repetida no aumenta automáticamente el soporte.
- DEP-002: independencia es una **afirmación evaluable**, no una propiedad inferida de IDs distintos.
- DEP-003: si no se conoce la dependencia, marcarla como desconocida; no suponer independencia.
- DEP-004: una evaluación referencia versiones exactas de sus entradas y reglas.
- DEP-005: una retractación no borra silenciosamente evaluaciones históricas; las marca como potencialmente desactualizadas.
- DEP-006: nueva evaluación no reescribe el resultado anterior; conserva vínculo `supersedes`.
- DEP-007: privacidad, retención y borrado pueden requerir eliminación real; la trazabilidad no justifica retención ilimitada.
- DEP-008: las relaciones entre evidencias no otorgan permisos ni autoridad.

## Estados conceptuales del ciclo de vida
`ACTIVE`, `CORRECTED`, `RETRACTED`, `WITHDRAWN` y `UNKNOWN`. No implican que una fuente externa pueda ser autenticada sin pruebas.

## Ejemplo de corrección
Una release note publicada indica versión 2.1; posteriormente se corrige a 2.3. Conservar referencia a la versión consultada, registrar la corrección y señalar que las evaluaciones basadas en 2.1 necesitan revisión. No declarar automáticamente falsa la afirmación original sin evaluar contexto y contenido.

## Riesgos
Falsas cadenas de independencia, grafos cíclicos, procedencia manipulada, enlaces rotos, cambios retrospectivos de fuente, información sensible en auditoría y re-evaluación costosa.

## Investigación necesaria
Definir si las dependencias son un grafo dirigido versionado, cómo detectar ciclos, cómo propagar estado `stale`, y cómo aplicar eliminación y minimización de datos sin prometer inmutabilidad.
