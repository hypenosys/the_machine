# Hoja de decisiones del titular — candidata v1

**Estado:** PROPUESTA / SIN RATIFICAR · **HOLD / NO-GO** · 21-10-2026

Esta hoja reúne decisiones pendientes; **ninguna casilla se considera marcada**, y ni un commit, ni un comentario, ni un merge constituyen aceptación. La aprobación exige registro explícito del titular, alcance, fecha, revisión de los documentos afectados y mecanismo de revocación. No se presupone firma criptográfica.

| ID | Pregunta para el titular | Alternativas que deben deliberarse | Efecto si no hay decisión |
|---|---|---|---|
| DEC-01 | ¿Limitar el primer corte a datos sintéticos, offline, sin efectos externos? | Sí / cambiar alcance documentando nuevos riesgos | Sin autorización de experimento |
| DEC-02 | ¿Comparar R1, R2, C y D, con segundo dominio y sin ganador previo? | Comparación completa / reducir con justificación | G2.2 bloqueado |
| DEC-03 | ¿Se delimita el núcleo puro sin E/S ni acceso al reloj, con E/S sintética en el harness? | Núcleo funcional y harness delimitado / abstracciones de E/S con riesgos explícitos | Frontera núcleo–harness pendiente; determinismo no demostrado |
| DEC-04 | ¿Qué política de retención, supresión y restauración aplica? | Política concreta / excluir por completo | F-10/E-10 original BLOQUEADO |
| DEC-05 | ¿Qué fixtures y oráculos versionados se autorizan? | F-01..09 y negativos aprobados / revisar alcance | Ninguna ejecución |
| DEC-06 | ¿Qué intercambio sintético, formato, E/S y dependencias se permiten? | Especificación limitada / no laboratorio | No hay permiso implícito para persistencia duradera |
| DEC-07 | ¿Es intencional que el repositorio sea público? ¿Qué licencia y derechos corresponden? | Mantener público con términos decididos / revisar visibilidad | GAP-001 OPEN; no licencia adoptada |
| DEC-08 | ¿Se autoriza una excepción temporal para código de laboratorio? | Excepción con lenguaje, límites, duración y revocación / no excepción | Prohibición total de código sigue vigente |
| GAP-010 | ¿Cuál es la precedencia normativa de documentos y quién ratifica gates? | Acta explícita de autoridad / mantener HOLD | G2.1 pendiente |
| G3 | ¿G3 regula iniciar código o fusionarlo? | Definición ratificada y relación con excepciones / sin cambio | Interpretaciones históricas en conflicto |
| REV-13 / tiempo | ¿Cómo distinguir orden de registro real de un `recorded_time` inyectado? | Testigo independiente / limitar las afirmaciones temporales | R-04 y resistencia a retrodatación no demostrados |
| REV-16 | ¿Cómo se acredita independencia de autoría, revisión y aprobación? | Revisores distintos con evidencia / declarar revisión no independiente | No atribuir revisión independiente |
| REV-17 | ¿Se versiona por separado perfil sensor y contrato genérico? | Adaptador, UTC, tolerancias y estados ratificados / diferir | No comparar semánticas incompatibles |
| REV-18 | ¿Se excluyen efectos remotos o se diseñan estados UNKNOWN y reconciliación? | Fuera del laboratorio / contrato remoto futuro separado | No afirmar exactly-once |
| REV-20 | ¿Qué versiones normativas se emplearán? | Referencias fechadas verificadas / referencias orientativas sin mapeos estables | No afirmar cobertura normativa específica |

## Evidencia exigible por decisión

Registrar: identificador, opción elegida, razonamiento, riesgos residuales, documentos/versión exactos, autoridad del decisor, fecha, alcance temporal, condiciones de revocación y contradicciones aceptadas o resueltas. Si faltan, el estado es **PENDIENTE**, no `ACCEPTED`.

## Secuencia de desbloqueo propuesta

1. Resolver DEC-07 y GAP-010/G3 sin modificar unilateralmente visibilidad o licencia.
2. Definir DEC-01..06, REV-17 y REV-18; preservar E-10 bloqueado.
3. Deliberar DEC-08 de forma **separada**: una decisión documental no autoriza construir o ejecutar harness.
4. Revisar de manera independiente las evidencias y decidir explícitamente sobre G2.1; G2.2..G2.4 siguen bloqueados hasta sus propias condiciones.

**No autoriza Rust, Cargo, CI, scripts ejecutables, pruebas, aceptación de ADR, GO o merge.**
