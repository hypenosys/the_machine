# Contrato de evidencia — Diseño educativo preliminar

**Estado: PROPUESTO, no implementado ni verificado.**

Una evidencia es un registro de algo observado o comunicado por una fuente. Debe ser posible corregir su interpretación sin borrar el registro original.

## Ejemplo legible
```text
ID: lectura-A-001
Origen: sensor-A
Hora declarada: 10:00
Valor: 85
Unidad: grados Celsius
Tipo: reporte de sensor
Estado: sin validación independiente
```

## Campos propuestos
- `id`: identifica el registro.
- `source_id`: identifica la fuente.
- `observed_at`: instante al que se refiere la lectura.
- `ingested_at`: instante de recepción.
- `payload`: contenido tipado y limitado en tamaño.
- `provenance`: cómo llegó al sistema.
- `purpose`: finalidad autorizada.
- `retention`: política de conservación.

## Invariantes
1. Nunca convertir una hipótesis en observación automáticamente.
2. Conservar correcciones con un historial explícito.
3. No ejecutar acciones a partir de una lectura sin autorización independiente.
4. Rechazar registros incompletos cuando el contrato exija los campos ausentes.
5. Evitar guardar información personal innecesaria.

## Preguntas abiertas
Formato de persistencia, identificación temporal, integridad criptográfica, versiones de esquema y límites de almacenamiento. Se decidirán tras investigación y pruebas.
