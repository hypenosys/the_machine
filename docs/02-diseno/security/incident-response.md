# Respuesta a incidentes — plan inicial

**Estado: PROPUESTO.** No existen todavía mecanismos automáticos de contención validados.

## 1. Detectar
Registrar síntoma, momento, alcance, fuentes y evidencia disponible sin recopilar secretos innecesarios.

## 2. Contener
Suspender conectores afectados, revocar capacidades y detener efectos externos. Preferir modo de solo lectura cuando sea seguro.

## 3. Preservar
Conservar evidencia mínima necesaria con control de acceso, integridad y retención definida; no difundir datos personales.

## 4. Analizar
Identificar actor, frontera vulnerada, causa, datos y sistemas afectados; distinguir hipótesis de hechos confirmados.

## 5. Recuperar
Restaurar desde fuentes verificadas, rotar credenciales comprometidas, aplicar corrección y comprobar invariantes antes de reactivar.

## 6. Aprender
Crear issue de seguridad restringida cuando corresponda, ADR de cambio, tests de regresión y actualización del registro de riesgos.

## Escenarios iniciales
Prompt injection con intento de acción, conector comprometido, fuga de credenciales, dependencia maliciosa, corrupción de memoria y borrado incompleto.

## Pendientes
Contactos, responsables, plazos, severidad, notificaciones legales, canal privado de reporte y simulacros. No publicar detalles explotables de incidentes activos.
