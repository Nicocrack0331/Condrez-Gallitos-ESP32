import paho.mqtt.client as mqtt

BROKER = "localhost"
PUERTO = 1883

TEMA_SOLICITUD = "condrez/negocios/solicitud"
TEMA_ESTADO = "condrez/negocios/estado"

def al_conectar(cliente, datos, flags, razon_codigo, propiedades=None):

    if razon_codigo == 0:
        print("Conexion MQTT establecida.")

        cliente.subscribe(TEMA_SOLICITUD)

    else:
        print("Error al conectar con MQTT.")

def al_recibir_mensaje(cliente, datos, mensaje):

    contenido = mensaje.payload.decode("utf-8")

    print("Mensaje recibido:", contenido)

    print("Tema:", mensaje.topic)


cliente = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="condrez_python"
)

cliente.on_connect = al_conectar
cliente.on_message = al_recibir_mensaje


def conectar_mqtt():

    try:
        cliente.connect(BROKER, PUERTO, 60)

        cliente.loop_start()

        print("Conectando al servidor MQTT...")

    except Exception as error:
        print("No fue posible conectar:", error)


def publicar_mensaje(tema, mensaje):

    resultado = cliente.publish(tema, mensaje)

    if resultado.rc == 0:
        print("Mensaje enviado correctamente.")
    else:
        print("Error al enviar el mensaje.")

def desconectar_mqtt():

    cliente.loop_stop()
    cliente.disconnect()

    print("Conexion MQTT finalizada.")
