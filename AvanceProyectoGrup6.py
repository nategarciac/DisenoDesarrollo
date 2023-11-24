#variables
userSelected=0
authorized=False

#lista usuarios, user default=user1
usuarios=["user1"]
#ordenar lista de usuarios
usuarios.sort()
#imprimir bienvenidad y la lista de usuarios en pantalla
print("\nBienvenidos a --SMART--HOME--\n")
print("--Usuarios Existentes--\n",usuarios[:50],"\n")

#usuario Default, pin  default =12345
user1=dict(pin="12345",casa={})

#solo PIN del usuario default
user1Pin=user1.get("pin")
#solo nombre de la casa del usuario default
user1Casa=user1.get("casa")


#correr mientras no se haya autorizado con un pin valido.
while authorized==False:

    
    user_id= input("Seleccione un nombre de Usuario:\n")

    for x in usuarios:
        if x ==(user_id):
            print("Bievenido:",user_id)
            userSelected=user_id
            
            pin=input("\nIngrese su PIN:\n")
            if pin==user1Pin:
                print("\nAuthorized!\n")
                authorized=True
            if authorized==True:
                options=int(input("\n--OPTIONS--:\nAgregar casa=1.\nSalir=2.\n"))
                if options==1:
                    houseName=input("Nombre de la casa:?\n")
                    user1.update({"casa": houseName})
                    print(userSelected,user1)
                    print("Casa Agregada a:",userSelected,"Nombre de casa:",houseName)



            elif pin!=user1Pin:
                print("PIN incorrecto!!!")
                authorized=False    





            
        if userSelected==0 and authorized==False:
            print("Usuario:'",user_id,"'NO existe! Favor Registrase.\n")
            nombre=input("Ingrese su nombre:")
            email=input("Ingrese su correo Electronico:")
            userSelected=input("Ingrese un UserId:")
            pin=input("Ingrese un PIN:")
            usuarios.append(user_id)
            user_id={"name":nombre,
                        "email":email,
                        "PIN":pin}
            
            
            
            print("TU PIN es:",user_id.get("PIN"))
            print("Authorized!\nUSUARIO AGREGADO!\n")
            print(userSelected,user_id)
            print("Usuarios existentes Actualizados:\n",usuarios[:50])
            authorized=True
            if userSelected!=user1:
                options=int(input("\n--OPTIONS--:\nAgregarcasa=1.\nSalir=2.\n"))
                if options==1:
                    houseName=input("Nombre de la casa:?\n")
                    user_id.update({"casa": houseName})
                    
                    print("Casa Agregada a:",userSelected,"Nombre de casa:",houseName)
                    print(userSelected,user_id)






