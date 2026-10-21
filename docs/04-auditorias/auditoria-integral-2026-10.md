# Informe ejecutivo y técnico de la auditoría integral — THE MACHINE

**Fecha de emisión:** Octubre de 2026
**Auditor independiente:** Jules — Equipo Multidisciplinar de Auditoría Técnica Independiente
**Repositorio:** `hypenosys/the_machine`
**Rama de auditoría:** `audit/integral-repository-review-2026-10`
**Rama base:** `master`
**Estado actual del proyecto:** **HOLD / NO-GO para escribir código**
**Recomendación del auditor:** **CONDITIONAL GO** (recomendación condicionada exclusivamente para evaluar un experimento minimalista offline).

---

## 1. Misión y alcance real de la auditoría

El presente informe consolida los hallazgos de la auditoría integral, crítica, adversarial y reproducible realizada sobre el repositorio **THE MACHINE**.

Siguiendo los principios **Evidence-First** and **Zero Fabrication**, el equipo de auditoría ha evaluado los documentos del proyecto sin asumir la validez de ninguna especificación por el mero hecho de figurar en `master`.

### Alcance efectivamente ejecutado
- **Inventario forense del código y metadatos**: Inspección recursiva de 70 archivos Markdown en la raíz y subdirectorios `docs/`, así como la verificación explícita de archivos ocultos y directorios punto (`.github/`, `.git/`). Verificación de clonado superficial (*shallow repository*) y comprobación de ausencia total de código Rust (`.rs`), manifiestos de Cargo (`Cargo.toml`) o flujos de CI/CD (`.github/workflows`).
- **Auditoría documental y de consistencia**: Revisión cruzada de la jerarquía normativa (`README.md`, `PHILOSOPHY.md`, `GLOSSARY.md`, `docs/00-empezar/`, `docs/01-investigacion/`, `docs/02-diseno/`, `docs/03-preimplementacion/`).
- **Auditoría de arquitectura y epistemología computacional**: Evaluación analítica de la especificación candidata Opción A (`Source`, `Artifact`, `Claim`, `EvidenceLink`, `Assessment`, `Relation`) y formulación/comparación de 4 alternativas arquitectónicas (Opciones A, B, C y D).
- **Auditoría de seguridad y modelo de amenazas**: Análisis de las 20 amenazas priorizadas (`TH-001`..`TH-020`), 17 requisitos verificables (`SEC-REQ-001`..`SEC-REQ-017`), 14 pruebas de seguridad y 5 Registros de Decisiones de Arquitectura (`ADR-0001`..`ADR-0005`).
- **Registro y priorización de brechas (Gap Analysis)**: Identificación y fichado detallado de 10 brechas clasificadas de `GAP-001` a `GAP-010`.
- **Evaluación de preparación (Readiness Gates G0-G5)**: Examen de criterios de paso para la autorización de la fase de código.

---

## 2. Registro de Comandos Ejecutados para Reproducibilidad

En cumplimiento del principio de **Reproducibilidad**, se registran los comandos exactos ejecutados para la inspección y verificación del repositorio:

```bash
# 1. Comprobación del estado del clonado y Git
git rev-parse --is-shallow-repository
# Output real: true

git log --oneline --all
# Output real: c3fdd58 docs: consolidate unified epistemic contract and stop at code gate (#14)

# 2. Inspección explícita de archivos e inspección de workflows ocultos (.github)
find . -type f | sort && ls -la .github/ 2>&1
# Output real: Inexistencia del directorio .github/ (ls: cannot access '.github/': No such file or directory)
# Total en repositorio: 70 archivos .md (0 archivos .rs, 0 Cargo.toml, 0 workflows CI/CD)

# 3. Verificación automatizada de enlaces relativos Markdown
python3 -c '
import os, re, glob
md_files = glob.glob("**/*.md", recursive=True)
links = []
for f in md_files:
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
        matches = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
        for text, target in matches:
            if not target.startswith("http://") and not target.startswith("https://") and not target.startswith("#"):
                links.append((f, target))
broken = []
for source_file, target in links:
    clean_target = target.split("#")[0]
    if not clean_target: continue
    target_path = os.path.normpath(os.path.join(os.path.dirname(source_file), clean_target))
    if not os.path.exists(target_path): broken.append((source_file, target, target_path))
print(f"Total markdown files: {len(md_files)} | Relative links: {len(links)} | Broken links: {len(broken)}")
'
# Output real: Total markdown files: 70 | Relative links: 80 | Broken links: 0

# 4. Verificación de archivos modificados en el diff
git status --short
# M README.md
# ?? docs/04-auditorias/
```

---

## 3. Hallazgos principales y contradicciones detectadas

