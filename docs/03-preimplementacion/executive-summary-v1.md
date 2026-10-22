# Resumen Ejecutivo para los Titulares del Proyecto — Paquete de Decisión v1 (HOLD)

**Cotitularidad declarada:** @Axlfc y @TopperH4rley. La presente corrección identifica a ambos como titulares del proyecto; **no presume** que cualquiera pueda ratificar unilateralmente, que se exija unanimidad ni que exista delegación. La regla de decisión conjunta, acreditación de identidad y mecanismo de resolución de desacuerdos quedan pendientes de acuerdo explícito de ambos (GAP-010 / REV-16). Hasta entonces, una firma o instrucción aislada no debe interpretarse como ratificación conjunta de gates.

**Fecha:** Octubre de 2026
**Para:** Titulares del Proyecto (@Axlfc y @TopperH4rley)
**De:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Ubicación:** `docs/03-preimplementacion/executive-summary-v1.md`
**Estado de gobernanza:** **HOLD / NO-GO** (ninguna autorización de código, compilación o ejecución; esta síntesis no certifica la ausencia universal de artefactos en todas las ramas)
**Objetivo:** Proporcionar a los titulares una síntesis directa de dos páginas sobre la subsanación de defectos documentales, el estado real del proyecto y las opciones de deliberación inmediata.

---

## 1. Diagnóstico de Estado y Veredicto Global

