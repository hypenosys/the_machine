# Issue #34 — auditoría AST reproducible y estado de evidencias (28-10-2026)

**Corte auditado:** `master` / `80db1db1b3a93c880e8cedbc70c556725f6da368`; árbol Git `0bd8957790f8f666606d5e0319d6c5ce6b47523a`. El corte se lee desde Git por SHA fijo; este informe y el auditor añadidos después no forman parte del universo auditado. **Alcance:** auditoría documental externa, no ejecución de THE MACHINE, de código de producto, harness de producto ni CI. `HOLD / NO-GO` no cambia.

## 1. REF-01 — inventario y resultado del parser

Se parsearon los **130 blobs `.md`** del árbol congelado. El manifiesto íntegro, con `(path, blob_sha)` ordenado y cada nodo de enlace, está en [`pr34-markdown-ast-manifest-80db1db1.json`](pr34-markdown-ast-manifest-80db1db1.json). El auditor read-only reproducible es [`pr34-markdown-ast-audit.py`](pr34-markdown-ast-audit.py); SHA-256 del script: `1fe7c86c1302081f0db1d9d9cf6577e82c7c1f6cc461001de5264f5ca3f13d62`. **SHA-256 del manifiesto:** `3ce0d6288b2455823618a5cb25890cf678f89b05f9c6d99d86e79c39d5a8854f`.

| Recuento del corte `80db1db` | Resultado |
|---|---:|
| Blobs Markdown inventariados | 130 |
| Enlaces renderizados extraídos | 196 |
| Enlaces a archivos locales existentes | 170 |
| Destinos con esquema externo (no visitados) | 26 |
| Imágenes Markdown / HTML `img[src]` observadas | 0 / 0 |
| HTML `a[href]` observado | 0 |
| Destinos locales ausentes, fuera del árbol o con `%` inválido detectados | **0** |
| Referencias con fragmento que requieran comprobar anclas | 0 |
| Enlaces a directorio observados | 0 |
| Diagnósticos de destino local | **0** |

**Parser/configuración:** Python `3.12.14`; `markdown-it-py 4.2.0`, `linkify-it-py 2.0.3`, `mdurl 0.1.2`, `uc-micro-py 2.0.0`; `MarkdownIt('default', html=True, linkify=True, typographer=False)`. El perfil CommonMark usa las extensiones estilo GFM activadas por el preset `default` (incluidas tablas/strikethrough) y autolinks de `linkify`. Se mantuvo HTML activado y se extrajeron `href/src` de nodos HTML renderizados cuando estaban presentes. El inventario contiene cero casos HTML/imágenes/fragmentos/directorios: sus recuentos cero describen este corpus. Las fixtures sintéticas comprueban ejemplos concretos de estos tipos, sin demostrar exhaustividad.

Instalación aislada y dos invocaciones idénticas (ningún módulo del producto se importó):

```sh
python3 -m pip install --target /tmp/the-machine-md-audit \
  markdown-it-py==4.2.0 linkify-it-py==2.0.3 mdurl==0.1.2 uc-micro-py==2.0.0
PYTHONPATH=/tmp/the-machine-md-audit python3 docs/04-auditorias/pr34-markdown-ast-fixtures.py
PYTHONPATH=/tmp/the-machine-md-audit python3 docs/04-auditorias/pr34-markdown-ast-audit.py /tmp/manifest-1.json
PYTHONPATH=/tmp/the-machine-md-audit python3 docs/04-auditorias/pr34-markdown-ast-audit.py /tmp/manifest-2.json
sha256sum /tmp/manifest-1.json /tmp/manifest-2.json
```

Ambas ejecuciones del auditor corregido produjeron SHA-256 `3ce0d6288b2455823618a5cb25890cf678f89b05f9c6d99d86e79c39d5a8854f`, 130 archivos, 196 nodos y cero diagnósticos. La repetición se hizo en un mismo entorno/host. El manifiesto incluye la versión de Python: otra versión puede producir otro digest aun cuando los resultados semánticos sean iguales.

Una segunda extracción ad hoc con el mismo parser contrastó el multiconjunto `(ruta, destino)` de los 196 nodos `link`, el inventario de 130 blobs y la existencia en el árbol de los destinos `EXISTS_FILE`. Comparte el parser y no prueba equivalencia con GitHub ni independencia humana.

**Reproducción independiente del HEAD anterior `b8490ec5fc414fc080b2c9ace48358e5de95dff3`:** se verificaron los hashes originales del script (`ade82bf789b308dd5391eb6181237d56b9fa250607cb3a90768e3e7a233212d2`) y manifiesto (`b71aaccb4f43e9e032aec2d7437824a9016979b45f879b2f550aa7d233dac765`). Dos ejecuciones con Python `3.12.14` y las cuatro versiones de dependencia anteriores produjeron `c2c2a96988ec04989507036e11ab2d30fa20a84133188a711cb55df1eea3c61f`; el único campo JSON distinto respecto del manifiesto publicado con Python `3.11.2` fue `python_version`. Se trata de una ejecución independiente, no de una revisión humana independiente atribuida a otro cotitular.

