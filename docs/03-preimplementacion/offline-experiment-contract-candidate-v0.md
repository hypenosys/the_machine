# Contrato candidato del experimento offline — v0

**Estado:** PROPUESTO / NO-GO PARA CÓDIGO. No es una autorización, ADR aceptado, interfaz Rust, prueba ejecutada ni elección de arquitectura.

## 1. Propósito y frontera de alcance
Delimitar un experimento de comparación semántica **con datos totalmente sintéticos**, que permita evaluar A/B/C/D de `precode-decision-protocol-v0.md` y `architecture-paper-falsification-v0.md` sin asumir ganadora. Un prototipo eventual sería local, de memoria, sin red, sin LLM, sin herramientas externas, sin acceso a ficheros del usuario, sin persistencia, sin secretos y sin telemetría. La prohibición de red debe comprobarse posteriormente con pruebas negativas; no se presume garantizada por el diseño.

**Activos del experimento:** fidelidad de las afirmaciones y atribuciones sintéticas; trazabilidad de evaluaciones; integridad de las reglas; ausencia de efectos secundarios; reproducibilidad del procedimiento. **Fronteras:** fixture no confiable → validador de esquema → comparación de dominio → resultado y razones; ningún fixture debe convertirse en política ni comando.

## 2. Separación de responsabilidades propuesta
| Responsabilidad | Núcleo mínimo candidato | Perfil de dominio |
|---|---|---|
| Identidades y versiones de artefactos, afirmaciones y evaluaciones | Contrato abstracto obligatorio, representación por decidir | Nombres y significado de entidades del dominio |
| Atribución y autenticación | Distinguir `declared` / `verified`; jamás confiar en texto | Evidencia y procedimiento externo para autenticar |
| Referencias de evidencia y dependencia | Referencias versionadas y tipo de vínculo | Reglas de independencia/corroboración |
| Tiempo | Distinguir referido, registro y evaluación; ausente ≠ igual | Precisión, zona, intervalos y comparabilidad |
| Comparabilidad | Permitir abstención, error estructurado | Equivalencia, tolerancias, unidades y normalización |
| Evaluación | Registrar regla/version, entradas/versiones, estado, motivos y supuestos | Oráculo de comparación y reglas semánticas |
| Retractación | Registrar vínculo explícito y vigencia derivada | Política de reevaluación |
| Privacidad | No prometer inmutabilidad; permitir eliminación y minimización | Política de retención aplicable |

Esta tabla especifica **capacidades observables**, no exige seis estructuras físicas ni reduce necesariamente a dos. La decisión A/B/C/D permanece abierta.

## 3. Tipos conceptuales y restricciones por resolver
- **ID/version:** identificadores estables, referencias a versiones exactas; no reutilización silenciosa. Codificación, unicidad y generación **ABIERTAS**.
- **Tiempo:** `valid_time`, `recorded_time`, `assessed_time` opcionales y no intercambiables. Zona, precisión, intervalos, origen del reloj y ordenación **ABIERTOS**. No inferir igualdad por ausencia.
- **Modalidad:** `OBSERVATION | TESTIMONY | HYPOTHESIS | PREDICTION | DERIVED` como vocabulario ilustrativo **NO APROBADO**.
- **Resultados conceptuales:** `SUPPORTED | REFUTED | CONFLICTED | INSUFFICIENT | NOT_COMPARABLE`; los resultados del perfil de sensores no se equiparan automáticamente con ellos.
- **Errores:** `MALFORMED` (entrada estructural inválida), `UNSUPPORTED_PROFILE` (perfil no reconocido), `UNRESOLVED_REFERENCE` (referencia inexistente), `LIMIT_EXCEEDED` (límite de recursos), `INTERNAL_FAILURE` (fallo inesperado). Etiquetas candidatas; no confundir error de ejecución con evaluación epistémica.
- **Límites:** tamaño máximo de entrada, número de afirmaciones, profundidad de relaciones, tiempos de ejecución y estrategia de desbordamiento **ABIERTOS**. Los 64 KiB de un documento anterior son hipótesis de perfil, no límite universal.
- **Serialización:** sin elección de JSON, CBOR, Protobuf ni formato temporal hasta ADR/revisión; un ejemplo de datos en texto no sería contrato machine-readable.

