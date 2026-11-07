# CONDREZ GALLITOS – ESP32

## Descripción del proyecto

Condrez Gallitos es un prototipo electrónico desarrollado con ESP32 y MicroPython. Su objetivo es detectar la presencia de un pedido en una zona de recogida y permitir que un empleado confirme una solicitud mediante un pulsador.

## Componentes utilizados

- ESP32.
- Sensor ultrasónico HC-SR04.
- Pulsador.
- LED amarillo.
- LED verde.
- LED rojo.
- Resistencias de 220 Ω.

## Conexiones

| Componente | GPIO |
|---|---|
| TRIG | 27 |
| ECHO | 26 |
| Pulsador | 4 |
| LED amarillo | 18 |
| LED verde | 19 |
| LED rojo | 21 |

## Funcionalidades

1. Detectar objetos mediante el sensor HC-SR04.
2. Identificar pedidos en la zona de recogida.
3. Confirmar solicitudes mediante un pulsador.
4. Indicar los estados mediante LED.
5. Reiniciar el sistema cuando la zona queda libre.
6. Evitar confirmaciones repetidas.

## Tecnologías

- MicroPython.
- ESP32.
- Wokwi.
- Git y GitHub.

## Simulación en Wokwi

(https://wokwi.com/projects/479995127566781441)

## Archivos del proyecto

- `main.py`: código fuente del ESP32.
- `diagram.json`: conexiones y componentes del circuito.
- `README.md`: documentación.

## Autor

Juan Nicolas Contreras Arias 

## Estado

Prototipo en desarrollo.

PSDT: No funciono el proyecto al sustentar ya que los leds estaban mal conectaos :( 