**Correcciones comprobadas con [`pr34-markdown-ast-fixtures.py`](pr34-markdown-ast-fixtures.py):** el auditor anterior calificaba como ausentes un archivo `assets/logo.png` y un directorio `assets/` existentes si no eran Markdown; ahora inventaría todos los blobs para resolver destinos. Para `a.md → b.md#source-heading` consultaba el encabezado de `a.md` en vez de `b.md`; ahora consulta el destino y mantiene los slugs como candidatos no certificados. El orden de ocurrencia de HTML en bloque seguía a todos los enlaces inline en vez del orden del documento; se corrigió. El recolector anterior omitía atributos `href/src` de etiquetas distintas de `a` e `img`; ahora los recoge también, sin afirmar que GitHub los conserve tras el filtrado HTML. La comparación histórica anterior reutilizaba una misma coincidencia AST para varias filas idénticas; ahora consume ocurrencias una a una. La fixture incluye dos filas históricas iguales para una sola ocurrencia AST y verifica 1/2 coincidencias, además de excluir un blob cambiado. En el corpus real no cambiaron los 80/80, el inventario ni las 196 entradas.

**Corrección posterior a PR #35:** el auditor integrado en `14366c2d901ea3025a89a2c39b20bb9cfeb5214d` terminaba con `ValueError: Invalid IPv6 URL` al encontrar `<a href="http://[">`, sin dejar una incidencia atribuida al archivo en el manifiesto. La fixture reproduce el caso y ahora exige una entrada y un diagnóstico `INVALID_URL` con ruta, blob y bloque de origen. La salida anterior era un fallo visible, no un éxito falso. El corpus congelado no contenía ese caso: los únicos cambios de contenido del manifiesto real son el hash del propio auditor. La versión integrada previamente tuvo SHA-256 de auditor `4a9d48798ecc2f65fa239751522828cf21061ad712b4e1833d54fbfd14f36beb` y de manifiesto `3fabf200f0235bd1dbd05371cc75bbca83d442601405f8578792983d332ce3c5`; esta corrección no altera esa evidencia histórica.

**Alcance de `INVALID_URL`:** esta categoría indica exclusivamente que `urllib.parse.urlsplit` lanzó `ValueError` al descomponer el destino. No es una validación completa de la URL: otros destinos malformados pueden no causar esa excepción y quedar como `EXTERNAL_SCHEME`, estado que tampoco certifica su validez ni disponibilidad. No se consulta la red ni se valida, por ejemplo, el puerto de todos los destinos externos.

Las fixtures ejecutadas cubren además inline y referencias, imágenes, HTML `href/src`, código literal, escapes, percent-encoding, traversal, directorios, anclas y dos serializaciones idénticas. Son ejemplos sintéticos, no prueba universal del comportamiento de GitHub. Los scripts se ejecutaron fuera de THE MACHINE; no se importó ni ejecutó código del producto.

### Comparación acotada con las 162 observaciones regex históricas

La comparación conserva **dos denominadores distintos**: el registro histórico corresponde a 103 Markdown del commit `3ff2f14fbc96c3f73768f1e870491155f36144b6`; el AST actual corresponde a 130 Markdown del commit `80db1db...`.

- Los manifiestos regex históricos contienen 162 observaciones en 23 archivos.
- Para 80 observaciones el `(path, blob_sha)` histórico sigue idéntico en el corte actual: **80/80** destinos aparecieron como enlaces renderizados con el mismo destino en el AST.
- Las 82 observaciones restantes pertenecen a seis blobs modificados: **no comparables** contra el texto actual. No se clasifican como falsos positivos ni como errores.
- Esta línea base regex es positiva solamente: no permite medir omisiones del regex histórico, ni convierte la igualdad de 80 pares en prueba exhaustiva del parser.
- El denominador y los recuentos AST del corte actual no se suman a 162.

El detalle de esta reconciliación está también en `historical_regex_comparison` del manifiesto.

### Límites residuales de REF-01

