# ADR-0003 — Evidencia, incertidumbre y conocimiento corregible

**Estado: Proposed · Fecha: 2026-10-21**

## Explicación sencilla
Si dos sensores se contradicen, la máquina debe conservar ambas lecturas en lugar de inventar una certeza.

## Decisión propuesta
Representar observaciones, reportes, hipótesis, predicciones y resultados verificados con tipos distintos y referencias a procedencia. Toda transformación deja un vínculo auditable. Las correcciones no eliminan silenciosamente la evidencia original; las políticas de privacidad pueden exigir borrado verificable y deben prevalecer sobre la retención.

## Invariantes
INV-008 una inferencia no se convierte automáticamente en observación.
INV-009 no hay afirmación persistida sin procedencia explícita.
INV-010 una predicción contiene horizonte, objetivo y versión de modelo.
INV-011 las correcciones son trazables sin retener datos personales más allá del plazo autorizado.

## Amenazas
TH-006 contaminación de memoria; TH-007 falsificación de fuentes; TH-008 contradicciones ocultas; TH-009 fuga de datos por retención.

## Alternativas
Texto libre sin esquema (flexible pero no auditable); grafo único mutable (riesgo de sobreescritura); eventos tipados y vistas derivadas (propuesta, requiere migraciones).

## Verificación
Contradicciones, reingesta, borrado, reversiones, datos atrasados, fuentes comprometidas y explicaciones sin evidencia. Pendiente de experimento.