## 4. Oráculos de aceptación previstos (NO EJECUTADOS)
| Caso | Precondición | Salida esperada conceptual | Prueba negativa |
|---|---|---|---|
| E-01 | Dos mediciones sintéticas equivalentes en alcance y tiempo, diferencia mayor que tolerancia explícita | `CONFLICTED`, ambas evidencias preservadas, regla versionada | No declarar una lectura «verdadera» |
| E-02 | Unidad/alcance incompatible sin normalización autorizada | `NOT_COMPARABLE` | No convertir silenciosamente |
| E-03 | Fuente autodeclarada «verificada» sin prueba de autenticación | `UNVERIFIED` | No elevar confianza por contenido |
| E-04 | Dos documentos derivados de origen común | Dependencia visible; no contar como independientes | No duplicar corroboración |
| E-05 | Retractación explícita de artefacto anterior | Historial conceptual y estado actual distinguibles | No sobrescribir la evaluación previa |
| E-06 | Tres tiempos diferentes o ausentes | Preservar sus roles y ausencia | No deducir simultaneidad |
| E-07 | «No se observó P» | Atribuir observación finita, no negación universal | No inferir «nunca P» |
| E-08 | Afirmaciones sobre versiones de software distintas | No declarar conflicto sin equivalencia de versión/ámbito | No igualar versiones |
| E-09 | Evidencia insuficiente | `INSUFFICIENT` con motivos | No inventar soporte |
| E-10 | Petición de supresión de contenido sintético marcado como sensible | Registrar obligaciones de minimización y efectos sobre referencias; **política pendiente** | No prometer borrado físico ni retención inmutable |

**E-10 está BLOQUEADO** hasta definir política de retención y supresión. El resto son oráculos propuestos, no resultados.

## 5. Amenazas del corte y verificaciones exigibles
- **Entrada hostil:** tamaños excesivos, referencias cíclicas, datos inválidos, contenido que simula instrucciones; debe tratarse como datos.
- **Confusión de autoridad:** una fuente no confiable no puede cambiar reglas, elevar su autenticación ni habilitar acciones.
- **Efectos secundarios:** cualquier socket, ejecución de procesos o escritura fuera de salida deliberada invalida el alcance; las pruebas negativas y el entorno de aislamiento están por diseñar.
- **Reproducibilidad:** fijar toolchain, plataforma, dependencias, fixtures, versiones de reglas y resultados esperados antes de ejecutar.
- **Privacidad:** no usar datos reales; E-10 es simulación de semántica de borrado, no prueba de borrado de disco.
- **Fuera de alcance:** Action Gateway, permisos persistentes, backups, identidad de usuarios, modelos generativos, operación y red. Sus riesgos no se declaran mitigados.

## 6. Decisiones pendientes y criterio de cierre
1. Aprobar caso de uso, activos y límites del corte.
2. Elegir contrato de entrada/salida y política de errores sin imponer una arquitectura ganadora.
3. Definir perfiles sintéticos, reglas de comparación, equivalencia, tiempos y versiones.
4. Resolver E-10 o excluirlo expresamente del primer corte con justificación y seguimiento.
5. Fijar límites de recursos, plataforma, toolchain y procedimiento de reproducción.
6. Revisar amenazas del corte y pruebas negativas; documentar riesgos residuales y responsables.
7. Determinar licencia antes de distribución pública y estado de ADR relevantes o excepciones limitadas.
8. Registrar decisión **GO expresa de los cotitulares, conforme a un mecanismo de gobernanza ratificado,** si, y solo si, los criterios de `readiness-review.md` quedan satisfechos o exceptuados formalmente.

**Estado final:** CONTRACT CANDIDATE / HOLD. Este documento **no autoriza Rust, Cargo, CI ni cambios de ADR**.
