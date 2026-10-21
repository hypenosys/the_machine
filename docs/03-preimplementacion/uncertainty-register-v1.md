# Registro de Incertidumbres, Bloqueos y Riesgos Residuales — THE MACHINE (v1)

**Fecha:** Octubre de 2026
**Autor:** Arquitecto Principal e Ingeniero de Ciberseguridad (@Jules)
**Ubicación:** `docs/03-preimplementacion/uncertainty-register-v1.md`
**Carácter:** **CANDIDATO NO NORMATIVO** (Registro de incertidumbres, brechas y riesgos pre-código).
**Estado del proyecto:** **HOLD / NO-GO (Cero código ejecutable, cero manifiestos Cargo)**

---

## 1. Registro Activo de Bloqueos (Blockers)

Se catalogan las condiciones técnicas, jurídicas o normativas que impiden avanzar a las fases de código o publicación sin una resolución previa:

### BLOQUEO-01 — Experimento de Privacidad y Supresión E-10 (Defecto B-08)
- **Estado Real:** **BLOQUEADO**.
- **Descripción:** El oráculo E-10 evalúa la supresión de contenido sensible. En la fase actual, el proyecto carece de una política formal de retención, minimización y supresión de datos adaptada a normativas de privacidad (RGPD/CCPA).
- **Condición de Desbloqueo Limitada:** Exclusivamente se autorizará un test de simulación de comportamiento en memoria volátil (ocultación de referencias activas en el Harness), **declarando explícitamente que dicha simulación NO constituye borrado físico en disco, anonimización irreversible ni cumplimiento legal**.

### BLOQUEO-02 — Ausencia de Licencia Legal (`GAP-001`)
- **Estado Real:** **BLOQUEADO para distribución o contribución pública**.
- **Descripción:** El repositorio carece de archivo `LICENSE`. Jurídicamente, todo el contenido permanece bajo derechos de autor reservados (*All Rights Reserved*).
- **Condición de Desbloqueo:** Elección e incorporación formal del archivo de licencia por parte del titular (@Axlfc) en `DEC-07`.

### BLOQUEO-03 — Autoridad Normativa Indefinida (`GAP-010`)
- **Estado Real:** **BLOQUEADO para la adopción normativa de especificaciones**.
- **Descripción:** La existencia de propuestas de decisión (incluyendo este paquete v1) no sustituye el procedimiento de autoridad normativa ni la ratificación por parte del titular.
- **Condición de Desbloqueo:** Aprobación explícita del Mapa de Autoridad Documental y precedencia de normas por el titular.

---

## 2. Estado Real y Riesgos Residuales de Brechas Abiertas (GAP-001..GAP-010)

| ID Brecha | Dominio | Severidad | Estado Real | Riesgo Residual Vigente |
|---|---|---|---|---|
| **GAP-001** | Gobernanza / Licencias | Medium | **OPEN** | Imposibilidad legal de aceptar contribuciones o publicar código de forma abierta. |
| **GAP-002** | Seguridad / Cobertura | High | **OPEN** | Amenazas TH-012, TH-016 y TH-019 carecen de pruebas ejecutadas en el plan global. |
| **GAP-003** | Arquitectura / Tiempo | High | **OPEN** | Falta de esquema formal de serialización y parsing de marcas bitemporales en Rust. |
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

- **TH-012 (Confused Deputy):** Se ha diseñado la especificación de prueba sintética `SEC-015` en la documentación. **Estado de Ejecución: NO EJECUTADO / UNVERIFIED**.
- **TH-016 (Backup irrecuperable / Persistencia Inconsistente):** Se ha diseñado la especificación de prueba sintética `SEC-016`. **Estado de Ejecución: NO EJECUTADO / UNVERIFIED**.
- **TH-019 (Insider Abuse / Alteración Unilateral de Reglas):** Se ha diseñado la especificación de prueba sintética `SEC-017`. **Estado de Ejecución: NO EJECUTADO / UNVERIFIED**.

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
| **Fidelidad de representación** | Propiedad Deseada | **HIPÓTESIS A PROBAR** | Requiere la corrida exitosa de los fixtures F-01..F-10 en el laboratorio sintético. |
