# Reflexión de arquitectura — decisiones que cambian el proyecto

## 1. ¿Qué problema queremos resolver primero?
¿Demostrar que el sistema distingue observación e inferencia, o demostrar que puede actuar de forma segura? Son problemas distintos. Mezclarlos desde v0 oscurece la evidencia.

## 2. ¿Qué significa «generalista»?
¿Un conjunto de contratos interoperables y módulos especializados, o un agente monolítico con acceso a todo? La segunda opción incrementa el radio de daño y dificulta la auditoría.

## 3. ¿Qué no debe hacer THE MACHINE?
No vigilar personas, no ejecutar acciones físicas sin autorización, no confundir fuentes con instrucciones, no almacenar datos por defecto sin finalidad. Deben traducirse en garantías, no solo valores.

## 4. ¿Qué cuenta como éxito?
Una demo que funciona no es suficiente. Éxito inicial sería un caso pequeño que cualquiera pueda explicar, reproducir, falsar y revisar.

## 5. ¿Qué simplificamos?
Sin red, sin plugins, sin autenticación remota, sin modelo generativo obligatorio y sin persistencia para el primer corte son simplificaciones candidatas, no decisiones aprobadas.

## 6. ¿Qué no debemos reinventar?
Criptografía, gestión de identidad, sandboxing del sistema operativo y motores de persistencia: evaluar implementaciones mantenidas antes de escribir las nuestras.

## 7. ¿Cómo sabremos que nos equivocamos?
Establecer contraejemplos: fuentes contradictorias, procedencia falsa, entrada malformada, revocación, crash y fuga de información. Cada afirmación de capacidad requiere condiciones de refutación.

## Propuesta para la reunión de arquitectura
Debatir opciones A/B/C, elegir alcance, definir un ADR de v0 y un protocolo de experimentación. **Detenerse antes de generar el primer archivo de código.**
