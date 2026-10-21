# Paquete de Decisión Preimplementación y Protocolo de Deliberación — THE MACHINE (v1)

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Repositorio:** `hypenosys/the_machine`
**Ubicación:** `docs/03-preimplementacion/decision-package-v1.md`
**Carácter:** **CANDIDATO NO NORMATIVO** (Documento de análisis, propuesta y deliberación; no aprueba decisiones de forma autónoma, no sustituye especificaciones ni autoriza código).
**Estado del proyecto:** **HOLD / NO-GO (Cero código ejecutable, cero manifiestos Cargo, cero tests en Rust)**
**Propósito:** Proporcionar al titular del proyecto (@Axlfc) una estructura de decisión rigurosa, trazable y falsable para orientar la deliberación formal sobre `DEC-01..DEC-08`, tras subsanar los ocho defectos semánticos y documentales identificados en revisiones previas.

---

## 1. Contexto, Principios y Taxonomía Epistémica

### 1.1 Naturaleza del Entregable
El presente paquete constituye una propuesta **CANDIDATA NO NORMATIVA**. No modifica el estado de los Registros de Decisiones de Arquitectura (`ADR-0001..0005`, los cuales permanecen en estado `Proposed`), no da por cerrado el registro de brechas de autoridad (`GAP-010`) ni autoriza la transición a la fase de implementación de software (Gate G4). Toda decisión normativa o cambio de estado del proyecto requiere una ratificación expresa por parte del titular del proyecto.

### 1.2 Taxonomía de Evidencia
En cumplimiento estricto de las directrices metodológicas de `AGENTS.md` y `PHILOSOPHY.md`, toda afirmación en este documento se adscribe a una de las siguientes categorías epistémicas:
- **OBSERVADO:** Hecho o estado verificado directamente en el árbol de archivos existente de `master`.
- **INFERIDO:** Deducción lógica fundamentada a partir de las especificaciones o diagramas observados.
- **PROPUESTO:** Opción, contrato o recomendación sometida a la deliberación del titular.
- **NO VERIFICADO:** Propiedad, prueba o hipótesis que carece de comprobación empírica en la fase actual.
- **VERIFICADO:** Resultado validado mediante evidencia experimental ejecutable (estado inalcanzable en la fase actual de preimplementación).

### 1.3 Dimensiones Temporales y Opcionalidad
Conforme a `claim-semantics-v0.md` y `offline-experiment-contract-candidate-v0.md`, el sistema reconoce la independencia conceptual de tres dimensiones temporales distintas:
1. `valid_time`: Intervalo o instante en el que el hecho ocurrió o es válido en el dominio externo (opcional).
2. `recorded_time`: Momento exacto en que la atestación o artefacto fue registrado en el sistema (opcional/según perfil).
3. `assessed_time`: Instante en el que el evaluador u oráculo emitió un dictamen epistemológico (opcional/según perfil).

La ausencia de cualquiera de estas marcas temporales **no se trata como un error de formato universal (`MALFORMED`)**, sino como una característica del dato a ser evaluada por las reglas del perfil de dominio correspondiente.

---

## 2. Matriz de Decisiones Preimplementación (DEC-01..DEC-08)

A continuación se presenta la matriz detallada de las ocho decisiones estratégicas. Cada decisión incluye sus opciones, costes, riesgos, evidencia asociada, dependencias, autoridad requerida y recomendación provisional.

### DEC-01 — Alcance y Límites del Producto Inicial (v0)
- **Opciones Evaluadas:**
  - *Opción A:* Laboratorio epistemológico offline de datos sintéticos sintético (sin red, sin persistencia duradera, sin LLM, sin acciones sobre el host).
  - *Opción B:* Pasarela de acciones simuladas (Action Gateway) con motor de políticas.
  - *Opción C:* Harness de investigación de aislamiento sobre SO.
- **Costes y Complejidad:** La Opción A presenta el menor coste de mantenimiento y complejidad accidental, enfocándose exclusivamente en la fidelidad del razonamiento.
- **Riesgos Asociados:** La Opción A no valida conectores de red, persistencia física ni aislamiento por SO.
- **Evidencia Observada:** Ninguna opción ha sido ejecutada (**NO VERIFICADO**).
- **Dependencias:** Ninguna (Decisión base).
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Recomendación Provisional (PROPUESTO):** Aprobar la **Opción A** exclusivamente para el primer experimento de laboratorio acotado (Gate G1).

