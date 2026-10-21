# Semántica mínima de afirmaciones — propuesta v0

**Estado: PROPOSED / NO-GO para código.**

## Regla central
Una afirmación es una proposición **atribuida** y **contextualizada**, no una sentencia verdadera por defecto. La semántica debe permitir abstenerse antes que inventar equivalencias.

## Campos semánticos conceptuales
- **Proposition**: sujeto, predicado tipado, objeto/valor y versión de vocabulario de dominio.
- **Polarity**: afirmación positiva o negación explícita. Ausencia de afirmación no equivale a negación.
- **Scope**: dominio, población, ubicación, versión de software, condiciones y cuantificadores cuando estén definidos; «siempre» requiere un alcance formalizado.
- **Time**: tiempo al que se refiere la proposición separado del momento en que se registró o evaluó.
- **Attribution**: fuente y artefacto de los que procede la proposición, distinguiendo declarado de autenticado.
- **Modality**: observación, testimonio, hipótesis, predicción o conclusión derivada; estas modalidades no son intercambiables.

## Invariantes semánticos
- SEM-001: «no se observó P» no implica «no P».
- SEM-002: «no hay evidencia de P» no implica «evidencia de no P».
- SEM-003: negación solo contrasta una proposición equivalente en sujeto, predicado, objeto, alcance y tiempo compatibles.
- SEM-004: «P en versión 2.1» y «no P en versión 2.3» pueden ser compatibles.
- SEM-005: una hipótesis no se presenta como observación.
- SEM-006: una cita de un documento demuestra que **el documento afirma P**, no que P sea cierto.
- SEM-007: la ausencia de un cuantificador explícito impide inferir universalidad.
- SEM-008: el resultado de una evaluación conserva el contexto y reglas que lo originaron.

## Ejemplos
1. «La función X nunca accede a red» (universal) frente a «en 100 pruebas no se observó tráfico» (observación finita): evidencia limitada, no demostración universal.
2. «El documento D afirma que F aparece en 2.1»: verificable contra el documento; «F aparece en 2.1» requiere evidencia independiente.
3. «Sensor A midió 55 °C a las 12:00»: atribución de medición; no verificación física.
4. «No existe registro de fallo»: afirmación sobre registros disponibles, no garantía de ausencia de fallo.

## Decisiones abiertas
Lenguaje formal de cuantificadores, identidad semántica entre vocabularios, intervalos temporales, representación de negación compuesta y criterios de equivalencia por dominio.
