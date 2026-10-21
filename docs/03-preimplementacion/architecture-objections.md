# Objeciones y revisión crítica previa a código

**Estado: deliberación abierta.**

## Objeción 1 — Confundir datos con verdad
Un valor validado solo tiene formato correcto. **Mitigación propuesta:** conservar etiquetas de procedencia declarada y separar validación de autenticación.

## Objeción 2 — Contradicción artificial
Dos temperaturas diferentes pueden corresponder a puntos o instantes distintos. **Mitigación:** comparabilidad explícita; si falta contexto, NO_COMPARABLE.

## Objeción 3 — Falsa precisión
Usar `f64` sin definir semántica puede generar diferencias por redondeo. **Mitigación:** investigar representación decimal o entero escalado antes de elegir tipo Rust.

## Objeción 4 — Complejidad ontológica prematura
Crear un sistema universal de unidades o conocimiento antes del primer caso bloquearía el aprendizaje. **Mitigación:** catálogo pequeño y versionado.

## Objeción 5 — Seguridad ilusoria
Un CLI offline sin red reduce superficie, pero sigue expuesto a entradas malformadas y agotamiento de recursos. **Mitigación:** límites y tests negativos; no afirmar sandboxing.

## Objeción 6 — Inercia de implementación
Un prototipo puede acabar dictando la arquitectura general. **Mitigación:** declarar módulos y formatos experimentales, permitir desecharlos y no aceptar ADR por tener código.

## Objeción 7 — Incompatibilidad con THE MACHINE generalista
Un laboratorio de observaciones es estrecho. **Respuesta provisional:** validar invariantes transferibles (procedencia, incertidumbre, contradicción) sin generalizar prematuramente.

## Objeción 8 — Licencia y gobernanza
Un repositorio privado no garantiza derecho a redistribuir. **Mitigación:** resolver titularidad y licencia antes de publicación, sin suponer licencia abierta.

## Decisión
Mantener **NO-GO** hasta resolver decisiones abiertas y registrar revisión explícita.
