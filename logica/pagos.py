ESTADOS_PAGO = [
    "pendiente",
    "confirmado",
    "en_revision"
]
pagos = []
def registrar_pago(id_solicitud, negocio, domiciliario, valor):

    if valor <= 0:
        print("Error: el valor del pago debe ser mayor a cero.")
        return False

    nuevo_pago = {
        "id_solicitud": id_solicitud,
        "negocio": negocio,
        "domiciliario": domiciliario,
        "valor": valor,
        "confirmacion_negocio": False,
        "confirmacion_domiciliario": False,
        "estado": "pendiente"
    }

    pagos.append(nuevo_pago)

    print("Pago registrado correctamente.")
    return True
def confirmar_pago_negocio(id_solicitud):

    for pago in pagos:

        if pago["id_solicitud"] == id_solicitud:

            pago["confirmacion_negocio"] = True

            actualizar_estado_pago(pago)

            print("El negocio ha confirmado el pago.")
            return True

    print("Pago no encontrado.")
    return False
def confirmar_pago_domiciliario(id_solicitud):

    for pago in pagos:

        if pago["id_solicitud"] == id_solicitud:

            pago["confirmacion_domiciliario"] = True

            actualizar_estado_pago(pago)

            print("El domiciliario ha confirmado la recepcion del dinero.")
            return True

    print("Pago no encontrado.")
    return False
def actualizar_estado_pago(pago):

    if (pago["confirmacion_negocio"]
            and pago["confirmacion_domiciliario"]):

        pago["estado"] = "confirmado"

    elif (pago["confirmacion_negocio"]
          != pago["confirmacion_domiciliario"]):

        pago["estado"] = "pendiente"
def mostrar_pagos():

    if not pagos:
        print("No hay pagos registrados.")
        return

    for pago in pagos:

        print(f"Solicitud: {pago['id_solicitud']}")
        print(f"Negocio: {pago['negocio']}")
        print(f"Domiciliario: {pago['domiciliario']}")
        print(f"Valor: ${pago['valor']}")
        print(f"Estado: {pago['estado']}")
