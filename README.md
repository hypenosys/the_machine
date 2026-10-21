# THE MACHINE

**Plataforma de investigación, evaluación de evidencia e ingeniería asistida por inteligencia artificial (en fase de diseño conceptual).**

---

## 1. Identidad y propósito

### ¿Qué es THE MACHINE?
**THE MACHINE** es un proyecto en fase de **diseño conceptual y preimplementación** concebido para explorar una arquitectura local (*Local-First*), orientada a la seguridad y con determinismo como hipótesis de diseño pendiente de verificación para el análisis de información, la verificación de procedencia y la evaluación asistida por modelos de lenguaje (LLM/IA).

### Estado de propiedad y licenciamiento
**El repositorio era público** según GitHub API consultada el 21-10-2026 (`visibility=public`, `private=false`). La respuesta histórica `license=null` precede a la incorporación de [`LICENSE.md`](LICENSE.md) en esta rama. La documentación original y materiales no software cubiertos se ofrecen bajo CC BY 4.0; el inventario de derechos de terceros, el cierre formal de **GAP-001** y la licencia de software futuro siguen pendientes. Los cotitulares declarados son @Axlfc y @TopperH4rley; su mecanismo de ratificación continúa sin formalizarse (GAP-010).

### Entrada rápida para principiantes (sin saber programar)
No necesitas experiencia previa en programación para comprender THE MACHINE ni para participar en la revisión de sus ideas:
- Si es tu primera vez en GitHub o en el proyecto, empieza por el itinerario adaptado en [`docs/00-empezar/README.md`](docs/00-empezar/README.md) y la [`guía de GitHub para principiantes`](docs/00-empezar/guia-github.md).
- Explora el [`primer experimento conceptual`](docs/00-empezar/primer-experimento.md) donde se explica cómo dos sensores con datos contradictorios pueden evaluarse sin inventar certezas.

### Objetivos de diseño
El desarrollo de THE MACHINE se orienta por los siguientes **objetivos de diseño** (propiedades que se pretenden alcanzar en la arquitectura e implementación futura, no capacidades actualmente operativas):
1. **Evidence-First**: Desacoplar afirmaciones de certezas absolutas, vinculando conocimiento a datos primarios y evaluaciones.
2. **Zero Fabrication**: Exigir trazabilidad y prohibir la invención de fuentes, pruebas o resultados.
3. **Security by Design**: Establecer fronteras de confianza estrictas, pasarela de acciones con política *deny-by-default* e inspección de salidas de modelos.
4. **Local-First & Privacidad**: Diseñar la plataforma para funcionar desconectada de red, preservando la soberanía de datos del usuario.
5. **Minimización de dependencias en Rust**: Priorizar la biblioteca estándar de Rust y auditar minuciosamente las dependencias de terceros para mitigar riesgos en la cadena de suministro (`ADR-0002`).

### ¿Qué NO es y qué todavía NO hace?
- **NO es un software en producción ni un producto terminado**.
- **No se autoriza código Rust**: el árbol documental de esta rama no demuestra la existencia de implementación ejecutable. No se ha inspeccionado exhaustivamente el historial, todas las ramas, binarios ni entornos externos; HOLD / NO-GO no es una afirmación universal sobre ausencia de artefactos.
- **NO ejecuta acciones en el sistema operativo**: Las pasarelas de autorización y ejecución son especificaciones de diseño no codificadas.
- **NO garantiza aún operabilidad desconectada ni privacidad efectiva**: Dichas propiedades son metas de diseño que deberán ser verificadas en binarios una vez iniciada la fase de código.

---

## 2. Estado real del proyecto (Cuatro Dimensiones)

El estado del proyecto se evalúa objetivamente mediante la auditoría integral de octubre de 2026 (`docs/04-auditorias/`):

| Dimensión / Área | Estado Documentado | Estado Implementado | Estado Verificado | Estado Real / Evaluación de Gate |
|---|---|---|---|---|
| **Documentación de inicio** | Existente | N/A (Documental) | Inspeccionada localmente | **Gate G0: PARCIAL** (Falta formalizar activos mínimos) |
| **Investigación técnica** | Estudios preliminares | N/A (Teórico) | Bloqueado en red | **Gate G1: PARCIAL / BLOQUEADO** (Red aislada) |
| **Arquitectura** | Candidata v0 (6 entidades) | Sin código | Sin prototipo | **Gate G2: BLOQUEADO** (ADRs Proposed / En revisión) |
| **Seguridad** | Modelo STRIDE v0 | Sin código | Sin ejecutable | **Gate G2: BLOQUEADO** (3 brechas en matriz P1) |
| **Gobernanza / Licencia** | En definición | N/A | Pendiente de elección | **GAP-001** (Pendiente de decisión de licencia) |
| **Código Rust** | No iniciado | Zero `.rs` | Zero tests | **Gate G3: NO INICIADO** (HOLD / Sin código) |
| **CI / CD / Tests** | Inexistente | Sin workflows | Sin runner | **GAP-007** (Sin infraestructura de test) |
| **Preparación Prototipo**| Evaluado en Gates | N/A | Evaluado en Gates | **HOLD / NO-GO** (Recomendación CONDITIONAL GO) |

