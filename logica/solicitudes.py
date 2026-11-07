from datetime import datetime
ESTADOS_SOLICITUD = [
    "solicitado",
    "asignado",
    "recogido",
    "entregado",
    "cancelado",
    "no atendida"
]
TARIFAS = {
    "cercana": 4000,
    "intermedia": 6000,
    "lejana": 8000
}
solicitudes = []
def crear_solicitud(negocio, destinatario, telefono,
                    direccion, barrio, zona):

    if zona not in TARIFAS:
        print("Error: la zona seleccionada no es valida.")
        return False
    if not negocio or not destinatario or not telefono or not direccion:
        print("Error: faltan datos obligatorios.")
        return False
    id_solicitud = len(solicitudes) + 1
    tarifa = TARIFAS[zona]

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nueva_solicitud = {
        "id": id_solicitud,
        "negocio": negocio,
        "destinatario": destinatario,
        "telefono": telefono,
        "direccion": direccion,
        "barrio": barrio,
        "zona": zona,
        "tarifa": tarifa,
        "domiciliario": None,
        "estado": "solicitado",
        "fecha_creacion": fecha,
        "confirmacion_negocio": False,
        "confirmacion_domiciliario": False
    }
    solicitudes.append(nueva_solicitud)

    print(f"Solicitud #{id_solicitud} creada correctamente.")
    return True
def mostrar_solicitudes():

    if not solicitudes:
        print("No hay solicitudes registradas.")
        return

    for solicitud in solicitudes:
        print(f"Solicitud: {solicitud['id']}")
        print(f"Negocio: {solicitud['negocio']}")
        print(f"Destinatario: {solicitud['destinatario']}")
        print(f"Zona: {solicitud['zona']}")
        print(f"Tarifa: ${solicitud['tarifa']}")
        print(f"Estado: {solicitud['estado']}")
        print (f"id de la solicitud: {solicitud['id']}")
def cambiar_estado(id_solicitud, nuevo_estado):
    if nuevo_estado not in ESTADOS_SOLICITUD:
        print("Error: estado no valido.")
        return False
    for solicitud in solicitudes:
        if solicitud["id"] == id_solicitud:
            solicitud["estado"] = nuevo_estado
            print("Estado actualizado correctamente.")
            return True

    print("Error: solicitud no encontrada.")
    return False
