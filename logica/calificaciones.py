calificaciones = []

def registrar_calificacion(id_solicitud, calificador, calificado, tipo, puntuacion, comentario):

    if puntuacion < 1 or puntuacion > 5:
        print("Error: la calificacion debe estar entre 1 y 5.")
        return False

    if tipo not in ["negocio", "domiciliario"]:
        print("Error: tipo de calificacion no valido.")
        return False

    # Verificar que los campos esten completos
    if not calificador or not calificado:
        print("Error: faltan datos de los usuarios.")
        return False

    # Crear calificacion
    nueva_calificacion = {
        "id_solicitud": id_solicitud,
        "calificador": calificador,
        "calificado": calificado,
        "tipo": tipo,
        "puntuacion": puntuacion,
        "comentario": comentario
    }

    calificaciones.append(nueva_calificacion)

    print("Calificacion registrada correctamente.")
    return True
def mostrar_calificaciones():

    if not calificaciones:
        print("No hay calificaciones registradas.")
        return

    for calificacion in calificaciones:

        print(f"Solicitud: {calificacion['id_solicitud']}")
        print(f"Calificador: {calificacion['calificador']}")
        print(f"Calificado: {calificacion['calificado']}")
        print(f"Puntuacion: {calificacion['puntuacion']}/5")
        print(f"Comentario: {calificacion['comentario']}")
def calcular_promedio(nombre_usuario):

    puntuaciones = []

    for calificacion in calificaciones:

        if calificacion["calificado"] == nombre_usuario:
            puntuaciones.append(calificacion["puntuacion"])

    if not puntuaciones:
        print("Este usuario todavia no tiene calificaciones.")
        return 0

    promedio = sum(puntuaciones) / len(puntuaciones)

    return round(promedio, 2)