### DEC-02 — Representación Arquitectónica de Evidencia y Atribución
- **Opciones Evaluadas:**
  - *Opción R1:* Contrato unificado de 6 entidades (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`).
  - *Opción R2:* Contrato minimalista de 2 entidades (`Artifact` opaco + `Attestation`).
  - *Opción Híbrida (C):* Envoltorio minimalista en el núcleo con perfil de grafos extendidos bajo demanda.
  - *Opción Baseline D:* Control específico de dominio sin abstracción genérica (Baseline).
- **Costes y Complejidad:** R1 impone mayor sobrecarga de tipos; R2 reduce el núcleo pero traslada complejidad al perfil; Híbrida equilibra flexibilidad; D carece de interoperabilidad.
- **Riesgos Asociados:** Elegir R1 sin evidencia empírica puede introducir complejidad accidental (`GAP-006`).
- **Evidencia Requerida:** Ejecución comparativa del arnés de pruebas sintéticas (`comparative-contract-v1.md`).
- **Dependencias:** DEC-01, Gate G1.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Recomendación Provisional (PROPUESTO):** Someter R1, R2, Híbrida y Baseline D a evaluación objetiva en el laboratorio sintético sin declarar ganador de forma anticipada.

### DEC-03 — Frontera de Computación del Núcleo y Harness de E/S
- **Opciones Evaluadas:**
  - *Opción A:* Núcleo puramente funcional (funciones puras sin E/S, sin red, sin acceso al reloj del SO), relegando la E/S al Harness sintético.
  - *Opción B:* Núcleo con abstracciones de traits para E/S y temporizadores.
- **Costes y Complejidad:** La Opción A garantiza determinismo absoluto y reproducibilidad simple de pruebas.
- **Riesgos Asociados:** Exige que el Harness prepare la totalidad del contexto temporal y de entradas.
- **Evidencia Observada:** `offline-experiment-contract-candidate-v0.md` describe esta separación.
- **Dependencias:** DEC-01.
- **Autoridad:** Titular del proyecto / ADR correspondiente.
- **Recomendación Provisional (PROPUESTO):** Aprobar la **Opción A** (Núcleo puramente funcional sin E/S).

### DEC-04 — Tratamiento de Privacidad y Supresión de Datos (Escenario E-10)
- **Opciones Evaluadas:**
  - *Opción A:* Permitir simulación lógica de supresión en memoria volátil sin prometer borrado físico ni cumplimiento legal.
  - *Opción B:* Bloquear por completo E-10 hasta disponer de una política formal de retención/supresión y cumplimiento normativo.
  - *Opción C:* Excluir expresamente E-10 del primer experimento sintético.
- **Costes y Complejidad:** La Opción B evita falsas expectativas de privacidad; la Opción A permite probar la semántica de referencias rotas en memoria.
- **Riesgos Residuales:** Afirmar que una simulación lógica equivale a borrado seguro o cumplimiento RGPD/CCPA es falso y peligroso.
- **Evidencia Observada:** E-10 figura como **BLOQUEADO** en `offline-experiment-contract-candidate-v0.md` (§4).
- **Dependencias:** DEC-01, Política de Seguridad y Privacidad.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Recomendación Provisional (PROPUESTO):** Mantener E-10 en estado **BLOQUEADO** para datos reales, autorizando únicamente una prueba de comportamiento lógico en memoria volátil (Opción A) bajo exención explícita.

### DEC-05 — Oráculos de Falsación Negativos y Pruebas
- **Opciones Evaluadas:**
  - *Opción A:* Adopción de la matriz unificada de oráculos sintéticos F-01..F-10, E-01..E-10, L-01..L-10 y R-01..R-08, con requisito de segundo dominio de prueba.
  - *Opción B:* Validación basada únicamente en casos de éxito (happy path).
- **Costes y Complejidad:** Requiere construir oráculos de abstención (`NOT_COMPARABLE`, `INSUFFICIENT_EVIDENCE`) y detección de contradicción.
- **Riesgos Asociados:** Sin oráculos negativos, el sistema puede inflar la certeza o validar fuentes no autenticadas.
- **Evidencia Requerida:** Matriz de trazabilidad v1 (`traceability-matrix-v1.md`).
- **Dependencias:** DEC-01, DEC-02.
- **Autoridad:** Titular del proyecto (@Axlfc).
- **Recomendación Provisional (PROPUESTO):** Aprobar la **Opción A** (Matriz unificada con pruebas negativas obligatorias).

### DEC-06 — Selección de Formato de Datos, Serialización y Persistencia
- **Opciones Evaluadas:**
  - *Opción A:* Diferir la selección de motor de persistencia (SQLite, Sled, RocksDB) y formatos binarios hasta evaluar los contratos en memoria.
  - *Opción B:* Definir inmediatamente el esquema de persistencia en disco.
- **Costes y Complejidad:** La Opción A minimiza dependencias prematuras y evita acoplamiento a librerías de almacenamiento.
- **Riesgos Asociados:** Ninguno en la fase de laboratorio sintético.
- **Evidencia Observada:** `GAP-003` señala la falta de esquema de serialización.
- **Dependencias:** DEC-02, DEC-03.
- **Autoridad:** Titular del proyecto / ADR correspondiente.
- **Recomendación Provisional (PROPUESTO):** Aprobar la **Opción A** (Diferir decisión de persistencia dura).

### DEC-07 — Licencia Legal y Política de Contribuciones
- **Opciones Evaluadas:**
  - *Opción A:* Dual MIT / Apache-2.0.
  - *Opción B:* Mozilla Public License 2.0 (MPL-2.0).
  - *Opción C:* Reservar todos los derechos hasta la primera versión pública.
- **Costes y Complejidad:** La falta de archivo `LICENSE` (`GAP-001`) impide legalmente contribuciones externas o distribución.
- **Riesgos Asociados:** Incertidumbre jurídica para colaboradores externos.
- **Evidencia Observada:** `GAP-001` abierto en `gap-register.md`.
- **Dependencias:** Ninguna.
- **Autoridad:** Titular del proyecto (@Axlfc) en exclusiva.
- **Recomendación Provisional (PROPUESTO):** El titular elegirá la licencia aplicable para resolver `GAP-001` previamente a cualquier apertura pública.

### DEC-08 — Autorización Expresa para Transición a Código (Gate G4)
- **Opciones Evaluadas:**
  - *Opción A:* Mantener el proyecto en estado **HOLD / NO-GO** hasta satisfacer la totalidad de condiciones de preimplementación y recibir orden explícita.
  - *Opción B:* Conceder autorización automática de código al aprobar el paquete de decisión.
- **Costes y Complejidad:** Ninguno.
- **Riesgos Asociados:** La Opción B viola el protocolo de gobernanza y autoriza implementación sin verificación de pre-código.
- **Evidencia Observada:** El estado del repositorio es strictly **HOLD / NO-GO** (**OBSERVADO**).
- **Dependencias:** Gates G0, G1, G2, G3.
- **Autoridad:** Titular del proyecto (@Axlfc) en exclusiva.
- **Recomendación Provisional (PROPUESTO):** Confirmar la **Opción A (HOLD / NO-GO)**. Ninguna aprobación documental constituye un permiso `GO` para programar software en Rust.

---

## 3. Disposición de Brechas y Gobernanza de Autoridad (GAP-001..GAP-010)

### 3.1 Cláusula de No Cierre Autónomo de GAP-010
Se establece explícitamente que la mera redacción o presentación de este paquete de decisión **NO CIERRA la brecha `GAP-010` (Indefinición del proceso normativo de consolidación)**. La brecha `GAP-010` permanecerá en estado **OPEN** hasta que el titular del proyecto ratifique formalmente el Mapa de Autoridad Documental y el procedimiento de precedencia de normas.

### 3.2 Estado Real de los Registros de Brechas y Decisiones
- **`GAP-001` (Licencia):** OPEN. Pendiente de decisión del titular (`DEC-07`).
- **`GAP-002` (Pruebas TH-012/016/019):** OPEN. Se han diseñado las especificaciones de prueba `SEC-015..017`, pero no están ejecutadas (**NO VERIFICADO**).
- **`GAP-003` (Especificación temporal):** OPEN. Mitigado conceptualmente en `comparative-contract-v1.md`, pendiente de esquema ejecutable.
- **`GAP-004` (Modelo de adversario local):** OPEN. Se aclara que las fronteras lógicas no son isoladores de memoria del SO.
- **`GAP-005` (ADRs en Proposed):** OPEN. `ADR-0001..0005` continúan en estado `Proposed`.
- **`GAP-010` (Autoridad Normativa):** OPEN. Pendiente de ratificación formal por el titular.

---

## 4. Resumen de Recomendaciones y Siguientes Pasos

1. **Mantener Estado HOLD / NO-GO:** No escribir código Rust, no crear manifiestos `Cargo.toml`, no añadir dependencias ni configurar flujos de CI de compilación.
2. **Someter a Deliberación:** Presentar al titular (@Axlfc) las recomendaciones provisionales sobre `DEC-01..DEC-08`.
3. **Procedimiento por Etapas:** Exigir el cumplimiento estricto del Protocolo de Autorización por Etapas (`staged-authorization-protocol-v1.md`), garantizando que la aprobación del marco documental (Gate G0) no autorice automáticamente las fases subsiguientes.
