#Todas las estructuras de las clases a utilizar
class User:
    def __init__(self,Nombre,Correo,Numeropin):
        self.Nombre=Nombre
        self.Correo=Correo
        self.Numeropin=Numeropin

class Casas:
    def __init__(self,Nombreusuario,Numeropin,Nombrecasa):
        self.Nombreusuario=Nombreusuario
        self.Numeropin=Numeropin
        self.Nombrecasa=Nombrecasa

class Habitaciones:
    def __init__(self,Nombrecasa,Nombrehabitacion):
        self.Nombrecasa=Nombrecasa
        self.Nombrehabitacion=Nombrehabitacion

#creando valores por default    
u1 = User("user1","rdarcia@aya.go.cr","12345")
casa1 = Casas ("user1","12345","Casa1")
habitacion1 = Habitaciones("Casa1","Cocina")
habitacion2 = Habitaciones("Casa1","Cuarto Principal")
habitacion3 = Habitaciones("Casa1","Sala")

# agregando valores a las Listas
usuarios = [u1]
casas = [casa1]
habitaciones = [habitacion1,habitacion2,habitacion3]

#variables de uso Global
estadoSesion=False
nombreUsuario=""
pindeusuario=""
nombreCasa=""

# Función que muestra la lista de usarios existentes.
def listadeusuarios():
    print ("Lista de usuarios")
    for x in range(len (usuarios)):
     print ("   " +usuarios[x].Nombre," ",usuarios[x].Correo)

# Función para agregar nuevos usuarios.
def Agregarusuario():
    nuevousuario = input ("¿Esta seguro de agregar un nuevo usuario? S/N\n")

    if nuevousuario == "S":
        nombrenuevo = input ( " Digite su nombre:")
        correoelectronico = input ( " Digite su correo:" )
        pin = input ( " Digite su pin " )

        if nombrenuevo!="" and pin!="":

            # Revisamos si el usuario existe para no ingresar el mismo usuario.
            if Buscarusuarioexistente(nombrenuevo, pin, "comprobar")== False:
                usuarionuevo = User(nombrenuevo,correoelectronico,pin)
                
                #uso de variable declaradas Globales
                global usuarios
                #agregando el nuevo usuario a la lista de usuarios
                usuarios.append(usuarionuevo)
                
                global nombreUsuario
                nombreUsuario=nombrenuevo
                global pindeusuario
                pindeusuario=pin
                return True
            else:
                return False
        else:
            print("No ingrese valores vacios")
            return False

    else:
        return False
        

# Buscar usuario
def Buscarusuarioexistente(nombre, numeropin, estado):
    if nombre != "" and numeropin != "":
        for x in range(len(usuarios)):
            if estado=="logeo":
                if usuarios[x].Nombre==nombre and usuarios[x].Numeropin==numeropin:

                    #uso de variable Global
                    global nombreUsuario
                    nombreUsuario=usuarios[x].Nombre
                    global pindeusuario
                    pindeusuario=usuarios[x].Numeropin
                    
                    return True
                else:
                    return False
            elif estado=="comprobar":
                if usuarios[x].Nombre==nombre:
                    return True
                else:
                    return False
    
    return False

# Funciones de las casas.
# Lista de todas las casas.
def Listausuarioscasas():
    print ("Lista de casas del usuario ",nombreUsuario)
    for i in range (len(casas)):
        if casas[i].Nombreusuario==nombreUsuario and casas[i].Numeropin==pindeusuario:
            print ("   ",casas[i].Nombrecasa)

# Agregar casa Nueva.
def Agregarcasanueva():
    nuevaCasa = input ("¿Esta seguro de agregar una nueva casa? S/N\n")
# Si el usuario solo da enter regresa a falso ya que no agrego casa.
    if nuevaCasa=="S":
        nombrenuevacasa= input ("Digite el nombre de la nueva casa: \n")
        if Buscarcasaexistente(nombrenuevacasa,"Ingresar")==False and nombrenuevacasa!= "":
            global casas
            registroNuevaCasa=  Casas (nombreUsuario,pindeusuario,nombrenuevacasa)
            casas.append(registroNuevaCasa)
            global nombreCasa
            nombreCasa=nombrenuevacasa
            return True
    return False

