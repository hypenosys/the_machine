# Paquete de Decisión Preimplementación y Protocolo de Deliberación — THE MACHINE (v1)

**Cotitularidad declarada:** @Axlfc y @TopperH4rley. La presente corrección identifica a ambos como titulares del proyecto; **no presume** que cualquiera pueda ratificar unilateralmente, que se exija unanimidad ni que exista delegación. La regla de decisión conjunta, acreditación de identidad y mecanismo de resolución de desacuerdos quedan pendientes de acuerdo explícito de ambos (GAP-010 / REV-16). Hasta entonces, una firma o instrucción aislada no debe interpretarse como ratificación conjunta de gates.

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Ubicación:** `docs/03-preimplementacion/decision-package-v1.md`
**Carácter:** **CANDIDATO NO NORMATIVO** (Documento de análisis, propuesta y deliberación; no aprueba decisiones de forma autónoma, no sustituye especificaciones ni autoriza código).
**Estado de gobernanza:** **HOLD / NO-GO** (sin autorización para crear, compilar o ejecutar código ni pruebas; la ausencia global de artefactos en todas las ramas no se ha verificado en este paquete)
**Propósito:** Proporcionar a los titulares del proyecto (@Axlfc y @TopperH4rley) una estructura de decisión rigurosa, trazable y falsable para orientar la deliberación formal sobre `DEC-01..DEC-08`, tras subsanar los ocho defectos semánticos y documentales identificados en revisiones previas.

---

## 1. Contexto, Principios y Taxonomía Epistémica

### 1.1 Naturaleza del Entregable
El presente paquete constituye una propuesta **CANDIDATA NO NORMATIVA**. No modifica el estado de los Registros de Decisiones de Arquitectura (`ADR-0001..0005`, los cuales permanecen en estado `Proposed`), no da por cerrado el registro de brechas de autoridad (`GAP-010`) ni autoriza la transición a la fase de implementación de software (Gate G3). Toda decisión normativa o cambio de estado del proyecto requiere una ratificación expresa por parte de los titulares del proyecto.

### 1.2 Taxonomía de Evidencia
En cumplimiento estricto de las directrices metodológicas de `AGENTS.md` y `PHILOSOPHY.md`, toda afirmación en este documento se adscribe a una de las siguientes categorías epistémicas:
- **OBSERVADO [DOCUMENTAL]:** Contenido o estado comprobado en una fuente identificada, con repositorio, rama o revisión y fecha cuando corresponda; un documento de la PR #25 no se atribuye automáticamente a `master`.
- **OBSERVADO [EXTERNO]:** Respuesta de una fuente externa identificada (p. ej., metadatos de GitHub), limitada al momento y campos consultados; no demuestra propiedades del núcleo.
- **INFERIDO:** Deducción fundamentada a partir de fuentes observadas, con supuestos y límites explícitos.
- **PROPUESTO:** Opción, contrato o recomendación sometida a deliberación; no equivale a una decisión aprobada.
- **NO VERIFICADO:** Propiedad, prueba o hipótesis sin evidencia suficiente para el alcance afirmado.
- **VERIFICADO [EXPERIMENTAL]:** Resultado de una ejecución reproducible con evidencia de entorno, entradas, observador y oráculo; **no existe tal evidencia autorizada para THE MACHINE en esta fase**. Una comprobación documental o de API no se etiqueta como verificación experimental.

### 1.3 Dimensiones Temporales y Opcionalidad
Conforme a `claim-semantics-v0.md` y `offline-experiment-contract-candidate-v0.md`, el sistema reconoce la independencia conceptual de tres dimensiones temporales distintas:
1. `valid_time`: Intervalo o instante en el que el hecho ocurrió o es válido en el dominio externo (opcional).
2. `recorded_time`: Momento exacto en que la atestación o artefacto fue registrado en el sistema (opcional/según perfil).
3. `assessed_time`: Instante en el que el evaluador u oráculo emitió un dictamen epistemológico (opcional/según perfil).

