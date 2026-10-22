# Revisión de coherencia y punto de decisión previo al código — v0

**Estado:** REVISIÓN PROPUESTA / HOLD / NO-GO. **No se aprueba arquitectura, licencia, ADR ni implementación.**

## 1. Por qué detener la expansión documental
Los PR #15–#19 aportan auditoría, protocolo de comparación, falsación conceptual, contrato experimental y política candidata de ciclo de vida. Más documentación sin pruebas puede aumentar el coste de mantener propuestas contradictorias. El próximo paso no es crear otra ontología: es fijar decisiones y criterios de rechazo verificables.

## 2. Diagnóstico de consistencia cruzada
| Asunto | Documentos | Tensión observada | Resolución propuesta, NO APROBADA |
|---|---|---|---|
| Modelo raíz | `unified-specification-candidate-v0.md`, `architecture-review.md`, `precode-decision-protocol-v0.md` | A (seis entidades) es candidata; B (dos) y C/D alternativas sin validación | No adoptar B ni ratificar A por inercia; exigir trazabilidad y pruebas comunes |
| Alcance del primer experimento | `vertical-slice-a.md`, `design-freeze-candidate-v0.md`, `offline-experiment-contract-candidate-v0.md` | Diseño previo permite lectura/escritura de fixture local; contrato reciente dice sin acceso a ficheros del usuario ni persistencia | Definir explícitamente si el harness de pruebas puede leer fixtures sintéticos y escribir salidas efímeras, distinguiéndolo del núcleo |
| Resultados | `contract-authority-map.md`, `unified-specification-candidate-v0.md`, `offline-experiment-contract-candidate-v0.md` | `CONFLICTO` de sensores no es `CONFLICTED` de Assessment | Mantener namespaces separados y reglas de mapeo versionadas; sin equivalencia implícita |
| Tiempo | `design-freeze-candidate-v0.md`, `claim-semantics-v0.md`, `unified-specification-candidate-v0.md` | Perfil sensorial propone RFC 3339 e instante UTC; núcleo distingue tres tiempos opcionales | No heredar reglas temporales del perfil al núcleo |
| Privacidad | `offline-experiment-contract-candidate-v0.md`, `evidence-lifecycle-privacy-candidate-v0.md` | E-10 bloqueado; simulación lógica en memoria es posible pero no autorizada | Definir si E-10 es simulación sin persistencia y dejar privacidad real abierta |
| Gates | `readiness-review.md`, `readiness-assessment.md` | Auditor recomienda CONDITIONAL GO, proyecto permanece NO-GO | GO solo por decisión expresa de los cotitulares conforme a gobernanza ratificada y alcance fijado |
| Seguridad | `security-review.md`, `gap-register.md` | Tres amenazas sin prueba global; algunas funciones no están en corte offline | Mantener backlog global sin atribuir al corte mitigaciones inexistentes |
| Licencia | `gap-register.md`, README | Hallazgo histórico anterior a `LICENSE.md`; repositorio público y CC BY 4.0 documental en esta PR, sin licencia de software | Revisar derechos de terceros y decidir licencia de software antes de distribuirlo; no confundir con bloqueo técnico de investigación privada |

## 3. Hipótesis arquitectónica que merece prueba
**H:** el núcleo puede ofrecer un contrato común de identidad, versiones, procedencia, dependencia, evaluación, incertidumbre y retractación, mientras cada perfil define equivalencia y significado de dominio.

Esta hipótesis **no prescribe** seis structs, dos structs, persistencia ni arquitectura distribuida. Se rechazaría si no puede conservar las obligaciones comunes entre sensores y afirmaciones sobre software sin pérdida semántica, o si necesita duplicar contratos incompatibles entre perfiles.

### Condiciones explícitas de rechazo
- Se pierde identidad/versionado de una evidencia o evaluación.
- Un artefacto no confiable consigue elevar autoridad, autenticación o ejecutar una acción.
- Se confunde ausencia de evidencia con negación, o atribución con verdad.
- La dependencia común se cuenta como corroboración independiente.
- La retractación no invalida la vigencia de resultados dependientes, o borra su historia de manera incompatible con política.
- El perfil impone semántica de temperatura al núcleo.
- La salida no puede explicar reglas, supuestos, evidencia y motivos de abstención.
- Se declara borrado físico, privacidad o seguridad operativa sin prueba.

## 4. Decisiones concretas que requieren ratificación
| ID | Decisión | Recomendación para deliberar | Estado |
|---|---|---|---|
| DEC-01 | Producto v0 | Laboratorio de afirmaciones/evidencias, con sensores como perfil de prueba, no producto final | ABIERTA |
| DEC-02 | Núcleo/perfiles | Contrato semántico común + perfiles versionados; representación física sin decidir | ABIERTA |
| DEC-03 | Alcance de harness | Fixtures sintéticos de prueba; núcleo sin E/S externa; salida efímera controlada por harness | ABIERTA |
| DEC-04 | E-10 | Simulación lógica de retractación/supresión en memoria; sin garantía de borrado físico | ABIERTA |
| DEC-05 | Evidencia de rechazo | F-01..F-10, segundo dominio, pruebas negativas y trazabilidad de resultados | ABIERTA |
| DEC-06 | Plataforma/serialización | Seleccionar solo después de fijar contrato y límites del corte | ABIERTA |
| DEC-07 | Licencia | Decisión expresa antes de distribución pública | ABIERTA |
| DEC-08 | Inicio de código | GO explícito de los cotitulares conforme a gobernanza ratificada, tras revisión de readiness y riesgos residuales | **NO-GO** |

## 5. Distinguir lo que se puede probar
**Sin código:** coherencia entre documentos, existencia de escenarios falsables, contradicciones normativas y suficiencia conceptual de ejemplos.

**Con código y autorización posterior:** serialización real, rendimiento, límites, memoria, aislamiento, ausencia de sockets/procesos, determinismo y seguridad del ejecutable.

No confundir el diseño de fixtures con su ejecución. No registrar PASS de seguridad, rendimiento ni conformidad legal.

## 6. Punto de parada deliberado
Este documento es un **informe de cierre de investigación documental previa**, no otra especificación normativa. Después de su revisión, no se recomienda producir nuevos contratos por inercia: corresponde decidir DEC-01..DEC-08, registrar disensos y preparar una autorización limitada **solo si** se cumplen los gates aplicables.

**Veredicto:** DOCUMENTACIÓN SUFICIENTE PARA DELIBERAR; INSUFICIENTE PARA AUTORIZAR CÓDIGO. **HOLD / NO-GO.**
