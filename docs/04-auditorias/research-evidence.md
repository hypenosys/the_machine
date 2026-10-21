# Fuentes y evidencias de investigación técnica — THE MACHINE

**Fecha de auditoría:** Octubre de 2026
**Auditor independiente:** Investigador de Inteligencia Artificial y Epistemología Computacional (Jules)
**Estado:** Informe de investigación y referencias

---

## 1. Declaración de límites y estado de conectividad

En estricto cumplimiento del principio **Evidence-First**:
- **Conectividad a red**: **BLOQUEADA**. Durante la ejecución de esta auditoría, las peticiones HTTP/HTTPS externas a repositorios y sitios web oficiales estuvieron bloqueadas por restricciones del sandbox de ejecución local.
- **Diferenciación de evidencias**:
  - *Conocimiento previo de estándares*: Conceptos de marcos normativos (NIST AI RMF, OWASP GenAI, MITRE ATLAS, SLSA, W3C PROV-DM) derivados del entrenamiento de base del auditor.
  - *Fuentes efectivamente consultadas*: Documentos Markdown presentes localmente en el repositorio `hypenosys/the_machine`.
  - *Inferencias analíticas*: Conclusiones razonadas sobre la aplicabilidad de dichos estándares al diseño de THE MACHINE.
  - *Validaciones ejecutadas*: Ninguna validación externa fue ejecutada por red.

---

## 2. Referencias a estándares y marcos normativos conocidos

A continuación se detallan los estándares y publicaciones de referencia que fundamentan la evaluación del diseño conceptual de THE MACHINE:

### 2.1. Marcos de seguridad en IA
- **NIST AI Risk Management Framework (AI RMF 1.0)**
  *Organismo*: National Institute of Standards and Technology.
  *Aplicabilidad*: Fundamenta la necesidad de aislar la salida de un modelo generativo y tratarla como una propuesta no confiable (*untrusted proposal*).
- **OWASP Top 10 for Large Language Model Applications**
  *Organismo*: OWASP Foundation.
  *Aplicabilidad*: Ofrece la taxonomía de riesgos para justificar los requisitos `SEC-REQ-001` (Prompt Injection - LLM01), `SEC-REQ-003` (Excessive Agency - LLM08) y `SEC-REQ-004` (Unsecured Egress).
- **MITRE ATLAS™ (Adversarial Threat Landscape for Artificial-Intelligence Systems)**
  *Organismo*: MITRE Corporation.
  *Aplicabilidad*: Clasificación de tácticas y técnicas adversariales sobre sistemas de IA.

### 2.2. Seguridad de software y procedencia
- **SLSA (Supply-chain Levels for Software Artifacts)**
  *Organismo*: OpenSSF.
  *Aplicabilidad*: Sustenta la propuesta de minimización de dependencias en Rust (`ADR-0002`).
- **W3C PROV Data Model (PROV-DM)**
  *Organismo*: World Wide Web Consortium (W3C).
  *Aplicabilidad*: Proporciona un modelo conceptual estándar de procedencia (`Entity`, `Activity`, `Agent`). Se utiliza en `architecture-review.md` como referencia comparativa para evaluar la complejidad del núcleo de seis entidades frente a modelos de procedencia estándar. *(Nota: La referencia a W3C PROV es un marco comparativo teórico, no una prueba empírica que demuestre mecánicamente la superioridad de una arquitectura sobre otra)*.
- **Modelos Bitemporales (Snodgrass)**
  *Referencia*: Literatura sobre bases de datos orientadas al tiempo.
  *Aplicabilidad*: Sirve de base teórica para evaluar cómo gestionar tiempo referido (*valid time*) frente a tiempo de registro (*transaction time*).

---

## 3. Matriz de contraste conceptual: Decisiones de THE MACHINE vs. Estándares

| Decisión de Diseño en THE MACHINE | Estándar de Referencia | Tipo de Evidencia | Conclusión Analítica |
|---|---|---|---|
| Minimización de dependencias (`ADR-0002`) | SLSA / OpenSSF | Conocimiento previo de estándar | Enfoque conceptual alineado con la reducción de superficie de ataque en la cadena de suministro. |
| Pasarela de acciones autorizadas (`ADR-0004`) | OWASP GenAI LLM08 / NIST AI RMF | Conocimiento previo de estándar | Enfoque conceptual alineado con la mitigación de agencias excesivas en modelos de lenguaje. |
| Ausencia de conectores de red por defecto | Principios Local-First | Inspección de documentos locales | Alineado con el diseño de soberanía de datos y funcionamiento desconectado. |
| Modelo ontológico de 6 entidades | W3C PROV-DM / Pragmatismo de Software | Análisis comparativo conceptual | Hipótesis de que el modelo de 6 entidades puede simplificarse. Requiere evaluación experimental directa. |

---

## 4. Estado de verificación de la investigación

- **Acceso a red / Web en vivo**: **BLOQUEADO**.
- **Consultas externas directas**: No fue posible verificar versiones específicas o URLs en vivo durante esta sesión por aislamiento de red.
- **Dictamen**: Las referencias a estándares en la documentación original son conceptualmente atingentes, pero su cumplimiento real requerirá pruebas en binarios compilados una vez iniciada la fase de código.
