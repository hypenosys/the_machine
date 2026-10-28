# Manifiesto de corte documental propuesto — GAP-010 / G3

**Fecha de preparación:** 2026-10-26. **Estado:** `CANDIDATE_FREEZE / NOT_ACCEPTED`. Este documento registra identificadores Git verificados por lectura de archivos en la PR #33; **no congela normativamente** una versión, no acredita firmas y no habilita permisos.

## Objetos inmutables observados

**HEAD de la rama al consultar:** `f3331245900c9d1df340bf8063a22f3a0b533d42`; PR #33 `OPEN / DRAFT`.

| Objeto para revisión | Ruta | Git blob SHA |
|---|---|---|
| Texto normativo candidato `DEC-GOV-010` y `DEC-GATE-003` | `docs/03-preimplementacion/finch-gap010-g3-ratification-package-candidate-2026-10-23.md` | `f8e5f96060adc6af384361ac3824728c694e5b22` |
| Acta de decisión y protocolo de aceptación | `docs/03-preimplementacion/finch-gap010-g3-joint-decision-record-candidate-2026-10-23.md` | `100596d5e16abe66e045d983b4f49e937ae84ff5` |

Los blobs son el objeto de revisión recomendado: el HEAD y la rama pueden avanzar sin alterar esos contenidos. Si cualquiera de los dos blobs cambia, se debe proponer un nuevo par de identificadores y contrastar si requiere nueva aceptación. No asumir que la revisión de una PR anterior cubre estos blobs.

## Secuencia de decisión que evita dependencias circulares

1. **Revisión humana:** cada cotitular accede a ambos documentos por el commit de corte anterior y contrasta los blobs indicados.
2. **Acuerdo sobre procedimiento:** ambas partes deben confirmar qué mecanismo de identidad, decisión, revocación y revisión independiente consideran válido. Este paso **todavía no consta** como completado.
3. **Manifestación separada:** cada titular expresa decisión específica para `DEC-GOV-010` y para `DEC-GATE-003`, mencionando el mismo par de blobs, sus reservas y la eventual aceptación de delegación. Una aprobación genérica no basta.
4. **Comprobación:** un revisor con independencia acreditada (o una revisión marcada expresamente no independiente) coteja las manifestaciones y las cláusulas. Ante desacuerdo o cambio de texto, `PENDING`.
5. **Acta posterior:** un registro nuevo referencia las declaraciones ya existentes y documenta fecha de efecto y alcance. No se exige a las declaraciones citar el SHA del acta posterior.
6. **Propagación condicionada:** solo tras una ratificación válida se podrían proponer cambios coordinados en los documentos que hoy describen G3 de manera distinta; eso no concedería automáticamente `AUT-CODE`, `AUT-EXEC`, `AUT-MERGE` ni `DEC-08`.

## Matriz de aceptación (sin respuestas imputadas)

| Decisión | @Axlfc | @TopperH4rley | Resultado |
|---|---|---|---|
| Mecanismo de ratificación e identidad | No constatado para este par de blobs | No constatado para este par de blobs | `PENDING` |
| `DEC-GOV-010` | Sin aceptación específica de este par de blobs acreditada | Sin aceptación específica de este par de blobs acreditada | `NOT_RATIFIED` |
| `DEC-GATE-003` | Sin aceptación específica de este par de blobs acreditada | Sin aceptación específica de este par de blobs acreditada | `NOT_RATIFIED` |
| Revisión independiente del par | No acreditada | No acreditada | `PENDING` |

**No borrar evidencias históricas:** la revisión `APPROVED` de `Axlfc` sobre `7c7fc642...`, la revisión `COMMENTED` de `TopperH4rley` sobre `9936fbe0...` y el comentario «OK» permanecen registrados en el acta candidata, pero no identifican estos dos blobs.

## Criterio de uso y parada

Este manifiesto **es una invitación a deliberación**, no un formulario que el agente pueda completar por terceros. No realizar commits adicionales de «ratificación» mientras falten declaraciones competentes; los cambios posteriores deben responder a nuevas pruebas o discrepancias verificadas.

**Estado final:** `GAP-010 = OPEN`; `DEC-GATE-003 = PENDING`; `AUT-CODE/AUT-EXEC/AUT-MERGE = NOT_GRANTED`; `HOLD / NO-GO`. Sin código, ejecución ni merge.
