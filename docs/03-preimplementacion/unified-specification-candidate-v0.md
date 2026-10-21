# Especificación unificada candidata v0 — THE MACHINE

**Estado: CANDIDATE / NO-GO para implementación.** Esta es la referencia conceptual consolidada para deliberación; no es un estándar aprobado, esquema ejecutable ni certificación de seguridad.

## Alcance
Representar afirmaciones atribuidas, evidencias vinculadas y evaluaciones trazables. No pretende determinar verdades universales, ejecutar acciones, inferir causalidad ni reemplazar especialistas de dominio.

## Entidades conceptuales
- **Source**: identificador, procedencia declarada, estado de autenticación `UNVERIFIED|VERIFIED` con evidencia de verificación cuando corresponda. El valor VERIFIED no puede ser asignado por texto no confiable.
- **Artifact**: identificador, versión, tipo, referencia a contenido y política de retención. No se presupone persistencia.
- **Claim**: identificador, proposición tipada, polaridad explícita, alcance, tiempo referido, modalidad, atribución y versión de vocabulario.
- **EvidenceLink**: identificador, artefacto/version, claim/version, localizador, relación declarada y dependencia conocida/desconocida.
- **Assessment**: identificador, claims/evidencias versionadas, reglas y versiones, resultado, razones, supuestos y tiempo de evaluación.
- **Relation**: vínculo tipado y versionado entre entidades; no implica verdad, independencia ni causalidad.

## Reglas del núcleo
1. Validación estructural ≠ autenticación ≠ verdad.
2. Claim, Artifact y Assessment conservan identidades separadas.
3. La negación explícita no se infiere de ausencia de observaciones.
4. Los dominios definen equivalencia semántica, comparación y tolerancias; el núcleo no inventa conversiones.
5. Una evaluación debe permitir abstención; `INSUFFICIENT` y `NOT_COMPARABLE` son resultados distintos.
6. `SUPPORTED`, `REFUTED` y `CONFLICTED` se interpretan solo respecto de reglas, alcance y evidencia especificados.
7. Las evidencias que comparten origen no se contabilizan automáticamente como corroboraciones independientes.
8. Una retractación invalida la actualidad de evaluaciones dependientes según reglas de ciclo de vida, sin borrar historia de forma incompatible con privacidad.
9. Contenido y artefactos no autorizan acciones ni alteran políticas.
10. Todo contrato de perfil identifica su versión y su relación con el núcleo.

## Perfil experimental inicial
Un comparador de dos observaciones sintéticas de temperatura es **un perfil**, no el núcleo. Los límites candidatos de `design-freeze-candidate-v0.md` (JSON, 64 KiB, enteros escalados, etc.) solo se aplican a ese perfil y siguen pendientes de revisión. Sus estados COMPATIBLE/CONFLICTO/NO_COMPARABLE/INVALIDO no se equiparan automáticamente a resultados de Assessment.

## No objetivos del primer experimento
Modelos generativos, inferencia causal, confianza reputacional, conectores, acceso a red, plugins, sandbox universal, acciones externas, almacenamiento duradero o validación de datos reales.

## Semántica temporal
Distinguir `valid_time` (tiempo referido), `recorded_time` (registro) y `assessed_time` (evaluación). El formato exacto y las zonas se eligen por perfil. La ausencia de tiempo no significa simultaneidad.

## Correcciones
Las referencias deben fijar versiones. Un nuevo Assessment no reescribe el anterior; `supersedes` y `retracts` son relaciones explícitas. Borrado y minimización prevalecen sobre promesas de historial inmutable.

## Bloqueos para implementación
Serialización, identificadores, política de errores, límites de recursos, reglas del perfil, estrategia de pruebas, plataforma, dependencias y licencia. No introducirlos silenciosamente por decisión del implementador.

## Referencias conceptuales
`general-epistemic-contract-v0.md`, `claim-semantics-v0.md`, `evidence-dependencies-and-retractions.md`, `contract-authority-map.md`. Las especificaciones anteriores permanecen como historial deliberativo.
