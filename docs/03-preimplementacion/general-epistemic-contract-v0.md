# Contrato epistemológico general — candidato v0

**Estado: PROPUESTO / NO-GO para código.** Sustituye conceptualmente la idea de usar temperaturas como modelo raíz; no modifica todavía los ADR.

## Unidades conceptuales
- **Source**: origen declarado o autenticado de información, con nivel de verificación explícito.
- **Artifact**: material recibido o producido (documento, medición, código, transcripción), identificado y versionado.
- **Claim**: proposición atribuida a una fuente sobre un sujeto, predicado, objeto y contexto. No es automáticamente verdadera.
- **EvidenceLink**: relación explícita entre un artefacto y una afirmación, con fragmento, localización y tipo de soporte u oposición.
- **Assessment**: evaluación fechada y versionada que aplica reglas declaradas a afirmaciones y evidencias.
- **Relation**: vínculo tipado entre entidades o afirmaciones, sin inferir causalidad por mera asociación.

## Invariantes
1. La fuente declarada no se presenta como autenticada.
2. Una afirmación no equivale a un hecho.
3. Una evaluación no modifica ni destruye la afirmación original.
4. Cada evaluación identifica las entradas y reglas que utilizó.
5. Contradicción, ausencia de soporte y falta de comparabilidad son estados diferentes.
6. Una conclusión no añade premisas ocultas ni inventa evidencia.
7. Ningún artefacto o texto fuente concede permisos ni ordena acciones.
8. Corregir o retirar información requiere trazabilidad y política de privacidad; no se promete inmutabilidad absoluta.
9. Identidad, igualdad semántica y contexto deben definirse por dominio; no existe equivalencia universal implícita.
10. El sistema puede **abstenerse** cuando no dispone de reglas o evidencia suficiente.

## Resultados de evaluación candidatos
- SUPPORTED: evidencia suficiente **bajo una regla concreta**.
- REFUTED: evidencia incompatible **bajo una regla concreta**.
- CONFLICTED: evidencias incompatibles entre sí sin resolución justificada.
- INSUFFICIENT: información insuficiente para evaluar.
- NOT_COMPARABLE: afirmaciones fuera del dominio de comparación.
- INVALID: entrada o referencia estructuralmente inválida.

Estos estados no son probabilidades, certificados de verdad ni diagnósticos. Se debe evitar que SUPPORTED sea interpretado como «verdadero universalmente».

## Lo que deliberadamente no fija el contrato
Ontología global, inferencia causal, grados de confianza, modelos de lenguaje, motor de persistencia, identificadores criptográficos, parser, serialización y lenguaje de reglas.

## Prueba de diseño
El mismo conjunto de conceptos debe representar sensores, versiones documentales y afirmaciones sobre software sin fingir que todos comparten las mismas reglas de verificación.
