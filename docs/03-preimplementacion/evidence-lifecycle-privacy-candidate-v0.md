# Ciclo de vida de evidencia, retractación y privacidad — propuesta v0

**Estado:** PROPUESTO / NO-GO PARA CÓDIGO. No es política legal aprobada, mecanismo implementado, garantía de borrado físico ni ADR aceptado.

## Problema
THE MACHINE necesita conservar la distinción entre «esto fue afirmado/evaluado» y «esto sigue siendo válido» sin convertir la procedencia en una excusa para retener indefinidamente información personal o sensible. El fixture F-10 / E-10 del contrato experimental está **ABIERTO**.

## Principios de diseño
1. **Identidad ≠ contenido:** una referencia estable no obliga a conservar el contenido original ni un hash reversible por diccionario de datos sensibles.
2. **Hecho histórico ≠ vigencia:** una evaluación anterior puede registrarse como ocurrida y, a la vez, estar retractada, obsoleta o privada de evidencias accesibles.
3. **Procedencia ≠ autenticidad:** un vínculo de origen describe dependencia; no demuestra que el origen sea auténtico.
4. **Integridad ≠ inmutabilidad absoluta:** auditoría, minimización, rectificación y supresión deben ser compatibles según política aplicable.
5. **Retirada ≠ borrado físico certificado:** cambiar el estado visible de una referencia no demuestra eliminación en copias, backups, cachés o medios físicos.
6. **Desconocido ≠ independiente:** si una dependencia no se conoce, no se presume independencia de evidencias.

## Estados conceptuales propuestos (no adoptados)
| Estado | Significado | Lo que NO garantiza |
|---|---|---|
| `ACTIVE` | Contenido disponible según política y referencias resolubles | Veracidad o autenticación |
| `SUPERSEDED` | Existe versión posterior explícita | Que la versión previa fuese falsa |
| `RETRACTED` | Fuente/autoridad declara retirada bajo una regla identificada | Que todas las copias hayan desaparecido |
| `RESTRICTED` | Acceso al contenido limitado | Borrado físico |
| `SUPPRESSION_PENDING` | Petición de supresión pendiente de resolución | Que proceda automáticamente borrar todo |
| `CONTENT_REMOVED` | Contenido inaccesible desde el sistema dentro de alcance declarado | Eliminación de backups o medios externos |
| `REFERENCE_REDACTED` | Solo se mantiene referencia mínima permitida | Anonimato garantizado |
| `UNKNOWN` | Estado no demostrable | Ninguna conclusión sobre disponibilidad |

No asumir una máquina de estados única ni transiciones automáticas hasta fijar autoridades, motivos, plazos y jurisdicción. `RETRACTED` y `CONTENT_REMOVED` son dimensiones diferentes: una retractación puede coexistir con contenido accesible y una supresión puede afectar información no retractada.

## Dependencias y propagación
Para cada evaluación conceptual se requiere identificar: entradas versionadas, reglas versionadas, dependencia conocida/desconocida, estado de vigencia, y razones de cualquier reevaluación. Una retractación de entrada debe disparar una **obligación de revisión** de resultados dependientes, no convertirlos automáticamente en falsos. Si no se puede resolver una dependencia, se registra `DEPENDENCY_UNKNOWN` y se evita atribuir corroboración independiente.

El contenido suprimido no debe reaparecer por citas incrustadas, resúmenes, índices, logs, exportaciones ni evaluaciones derivadas. La propagación de supresión exige definir qué derivados pueden conservarse y bajo qué base; si no existe decisión, el estado es **BLOQUEADO**.

## Escenarios adversariales en papel (NO EJECUTADOS)
| Caso | Secuencia sintética | Obligación conceptual | Estado |
|---|---|---|---|
| L-01 | `A@v1` evaluado, `A@v2` corrige `v1` | Mantener ambas versiones conceptuales y marcar vigencia sin sobrescribir | DESCRITO |
| L-02 | `A@v1` retractado tras evaluación `V1` | `V1` histórico no presentado como evaluación actual | DESCRITO |
| L-03 | `B` y `C` derivan de `A`; `A` retractado | Revisar dependientes sin contarlos como evidencia independiente | DESCRITO |
| L-04 | Petición de supresión de `A` que aparece en resumen `B` | Considerar propagación a derivados y citas | ABIERTO |
| L-05 | Contenido eliminado pero hash identificable permanece | Evaluar riesgo de reidentificación; hash no es anonimización automática | ABIERTO |
| L-06 | Se solicita borrado con backup fuera del proceso | No certificar eliminación fuera del alcance comprobado | ABIERTO |
| L-07 | Una fuente se retracta pero otra evidencia independiente permanece | Reevaluar con la evidencia restante, sin inferir falsedad universal | DESCRITO |
| L-08 | Petición de borrado maliciosa o no autorizada | No borrar por instrucciones dentro de artefactos no confiables | ABIERTO |
| L-09 | Dos jurisdicciones o políticas de retención incompatibles | Registrar conflicto y escalar decisión; no automatizar preferencia legal | ABIERTO |
| L-10 | Un tercero reclama acceso a evidencia restringida | Requerir política de autorización, sin exposición por enlaces de auditoría | ABIERTO |

`DESCRITO` significa solo que existe una hipótesis razonada, **no** que la solución haya sido verificada.

## Políticas y decisiones que deben definirse antes de una implementación real
- Clasificación de datos: públicos, privados, personales, secretos, sintéticos y derivados; alcance y responsable.
- Base y duración de retención, supresión, rectificación, bloqueo y excepciones legales por jurisdicción, revisadas por quien corresponda.
- Separación entre **datos de contenido**, **metadatos**, **identificadores**, **hashes**, **índices**, **evaluaciones** y **copias externas**.
- Modelo de autoridad para pedir, validar, autorizar, rechazar, registrar y auditar supresiones.
- Política de derivación y redacción: qué información mínima puede permanecer después de la eliminación.
- Modelo de persistencia y backup **solo si** se incorpora almacenamiento real; no imponer append-only.
- Pruebas negativas para fuga de información y recuperación de datos suprimidos, y límites de cualquier certificación.
- Impacto sobre `valid_time`, `recorded_time`, `assessed_time` y trazabilidad de decisiones.

## Aplicación al experimento offline sin persistencia
El primer corte propuesto **solo utiliza datos sintéticos y memoria volátil**. Puede simular `retracts`, `supersedes`, vigencia y solicitudes de supresión como **eventos lógicos**. No puede demostrar borrado seguro de disco, cumplimiento normativo, control de backups ni propagación en sistemas externos.

**Criterio de desbloqueo limitado para E-10:** permitir un test conceptual de «retirar contenido del conjunto activo de memoria y no exponerlo en la salida actual» **solo si** se declara expresamente que no equivale a borrado físico, anonimización ni cumplimiento legal. La política general de privacidad seguiría ABIERTA.

## Decisión pendiente
¿Se autoriza acotar E-10 al comportamiento lógico en memoria del primer experimento, manteniendo los escenarios L-04..L-10 como deuda bloqueante para cualquier sistema con datos reales o persistencia? **No se presume autorización.**

**Veredicto:** política candidata para discusión. **HOLD / NO-GO para Rust, Cargo, CI y ADR aceptados.**
