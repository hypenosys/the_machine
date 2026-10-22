# Registro de Incertidumbres, Bloqueos y Riesgos Residuales — THE MACHINE (v1)

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Ubicación:** `docs/03-preimplementacion/uncertainty-register-v1.md`
**Carácter:** **CANDIDATO NO NORMATIVO** (Registro de incertidumbres, brechas y riesgos pre-código).
**Estado de gobernanza:** **HOLD / NO-GO** para escribir, compilar o ejecutar código. No se certifica la ausencia de artefactos en todas las ramas.

---

## 1. Registro Activo de Bloqueos (Blockers)

Se catalogan las condiciones técnicas, jurídicas o normativas que impiden avanzar a las fases de código o publicación sin una resolución previa:

### BLOQUEO-01 — Experimento de Privacidad y Supresión E-10 (Defecto B-08)
- **Estado Real:** **BLOQUEADO**.
- **Análisis de Tres Dimensiones:**
  1. *Escenario E-10 original (Supresión física en disco y cumplimiento normativo RGPD/CCPA):* Permanecer estrictamente en estado **BLOQUEADO** por falta de política formal de retención/supresión y modelo de persistencia.
  2. *Simulación alternativa acotada en memoria volátil (ocultación de referencias activas en el Harness):* **PROPONER solicitar autorización expresa a los cotitulares** si se desea evaluar el comportamiento de referencias rotas en memoria volátil, **declarando explícitamente que dicha simulación NO constituye borrado físico en disco, anonimización irreversible ni cumplimiento legal**.
  3. *Exclusión explícita del alcance:* Posibilidad de excluir formalmente E-10 del primer laboratorio sintético sin prometer ni certificar privacidad garantizada.

### BLOQUEO-02 — Alcance y ratificación de la licencia (`GAP-001`)
- **Estado Real:** **REPOSITORIO PÚBLICO; LICENCIA DOCUMENTAL CC BY 4.0 INCORPORADA A MASTER MEDIANTE PR #25; ALCANCE JURÍDICO PENDIENTE**. La consulta GitHub API del 21-10-2026 (`visibility=public`, `license=null`) es histórica y anterior a `LICENSE.md`; no describe la rama actual. Quedan pendientes revisión de derechos de terceros, licencia de código futuro y cierre formal.
- **Descripción actualizada:** El hallazgo original se formuló antes de `LICENSE.md`. `master` incluye CC BY 4.0 para materiales documentales originales cubiertos; no acredita derechos sobre materiales de terceros ni concede licencia para software futuro. El cierre jurídico y formal de GAP-001 permanece abierto.
- **Condición de Desbloqueo:** Revisión por los cotitulares de derechos de terceros, alcance de CC BY 4.0 documental y licencia del software futuro, con cierre formal de GAP-001 cuando corresponda. No modificar visibilidad unilateralmente.

### BLOQUEO-03 — Autoridad Normativa Indefinida (`GAP-010`)
- **Estado Real:** **BLOQUEADO para la adopción normativa de especificaciones**.
- **Descripción:** La existencia de propuestas de decisión (incluyendo este paquete v1) no sustituye el procedimiento de autoridad normativa ni la ratificación por parte de los cotitulares.
- **Condición de Desbloqueo:** Aprobación explícita del Mapa de Autoridad Documental y precedencia de normas por los cotitulares.

---

## 2. Estado Real y Riesgos Residuales de Brechas Abiertas (GAP-001..GAP-010)