---

## 3. Arquitectura candidata y propuestas de simplificación

La especificación candidata principal (**Opción A**, `docs/03-preimplementacion/unified-specification-candidate-v0.md`) propone un núcleo ontológico compuesto por seis entidades: `Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment` y `Relation`.

Asimismo, el informe de auditoría (`docs/04-auditorias/architecture-review.md`) introduce como **propuesta del auditor** la **Opción B** (Núcleo Mínimo de Procedencia basado en `Artifact` + `Attestation` bitemporales), la cual plantea delegar la semántica compleja a módulos de dominio.

*Estado de la arquitectura*: La Opción A se mantiene como la candidata oficial en la documentación actual del proyecto. La Opción B es una propuesta en evaluación. Corresponde a la gobernanza del proyecto decidir la adopción o hibridación de estas alternativas mediante ensayos experimentales.

---

## 4. Rutas de lectura del repositorio

### Ruta 1: Introducción conceptual para principiantes (sin programar)
1. Comience por [`docs/00-empezar/README.md`](docs/00-empezar/README.md) y [`docs/00-empezar/guia-github.md`](docs/00-empezar/guia-github.md).
2. Lea el [`primer experimento conceptual`](docs/00-empezar/primer-experimento.md) sobre contradicción de sensores.
3. Consulte [`PHILOSOPHY.md`](PHILOSOPHY.md) para conocer la visión del proyecto y [`GLOSSARY.md`](GLOSSARY.md) para los términos.

### Ruta 2: Arquitectura y especificaciones previas a código
1. Revise la especificación candidata en [`docs/03-preimplementacion/unified-specification-candidate-v0.md`](docs/03-preimplementacion/unified-specification-candidate-v0.md).
2. Analice la evaluación crítica de arquitectura en [`docs/04-auditorias/architecture-review.md`](docs/04-auditorias/architecture-review.md).
3. Inspeccione las propuestas ADR en [`docs/02-diseno/adr/`](docs/02-diseno/adr/).

### Ruta 3: Seguridad y análisis de amenazas
1. Consulte el Informe de Auditoría de Seguridad en [`docs/04-auditorias/security-review.md`](docs/04-auditorias/security-review.md).
2. Lea el Modelo de Amenazas STRIDE v0 en [`docs/02-diseno/security/threat-model-v0.md`](docs/02-diseno/security/threat-model-v0.md).
3. Examine los Requisitos Verificables en [`docs/02-diseno/security/requirements.md`](docs/02-diseno/security/requirements.md).

---

## 5. Índice de documentación y reportes de auditoría

Toda la documentación técnica se encuentra organizada en `docs/`:

- **`docs/00-empezar/`**: Introducción conceptual e itinerarios para principiantes.
- **`docs/01-investigacion/`**: Estudios de aislamiento, autorización, persistencia y cadena de suministro en Rust.
- **`docs/02-diseno/`**: Modelo de amenazas, flujos de datos (DFD), requisitos de seguridad y registros ADR-0001 a ADR-0005 (`Proposed`).
- **`docs/03-preimplementacion/`**: Especificaciones candidatas, consistencia, semántica de afirmaciones y casos de aceptación.
- **`docs/04-auditorias/`**: **Entregables de la auditoría integral de octubre de 2026**:
  - [`auditoria-integral-2026-10.md`](docs/04-auditorias/auditoria-integral-2026-10.md): Informe ejecutivo y técnico de la auditoría.
  - [`gap-register.md`](docs/04-auditorias/gap-register.md): Registro oficial de brechas (GAP-001 a GAP-010).
  - [`architecture-review.md`](docs/04-auditorias/architecture-review.md): Evaluación de arquitectura y comparación de Opciones A, B, C y D.
  - [`security-review.md`](docs/04-auditorias/security-review.md): Revisión de seguridad, trazabilidad de amenazas y evaluación de riesgos.
  - [`research-evidence.md`](docs/04-auditorias/research-evidence.md): Fuentes de investigación, marcos normativos (NIST, OWASP, MITRE, SLSA, W3C) y límites de conectividad.
  - [`readiness-assessment.md`](docs/04-auditorias/readiness-assessment.md): Evaluación histórica de Readiness Gates G0-G5; cualquier recomendación CONDITIONAL GO no es autorización.
  - [`informe-auditoria-adversarial-2026.md`](docs/04-auditorias/informe-auditoria-adversarial-2026.md): Informe adversarial histórico, preservado como fuente, no norma ratificada.
  - [`independent-review-remediation-triage-2026-10-21.md`](docs/04-auditorias/independent-review-remediation-triage-2026-10-21.md): Seguimiento candidato de hallazgos REV-01..20 en la PR documental #25; no sustituye decisiones de los cotitulares.

