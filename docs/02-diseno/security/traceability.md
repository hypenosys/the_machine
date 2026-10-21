# Matriz de trazabilidad y cobertura — v0

**Estado: revisión documental, no auditoría de seguridad.**

## Cobertura nominal de amenazas
- TH-001..TH-011 y TH-013..TH-020 tienen al menos un requisito propuesto en [requirements.md](requirements.md).
- TH-012 se cubre mediante SEC-REQ-017, **sin prueba asignada**.
- TH-016 y TH-019 tienen requisitos **sin prueba asignada**.
- Los escenarios de permisos y egress necesitan controles operativos concretos antes de que puedan probarse.
- El listado de 20 amenazas no es exhaustivo: requiere nueva revisión por arquitectura y despliegue.

## Estados separados
| Estado | Significado |
|---|---|
| PROPOSED | Documento o idea en evaluación |
| DESIGNED | Contrato aprobado y revisado |
| IMPLEMENTED | Código presente, sin evidencia suficiente |
| TESTED | Prueba ejecutada con evidencia, resultado explícito |
| VERIFIED | Cumple el criterio bajo el alcance y entorno documentados |
| BLOCKED | Faltan decisiones, herramientas o datos |
| FAILED | Resultado contradice el requisito |

## Gates
G0/G1: documentación e investigación; G2: diseño; G3: implementación; G4: despliegue; G5: operación. Ningún gate queda automáticamente superado por fusionar documentos.

## Política de revisión
Antes de aceptar un ADR, comprobar que cada amenaza relevante tiene al menos un requisito y cada requisito tiene una prueba negativa. La cobertura de enlaces es necesaria pero no suficiente.
