ROLES_PERMITIDOS = [
    "administrador",
    "negocio",
    "domiciliario"
]
usuarios = []
def registrar_usuario(nombre, usuario, contrasena, rol):
    if rol not in ROLES_PERMITIDOS:
        print("Error: el rol ingresado no es valido.")
        return False
    if not nombre or not usuario or not contrasena:
        print("Error: todos los campos son obligatorios.")
        return False
    for persona in usuarios:
        if persona["usuario"] == usuario:
            print("Error: este nombre de usuario ya existe.")
            return False
    nuevo_usuario = {
        "nombre": nombre,
        "usuario": usuario,
        "contrasena": contrasena,
        "rol": rol,
        "activo": True
    }
    usuarios.append(nuevo_usuario)
    print("Usuario registrado correctamente.")
    return True
def mostrar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for persona in usuarios:
        print(f"Nombre: {persona['nombre']}")
        print(f"Usuario: {persona['usuario']}")
        print(f"Rol: {persona['rol']}")
        print(f"Activo: {persona['activo']}")
