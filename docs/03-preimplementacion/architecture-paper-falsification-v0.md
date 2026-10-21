# Falsación conceptual en papel del núcleo — v0

**Estado:** PROPUESTO / REVISIÓN DOCUMENTAL, NO EXPERIMENTO EJECUTADO. **Código:** HOLD / NO-GO.

## Objetivo y límites
Aplicar adversarialmente los fixtures F-01..F-10 de `precode-decision-protocol-v0.md` a cuatro alternativas. Este documento prueba **si una representación puede describirse conceptualmente sin contradicción evidente**, no si funciona en Rust, cuánto cuesta, si escala ni si supera tests. Ninguna alternativa se declara ganadora. Los ejemplos son **construcciones hipotéticas**, no resultados observados.

## Convenciones del ejercicio
- `S` fuente declarada; `A` artefacto/version; `C` afirmación; `E` enlace de evidencia; `V` evaluación; `R` relación. `Att` atestación propuesta, sin asumir firma criptográfica.
- La autenticación es independiente del contenido: `UNVERIFIED` no se eleva a `VERIFIED` sin verificación externa.
- `valid_time` (tiempo referido), `recorded_time` (captura) y `assessed_time` (evaluación) son distintos; los formatos siguen sin definir.
- El resultado `CONFLICTED` depende de una regla explícita del perfil, no del desacuerdo de dos cadenas.
- Los resultados de abajo son **viabilidad conceptual provisional**, nunca `PASS` técnico.

## Ejemplo 1: conflicto aparente de sensores (F-01, F-02, F-06, F-08)
Datos sintéticos:
- `S1` declara `temperatura = 55 °C`, para máquina `M1`, intervalo `T1`, artefacto `A1@v1`.
- `S2` declara `temperatura = 72 °C`, mismo equipo e intervalo, `A2@v1`.
- Perfil `P-temp@v1`: comparación solo si equipo, intervalo y unidad normalizada son equivalentes; tolerancia declarada de 2 °C. Estos valores y tolerancia son **supuestos del ejemplo**, no especificación adoptada.
- `S3` declara `temperatura = 72 °F` para `M2`, `T2`, `A3@v1`: sin regla de conversión/identidad, abstención `NOT_COMPARABLE`.

| Alternativa | Representación conceptual posible | Riesgo a falsar |
|---|---|---|
| A, seis entidades | `S1/S2 → A1/A2 → C1/C2 → E1/E2 → V1(CONFLICTED)`, con regla `P-temp@v1` y tiempos; `C3` no comparable | Sobrecarga de entidades para observaciones simples; semántica del perfil sigue externa |
| B, Artifact+Attestation | `A1/A2` y `Att1/Att2` contienen procedencia y payload tipado; un evaluador de perfil externo produce `AttV1` con referencias versionadas | Si las atestaciones son texto opaco, no hay identidad de Claim ni dependencia evaluable sin reintroducirlas |
| C, híbrida | Artefactos con procedencia y perfil `P-temp@v1` que define claims, enlaces y evaluaciones | Acoplamiento y divergencia entre perfiles; interoperabilidad no demostrada |
| D, específica | Dos lecturas con identificadores y función conceptual de comparación | Pierde generalidad; trazabilidad de fuentes y versiones requiere ampliación |

**Resultado documental:** las cuatro opciones pueden describir el caso básico **si** se les permiten campos auxiliares; ello no demuestra equivalencia funcional. B/C/D podrían ocultar en perfiles la misma complejidad de A.

## Ejemplo 2: evidencia derivada y retractación (F-03, F-04, F-05, F-09)
Datos sintéticos: `S1` sin autenticar produce `A1@v1`; `A2@v1` y `A3@v1` citan `A1@v1`. Una evaluación `V1` usa A2 y A3. Luego `A1@v2` retracta una medición previa. No se deduce independencia de A2/A3 ni se borra automáticamente `V1`; su vigencia debe recalcularse.

- **A:** `EvidenceLink` y `Relation` versionados representan dependencia y retractación; `Assessment` conserva reglas, estado y tiempo. **Pregunta abierta:** ¿cómo se detectan dependencias desconocidas?
- **B:** `Att` necesita vínculos explícitos `derived_from`, `retracts`, `assessed_with` y estado de autenticación. **Pregunta abierta:** ¿es una simplificación real o solo un cambio de nombre de relaciones?
- **C:** los perfiles deben definir dependencias compatibles entre dominios. **Pregunta abierta:** ¿cómo retractar transversalmente sin un vocabulario común?
- **D:** requiere introducir un registro de procedencia y un historial de evaluación que el caso mínimo no contemplaba. **Pregunta abierta:** ¿en qué punto deja de ser mínima?