### 3.1. Inexistencia de archivo de licencia legal (GAP-001 - Medium / Legal)
El repositorio se presenta en `CONTRIBUTING.md` y `README.md` como un proyecto con intención de apertura. Sin embargo, **no existe ningún archivo `LICENSE`** en la raíz. Según el marco legal de propiedad intelectual, el código y la documentación sin licencia se consideran "Todos los derechos reservados", lo que constituye una limitación legal para la redistribución o contribución pública.

### 3.2. Hipótesis de sobreingeniería en el núcleo epistemológico y precisión sobre semántica temporal (GAP-003 y GAP-006)
`docs/03-preimplementacion/unified-specification-candidate-v0.md` (línea 35) ya menciona conceptualmente `valid_time`, `recorded_time` y `assessed_time`. El hallazgo real (**GAP-003**) es la **ausencia de una especificación formal de tipos, formato de serialización y reglas de verificación bitemporal en tiempo de ejecución**. Asimismo, el modelo de 6 entidades de la Opción A presenta una hipótesis de sobrecarga que debe ser evaluada mediante experimentos frente a alternativas como la Opción B (propuesta del auditor).

### 3.3. Incobertura de pruebas en la matriz global de seguridad (GAP-002)
Tres amenazas graves (`TH-012` Confused Deputy, `TH-016` Backup irrecuperable y `TH-019` Insider abuse) **carecen de pruebas especificadas** (`SEC-XXX`) en la matriz de trazabilidad global.

### 3.4. Estado de los Registros de Decisiones de Arquitectura (GAP-005)
Los 5 ADRs centrales del proyecto (`ADR-0001` a `ADR-0005`) permanecen en estado `Proposed`.

---

## 4. Matriz de estado real del proyecto (Gates G0-G5)

| Gate | Criterio de Aceptación | Estado Real / Evaluación | Justificación |
|---|---|---|---|
| **G0 — Documentación** | Problema, activos y límites de confianza descritos. | **PARCIAL** | Alineado con `readiness-review.md`. Falta formalizar el producto mínimo de gobernanza. |
| **G1 — Investigación** | Fuentes contrastadas y alternativas analizadas. | **PARCIAL / BLOQUEADO** | Alternativas analizadas. Investigación externa por red BLOQUEADA en sandbox. |
| **G2 — Diseño** | ADRs Accepted y contratos de datos definitivos. | **BLOQUEADO** | ADRs en `Proposed` y 3 brechas P1 en la matriz global de seguridad. |
| **G3 — Implementación** | Código Rust compilable y tests unitarios. | **NO INICIADO** | Zero líneas de código Rust. Estado de HOLD / Sin código. |
| **G4 — Despliegue** | Sandbox verificado y pruebas adversariales. | **NO INICIADO** | Requiere fase G3. |
| **G5 — Operación** | Monitorización y respuesta a incidentes. | **NO INICIADO** | Inaplicable en estado actual. |

---

## 5. Índice de entregables de la auditoría en `docs/04-auditorias/`

Toda la evidencia de esta auditoría se encuentra detallada en los seis documentos en `docs/04-auditorias/`:

1. [`auditoria-integral-2026-10.md`](auditoria-integral-2026-10.md): Informe ejecutivo y técnico consolidado (este documento).
2. [`gap-register.md`](gap-register.md): Registro oficial con las 10 brechas priorizadas (`GAP-001` a `GAP-010`).
3. [`architecture-review.md`](architecture-review.md): Evaluación de la Opción A y análisis comparativo con la Opción B (propuesta del auditor), C y D.
4. [`security-review.md`](security-review.md): Modelo de amenazas, trazabilidad de seguridad y riesgos residuales (clasificados como NO EVALUADO / Hipótesis).
5. [`research-evidence.md`](research-evidence.md): Inventario de referencias normativas (NIST, OWASP, MITRE, SLSA, W3C) y registro de límites por aislamiento de red.
6. [`readiness-assessment.md`](readiness-assessment.md): Evaluación de Readiness Gates (G0-G5) y recomendación CONDITIONAL GO.

---

## 6. Secuencia priorizada de acciones recomendadas

1. **Primero (Gobernanza)**: Decidir sobre el archivo de licencia `LICENSE` (**GAP-001**) previa distribución pública.
2. **Segundo (Arquitectura)**: Evaluar la especificación del núcleo (Opción A vs. Opción B) mediante un experimento minimalista e incorporar la especificación formal de serialización bitemporal (**GAP-003**).
3. **Tercero (Seguridad)**: Asignar pruebas a `TH-012`, `TH-016` y `TH-019` en la planificación global de seguridad (**GAP-002**).
