# Estructura de datos en memoria
usuarios = []

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre = input("Ingrese su nombre de usuario: ")
    correo = input("Ingrese su correo electrónico: ")
    pin = input("Ingrese su PIN: ")
    usuario = {"nombre": nombre, "correo": correo, "pin": pin, "casas": []}
    usuarios.append(usuario)
    print("Usuario registrado exitosamente.")

# Función para mostrar la lista de usuarios con nombre y correo
def mostrar_usuarios():
    if usuarios:
        print("Usuarios registrados:")
        for i, usuario in enumerate(usuarios, 1):
            print(f"{i}. Nombre: {usuario['nombre']}, Correo: {usuario['correo']}")
    else:
        print("No hay usuarios registrados.")

# Función para validar el PIN del usuario
def validar_pin(usuario):
    pin_ingresado = input("Ingrese su PIN: ")
    return pin_ingresado == usuario["pin"]

# Función para registrar una nueva habitación
def registrar_habitacion(casa):
    nombre_habitacion = input("Ingrese el nombre de la habitación: ")
    if nombre_habitacion not in [h["nombre"] for h in casa["habitaciones"]]:
        casa["habitaciones"].append({"nombre": nombre_habitacion, "dispositivos": []})
        print(f"Habitación '{nombre_habitacion}' registrada.")
    else:
        print("Ya existe una habitación con ese nombre.")

# Función para registrar un nuevo dispositivo
def registrar_dispositivo(habitacion):
    nombre_dispositivo = input("Ingrese el nombre del dispositivo: ")
    estado_inicial = input("Ingrese el estado inicial (encendido/apagado): ")
    dispositivo = {"nombre": nombre_dispositivo, "estado": estado_inicial, "programacion": None}
    habitacion["dispositivos"].append(dispositivo)
    print(f"Dispositivo '{nombre_dispositivo}' registrado en la habitación.")

# Método para mostrar la lista de dispositivos en una habitación
def mostrar_dispositivos_en_habitacion(habitacion):
    if habitacion["dispositivos"]:
        print("Dispositivos en la habitación:")
        for dispositivo in habitacion["dispositivos"]:
            print(f"- {dispositivo['nombre']}, Estado: {dispositivo['estado']}")
    else:
        print("No hay dispositivos registrados en esta habitación.")

# Menú principal
def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Mostrar usuarios")
        print("2. Registrar nuevo usuario")
        print("3. Seleccionar usuario")
        print("4. Salir")
        
        opcion = input("Seleccione una opción:")
        
        if opcion == "1":
            mostrar_usuarios()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            menu_seleccionar_usuario()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Menú para seleccionar un usuario existente
def menu_seleccionar_usuario():
    while True:
        print("\nSeleccione un usuario:")
        mostrar_usuarios()
        print("N. Nuevo usuario")
        print("S. Volver al menú principal")
        
        opcion = input("Seleccione el número de usuario o 'N' para uno nuevo, 'S' para volver: ")
        
        if opcion.lower() == "n":
            registrar_usuario()
        elif opcion.lower() == "s":
            break
        else:
            try:
                usuario_seleccionado = usuarios[int(opcion) - 1]
                if validar_pin(usuario_seleccionado):
                    menu_casas(usuario_seleccionado)
            except (ValueError, IndexError):
                print("Opción no válida. Intente nuevamente.")

# Menú para operaciones con las casas de un usuario
def menu_casas(usuario):
    while True:
        print(f"\nBienvenido, {usuario['nombre']}!")
        print("Casas registradas:")
        for i, casa in enumerate(usuario["casas"], 1):
            print(f"{i}. Casa {i}")
        
        print("N. Nueva casa")
        print("S. Volver al menú principal")
        
        opcion = input("Seleccione el número de casa o 'N' para una nueva, 'S' para volver: ")
        
        if opcion.lower() == "n":
            usuario["casas"].append({"nombre": f"Casa {len(usuario['casas']) + 1}", "habitaciones": []})
            print("Nueva casa registrada.")
        elif opcion.lower() == "s":
            break
        else:
            try:
                casa_seleccionada = usuario["casas"][int(opcion) - 1]
                menu_operaciones_casa(casa_seleccionada)
            except (ValueError, IndexError):
                print("Opción no válida. Intente nuevamente.")

# Menú para operaciones con las habitaciones y dispositivos de una casa
def menu_operaciones_casa(casa):
    while True:
        print("\nOperaciones en la casa:")
        print("1. Registrar nueva habitación")
        print("2. Mostrar habitaciones")
        print("3. Registrar nuevo dispositivo")
        print("4. Mostrar dispositivos en una habitación")
        print("5. Volver a la selección de casas")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_habitacion(casa)
        elif opcion == "2":
            if casa["habitaciones"]:
                print("Habitaciones registradas:")
                for habitacion in casa["habitaciones"]:
                    print(f"- {habitacion['nombre']}")
            else:
                print("No hay habitaciones registradas en esta casa.")
        elif opcion == "3":
            menu_registrar_dispositivo(casa)
        elif opcion == "4":
            menu_mostrar_dispositivos_en_habitacion(casa)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Menú para registrar un nuevo dispositivo en una habitación
def menu_registrar_dispositivo(casa):
    if casa["habitaciones"]:
        print("Habitaciones disponibles:")
        for i, habitacion in enumerate(casa["habitaciones"], 1):
            print(f"{i}. {habitacion['nombre']}")
        
        opcion_habitacion = input("Seleccione el número de habitación: ")
        
        try:
            habitacion_seleccionada = casa["habitaciones"][int(opcion_habitacion) - 1]
            registrar_dispositivo(habitacion_seleccionada)
        except (ValueError, IndexError):
            print("Opción no válida. Intente nuevamente.")
    else:
        print("No hay habitaciones registradas en esta casa. Registre una habitación primero.")

# Menú para mostrar dispositivos en una habitación
def menu_mostrar_dispositivos_en_habitacion(casa):
    if casa["habitaciones"]:
        print("Habitaciones disponibles:")
        for i, habitacion in enumerate(casa["habitaciones"], 1):
            print(f"{i}. {habitacion['nombre']}")
        
        opcion_habitacion = input("Seleccione el número de habitación: ")
        
        try:
            habitacion_seleccionada = casa["habitaciones"][int(opcion_habitacion) - 1]
            mostrar_dispositivos_en_habitacion(habitacion_seleccionada)
        except (ValueError, IndexError):
            print("Opción no válida. Intente nuevamente.")
    else:
        print("No hay habitaciones registradas en esta casa. Registre una habitación primero.")

# Función principal
def main():
    menu_principal()

if __name__ == "__main__":
    main()
