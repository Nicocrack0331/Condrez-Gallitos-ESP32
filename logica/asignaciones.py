domiciliarios = []
ultimo_turno = -1
def registrar_domiciliario(nombre, telefono):

    nuevo_domiciliario = {
        "nombre": nombre,
        "telefono": telefono,
        "disponible": True,
        "ocupado": False
    }

    domiciliarios.append(nuevo_domiciliario)

    print(f"Domiciliario {nombre} registrado correctamente.")
def buscar_domiciliario():

    global ultimo_turno

    total = len(domiciliarios)

    if total == 0:
        print("No hay domiciliarios registrados.")
        return None

    for intento in range(total):

        posicion = (ultimo_turno + 1 + intento) % total

        persona = domiciliarios[posicion]

        if persona["disponible"] and not persona["ocupado"]:

            ultimo_turno = posicion

            return persona

    print("No hay domiciliarios disponibles.")
    return None
def ocupar_domiciliario(nombre):

    for persona in domiciliarios:

        if persona["nombre"] == nombre:

            if not persona["disponible"] or persona["ocupado"]:
                print("El domiciliario no esta disponible.")
                return False

            persona["ocupado"] = True

            print(f"{nombre} ha aceptado la solicitud.")
            return True

    print("Domiciliario no encontrado.")
    return False
def liberar_domiciliario(nombre):

    for persona in domiciliarios:

        if persona["nombre"] == nombre:

            persona["ocupado"] = False

            print(f"{nombre} ahora esta libre.")
            return True

    print("Domiciliario no encontrado.")
    return False
def cambiar_disponibilidad(nombre, estado):

    for persona in domiciliarios:

        if persona["nombre"] == nombre:

            if persona["ocupado"] and estado:
                print("El domiciliario tiene una solicitud activa.")
                return False

            persona["disponible"] = estado

            print("Disponibilidad actualizada.")
            return True
    print("Domiciliario no encontrado.")
    return False