# Buscar casa existente.
def Buscarcasaexistente(casa,estado):
    if casa!="":
        for (i)in range (len(casas)):
            # Revisar: Para agregarle valor a las variables globales.
            if estado=="Revisar":
                if casas[i].Nombreusuario==nombreUsuario and casas[i].Numeropin==pindeusuario and casas[i].Nombrecasa==casa:
                    global nombreCasa
                    nombreCasa=casas[i].Nombrecasa
                    return True
                # Ingresar: Es para evitar el ingreso de datos duplicados que ya existen
            elif estado=="Ingresar":
                if casas[i].Nombreusuario==nombreUsuario and casas[i].Numeropin==pindeusuario and casas[i].Nombrecasa==casa:
                    print("La casa que intenta ingresar ya existe\n")
                    return True
    
    return False

# Funciones de las habitaciones.
# Lista de todas las habitaciones de una casa.
def Listadehabitacionescasa():
    print(" Lista de habitaciones ",nombreCasa)
    for (i)in range (len(habitaciones)):
        if habitaciones[i].Nombrecasa==nombreCasa:
            print ("   ",habitaciones[i].Nombrehabitacion)

def Buscarhabitacionesexistentes(habitacion, estado):
    if habitacion!="":
        for (i) in range (len(habitaciones)):
            if estado=="Revisar":
                if habitaciones[i].Nombrehabitacion==habitacion and habitaciones[i].Nombrecasa==nombreCasa:
                    
                    return True
            elif estado=="Ingresar":
                if habitaciones[i].Nombrehabitacion==habitacion and habitaciones[i].Nombrecasa==nombreCasa:
                    print("La habitacion que intenta ingresar ya existe\n")
                    
    return False

def Agregarnuevahabitacion():
    habitacionnueva = input ("¿Esta seguro de agregar una nueva habitación? S/N\n")
    if habitacionnueva=="S":

        nombrehabitacionnueva= input ("Digite el nombre de la nueva habitación: \n")

        if Buscarhabitacionesexistentes(nombrehabitacionnueva, "Ingresar")==False and nombrehabitacionnueva!= "":
            global habitaciones
            registronuevaHabitacion = Habitaciones(nombreCasa,nombrehabitacionnueva)
            habitaciones.append(registronuevaHabitacion)

            return True
    return False
    
#funcion Inicio de sesión es tipo bool.
def Iniciodesecion():
    print ( " Bienvenido a la aplicación SMART HOME:\n")
    listadeusuarios()
    Valordeinicio = input (" Digite su usuario o Ingrese nuevo usuario con (N):\n")
    if Valordeinicio == "N":
        estadoRegistroNuevo=Agregarusuario()
        if estadoRegistroNuevo==True:
            listadeusuarios()
        return estadoRegistroNuevo
    
    pinabuscar = input ( " Digite el numero de pin :")
    return Buscarusuarioexistente(Valordeinicio,pinabuscar,"logeo")
    
def InicioRegistroCasa():
    
    Listausuarioscasas()

    siquiereagregarcasa = input (" Digite el nombre de la casa o (N) para nueva casa:\n")

    if siquiereagregarcasa == "N":
        estadoRegistroNuevo=Agregarcasanueva()
        if estadoRegistroNuevo==True:
            Listausuarioscasas()
        return estadoRegistroNuevo
# Se agrega estado de busquedad si es dato que existe va a revisar. 
    return Buscarcasaexistente(siquiereagregarcasa, "Revisar")

def InicioRegistroHabitacion():
    Listadehabitacionescasa()

    siquiereagregarhabitacion = input (" Digite el nombre de la habitacion o (N) para nueva habitacion:\n")

    if siquiereagregarhabitacion == "N":
        estadoRegistroNuevo=Agregarnuevahabitacion()
        if estadoRegistroNuevo==True:
            Listadehabitacionescasa()
        return estadoRegistroNuevo
        

    return Buscarhabitacionesexistentes(siquiereagregarhabitacion, "Revisar")
      
#inicio programa        
estadoSesion=Iniciodesecion()

while estadoSesion ==False:
    estadoSesion=Iniciodesecion()

#si ingreso bien, entonces entra a las casas    
if estadoSesion:
    print ( "Inicio de Sesion correcto ",nombreUsuario)

    estadoRegistroCasa=InicioRegistroCasa()
    
    while estadoRegistroCasa==False:
        estadoRegistroCasa=InicioRegistroCasa()

    if estadoRegistroCasa:
        estadoRegistroHabitacion=InicioRegistroHabitacion()

        while estadoRegistroHabitacion==False:
            estadoRegistroHabitacion=InicioRegistroHabitacion()

