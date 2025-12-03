#Hacemos los arrays
nombre = []
apellidos = []
telefono = []
dni = []

#Funcion dar de alta al cliente
def cliente_alta ():
    pedir_dni = input("Introduzca el DNI:")
    if pedir_dni in dni:
        print ("El cliente existe")
    else:
        pedir_nombre = input("Introduce el nombre: ")
        pedir_apellidos = input("Introduce el apellido: ")
        pedir_telefono = input("Introduce el telefono: ")
        dni.append(pedir_dni)
        nombre.append(pedir_nombre)
        apellidos.append(pedir_apellidos)
        telefono.append(pedir_telefono)
        print("Ya se ha añadido el cliente")
#Funcion lista de clientes
def listar_clientes():
    if not dni:
        print("No hay clientes")
    else:
        for i in range(len(dni)):
            print(dni[i], "/", nombre[i], "/", apellidos[i], "/", telefono[i])
            encontrado = True
    if not encontrado:
        print ("El cliente no ha sido encontrado")
#Funcion buscar cliente
def buscar_cliente_por_dni ():
    pedir_dni = input ("Introduce el DNI que quieres buscar: ")
    encontrado = False
    for i in range (len(dni)):
        if dni [i] == pedir_dni:
            print(f"{dni[i]} / {nombre[i]} / {apellidos[i]} / {telefono [i]}")
            encontrado = True
    if not encontrado:
        print ("Cliente no encontrado.")
#Funcion cambiar el telefono por cliente
def modificar_telefono():
    dni1 = input("Introduce el DNI que quieres buscar: ")
    encontrado = False
    for i in range (len(dni)):
        if dni [i] == dni1:
            nuevo = input("Introduce el nuevo telefono: ")
            telefono[i] = nuevo
            print("Teléfono actualizado.")
            encontrado = True
    if not encontrado:
        print("Cliente no encontrado.")
#Funcion eliminar cliente
def eliminar_cliente():
    perdir_dni = input("Introduce el DNI que quieres eliminar: ")
    for i in range(len(dni)):
        if dni[i] == perdir_dni:
            dni.pop(i)
            nombre.pop(i)
            apellidos.pop(i)
            telefono.pop(i)
            print("Cliente eliminado.")
            return  
    print("Cliente no encontrado.")
#Funcion guardar clientes en fichero
def guardar_fichero():
    with open("clientes.txt", "w") as f:
        for i in range(len(dni)):
            f.write(f"{dni[i]}/{nombre[i]};{apellidos[i]}/{telefono[i]}")
    print("Clientes guardados en fichero.")
#Hacemos el menu
opcion = 0
while opcion != 7:
    print("1. Dar alta cliente")
    print("2. Lista de los clientes")
    print("3. Buscar cliente")
    print("4. Cambiar telefono de cliente")
    print("5. Eliminar cliente")
    print("6. Guardar clientes en el fichero")
    print("7. Salir")
    
    opcion = int(input("Elige una opcion: "))

    if opcion == 1: cliente_alta()
    elif opcion == 2: listar_clientes()
    elif opcion == 3: buscar_cliente_por_dni()
    elif opcion == 4: (modificar_telefono)
    elif opcion == 5: eliminar_cliente()
    elif opcion == 6: guardar_fichero()
    elif opcion == 7: cliente_alta()
    else:
        print("Esa opcion no es valida")
