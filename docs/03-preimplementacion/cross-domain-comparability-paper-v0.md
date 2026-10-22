# Comparabilidad entre dominios y presupuesto conceptual — v0

**Estado:** DISEÑO EN PAPEL / NO RATIFICADO / NO EJECUTADO · HOLD / NO-GO.

## Reglas previas de comparabilidad
Una pareja de afirmaciones solo puede clasificarse como contradicción cuando coinciden el **sujeto**, la **propiedad**, el **ámbito**, la **versión pertinente**, la **modalidad** (hecho, posibilidad, obligación, negación), el **tiempo válido** y una regla de comparación del dominio. Las unidades se normalizan únicamente mediante reglas explícitas. Si falta información decisiva: **abstención**, no conflicto automático.

| ID | Dominio | Entradas ficticias | Expectativa de diseño | Motivo |
|---|---|---|---|---|
| CMP-01 | Sensor | M1 a T1: 55 °C y 72 °C, tolerancia ilustrativa 2 °C | Conflicto condicionado al perfil | Mismo sujeto/tiempo/unidad; diferencia supera tolerancia asumida |
| CMP-02 | Sensor | M1 a T1: 55 °C; M2 a T1: 72 °C | NO COMPARABLE | Distinto sujeto |
| CMP-03 | Sensor | M1 a T1: 55 °C; M1 a T2: 72 °C | NO COMPARABLE salvo regla temporal | Instantes distintos |
| CMP-04 | Documentación | Módulo X v2.1 «sin red»; v2.3 «con red» | NO COMPARABLE como contradicción directa | Versiones distintas; compatibilidad global no demostrada |
| CMP-05 | Documentación | Módulo X v2.3 «siempre sin red»; misma versión «permite red» | Potencial conflicto, sujeto a modalidad y definición de «red» | Coincidencia parcial de alcance |
| CMP-06 | Documentación | «no se ha observado red»; «red es posible» | NO CONFLICTO lógico | Ausencia observada no implica imposibilidad |
| CMP-07 | Ambos | Fuente se declara verificada, sin verificador independiente | Procedencia UNKNOWN | Etiqueta no acredita identidad |

**Advertencia:** «conflicto», «no comparable» y «abstención» son expectativas conceptuales, no salidas de un sistema ni equivalencias automáticas con `CONFLICTO/NO_COMPARABLE` del perfil sensor o `CONFLICTED/NOT_COMPARABLE` epistemológicos. El perfil definitivo sigue pendiente.

## Presupuesto de complejidad sin cifras inventadas

| Responsabilidad | R1 | R2 | Híbrida C | Baseline D |
|---|---|---|---|---|
| Fuente e identidad | Source + reglas | Attestation + verificador | Attestation + perfil | Campos y validación local |
| Afirmación tipada | Claim | Payload/Attestation | Perfil tipado | Modelo específico |
| Evidencia y dependencia | EvidenceLink/Relation | Enlaces/metadata | Extensión de grafo | Relaciones ad-hoc |
| Evaluación versionada | Assessment | Attestation de evaluación | Evaluador del perfil | Evaluación específica |
| Segundo dominio | Ontología/adaptador | Adaptador semántico | Nuevo perfil y compatibilidad | Ampliación de modelo |
| Retractación | Relación versionada | Nueva atestación | Regla de perfil | Historial específico |
| Seguridad y permisos | Externos al modelo | Externos al modelo | Externos al modelo | Externos al modelo |

**Observación conceptual:** ninguna alternativa elimina las responsabilidades; puede ubicarlas en distintos componentes. No hay datos de rendimiento, mantenimiento, coste, tamaño ni seguridad que permitan puntuar o escoger ganador.

## Regla de decisión posterior
La selección arquitectónica deberá usar los mismos casos y oráculos, registrar pérdidas semánticas, abstenciones y adaptaciones, incluir segundo dominio y documentar costes totales (núcleo + perfiles + adaptadores + migración + reglas). No hay ranking válido todavía.

**Siguiente paso documental recomendado:** revisión adversarial cruzada de estos tres contratos en papel, con registro de contradicciones y límites. La revisión no debe declararse independiente si la realiza el mismo autor o agente.
