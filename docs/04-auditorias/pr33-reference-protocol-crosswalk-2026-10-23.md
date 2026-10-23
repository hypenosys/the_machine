# PR #33 — reconciliación de contratos de integridad de referencias (23-10-2026)

**Tipo:** dictamen documental de compatibilidad, sin ejecución de verificador de THE MACHINE. **Estado:** candidato de auditoría, `HOLD / NO-GO`. Fuentes: `pr33-reference-integrity-protocol-candidate-2026-10-23.md`, `pr33-independent-markdown-parser-acceptance-contract-2026-10-23.md`, `pr33-inline-link-coverage-reconciliation-2026-10-23.md` y registro Finch §§4.10–4.18.

## 1. Alcances que no deben mezclarse

| Evidencia | Corte | Unidad | Interpretación permitida |
|---|---|---|---|
| Reconciliación histórica de 100 rutas | `025c69eb9183d8ef96855bab184e1b4fe5193332` | Archivos revisados por métodos heterogéneos | Inventario de alcance, **no** 100 documentos validados con un parser |
| Protocolo LNK-01..08 | `96dddefa060c64c4329a22d9f26e2aef2327c910` (101 Markdown) | Requisitos y estados | **Propuesta**, no resultados de ejecución |
| Nueve manifiestos regex | `3ff2f14fbc96c3f73768f1e870491155f36144b6` (103 Markdown) | 162 apariciones sintácticas aproximadas | Inventario reproducido, no nodos AST certificados |
| Contrato de contraste AST | Mismo corte de 103 Markdown propuesto como entrada | Casos F-01..F-18 y evidencia futura | **Oráculo propuesto**, `PARSER_CONTRAST_NOT_RUN` |
| Delta documental de la PR | HEAD mutable | Documentos nuevos o modificados | Nunca heredará automáticamente la certificación de un corte previo |

**No existe contradicción aritmética** entre 100, 101 y 103 cuando cada cifra conserva su SHA y método. Sí existe **riesgo de falsa equivalencia** si se presentan como progresión de un mismo control.

## 2. Cruce de taxonomías y reglas de precedencia

| Requisito LNK del protocolo | Caso(s) del contrato AST | Resultado canónico en la dimensión de evaluación |
|---|---|---|
| LNK-01 inline e imagen | F-01, F-02, F-04, F-12, F-17, F-18 | `VALID`, `MISSING_TARGET`, `NOT_EVALUATED` |
| LNK-02 uso y definición de referencias | F-03, F-15 | `UNDEFINED_REFERENCE` solo si el uso es inequívoco; las definiciones son inventario aparte |
| LNK-03 fragmentos | F-06, F-07, F-14 | `MISSING_ANCHOR` solo con política fijada; si no, `RENDERER_UNKNOWN` |
| LNK-04 HTML | F-09, F-11 | `NOT_EVALUATED` si el modo/parser no soporta la semántica; no asumir ausencia |
| LNK-05 externo | F-08 | `EXTERNAL_UNCHECKED` en la **auditoría offline**; comprobación temporal de red, si autorizada, en canal separado |
| LNK-06 texto literal en código | F-10, F-11 | `LITERAL_REFERENCE` es naturaleza sintáctica, **no** `VALID` |
| LNK-07 directorios | F-01/F-05 si el destino es directorio | `POLICY_UNKNOWN` hasta definir si se acepta destino de directorio o índice |
| LNK-08 codificación y escapes | F-05, F-12, F-13, F-16, F-18 | `MALFORMED` o `POLICY_UNKNOWN` según capa; no perder destino original |

Los códigos `REGEX_FALSE_POSITIVE`, `REGEX_MISSED_LINK`, `PARSER_UNSUPPORTED`, `AMBIGUOUS` e `INTENTIONAL_NON_RENDERED` del contrato AST son **etiquetas de reconciliación entre métodos**, no reemplazan la evaluación `VALID/MISSING_TARGET/...` del protocolo. `OUTSIDE_REPOSITORY` e `INVALID_PERCENT_ENCODING` son diagnósticos de normalización que se traducen a `MALFORMED` o `POLICY_UNKNOWN` conforme a política fijada; no introducirlos como nuevos estados canónicos sin decisión explícita.

## 3. Hallazgos de ambigüedad abiertos

- **R-01 — Directorio:** una de las 162 apariciones apunta a un directorio. `exists_in_git_tree` no prueba `VALID` bajo LNK-07: hace falta política sobre enlaces a directorios e índices. **Estado:** `POLICY_UNKNOWN` para la evaluación semántica de esa aparición.
- **R-02 — URL externa:** el comentario GitHub identificado por `6359388844` fue observado mediante API en una comprobación documental ad hoc. Esto demuestra existencia temporal de ese comentario, **pero no cambia automáticamente** `EXTERNAL_UNCHECKED` de un futuro pase formal **offline**. Registrar `OBSERVED_VIA_API_AT_TIME` como evidencia auxiliar y mantener separados los universos.
- **R-03 — Definiciones y usos:** el inventario regex no contiene `REFERENCE_DEFINITION`, pero el parser aún no ha probado ausencia de referencias semánticas. **Estado:** `NOT_EVALUATED`.
- **R-04 — Cobertura de HTML y tablas:** el cribado secundario de patrones no equivale a parser GFM. **Estado:** `NOT_EVALUATED`.
- **R-05 — Fragmentos:** no se detectaron anclas locales en las 162 filas; esto no constituye una prueba positiva de resolución de anchors. **Estado:** `NOT_EVALUATED` para la cobertura AST de anclas.

## 4. Condiciones mínimas para cerrar estas ambigüedades

1. Fijar parser, extensiones y política de directorios/anchors para el mismo commit.
2. Extraer nodos AST y conservar la identidad de las apariciones con posiciones.
3. Reconciliar cada nodo con los manifiestos históricos sin reescribirlos.
4. Resolver la aparición a directorio según política explícita, y registrar cualquier discrepancia.
5. Separar resultados offline de observaciones HTTP/API temporales.
6. Obtener revisión independiente antes de `LINKS_READY_FOR_REVIEW`.

**Conclusión acotada:** los contratos son compatibles **si** se distinguen naturaleza sintáctica, diagnóstico de reconciliación, diagnóstico de normalización y evaluación del destino. No hay base para afirmar `PASS_GLOBAL`, `LINKS_READY_FOR_REVIEW` ni ratificación de gobernanza. Este documento no autoriza implementación, ejecución ni merge.