La ausencia de cualquiera de estas marcas temporales **no constituye por sí sola un error de formato universal (`MALFORMED`)**. El perfil versionado puede exigir una marca concreta; en ese caso se debe distinguir un **incumplimiento de esquema del perfil** de una abstención epistemológica por información insuficiente. La regla de clasificación y su oráculo permanecen pendientes de ratificación.

---

## 2. Matriz de Decisiones Preimplementación (DEC-01..DEC-08)

A continuación se presenta la matriz detallada de las ocho decisiones estratégicas. Cada decisión incluye sus opciones, costes, riesgos, evidencia asociada, dependencias, autoridad requerida y recomendación provisional.

### DEC-01 — Alcance y Límites del Producto Inicial (v0)
- **Opciones Evaluadas:**
  - *Opción A:* Laboratorio epistemológico offline de datos sintéticos (sin red, sin persistencia duradera, sin LLM, sin acciones sobre el host).
  - *Opción B:* Pasarela de acciones simuladas (Action Gateway) con motor de políticas.
  - *Opción C:* Harness de investigación de aislamiento sobre SO.
- **Costes y Complejidad (estimación, NO VERIFICADA):** La Opción A podría requerir menos integración y mantenimiento que una pasarela de acciones o un harness de aislamiento de SO; no existe medición comparativa ni estimación de esfuerzo aprobada.
- **Riesgos Asociados:** La Opción A no valida conectores de red, persistencia física ni aislamiento por SO.
- **Evidencia Observada:** Ninguna opción ha sido ejecutada (**NO VERIFICADO**).
- **Dependencias:** Ninguna (Decisión base).
- **Autoridad:** Titulares del proyecto (@Axlfc y @TopperH4rley).
- **Recomendación Provisional (PROPUESTO):** Aprobar la **Opción A** exclusivamente para el laboratorio sintético en la fase de diseño (Subgate G2.2).