| ID Brecha | Dominio | Severidad | Estado Real | Riesgo Residual Vigente |
|---|---|---|---|---|
| **GAP-001** | Gobernanza / Licencias | Medium | **OPEN** | Repositorio público con `LICENSE.md` documental CC BY 4.0 en `master`; pendientes alcance de derechos, licencia de código futuro y cierre formal DEC-07/GAP-001. |
| **GAP-002** | Seguridad / Cobertura | High | **OPEN** | Los diseños SEC-015..017 ya están trazados como propuestas para TH-016/019/012; ninguna prueba se ha ejecutado. |
| **GAP-003** | Arquitectura / Tiempo | High | **OPEN** | Hay semántica temporal y perfiles de serialización candidatos, pero falta un contrato general ratificado; no hay validación implementada en Rust. |
| **GAP-004** | Seguridad / Adversario | High | **OPEN** | Inexistencia de anclaje de confianza si un atacante posee privilegios locales en el host. |
| **GAP-005** | Gobernanza / ADRs | High | **OPEN** | `ADR-0001..0005` permanecen en estado `Proposed` sin valor normativo aceptado. |
| **GAP-006** | Arquitectura / Tipos | Medium | **OPEN** | Posible sobrecarga de complejidad accidental en el modelo R1 sin prueba empírica. |
| **GAP-007** | QA / Reproducibilidad | Medium | **OPEN** | Inexistencia de flujos automatizados de linter o verificación de enlaces Markdown. |
| **GAP-008** | Seguridad / Logging | Medium | **OPEN** | Falta de definición de wrapper de tipos para evitar fugas de datos sensibles en logs. |
| **GAP-009** | Accesibilidad / DX | Low | **OPEN** | Disparidad de tono pedagógico entre carpetas de inicio y documentación técnica. |
| **GAP-010** | Gobernanza | Medium | **OPEN** | Falta de procedimiento formal aprobado para la consolidación de especificaciones. |

---

## 3. Cobertura Real de Amenazas de Seguridad (TH-012, TH-016, TH-019)

En cumplimiento de las reglas metodológicas de `AGENTS.md` (Regla 2: "No inventar pruebas"), se aclara la distinción estricta entre una **propuesta de especificación de test** y una **prueba ejecutada**:

- **TH-012 (Confused Deputy):** Prueba candidata `SEC-017` vinculada a `SEC-REQ-017` en `security/verification-plan.md` y `security/traceability.md`. **PROPUESTA / NO EJECUTADA**. El informe adversarial histórico usaba otro número; no confundirlo con la asignación candidata actual.
- **TH-016 (Backup irrecuperable / Persistencia Inconsistente):** Prueba candidata `SEC-015` vinculada a `SEC-REQ-015` para restauración de backup. **PROPUESTA / NO EJECUTADA**. La antigua `SEC-016` del informe adversarial comprobaba corrupción en carga, que no demuestra recuperabilidad.
- **TH-019 (Insider Abuse / Alteración Unilateral de Reglas):** Prueba candidata `SEC-016` vinculada a `SEC-REQ-016` para separación de autoridad. **PROPUESTA / NO EJECUTADA**.

**Conclusión:** `GAP-002` se mantiene estrictamente en estado **OPEN** hasta que las pruebas propuestas sean implementadas, ejecutadas y verificadas empíricamente.

---

## 4. Registro de Hipótesis Abiertas y Propiedades Deseadas

A fin de erradicar afirmaciones absolutas o injustificadas (Defecto B-05), se clasifican rigurosamente las propiedades del sistema:

| Propiedad / Afirmación | Categoría Epistémica | Estado Actual | Límite o Riesgo Residual |
|---|---|---|---|
| **Determinismo de evaluación** | Propiedad Deseada | **HIPÓTESIS** | Exige que el núcleo sea puramente funcional y carezca de E/S o lectura de reloj. |
| **Inmutabilidad del historial** | Propiedad Deseada | **HIPÓTESIS** | Depende del diseño de la estructura de datos en memoria; no protege contra corrupción de disco o RAM. |
| **Cero superficie de ataque** | Afirmación Errónea | **FALSO / ELIMINADO** | Todo software posee superficie de ataque; la meta es minimizar el privilegio local. |
| **Aislamiento absoluto de seguridad** | Afirmación Errónea | **FALSO / ELIMINADO** | Las fronteras entre Evaluador y Acción son lógicas; no constituyen un sandbox de memoria de SO. |
| **Fidelidad de representación** | Propiedad Deseada | **HIPÓTESIS A PROBAR** | Requiere pruebas autorizadas sobre F-01..F-09 y los casos adicionales expresamente aprobados; F-10/E-10 original permanece BLOQUEADO. |
