# Tres casos heterogéneos para refutar el diseño

**Estado: casos conceptuales sintéticos; no ejecutados.**

## Caso HET-001 — Sensores
Un artefacto declara una lectura de 55 °C y otro 85 °C. Dos Claims apuntan al mismo punto de medición y contexto, pero solo un comparador de dominio puede decidir si el instante, calibración, tolerancia y unidad permiten contraste.

**Resultado aceptable:** CONFLICTED únicamente si las condiciones de comparabilidad se demuestran; de lo contrario NOT_COMPARABLE o INSUFFICIENT. No acusar a una fuente de mentir.

## Caso HET-002 — Documentación
Un documento afirma que la funcionalidad F apareció en la versión 2.1; otro la sitúa en la 2.3. Ambos Claims conservan citas y versiones de documento. Una release note o historial verificable podría actuar como evidencia adicional.

**Resultado aceptable:** mostrar discrepancia y procedencia; no elegir la versión más reciente o la fuente más conocida sin una regla justificada.

## Caso HET-003 — Software
Una afirmación dice «la función X realiza una conexión de red» y otra dice «X nunca accede a la red». El código, las dependencias y las rutas de ejecución son artefactos; el análisis estático o dinámico produce evidencia con alcance limitado.

**Resultado aceptable:** distinguir «no se observó conexión en este test» de «es imposible que conecte». No convertir ausencia de evidencia en prueba de ausencia.

## Falsación transversal
- Mismo Claim en dos fuentes no implica independencia de evidencia.
- Dos artefactos con contenido idéntico no son automáticamente dos corroboraciones independientes.
- Cambiar el contexto puede eliminar una aparente contradicción.
- Una fuente retirada no debe permanecer citada como vigente sin advertencia.
- Una inferencia basada en una regla desactualizada requiere reevaluación.
- Si un caso exige inventar un campo específico dentro del núcleo común, considerar adaptador de dominio.

## Criterio de éxito
Representar los tres casos sin perder atribución, contexto, trazabilidad y posibilidad de abstención; **no** se exige resolverlos automáticamente.
