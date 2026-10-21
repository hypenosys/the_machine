# Contrato epistemológico v0 — propuesta para revisión

**Estado: PROPOSED / NO-GO para código.** No es un esquema ejecutable.

## Objetivo
Evaluar si dos **observaciones sintéticas declaradas** pueden compararse y, en tal caso, si son compatibles según una regla explícita. Una observación no equivale a un hecho comprobado.

## Campos conceptuales obligatorios
- `observation_id`: identificador estable dentro del lote.
- `source_claim`: identificador **declarado** de fuente; no autenticado.
- `subject_id`: entidad o punto de medida declarado.
- `quantity_id`: magnitud tipada, definida en catálogo cerrado v0.
- `value`: número finito dentro de límites explícitos.
- `unit_id`: unidad del catálogo de la magnitud.
- `observed_at`: instante con zona u offset explícito, o error de validación.
- `context_id`: contexto de medición declarado; evita comparar condiciones distintas.
- `schema_version`: versión del contrato.

## Fuera de alcance
Confianza reputacional, atribución de culpa, probabilidades, autenticación de fuente, conversiones universales, datos físicos reales, diagnóstico industrial y decisiones automáticas.

## Reglas de comparabilidad
1. Dos registros solo se comparan si pasan validación estructural.
2. Deben coincidir sujeto, magnitud y contexto.
3. Las unidades deben ser idénticas en v0; **no se aplican conversiones implícitas**.
4. Los instantes deben coincidir exactamente en v0 tras normalización temporal definida; tolerancias temporales quedan para un ADR posterior.
5. La comparación numérica requiere tolerancia declarada por magnitud; sin tolerancia definida, devolver **NO_COMPARABLE**, no asumir cero.
6. Si las condiciones anteriores se cumplen, diferencia absoluta ≤ tolerancia → **COMPATIBLE**; diferencia mayor → **CONFLICTO**.
7. Los identificadores repetidos con contenidos diferentes se rechazan como error de integridad de lote, no se fusionan.
8. El orden de entrada no debe alterar el conjunto de resultados.

## Salidas
- `COMPATIBLE`: acuerdo según criterio v0, **no confirma verdad**.
- `CONFLICTO`: incompatibilidad según criterio v0, **no identifica fuente falsa**.
- `NO_COMPARABLE`: faltan equivalencias o condiciones necesarias.
- `INVALIDO`: al menos un registro no satisface el contrato.

Cada salida debe contener identificadores implicados, regla aplicada y razón legible. Una salida no añade hechos que no figuren en los registros.

## Decisiones que permanecen abiertas
Precisión decimal y redondeo, codificación del tiempo, catálogo de unidades y tolerancias, cardinalidad máxima, orden canónico, serialización, política de duplicados idénticos y granularidad de errores.

**Nota:** los campos declarados nunca prueban que el sensor, instante o sujeto existieran realmente.
