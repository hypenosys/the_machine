# Matriz de garantías de procedencia y confianza — candidata v0

**Estado:** DISEÑO DOCUMENTAL / NO RATIFICADO · HOLD / NO-GO. **No son resultados empíricos.** No hay código, validación de firmas, pruebas ejecutadas ni fuentes reales en este documento.

## 1. Modelo de afirmaciones separadas

| Afirmación que alguien podría formular | Qué evidencia mínima sería pertinente | Qué NO demuestra esa evidencia | Respuesta sin evidencia |
|---|---|---|---|
| «Estos bytes coinciden con un digest previo» | Digest esperado obtenido por canal independiente, algoritmo y bytes canonizados | Autor, verdad, momento de creación | INDETERMINADO |
| «El mensaje fue firmado por la clave K» | Firma válida, mensaje exacto, algoritmo y clave pública K | Titular humano de K, autorización, verdad | NO VERIFICADO |
| «La clave K pertenece a la organización O» | Vinculación de identidad independiente, alcance, vigencia y revocación | Que O produjo físicamente los datos o que son ciertos | IDENTIDAD NO ACREDITADA |
| «El artefacto procede del dispositivo D» | Cadena de captura, identidad de dispositivo, contexto y controles de manipulación | Ausencia de fallos del sensor ni verdad universal | PROCEDENCIA NO ACREDITADA |
| «La afirmación C es verdadera» | Oráculo de dominio, evidencias comparables, incertidumbre y contraejemplos | Validez de todas las afirmaciones relacionadas | NO EVALUABLE |
| «El evento ocurrió antes de T» | Testigo temporal independiente y semántica temporal explícita | Que el reloj local o `recorded_time` prueben ocurrencia | ORDEN NO DEMOSTRADO |
| «B y C son evidencias independientes» | Linaje trazado y ausencia justificada de origen común en el alcance conocido | Independencia absoluta ante dependencias desconocidas | INDEPENDENCIA DESCONOCIDA |
| «El contenido ha sido eliminado físicamente» | Política, alcance de soportes/cachés/copias y oráculo externo de eliminación | Destrucción de copias desconocidas o recuerdos derivados | GARANTÍA NO DEMOSTRADA |

**Regla:** no elevar `claimed` a `verified` mediante una etiqueta del propio artefacto. La verificación criptográfica, la acreditación de identidad, la procedencia y la evaluación epistemológica son preguntas diferentes. Ningún campo de confianza es un número universal.

## 2. Contrato conceptual mínimo de procedencia

Un registro candidato de evaluación de procedencia distinguiría:
- **Sujeto:** `artifact_ref` y revisión inmutable referenciada.
- **Afirmación:** `assertion_kind`, `claimed_value`, `claimant_ref` (si consta).
- **Base de evaluación:** `evidence_refs`, `verification_method_ref`, `rule_revision` y alcance.
- **Tiempos:** `valid_time`, `recorded_time`, `assessed_time`, sin equipararlos.
- **Resultado:** `VERIFIED_FOR_SCOPE`, `REFUTED_FOR_SCOPE`, `UNKNOWN` o `NOT_APPLICABLE`, con razones y límites.
- **Dependencias:** `derived_from`, `supersedes`, `retracts` cuando se conozcan, y `dependency_status=UNKNOWN` cuando no.
- **Historial:** nueva revisión para correcciones; no sobrescribir evaluaciones anteriores silenciosamente.

**Advertencia de nomenclatura:** estos son campos y valores *ilustrativos*, no un esquema ratificado ni sustitutos de los estados `SUPPORTED/REFUTED/CONFLICTED` del contrato comparativo. Se necesita una traducción explícita antes de combinar estados.

## 2.1 Separación de estados de garantía y veredictos de dominio

Los estados `VERIFIED_FOR_SCOPE`, `REFUTED_FOR_SCOPE`, `UNKNOWN` y `NOT_APPLICABLE` describen **una garantía de procedencia delimitada**. Los estados `SUPPORTED`, `REFUTED`, `CONFLICTED` y `NOT_COMPARABLE` del contrato comparativo describen **una evaluación epistemológica bajo reglas de dominio**. Son espacios semánticos diferentes.

| Garantía de procedencia | Significado | ¿Determina un veredicto de dominio? |
|---|---|---|
| `VERIFIED_FOR_SCOPE` | Garantía concreta verificada dentro de un alcance explícito | No; el contenido puede ser falso |
| `REFUTED_FOR_SCOPE` | Garantía concreta refutada en ese alcance | No; la afirmación puede tener otro respaldo |
| `UNKNOWN` | Evidencia insuficiente sobre esa garantía | No; conservar incertidumbre |
| `NOT_APPLICABLE` | Garantía ajena al sujeto o alcance | No; no equivale a `NOT_COMPARABLE` |

**Decisión editorial reversible:** no hay mapeo automático entre espacios; una traducción futura requiere reglas de perfil explícitas y versionadas, sin atribuirles aprobación. Los términos en español de la primera tabla son explicaciones humanas, no estados canónicos.

## 3. Casos de falsación en papel (premisas y resultados lógicos)

| Caso | Premisa sintética | Respuesta conceptual requerida | Resultado del análisis en papel |
|---|---|---|---|
| PROV-01 | Dos bytes idénticos, autores distintos no acreditados | Integridad comparable; autor desconocido | La igualdad no identifica autor |
| PROV-02 | Firma válida bajo K, titular K desconocido | Firma vinculada a K; identidad no acreditada | Firma no prueba titular |
| PROV-03 | Dos informes copian A y omiten linaje | Independencia UNKNOWN; no duplicar apoyo | Número de informes no prueba independencia |
| PROV-04 | `recorded_time` posterior a `valid_time` | Conservar tiempos separados | Captura posterior no prueba hora del evento |
| PROV-05 | Fuente retracta A@v1 y publica A@v2 | Conservar ambas versiones y reevaluaciones | No borrar la historia |
| PROV-06 | Etiqueta `VERIFIED` sin verificador | Estado no acreditado | Autodeclaración no verifica |

Los resultados son **deducciones conceptuales condicionadas a premisas inventadas**. No son PASS/FAIL de implementaciones R1/R2/C/D.

## 4. Decisiones de diseño derivadas, reversibles

1. **Separar capas:** integridad de bytes, autenticación de clave, identidad, procedencia y verdad.
2. **No puntuar confianza por recuento bruto de fuentes** sin linaje.
3. **Mantener abstención explícita** cuando falten identidad, oráculo, ámbito o dependencia.
4. **Versionar retractaciones** y conservar el razonamiento histórico.
5. **No seleccionar arquitectura** hasta comprobar que las cuatro expresan estas responsabilidades con el mismo contrato y el segundo dominio.

## 5. Qué falta antes de elegir

**Pendientes documentales:** vocabulario de identidades, modelo de revocación, reglas de independencia, oráculo de dominio, revisión de derechos y amenaza de falsificación. **Pendientes de evidencia:** implementación, fixtures finales, controles positivos/negativos, revisión independiente y mediciones, todos no realizados.

**Próximo entregable recomendado:** contrato en papel de linaje, retractación y re-evaluación, seguido de una tabla de comparabilidad entre telemetría y documentación técnica. Ninguno concede AUT-CODE/AUT-EXEC/AUT-MERGE.
