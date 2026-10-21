# Requisitos de seguridad verificables — v0

**Estado: PROPUESTO.** Estos son requisitos de aceptación, no controles implementados.

## Cómo leerlos
Cada requisito responde: ¿qué debe ocurrir?, ¿qué debe impedirse?, ¿cómo se prueba? Los identificadores permanecen estables aunque cambie el código.

| ID | Requisito verificable | Amenaza | ADR | Prueba |
|---|---|---|---|---|
| SEC-REQ-001 | Ningún contenido externo concede autorización | TH-001 | ADR-0001, 0004 | SEC-001 |
| SEC-REQ-002 | Peticiones de privilegio sin concesión válida son denegadas | TH-002 | ADR-0001, 0004 | SEC-002 |
| SEC-REQ-003 | Acciones fuera de alcance se rechazan antes del efecto | TH-003 | ADR-0004 | SEC-003 |
| SEC-REQ-004 | No existe egress externo sin permiso explícito | TH-004 | ADR-0001 | SEC-004 |
| SEC-REQ-005 | Entradas sobre límites se rechazan sin efecto externo | TH-005 | ADR-0001 | SEC-005 |
| SEC-REQ-006 | Reportes contradictorios se preservan sin inventar certeza | TH-006, TH-008 | ADR-0003 | SEC-006 |
| SEC-REQ-007 | La procedencia falsa o no autenticada no se presenta como verificada | TH-007 | ADR-0003 | SEC-007 |
| SEC-REQ-008 | La supresión autorizada alcanza derivados sujetos a política | TH-009, TH-017 | ADR-0003, 0005 | SEC-008 |
| SEC-REQ-009 | La revocación se comprueba antes de ejecutar | TH-010 | ADR-0004 | SEC-009 |
| SEC-REQ-010 | Reintentos no duplican efectos irreversibles | TH-011 | ADR-0004, 0005 | SEC-010 |
| SEC-REQ-011 | Escrituras interrumpidas se detectan y recuperan o abortan | TH-013, TH-014 | ADR-0005 | SEC-011 |
| SEC-REQ-012 | Logs no revelan secretos incluidos en entradas | TH-015 | ADR-0005 | SEC-012 |
| SEC-REQ-013 | Una dependencia no aprobada bloquea la entrega | TH-018 | ADR-0002 | SEC-013 |
| SEC-REQ-014 | Una salida inválida del modelo nunca ejecuta acciones | TH-020 | ADR-0001, 0004 | SEC-014 |
| SEC-REQ-015 | La restauración de backup se demuestra con datos sintéticos | TH-016 | ADR-0005 | Pendiente |
| SEC-REQ-016 | La administración sensible requiere separación de deberes | TH-019 | ADR-0001, 0004 | Pendiente |
| SEC-REQ-017 | La delegación no permite confused deputy | TH-012 | ADR-0004 | Pendiente |

## Requisitos transversales pendientes de diseño
Identidad, secreto y clave, aislamiento de procesos, integridad del binario, cadena de suministro, consentimiento, políticas de conservación, observabilidad, rate limiting y actualización segura.

## Regla de aceptación
Un requisito se marca VERIFIED solo si existe un resultado reproducible asociado al commit, entorno, datos sintéticos, comandos y resultado esperado/obtenido. «Documentado» no significa «verificado».
