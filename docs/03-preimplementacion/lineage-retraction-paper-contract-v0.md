# Contrato conceptual de linaje, retractación y reevaluación — v0

**Estado:** CANDIDATO / EJERCICIO EN PAPEL / NO EJECUTADO · HOLD / NO-GO.

## Pregunta de diseño
¿Puede una evaluación conservar el historial cuando una evidencia es retractada, sin asumir que dos artefactos son independientes ni borrar las conclusiones anteriores?

## Invariantes propuestos
1. Toda afirmación y evaluación referencia revisiones exactas, no solo nombres mutables.
2. `derived_from` y `cites` no significan lo mismo: citar no demuestra derivación, y la ausencia de vínculo no demuestra independencia.
3. Una retractación es **una nueva afirmación versionada**, no eliminación física ni reescritura del pasado.
4. La reevaluación crea un nuevo dictamen con referencia a regla y entradas; no altera silenciosamente el dictamen antiguo.
5. Una dependencia desconocida debe expresarse como `UNKNOWN`, no como `INDEPENDENT`.
6. Si el oráculo no permite decidir, se conserva abstención con motivo.

## Caso conceptual LIN-01
- `A@v1`: fuente sintética declara temperatura 55 °C.
- `B@v1`: resumen de A, con linaje declarado.
- `C@v1`: copia de A cuyo linaje no se declara inicialmente.
- `V@v1`: evaluación conceptual que considera B y C como dos apoyos; esta premisa debe señalarse como **no justificada**.
- `A@v2`: la fuente retracta A@v1.
- `C@v2`: revisión que reconoce derivación de A@v1.
- `V@v2`: reevaluación conceptual que reduce los apoyos independientes acreditados a **cero** para este escenario, sin borrar V@v1.

**Deducción:** B y C no son apoyos independientes bajo las premisas finales. No se demuestra que un motor concreto detecte la dependencia ni actualice V automáticamente.

## Matriz de responsabilidades arquitectónicas

| Responsabilidad | R1 | R2 | Híbrida C | Baseline D |
|---|---|---|---|---|
| Referenciar artefactos versionados | Artifact + relaciones | Artifact + metadatos/Attestation | Núcleo + perfil | Campos específicos |
| Representar derivación | EvidenceLink/Relation candidatos | Vínculo tipado en Attestation o adaptador | Perfil de relaciones | Relación ad-hoc |
| Retractación sin sobrescritura | Nueva relación/Assessment | Nueva Attestation referenciada | Regla del perfil | Registro específico |
| Abstención por linaje desconocido | Assessment/regla externa | Evaluador externo | Evaluador del perfil | Regla de dominio |
| Conservar historial de dictámenes | Assessment versionado | Attestation versionada | Extensión versionada | Historial propio |

La tabla indica **posibilidades conceptuales**, no capacidades implementadas. El número de tipos nominales no mide la complejidad total.

## Criterios documentales para revisar el contrato
- Caso positivo: dos mediciones verdaderamente independientes según premisas explícitas.
- Caso negativo: dos informes que copian la misma fuente.
- Caso ambiguo: origen común no demostrable ni descartable.
- Caso de retractación: la fuente retira una revisión antigua y queda registro de ambos dictámenes.
- Caso de oráculo inválido: marcar no evaluable a todas las arquitecturas afectadas, no solo a la desfavorecida.

**Próxima decisión:** completar la comparabilidad entre dominios y después un presupuesto de complejidad conceptual, sin elegir ganador. **No autoriza código ni ejecución.**