La documentación candidata sitúa **THE MACHINE** en la etapa de **preimplementación de arquitectura** y propone G2 como referencia de trabajo. **La correspondencia normativa entre G0..G5 y los subgates G2.1..G2.4 no está ratificada** (GAP-010 / REV-05); por ello, esta descripción no constituye certificación formal de haber superado G0/G1 ni de encontrarse en un gate aprobado. Tras la fusión accidental y posterior reversión de entregables previos (PR #22 y PR #23), se ha realizado un trabajo integral de recuperación documental y corrección semántica.

La documentación de auditoría histórica (`informe-auditoria-adversarial-2026.md` en `docs/04-auditorias/`) se conserva separada del **Paquete de Decisión v1** y de la revisión documental candidata de la PR #25. **En el alcance de esta intervención no se ha creado ni ejecutado código Rust, manifiestos Cargo, scripts ni CI.** Esta constatación sobre los cambios documentales no equivale a una comprobación exhaustiva de todos los árboles o ramas del repositorio. El proyecto mantiene **HOLD / NO-GO** y ninguna evidencia experimental aprobada.

---

## 2. Resumen de Resolución de los Ocho Defectos Documentales (B-01..B-08)

| Defecto Subsanado | Problema Identificado Anteriormente | Solución Aplicada en la Entrega v1 |
|---|---|---|
| **B-01 — Integridad Documental** | Sustitución silenciosa del informe de auditoría. | Se ha recuperado y mantenido intacto `informe-auditoria-adversarial-2026.md` en `docs/04-auditorias/`, separando auditoría, propuestas y decisiones. |
| **B-02 — Correspondencia R/F/E/L** | Mapeos temáticos imprecisos entre criterios y fixtures. | Se ha reconstruido la matriz (`traceability-matrix-v1.md`), identificando vacíos como **"SIN FIXTURE DIRECTO"** (R-01, R-07) y proponiendo F-11/F-12 sin renumerar. |
| **B-03 — Comparación Arquitectónica** | Evaluación asimétrica o sesgada entre modelos. | Se ha redactado el contrato neutro (`comparative-contract-v1.md`) aplicando las mismas entradas y expectativas a R1, R2, Híbrida C y Baseline D. |
| **B-04 — Semántica Temporal** | Riesgo de colapsar marcas de tiempo en errores de esquema. | Se preserva la independencia de `valid_time`, `recorded_time` y `assessed_time`: su ausencia no es `MALFORMED` universal, pero un perfil versionado puede exigir campos y declarar errores de esquema propios. El oráculo de clasificación no está ratificado. |
| **B-05 — Garantías Injustificadas** | Afirmaciones absolutas («determinismo 100%», «cero superficie»). | Se han acotado afirmaciones en los documentos v1 intervenidos; **no se acredita una revisión exhaustiva de todas las declaraciones del repositorio**. El determinismo permanece como hipótesis a contrastar. |
| **B-06 — Dependencias y Gates** | Circularidad entre experimentar y autorizar la prueba. | Se ha propuesto un protocolo por etapas (`staged-authorization-protocol-v1.md`); la armonización con las definiciones históricas de gates sigue pendiente de ratificación. |
| **B-07 — Autoridad Normativa** | Cierre prematuro de `GAP-010` sin ratificación. | Se marca el paquete como **CANDIDATO NO NORMATIVO**. `GAP-010` permanece OPEN hasta aprobación explícita de los titulares. |
| **B-08 — Seguridad y Privacidad** | Confusión entre propuestas de test y pruebas ejecutadas. | E-10 permanece **BLOQUEADO**. Se distingue rigurosamente entre especificaciones diseñadas (`SEC-015..017`) y pruebas ejecutadas (0 ejecutadas). |

---

## 3. Matriz Sintética de Decisiones para el Titular (DEC-01..DEC-08)

1. **`DEC-01` (Alcance):** Aprobar exclusivamente un **Laboratorio Epistemológico Offline** de datos sintéticos (sin red, sin persistencia, sin LLM).
2. **`DEC-02` (Representación):** Someter a prueba R1 (6 tipos), R2 (2 tipos), Híbrida C y Baseline D en el laboratorio neutro sin declarar ganador previo.
3. **`DEC-03` (Frontera de E/S):** Diseñar el núcleo como funciones puras sin E/S ni acceso al reloj, planteando el determinismo como hipótesis a probar.
4. **`DEC-04` (Privacidad / E-10):** Mantener E-10 **BLOQUEADO** para datos reales y **PROPONER solicitar autorización expresa a los titulares** para una prueba de ocultación lógica en memoria volátil.
5. **`DEC-05` (Oráculos):** Deliberar sobre la matriz de pruebas negativas (F-01..F-09 y R-01..R-08), con F-10/E-10 BLOQUEADO y casos adicionales sujetos a aprobación con vocabulario estandarizado (`SUPPORTED`, `REFUTED`, `CONFLICTED`, `INSUFFICIENT`, `NOT_COMPARABLE`).
6. **`DEC-06` (Persistencia):** Diferir el motor de persistencia duradera; fijar antes de G2.2 el formato versionado de intercambio sintético y los límites de E/S.
7. **`DEC-07` (Licencia):** Se ha recibido la instrucción de incorporar **CC BY 4.0** y `LICENSE.md` se incorporó a `master` mediante la PR #25 para documentación original y materiales no software con derechos suficientes. La revisión de derechos de terceros, el cierre formal de `GAP-001` y la licencia de software futuro quedan pendientes. La observación de API `license=null` de 2026-10-21 precede a esta incorporación y no describe el estado de la rama actual.
8. **`DEC-08` (Autorización de Código):** Mantener **HOLD / NO-GO** como recomendación provisional. El paquete distingue una eventual **excepción temporal y delimitada** que solo los titulares podrían autorizar expresamente por acta, separando escritura, compilación y ejecución; ninguna está autorizada ahora. Aprobar documentación, G2.1 o una PR **no autoriza código, pruebas ni G3**.

---

## 4. Opciones de Acción Inmediata para los Cotitulares (@Axlfc y @TopperH4rley)

Los titulares disponen de tres alternativas claras de decisión:

- **Opción I — Mantener en HOLD sin ratificar G2.1:** Revisar la documentación entregada, mantener el proyecto congelado y aplazar la apertura de la fase experimental Subgate G2.2 hasta una deliberación posterior.
- **Opción II — Ratificar expresamente G2.1, previa subsanación documental:** Los titulares pueden ratificar el marco metodológico tras resolver las contradicciones materiales de las fuentes candidatas. La mera fusión de una PR no supone ratificación; G2.2 y G3 permanecen bloqueados.
- **Opción III — Solicitar Modificaciones:** Requerir ajustes específicos en los contratos candidatos o en las recomendaciones provisionales de `DEC-01..DEC-08`.

---

## 5. Recomendación Técnica Final

**Recomendación única (condicionada): Opción III, solicitar modificaciones documentales concretas antes de decidir G2.1.** Las contradicciones materiales detectadas en el informe independiente REV-01..REV-20 deben contrastarse con las fuentes originales y corregirse donde queden confirmadas. Después, presentar a los titulares una propuesta de ratificación expresa de G2.1. Hasta entonces, **HOLD / NO-GO**, sin autorización de G2.2 ni G3.