**Resultado documental:** no es posible justificar una clasificación de riesgo residual, coste ni victoria de diseño. El requisito transversal de dependencia/retractación exige semántica explícita con independencia de la cantidad de entidades de primer nivel.

## Ejemplo 3: negación, atribución y privacidad (F-07, F-10)
`A4` contiene «No se observó fallo durante 10 pruebas». No equivale a «el sistema nunca falla». `A5` contiene un dato personal marcado para supresión.

- **Todas las opciones:** deben conservar modalidad, cuantificador y atribución; ninguna puede inferir universalidad de una muestra finita.
- **Todas las opciones:** la supresión requiere política explícita sobre contenido, metadatos, referencias, evaluaciones derivadas y copias. Un hash no garantiza autenticidad ni resuelve por sí mismo la privacidad.
- **A:** una relación versionada no debe convertirse en obligación de conservar datos personales indefinidamente.
- **B/C/D:** un log append-only o una atestación permanente puede filtrar contenido sensible incluso si se elimina el artefacto original.

**Resultado documental:** F-10 **no está resuelto por ninguna opción**; falta política de borrado, retención y propagación de supresiones. No etiquetar F-10 como aprobado.

## Segundo dominio: afirmación sobre una versión de software
- `A6`: informe que afirma «el módulo X usa red en versión 2.1».
- `A7`: informe que afirma «el módulo X no usa red en versión 2.3».
- Resultado requerido: no declarar contradicción sin fijar versión, ámbito, modalidad y fuente. Un informe **afirma** algo; no autentica la verdad del comportamiento del software.
- La misma prueba se aplica a A/B/C/D; para B/C/D hay que documentar dónde residen versión de vocabulario, Claim, atribución y evaluación.

## Matriz de estado (NO son resultados de tests)
| Fixture | Estado de razonamiento | Principal brecha transversal |
|---|---|---|
| F-01 | DESCRITO | Reglas tipadas y equivalencia de mediciones |
| F-02 | DESCRITO | `NOT_COMPARABLE` y conversiones permitidas |
| F-03 | DESCRITO | Verificación de identidad de fuente |
| F-04 | DESCRITO | Dependencia de origen y corroboración |
| F-05 | DESCRITO | Invalidación y versiones de evaluaciones |
| F-06 | DESCRITO | Tipos, zonas, serialización y relojes |
| F-07 | DESCRITO | Modalidad y cuantificadores |
| F-08 | DESCRITO | Equivalencia de alcance y versión |
| F-09 | DESCRITO | Reglas de abstención |
| F-10 | **ABIERTO** | Retención, borrado y referencias derivadas |

`DESCRITO` solo significa que se expuso una hipótesis de representación; no implica cobertura, ejecución ni satisfacción de criterios de aceptación.

## Objeciones adversariales a la comparación
1. Contar entidades de nivel superior no mide complejidad: una `Attestation` universal puede contener una ontología escondida.
2. El sensor de temperatura favorece esquemas estrechos; el segundo dominio evita extrapolar indebidamente.
3. Los ejemplos construidos por quien propone una arquitectura no son validación independiente.
4. La reproducibilidad exige fixtures machine-readable, salidas esperadas, oráculos de comparación y procedimientos fijados **antes** de cualquier prueba.
5. Seguridad y privacidad requieren un modelo de amenazas específico, no un ranking conceptual.
6. La autoridad de un documento y la validez de una afirmación son problemas diferentes.

## Decisiones aún bloqueadas
- Selección A/B/C/D, contrato de datos, esquema temporal, política de borrado, criterios de equivalencia por dominio, errores, límites de recursos, plataforma y dependencias.
- Antes de un posible GO: formalizar un **contrato de experimento** y las pruebas negativas, resolver o exceptuar explícitamente las condiciones del readiness review, y obtener autorización expresa del titular.
- **No iniciar Rust, Cargo, CI ni aceptar ADR** como consecuencia automática de esta revisión.

**Veredicto:** CONTINUAR INVESTIGACIÓN DOCUMENTAL. **HOLD / NO-GO para código.**