### DEC-02 — Representación Arquitectónica de Evidencia y Atribución
- **Opciones Evaluadas:**
  - *Opción R1:* Contrato unificado de 6 entidades (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`).
  - *Opción R2:* Contrato minimalista de 2 entidades (`Artifact` opaco + `Attestation`).
  - *Opción Híbrida (C):* Envoltorio minimalista en el núcleo con perfil de grafos extendidos bajo demanda.
  - *Opción Baseline D:* Control específico de dominio sin abstracción genérica (Baseline).
- **Costes y Complejidad (HIPÓTESIS):** R1 podría aumentar la sobrecarga de tipos; R2 podría desplazar complejidad al perfil; la alternativa híbrida pretende equilibrar ambos costes; D podría exigir adaptaciones adicionales entre dominios. **No hay mediciones ni evidencia experimental que permita afirmar superioridad, equilibrio o ausencia de interoperabilidad de ninguna opción.**
- **Riesgos Asociados:** Elegir R1 sin evidencia empírica puede introducir complejidad accidental (`GAP-006`).
- **Evidencia Requerida:** Ejecución comparativa del arnés de pruebas sintéticas (`comparative-contract-v1.md`).
- **Dependencias:** DEC-01, Subgate G2.2.
- **Autoridad:** Titulares del proyecto (@Axlfc y @TopperH4rley).
- **Recomendación Provisional (PROPUESTO):** Someter R1, R2, Híbrida y Baseline D a evaluación objetiva en el laboratorio sintético sin declarar ganador de forma anticipada (Subgate G2.4).

### DEC-03 — Frontera de Computación del Núcleo y Harness de E/S
- **Opciones Evaluadas:**
  - *Opción A:* Núcleo puramente funcional (funciones puras sin E/S, sin red, sin acceso al reloj del SO), relegando la E/S al Harness sintético.
  - *Opción B:* Núcleo con abstracciones de traits para E/S y temporizadores.
- **Costes y Complejidad:** La Opción A **se plantea como una hipótesis de determinismo**, condicionada a la inmutabilidad de las entradas sintéticas, la especificación explícita de reglas, el orden de procesamiento, el contexto temporal y la ausencia de estado oculto o efectos secundarios. Esta caracterización se armoniza con `uncertainty-register-v1.md`, donde se clasifica rigurosamente como **HIPÓTESIS A PROBAR** y no como propiedad garantizada.
- **Riesgos Asociados:** Exige que el Harness prepare la totalidad del contexto temporal y de entradas.
- **Evidencia Observada:** `offline-experiment-contract-candidate-v0.md` describe esta separación.
- **Dependencias:** DEC-01.
- **Autoridad:** Titulares del proyecto / ADR correspondiente.
- **Recomendación Provisional (PROPUESTO):** Aprobar la **Opción A** (Núcleo puramente funcional sin E/S) como hipótesis de diseño para el laboratorio.

### DEC-04 — Tratamiento de Privacidad y Supresión de Datos (Escenario E-10)
- **Opciones Evaluadas:**
  - *Opción A:* Distinguir tres dimensiones claras:
    1. *Escenario E-10 original (Supresión física y cumplimiento legal):* Permanecer estrictamente en estado **BLOQUEADO**.
    2. *Simulación alternativa acotada en memoria volátil (ocultación de referencias):* **PROPONER solicitar autorización expresa a los titulares** para una prueba limitada en memoria, declarando explícitamente que no equivale a borrado físico ni cumplimiento normativo.
    3. *Exclusión explícita de E-10:* Excluir formalmente E-10 del alcance del primer corte sintético sin prometer privacidad garantizada.
  - *Opción B:* Mantener E-10 totalmente bloqueado sin simulación en memoria.
- **Costes y Complejidad:** La Opción B evita confusiones; la Opción A (vía simulación acotada) exige exención expresa.
- **Riesgos Residuales:** Presentar una prueba de memoria como borrado físico en disco o cumplimiento RGPD/CCPA es falso e inaceptable.
- **Evidencia Observada:** E-10 figura como **BLOQUEADO** en `offline-experiment-contract-candidate-v0.md` (§4).
- **Dependencias:** DEC-01, Política de Seguridad y Privacidad.
- **Autoridad:** Titulares del proyecto (@Axlfc y @TopperH4rley).
- **Recomendación Provisional (PROPUESTO):** Mantener E-10 original en estado **BLOQUEADO** para datos reales, y **PROPONER solicitar autorización expresa a los titulares** si se desea evaluar una simulación lógica acotada en memoria volátil bajo una autorización específica y limitada.

### DEC-05 — Oráculos de Falsación Negativos y Pruebas
- **Opciones Evaluadas:**
  - *Opción A:* Deliberación sobre la matriz de oráculos sintéticos F-01..F-09, E-01..E-09, L-01..L-10 y R-01..R-08; F-10/E-10 original permanece BLOQUEADO y F-11/F-12 son propuestas independientes, empleando la taxonomía estandarizada (`SUPPORTED`, `REFUTED`, `CONFLICTED`, `INSUFFICIENT`, `NOT_COMPARABLE`) y distinguiendo dictámenes de errores internos del sistema (`INTERNAL_FAILURE`, `MALFORMED`).
  - *Opción B:* Validación basada únicamente en casos de éxito (happy path).
- **Costes y Complejidad:** Requiere construir oráculos de abstención (`NOT_COMPARABLE`, `INSUFFICIENT`) y detección de contradicción (`CONFLICTED`).
- **Riesgos Asociados:** Sin oráculos negativos, el sistema puede inflar la certeza o tratar procedencia no verificada como autenticada.
- **Evidencia Requerida:** Matriz de trazabilidad v1 (`traceability-matrix-v1.md`).
- **Dependencias:** DEC-01, DEC-02.
- **Autoridad:** Titulares del proyecto (@Axlfc y @TopperH4rley).
- **Recomendación Provisional (PROPUESTO):** Aprobar la **Opción A** (Matriz unificada con pruebas negativas obligatorias y vocabulario epistémico estandarizado).

### DEC-06 — Selección de Formato de Datos, Serialización y Persistencia
- **Opciones Evaluadas:**
  - *Opción A:* Diferir la selección de motor de persistencia (SQLite, Sled, RocksDB) y formatos binarios hasta evaluar los contratos en memoria.
  - *Opción B:* Definir inmediatamente el esquema de persistencia en disco.
- **Costes y Complejidad (hipótesis):** Diferir la persistencia podría reducir dependencias y acoplamiento prematuros, pero desplaza decisiones y puede introducir costes de migración. No exime de definir un formato de intercambio sintético y su política de dependencias antes de G2.2.
- **Riesgos Asociados:** Ambigüedad de entradas/salidas y falta de reproducibilidad si no se fija el formato de intercambio del laboratorio; persistencia duradera sigue fuera de alcance.
- **Evidencia Observada:** `GAP-003` señala la falta de esquema de serialización.
- **Dependencias:** DEC-02, DEC-03.
- **Autoridad:** Titulares del proyecto / ADR correspondiente.
- **Recomendación Provisional (PROPUESTO):** Diferir la persistencia duradera; especificar antes de G2.2 el formato de intercambio sintético, versionado, límites de E/S y dependencias sin presuponer aprobación.

### DEC-07 — Licencia Legal y Política de Contribuciones
- **Opciones Evaluadas:**
  - *Opción A:* Dual MIT / Apache-2.0.
  - *Opción B:* Mozilla Public License 2.0 (MPL-2.0).
  - *Opción C:* Mantener reserva de derechos sin licencia general de reutilización mientras los titulares deliberan, **aunque el repositorio ya sea públicamente accesible**. La visibilidad pública no implica autorización de distribución por terceros.
- **Costes y Complejidad:** La falta de archivo `LICENSE` (`GAP-001`) deja sin permisos generales explícitos de reutilización o redistribución. El repositorio ya es público; esto no demuestra que cada archivo carezca de avisos específicos ni determina automáticamente la titularidad de terceros.
- **Riesgos Asociados:** Incertidumbre jurídica para colaboradores externos.
- **Evidencia documental (rama PR #25):** Se ha añadido `LICENSE.md` con referencia oficial a CC BY 4.0 para documentación original y materiales no software con derechos suficientes. `gap-register.md` conserva su estado histórico OPEN; no se ha verificado inventario completo de derechos de terceros ni se ha seleccionado licencia para futuro software.
- **Dependencias:** Ninguna.
- **Autoridad:** Titulares del proyecto (@Axlfc y @TopperH4rley) en exclusiva.
- **Decisión expresa recibida (alcance documental):** Se ha recibido la instrucción de incorporar CC BY 4.0; se incorpora en esta PR para la documentación original y materiales no software cuyos derechos puedan licenciarse. **Pendiente:** revisar titularidad y materiales de terceros, registrar cierre o alcance residual de `GAP-001` mediante autoridad competente y decidir por separado una licencia adecuada para cualquier código futuro. El dato histórico de GitHub API (2026-10-21, `visibility=public`, `license=null`) es anterior al commit de licencia y no debe reutilizarse como estado actual.

### DEC-08 — Autorización Expresa para Código de Laboratorio y Transición G3 (SIN RATIFICAR)
- **Opción A — HOLD / NO-GO:** No autorizar creación ni ejecución de código, harness, manifiestos Cargo, scripts o CI; mantener bloqueados los subgates y G3.
- **Opción B — Excepción temporal y delimitada, solo si los titulares lo deciden expresamente:** Definir por acta el objetivo del laboratorio, lenguaje y herramientas, revisión exacta de contratos y fixtures, entorno, datos sintéticos permitidos, actividades concretas (diseño, escritura, compilación y ejecución se autorizan **por separado**), exclusiones, vigencia, condiciones de suspensión/revocación, responsables y evidencias exigibles. La excepción no autorizaría por defecto red, conectores, efectos remotos, persistencia duradera, datos reales, merge ni transición general a G3.
- **Opción C — Autorización automática al aprobar documentación:** **No admisible como inferencia de gobernanza**. Un commit, revisión, merge o ratificación aislada de G2.1 no autoriza código ni pruebas.
- **Costes y riesgos:** Una excepción aumenta superficie de riesgo y complejidad de supervisión; requiere límites verificables y decisión específica. La prohibición actual evita iniciar actividades sin autoridad, pero pospone validación experimental.
- **Dependencias:** DEC-01..06, GAP-010, significado de G3 (REV-05), alcance de G2.1..G2.4 y decisiones sobre privacidad/seguridad. Las definiciones históricas de G3 (antes de escribir código frente a antes de fusionarlo) continúan en conflicto y no se resuelven por este texto.
- **Autoridad:** Titulares del proyecto; independencia de revisión y evidencia de ratificación aún pendientes (REV-16).
- **Recomendación provisional (PROPUESTO):** Mantener **Opción A**. Presentar la Opción B únicamente como posibilidad a deliberar mediante acto expreso y separado; no activarla ni tratarla como autorización implícita.
- **Estado de gobernanza documentado:** **SIN RATIFICAR / HOLD / NO-GO**. No consta en las fuentes examinadas una excepción expresa concedida ni un gate ratificado. Esta PR es exclusivamente documental y no ha ejecutado código; la frase no certifica actividad histórica ni el contenido de otras ramas.

---

## 3. Disposición de Brechas y Gobernanza de Autoridad (GAP-001..GAP-010)

### 3.1 Cláusula de No Cierre Autónomo de GAP-010
Se establece explícitamente que la mera redacción o presentación de este paquete de decisión **NO CIERRA la brecha `GAP-010` (Indefinición del proceso normativo de consolidación)**. La brecha `GAP-010` permanecerá en estado **OPEN** hasta que los titulares del proyecto ratifiquen formalmente el Mapa de Autoridad Documental y el procedimiento de precedencia de normas.

### 3.2 Estado Real de los Registros de Brechas y Decisiones
- **`GAP-001` (Licencia):** OPEN. Pendiente de decisión de los titulares (`DEC-07`).
- **`GAP-002` (Pruebas TH-012/016/019):** OPEN. Se han diseñado las especificaciones de prueba `SEC-015..017`, pero no están ejecutadas (**NO VERIFICADO**).
- **`GAP-003` (Especificación temporal):** OPEN. Mitigado conceptualmente en `comparative-contract-v1.md`, pendiente de esquema ejecutable.
- **`GAP-004` (Modelo de adversario local):** OPEN. Se aclara que las fronteras lógicas no son isoladores de memoria del SO.
- **`GAP-005` (ADRs en Proposed):** OPEN. `ADR-0001..0005` continúan en estado `Proposed`.
- **`GAP-010` (Autoridad Normativa):** OPEN. Pendiente de ratificación formal por los titulares.

---

## 4. Resumen de Recomendaciones y Siguientes Pasos

1. **Mantener Estado HOLD / NO-GO:** No escribir código Rust, no crear manifiestos `Cargo.toml`, no añadir dependencias ni configurar flujos de CI de compilación.
2. **Someter a Deliberación:** Presentar a los titulares (@Axlfc y @TopperH4rley) las recomendaciones provisionales sobre `DEC-01..DEC-08`.
3. **Protocolo por etapas candidato:** Contrastar el Protocolo de Autorización por Etapas (`staged-authorization-protocol-v1.md`) con las definiciones históricas de G0..G5; su precedencia y el significado de G3 están SIN RATIFICAR (GAP-010 / REV-05). Ninguna aprobación documental G2.1 autoriza por sí sola código ni laboratorio.
