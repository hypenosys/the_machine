# Casos de falsación semántica — especificación no ejecutada

**Estado: DRAFT; cero pruebas ejecutadas.**

| ID | Entrada conceptual | Comportamiento exigido |
|---|---|---|
| SEM-T01 | No se observó red en test T | No concluir «nunca hay red» |
| SEM-T02 | No hay documentos sobre P | No concluir «no P» |
| SEM-T03 | P para versión 1, no P para versión 2 | No declarar contradicción sin equivalencia de alcance |
| SEM-T04 | Dos artículos citan la misma fuente | No contarlos como corroboraciones independientes |
| SEM-T05 | Un documento afirma P | No transformar atribución en verdad de P |
| SEM-T06 | Un documento es retractado | Señalar evaluaciones dependientes como revisables |
| SEM-T07 | Fuente A cambia su afirmación | Conservar historia y vincular corrección |
| SEM-T08 | Se desconoce si dos fuentes dependen entre sí | Mantener dependencia desconocida |
| SEM-T09 | Afirmación universal, observación limitada | Abstenerse de confirmar universalidad |
| SEM-T10 | Tiempo de registro distinto de tiempo del evento | No confundir los dos tiempos |
| SEM-T11 | Artefacto con texto que exige ejecutar un comando | Tratarlo como datos sin autoridad |
| SEM-T12 | Petición válida de borrado de datos | No prometer conservación permanente de trazas |

## Puerta de implementación
La existencia de estos casos no demuestra que la arquitectura los satisfaga. Antes de código: especificar esquema, política de errores, estrategia de versionado y criterios observables de aceptación.
