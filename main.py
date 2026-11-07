from logica.usuarios import registrar_usuario, mostrar_usuarios
from logica.solicitudes import (
    crear_solicitud,
    mostrar_solicitudes,
    cambiar_estado
)
from logica.asignaciones import (
    registrar_domiciliario,
    buscar_domiciliario,
    ocupar_domiciliario,
    liberar_domiciliario,
    cambiar_disponibilidad
)
from logica.pagos import (
    registrar_pago,
    confirmar_pago_negocio,
    confirmar_pago_domiciliario,
    mostrar_pagos
)
from logica.calificaciones import (
    registrar_calificacion,
    mostrar_calificaciones,
    calcular_promedio
)
NOMBRE_SISTEMA = "CONDREZ GALLITOS"
VERSION = "1.0.0"
def mostrar_encabezado():

    print("=" * 50)
    print(f"{NOMBRE_SISTEMA:^50}")
    print("Sistema de gestion de domicilios".center(50))
    print(f"Version: {VERSION}".center(50))
    print("=" * 50)
def pausar():

    input("\nPresione ENTER para continuar...")
def menu_usuarios():

    while True:

        print("\n========== GESTION DE USUARIOS ==========")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("0. Volver al menu principal")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            nombre = input("Nombre completo: ")
            usuario = input("Nombre de usuario: ")
            contrasena = input("Contrasena: ")
            rol = input("Rol (administrador, negocio, domiciliario): ")

            registrar_usuario(nombre, usuario, contrasena, rol)

        elif opcion == "2":

            mostrar_usuarios()

        elif opcion == "0":

            break

        else:

            print("Opcion no valida.")

        pausar()
def menu_solicitudes():

    while True:

        print("\n========== GESTION DE SOLICITUDES ==========")
        print("1. Crear solicitud")
        print("2. Mostrar solicitudes")
        print("3. Cambiar estado")
        print("0. Volver al menu principal")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            negocio = input("Nombre del negocio: ")
            destinatario = input("Nombre del destinatario: ")
            telefono = input("Telefono: ")
            direccion = input("Direccion: ")
            barrio = input("Barrio o instrucciones: ")
            zona = input("Zona (cercana, intermedia, lejana): ").lower()

            crear_solicitud(
                negocio,
                destinatario,
                telefono,
                direccion,
                barrio,
                zona
            )

        elif opcion == "2":

            mostrar_solicitudes()

        elif opcion == "3":

            try:
                id_solicitud = int(input("ID de la solicitud: "))
                estado = input("Nuevo estado: ").lower()

                cambiar_estado(id_solicitud, estado)

            except ValueError:

                print("El ID debe ser un numero.")

        elif opcion == "0":

            break

        else:

            print("Opcion no valida.")

        pausar()
def menu_domiciliarios():

    while True:

        print("\n========== GESTION DE DOMICILIARIOS ==========")
        print("1. Registrar domiciliario")
        print("2. Buscar siguiente turno")
        print("3. Aceptar solicitud")
        print("4. Liberar domiciliario")
        print("5. Cambiar disponibilidad")
        print("0. Volver al menu principal")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            nombre = input("Nombre del domiciliario: ")
            telefono = input("Telefono: ")

            registrar_domiciliario(nombre, telefono)

        elif opcion == "2":

            persona = buscar_domiciliario()

            if persona:
                print("Siguiente turno:", persona["nombre"])

        elif opcion == "3":

            nombre = input("Nombre del domiciliario: ")
            ocupar_domiciliario(nombre)

        elif opcion == "4":

            nombre = input("Nombre del domiciliario: ")
            liberar_domiciliario(nombre)

        elif opcion == "5":

            nombre = input("Nombre del domiciliario: ")
            estado = input("Disponible (si/no): ").lower()

            if estado in ["si", "no"]:
                cambiar_disponibilidad(nombre, estado == "si")
            else:
                print("Respuesta no valida.")

        elif opcion == "0":

            break

        else:

            print("Opcion no valida.")

        pausar()
def menu_pagos():

    while True:

        print("\n========== GESTION DE PAGOS ==========")
        print("1. Registrar pago")
        print("2. Confirmar pago del negocio")
        print("3. Confirmar recepcion del domiciliario")
        print("4. Mostrar pagos")
        print("0. Volver al menu principal")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            try:
                id_solicitud = int(input("ID de solicitud: "))
                negocio = input("Nombre del negocio: ")
                domiciliario = input("Nombre del domiciliario: ")
                valor = float(input("Valor del pago: "))

                registrar_pago(
                    id_solicitud,
                    negocio,
                    domiciliario,
                    valor
                )

            except ValueError:

                print("El ID y el valor deben ser numericos.")

        elif opcion == "2":

            try:
                id_solicitud = int(input("ID de solicitud: "))
                confirmar_pago_negocio(id_solicitud)

            except ValueError:

                print("ID no valido.")

        elif opcion == "3":

            try:
                id_solicitud = int(input("ID de solicitud: "))
                confirmar_pago_domiciliario(id_solicitud)

            except ValueError:

                print("ID no valido.")

        elif opcion == "4":

            mostrar_pagos()

        elif opcion == "0":

            break

        else:

            print("Opcion no valida.")
        pausar()
def menu_calificaciones():

    while True:

        print("\n========== GESTION DE CALIFICACIONES ==========")
        print("1. Registrar calificacion")
        print("2. Mostrar calificaciones")
        print("3. Consultar promedio")
        print("0. Volver al menu principal")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            try:
                id_solicitud = int(input("ID de solicitud: "))
                calificador = input("Quien califica: ")
                calificado = input("A quien califica: ")
                tipo = input("Tipo (negocio/domiciliario): ").lower()
                puntuacion = int(input("Puntuacion (1 a 5): "))
                comentario = input("Comentario: ")

                registrar_calificacion(
                    id_solicitud,
                    calificador,
                    calificado,
                    tipo,
                    puntuacion,
                    comentario
                )

            except ValueError:

                print("ID y puntuacion deben ser numericos.")

        elif opcion == "2":

            mostrar_calificaciones()

        elif opcion == "3":

            nombre = input("Nombre del usuario: ")

            promedio = calcular_promedio(nombre)

            if promedio > 0:
                print(f"Promedio de {nombre}: {promedio}/5")

        elif opcion == "0":

            break

        else:

            print("Opcion no valida.")

        pausar()
def menu_principal():

    while True:

        print("\n========== MENU PRINCIPAL ==========")
        print("1. Gestion de usuarios")
        print("2. Gestion de solicitudes")
        print("3. Gestion de domiciliarios")
        print("4. Gestion de pagos")
        print("5. Gestion de calificaciones")
        print("0. Salir del sistema")

        opcion = input("\nSeleccione una opcion: ")

        if opcion == "1":

            menu_usuarios()

        elif opcion == "2":

            menu_solicitudes()

        elif opcion == "3":

            menu_domiciliarios()

        elif opcion == "4":

            menu_pagos()

        elif opcion == "5":

            menu_calificaciones()

        elif opcion == "0":

            print("\nCerrando Condrez Gallitos...")
            print("Gracias por utilizar nuestro sistema.")
            break

        else:

            print("Opcion no valida.")
def main():
    mostrar_encabezado()
    print("\nIniciando sistema")
    menu_principal()
if __name__ == "__main__":
    main()