---

## 6. Modelo de seguridad y mitigaciones propuestas

El diseño de seguridad de THE MACHINE se basa en la prevención proactiva:
- **Modelado STRIDE v0**: 20 amenazas identificadas (`TH-001` a `TH-020`).
- **Requisitos de seguridad**: 17 requisitos verificables (`SEC-REQ-001` a `SEC-REQ-017`).
- **Pasarela de acciones (Action Gateway - ADR-0004)**: Intercepción de peticiones de herramientas mediante políticas *deny-by-default*.

*Aviso de estado*: Los controles descritos aquí son **objetivos de diseño conceptual**, no controles acreditados en funcionamiento. Esta revisión documental no incluye evidencia de implementación o ejecución de las mitigaciones; tampoco certifica la ausencia de código en otras ramas o entornos.

---

## 7. Principales brechas identificadas (Gap Register)

Entre los 10 hallazgos registrados en [`docs/04-auditorias/gap-register.md`](docs/04-auditorias/gap-register.md), destacan:
1. **GAP-001**: Se ha incorporado [`LICENSE.md`](LICENSE.md) con CC BY 4.0 para documentación y materiales no software originales cuyos derechos correspondan a los licenciantes. El cierre formal del GAP, el inventario de derechos de terceros y la licencia de eventual código siguen sujetos a verificación y decisión separadas.
2. **GAP-002**: SEC-015..017 están documentadas como pruebas candidatas para TH-016, TH-019 y TH-012 respectivamente; ninguna ha sido ejecutada o verificada.
3. **GAP-003**: Incompleitud en la especificación formal y serialización de campos temporales (`valid_time`, `recorded_time`, `assessed_time`).
4. **GAP-004**: Indefinición del modelo de adversario y anclaje de confianza para persistencia de capacidades locales.
5. **GAP-005**: Registros de decisión de arquitectura (ADR) en estado `Proposed`.

---

## 8. Hitos proyectados

1. **Hito 1**: Verificar alcance y derechos de la licencia documental CC BY 4.0 ya propuesta en esta rama, resolver formalmente `GAP-001` y deliberar la gobernanza de ADRs; sin licencia de software aprobada.
2. **Hito 2**: Evaluación y decisión sobre la especificación del núcleo (Opción A vs. Opción B) y formalización de la semántica temporal (`GAP-003`).
3. **Hito 3**: Revisión y autorización de las pruebas candidatas SEC-015..017; su existencia documental no cierra `GAP-002`.
4. **Hito 4**: Decisión expresa del titular para evaluar la recomendación de un primer experimento minimalista offline de dos sensores (`docs/03-preimplementacion/vertical-slice-a.md`).

---

## 9. Gobernanza y contribuciones

Actualmente el proyecto está en estado de **HOLD / Sin código**, por lo que no acepta Pull Requests de código funcional en Rust. Las contribuciones se limitan a la revisión crítica de la documentación, modelos de seguridad y especificaciones de arquitectura presentadas mediante solicitudes de cambio o nuevos registros ADR (`docs/02-diseno/adr/TEMPLATE.md`).


## 10. Licencia documental

La documentación original y demás materiales no software cubiertos por los derechos de los colaboradores se ofrecen bajo **Creative Commons Attribution 4.0 International (CC BY 4.0)** según [`LICENSE.md`](LICENSE.md). Se exige atribución y aviso de modificaciones. Los contenidos de terceros y el futuro código fuente no quedan automáticamente licenciados por esta declaración. La adopción documental en la rama de la PR no ratifica los gates ni demuestra que todos los materiales tengan derechos aclarados.
