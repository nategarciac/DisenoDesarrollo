
import json

# Estructura de datos en memoria
usuarios = []

# Función para guardar los datos en el archivo
def guardar_datos():
    with open("datos.txt", "w") as archivo:
        json.dump(usuarios, archivo)

# Función para cargar los datos desde el archivo
def cargar_datos():
    try:
        with open("datos.txt", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

# Función para cambiar el PIN del usuario
def cambiar_pin(usuario):
    nuevo_pin = input("Ingrese su nuevo PIN: ")
    usuario["pin"] = nuevo_pin
    print("PIN cambiado exitosamente.")

# Función para registrar un nuevo usuario con validaciones
def registrar_usuario():
    nombre = input("Ingrese su nombre de usuario: ")
    
    # Validar si el nombre de usuario ya existe
    while any(usuario["nombre"].lower() == nombre.lower() for usuario in usuarios):
        print("Ya existe un usuario con ese nombre. Intente nuevamente.")
        nombre = input("Ingrese su nombre de usuario: ")
    
    correo = input("Ingrese su correo electrónico: ")
    
    # Validar si el correo electrónico ya está registrado
    while any(usuario["correo"].lower() == correo.lower() for usuario in usuarios):
        print("Ya existe un usuario con ese correo electrónico. Intente nuevamente.")
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
    if pin_ingresado == usuario["pin"]:
        return True
    else:
        print("PIN incorrecto. Intente nuevamente.")
        return False

# Función para registrar una nueva habitación
def registrar_habitacion(casa):
    nombre_habitacion = input("Ingrese el nombre de la habitación: ")
    cerradura_abierta = input("La cerradura está abierta? (Sí/No): ").lower() == "si"
    
    if nombre_habitacion not in [h["nombre"] for h in casa["habitaciones"]]:
        casa["habitaciones"].append({"nombre": nombre_habitacion, "dispositivos": [], "cerradura_abierta": cerradura_abierta})
        print(f"Habitación '{nombre_habitacion}' registrada.")
    else:
        print("Ya existe una habitación con ese nombre.")

# Función para registrar un nuevo dispositivo
def registrar_dispositivo(habitacion):
    nombre_dispositivo = input("Ingrese el nombre del dispositivo: ")
    estado_inicial = input("Ingrese el estado inicial (encendido/apagado): ")
    dispositivo = {"nombre": nombre_dispositivo, "estado": estado_inicial, "programaciones": []}
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

        if not usuarios:
            opcion = input("Seleccione 'N' para un nuevo usuario o 'S' para volver: ")
            if opcion.lower() == "n":
                registrar_usuario()
        else:
            opcion = input("Seleccione el número de usuario o 'S' para volver: ")
            if opcion.lower() == "s":
                break
            try:
                usuario_seleccionado = usuarios[int(opcion) - 1]
                if validar_pin(usuario_seleccionado):
                    menu_opciones_usuario(usuario_seleccionado)
            except (ValueError, IndexError):
                print("Opción no válida. Intente nuevamente.")

# Menú de opciones para un usuario seleccionado
def menu_opciones_usuario(usuario):
    while True:
        print(f"\nBienvenido, {usuario['nombre']}!")
        print("Opciones:")
        print("1. Mostrar casas")
        print("2. Cambiar PIN")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_casas(usuario)
        elif opcion == "2":
            cambiar_pin(usuario)
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Menú para operaciones con las casas de un usuario
def menu_casas(usuario):
    while True:
        print(f"\nBienvenido, {usuario['nombre']}!")
        print("Casas registradas:")
        for i, casa in enumerate(usuario["casas"], 1):
            print(f"{i}. Casa {i}")
        
        print("N. Nueva casa")
        print("S. Volver a las opciones de usuario")
        
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

# Función para programar encendido y apagado de un dispositivo
def programar_dispositivo(dispositivo):
    hora_encendido = input("Ingrese la hora de encendido (formato HH:MM): ")
    hora_apagado = input("Ingrese la hora de apagado (formato HH:MM): ")

    programacion = {"hora_encendido": hora_encendido, "hora_apagado": hora_apagado}
    dispositivo["programaciones"].append(programacion)
    print("Programación registrada con éxito.")

# Función para mostrar las programaciones de un dispositivo
def mostrar_programaciones(dispositivo):
    if dispositivo["programaciones"]:
        print("Programaciones del dispositivo:")
        for i, programacion in enumerate(dispositivo["programaciones"], 1):
            print(f"{i}. Encendido a las {programacion['hora_encendido']}, Apagado a las {programacion['hora_apagado']}")
    else:
        print("No hay programaciones registradas para este dispositivo.")

# Función para eliminar una programación de un dispositivo
def eliminar_programacion(dispositivo):
    mostrar_programaciones(dispositivo)
    if dispositivo["programaciones"]:
        opcion_programacion = input("Seleccione el número de la programación a eliminar: ")
        try:
            indice_programacion = int(opcion_programacion) - 1
            if 0 <= indice_programacion < len(dispositivo["programaciones"]):
                del dispositivo["programaciones"][indice_programacion]
                print("Programación eliminada con éxito.")
            else:
                print("Número de programación no válido.")
        except ValueError:
            print("Ingrese un número válido.")
    else:
        print("No hay programaciones registradas para este dispositivo.")

# Menú para operaciones con las habitaciones y dispositivos de una casa
def menu_operaciones_casa(casa):
    while True:
        print("\nOperaciones en la casa:")
        print("1. Registrar nueva habitación")
        print("2. Mostrar habitaciones")
        print("3. Cambiar estado de la cerradura de una habitación")
        print("4. Registrar nuevo dispositivo")
        print("5. Mostrar dispositivos en una habitación")
        print("6. Programar dispositivo")
        print("7. Mostrar programaciones de un dispositivo")
        print("8. Eliminar programación de un dispositivo")
        print("9. Volver a la selección de casas")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_habitacion(casa)
        elif opcion == "2":
            mostrar_habitaciones(casa)
        elif opcion == "3":
            menu_cambiar_estado_cerradura(casa)
        elif opcion == "4":
            menu_registrar_dispositivo(casa)
        elif opcion == "5":
            menu_mostrar_dispositivos_en_habitacion(casa)
        elif opcion == "6":
            menu_programar_dispositivo(casa)
        elif opcion == "7":
            menu_mostrar_programaciones(casa)
        elif opcion == "8":
            menu_eliminar_programacion(casa)
        elif opcion == "9":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Funciones adicionales para la gestión de programaciones
def menu_programar_dispositivo(casa):
    dispositivo = seleccionar_dispositivo(casa)
    if dispositivo:
        programar_dispositivo(dispositivo)

def menu_mostrar_programaciones(casa):
    dispositivo = seleccionar_dispositivo(casa)
    if dispositivo:
        mostrar_programaciones(dispositivo)

def menu_eliminar_programacion(casa):
    dispositivo = seleccionar_dispositivo(casa)
    if dispositivo:
        eliminar_programacion(dispositivo)

def seleccionar_dispositivo(casa):
    if casa["habitaciones"]:
        print("Habitaciones disponibles:")
        for i, habitacion in enumerate(casa["habitaciones"], 1):
            print(f"{i}. {habitacion['nombre']}")
        
        opcion_habitacion = input("Seleccione el número de habitación: ")
        
        try:
            habitacion_seleccionada = casa["habitaciones"][int(opcion_habitacion) - 1]
            return seleccionar_dispositivo_en_habitacion(habitacion_seleccionada)
        except (ValueError, IndexError):
            print("Opción no válida. Intente nuevamente.")
    else:
        print("No hay habitaciones registradas en esta casa. Registre una habitación primero.")

def seleccionar_dispositivo_en_habitacion(habitacion):
    if habitacion["dispositivos"]:
        print("Dispositivos en la habitación:")
        for i, dispositivo in enumerate(habitacion["dispositivos"], 1):
            print(f"{i}. {dispositivo['nombre']}")
        
        opcion_dispositivo = input("Seleccione el número de dispositivo: ")
        
        try:
            dispositivo_seleccionado = habitacion["dispositivos"][int(opcion_dispositivo) - 1]
            return dispositivo_seleccionado
        except (ValueError, IndexError):
            print("Opción no válida. Intente nuevamente.")
    else:
        print("No hay dispositivos registrados en esta habitación. Registre un dispositivo primero.")

# Función para mostrar las habitaciones y sus estados de cerradura
def mostrar_habitaciones(casa):
    if casa["habitaciones"]:
        print("Habitaciones registradas:")
        for habitacion in casa["habitaciones"]:
            estado_cerradura = "abierta" if habitacion["cerradura_abierta"] else "cerrada"
            print(f"- {habitacion['nombre']}, Estado de la cerradura: {estado_cerradura}")
    else:
        print("No hay habitaciones registradas en esta casa.")

# Menú para cambiar el estado de la cerradura de una habitación
def menu_cambiar_estado_cerradura(casa):
    if casa["habitaciones"]:
        print("Habitaciones disponibles:")
        for i, habitacion in enumerate(casa["habitaciones"], 1):
            print(f"{i}. {habitacion['nombre']}")
        
        opcion_habitacion = input("Seleccione el número de habitación: ")
        
        try:
            habitacion_seleccionada = casa["habitaciones"][int(opcion_habitacion) - 1]
            cambiar_estado_cerradura(habitacion_seleccionada)
        except (ValueError, IndexError):
            print("Opción no válida. Intente nuevamente.")
    else:
        print("No hay habitaciones registradas en esta casa. Registre una habitación primero.")

# Función para cambiar el estado de la cerradura de una habitación
def cambiar_estado_cerradura(habitacion):
    habitacion["cerradura_abierta"] = not habitacion["cerradura_abierta"]
    estado = "abierta" if habitacion["cerradura_abierta"] else "cerrada"
    print(f"Cerradura de la habitación '{habitacion['nombre']}' cambiada a {estado}.")

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
    global usuarios
    usuarios = cargar_datos()
    menu_principal()
    guardar_datos()

if __name__ == "__main__":
    main()
