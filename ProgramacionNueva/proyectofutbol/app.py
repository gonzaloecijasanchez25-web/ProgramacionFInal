lista_equipos = []
equipo = {}
nombre = 0
ciudad = 0
estado = 0
seguir = 0
mensaje = ""
id_busqueda = 0

from equipos import generar_id, crear_equipo, listar_equipos, buscar_equipo_por_id, eliminar_equipo, actualizar


def menu_equipo():
    seguir = 0
    while seguir == 0:
        print("-----MENU EQUIPOS-----")
        print("1. Añadir Equipos")
        print("2. Listar Equipos")
        print("3. Buscar por id")
        print("4. Actualizar datos")
        print("5. Eliminar equipo")

        opcion = input("Introduzca la opcion que desees: ")
        match opcion:
            case "1":
                mensaje = crear_equipo(lista_equipos)
            case "2":
                mensaje = listar_equipos(lista_equipos)
            case "3":
                mensaje = buscar_equipo_por_id(lista_equipos)
            case "4":
                mensaje = actualizar(lista_equipos)
            case "5":
                mensaje =eliminar_equipo(lista_equipos)
            case "6":
                print("Yendo a menu general")
                seguir += 1
            case _:
                mensaje ="Opcion invalida"
        
        print(mensaje)



menu_equipo()