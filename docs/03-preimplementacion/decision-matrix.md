# Matriz de decisión previa a implementación

**Estado: PROPUESTA para discusión.** Escalas cualitativas, no mediciones.

| Criterio | A: evidencia offline | B: acciones simuladas | C: aislamiento |
|---|---|---|---|
| Explicable a principiante | Alta | Media | Baja |
| Efectos externos por diseño | Ninguno | Ninguno en simulación | Pruebas de proceso |
| Dependencias necesarias | Potencialmente std | Potencialmente std | Dependiente del SO |
| Riesgo de sobrediseño | Bajo | Medio | Alto |
| Comportamiento que puede ilustrar en fixtures sintéticos (no seguridad acreditada) | Procedencia declarada, comparabilidad y contradicción bajo reglas explícitas | Política determinista simulada | Restricciones de entorno |
| Principal incertidumbre | Semántica de evidencia | Identidad y revocación | Portabilidad |

## Reglas para seleccionar
1. Elegir **una** capacidad observable, no un motor general completo.
2. Definir no-objetivos y límites de recursos.
3. Acordar criterios de aceptación y pruebas negativas antes de implementar.
4. Decidir cómo se documentarán resultados para usuarios noveles.
5. Identificar explícitamente las propiedades que **no** se estarán probando.

## Preguntas de arquitectura sin respuesta
- ¿El primer entregable será ejecutable de consola, biblioteca, web estática o documento interactivo?
- ¿Qué plataformas son obligatorias en v0 y cuáles futuras?
- ¿Cómo representamos tiempo, identidad de fuente, versiones y correcciones?
- ¿Qué formato de entrada minimiza superficie de parser?
- ¿Cómo evitamos confundir un test con evidencia de seguridad integral?
