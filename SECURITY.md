# Política de Seguridad / Security Policy

## Alcance y Estado del Proyecto
THE MACHINE es un proyecto en fase de **diseño conceptual y preimplementación** (HOLD / Sin código). No contiene ejecutables en producción.

## Reporte Responsable de Vulnerabilidades
Si detectas una debilidad de seguridad en los modelos de amenazas, especificaciones de arquitectura, pasarelas de autorización o en los scripts de auditoría:

1. **NO publiques issues o discusiones públicas** con detalles explotables ni vectores de ataque activos.
2. Utiliza preferentemente la función privada de **GitHub Security Advisories** del repositorio.
3. De forma alternativa, contacta de forma privada con los cotitulares designados en [`GOVERNANCE.md`](GOVERNANCE.md):
   - [@Axlfc](https://github.com/Axlfc)
   - [@TopperH4rley](https://github.com/TopperH4rley)

## Principios de Respuesta a Incidentes
Conforme a [`docs/02-diseno/security/incident-response.md`](docs/02-diseno/security/incident-response.md):
- Las comunicaciones se gestionan de manera confidencial hasta acordar una mitigación o registro formal en el registro de brechas (`gap-register.md`).
- No se incorporan secretos reales ni datos personales en evidencias o reportes.
- Se prioriza la defensa en profundidad, el principio de menor privilegio y la verificación sin invención de certezas.