1. El parser no es el renderizador GitHub. La equivalencia de GFM, filtrado de HTML y la política de slug/anchors de GitHub **no se certifican**. No había enlaces con `#` que resolver en este corte.
2. Los enlaces de red no se abrieron ni se verificó su disponibilidad externa.
3. El parser no expone posición por nodo inline: cada incidencia conserva el rango de líneas del bloque padre, no una línea/columna exacta. En tres entradas no se pudo preservar el lexema original desde el AST; el manifiesto deja `raw_target=null` y registra el destino parseado. El emparejamiento de texto en las otras entradas tampoco finge una columna exacta.
4. No hubo observaciones de imagen, atributos HTML, fragmentos ni rutas a directorio en el corpus real; sus fixtures son sintéticas y no demuestran cobertura exhaustiva.
5. Los destinos locales se comprobaron contra los blobs/directorios del mismo árbol Git, no contra un renderizador/servidor de GitHub. No se afirma una validación universal de enlaces externos o semántica visual. El parser normaliza destinos: por ejemplo, `broken%ZZ.md` puede llegar como `broken%25ZZ.md`; no se certifica la detección de todos los escapes inválidos del lexema fuente. La decodificación UTF-8 usa reemplazo y la comparación histórica depende de las filas reconocidas por la expresión regular.

**Estado REF-01:** `AST_AUDIT_REPRODUCED_WITH_EXPLICIT_LIMITS`; cero destinos locales problemáticos detectados en este alcance; pendiente la revisión de la versión corregida y la independencia exigida por CLOSE-01 antes de `LINKS_READY_FOR_REVIEW`. No se afirma `0 contradicciones` ni integridad universal.

## 2. SEC-01 — clasificación de cobertura documental

La evidencia en `verification-plan.md`, `traceability.md`, el registro de oráculos REV-19 y los documentos de idempotencia/separación respalda lo siguiente. Estos estados distinguen el **alcance documental** del **resultado de pruebas**; ninguno es `PASS`.

| Caso | Estado de cobertura | Ejecución | Bloqueo / alcance acreditado |
|---|---|---|---|
| `TH-008` / `SEC-REQ-006` | `PARTIAL` | `NOT_RUN` | `SEC-006` trata un conflicto epistemológico concreto, no todos los mecanismos de ocultación. `O-TH008` sólo candidato, sin ID SEC ratificado; requiere protocolo/autoridad de prueba antes de ejecutarse. |
| `TH-017` / `SEC-REQ-008` | `PARTIAL` | `NOT_RUN` | `SEC-008` no demuestra vencimientos aplicados a todas las copias. `O-TH017` candidato; faltan política, alcance de copias y aprobación. |
| `TH-014` / `SEC-REQ-011` | `PARTIAL` | `NOT_RUN` | `SEC-011` cubre truncamiento local sintético, no pérdida de energía real. `O-TH014` candidato; simulación futura y prueba física son alcances distintos, esta última no autorizada. |
| `TH-011` / `SEC-REQ-010` | `PARTIAL` local; `BLOCKED` remoto | `NOT_RUN` | `SEC-010` nominal no demuestra replay remoto ni exactly-once. Un resultado remoto incierto debe permanecer `UNKNOWN`; falta contrato aprobado de reconciliación. |
| `TH-019` / `SEC-REQ-016` | `PARTIAL` documental; `BLOCKED` para cierre | `NOT_RUN` | `SEC-016` sigue pendiente/no asignada de forma ratificada. No están definidos identidad efectiva, operaciones sensibles ni independencia del aprobador; el oráculo C-02 es propuesta. |

**Autorización requerida antes de cualquier prueba futura:** aprobación separada del protocolo y del oráculo para cada alcance, decisión sobre IDs de pruebas, fuente/fixtures versionados, entorno y responsable autorizados, evidencia reproducible y revisión independiente. Para `TH-014`, cualquier prueba de corte eléctrico real requeriría autorización específica adicional. El contenido actual no autoriza escribir, compilar, ejecutar ni desplegar THE MACHINE.

**Estado SEC-01:** clasificación documental completada como arriba; pruebas ejecutadas = 0; oráculos ratificados = 0; `HOLD / NO-GO`.

## 3. Gobernanza y cierre del issue

La casilla GOV-01 del issue se corrigió a pendiente; la evidencia versionada no respalda la marca anterior de completada: el acta candidata conserva `NOT_RATIFIED` y los comentarios/revisiones de PR #33 no aceptan de forma específica los blobs para `DEC-GOV-010` y `DEC-GATE-003`. La revisión `APPROVED`/comentario `OK` anteriores no sustituyen la decisión conjunta atribuible. **No se imputan votos a los cotitulares.**

CLOSE-01 también sigue abierto: la reproducción técnica independiente no acredita por sí sola la identidad de un revisor humano distinto del autor ni una aprobación de la versión corregida. Por ello, aunque REF-01 y SEC-01 tienen evidencia nueva y reproducible, no se cierra ni se marca íntegramente resuelto el issue. `AUT-CODE`, `AUT-EXEC`, `AUT-MERGE` y `DEC-08` permanecen fuera de alcance y no concedidos.
