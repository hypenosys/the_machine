# Revisión de preparación para código — cierre de Iteración 10

**Resultado: NO-GO.** No se ha realizado revisión independiente, experimentos ni compilación.

| Decisión | Propuesta | Pendiente antes de GO |
|---|---|---|
| Alcance | Laboratorio offline con datos sintéticos | Aprobación de alcance |
| Intercambio | JSON UTF-8 versionado | Parser, política de campos duplicados y dependencia |
| Número | Entero escalado `milli_degC` | Límites aritméticos y overflow |
| Tiempo | RFC 3339 normalizado | Precisión y segundos intercalares |
| Comparación | Sujeto, magnitud, contexto, unidad y tiempo idénticos | Revisión de semántica y tolerancia |
| Error | Rechazo atómico del lote | Esquema de errores y exit codes |
| Seguridad | Sin red ni acciones externas | Demostrar límites, no asumirlos |
| Portabilidad | Sin plataforma v0 elegida | Matriz de compiladores/targets |
| Publicación | Repositorio público según comprobación del 21-10-2026; CC BY 4.0 documental incorporada en PR #25 | Derechos de terceros, licencia de software futuro y cierre formal de GAP-001 |
| Verificación | Casos conceptuales | Fixtures, comandos y resultados reales |

## Riesgos bloqueantes
1. El parser JSON puede aceptar duplicados o valores de forma distinta a lo previsto.
2. El manejo del tiempo puede introducir comparaciones erróneas.
3. El tamaño de entrada no limita automáticamente CPU o memoria.
4. El catálogo de unidades podría crecer sin versionado y romper comparabilidad.
5. Una salida local mal diseñada puede sobrescribir archivos; debe restringirse explícitamente.
6. Un conjunto de pruebas positivas no sustituye fuzzing ni pruebas negativas.

## Criterio de parada explícito
**No generar crates, archivos Rust, Cargo.toml, scripts ejecutables ni workflows CI** hasta recibir decisión de GO para este alcance. Solo documentación y revisión conceptual.
