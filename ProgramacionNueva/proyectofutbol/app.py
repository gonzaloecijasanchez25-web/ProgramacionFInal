from equipos import generar_id, crear_equipo, listar_equipos, buscar_equipo_por_id, eliminar_equipo, actualizar
from jugadores import generar_id as generar_id_j, crear_jugador, listar_jugadores, buscar_jugador_por_id, eliminar_jugador, actualizar_jugador
from calendario import generar_id as generar_id_p, crear_partido, listar_partidos, buscar_partido_por_id, reprogramar_partido, eliminar_partido
from ranking import registrar_resultado, generar_clasificacion, estadisticas_equipo

lista_equipos = []
lista_jugadores = []
partidos = []
seguir = 0
mensaje = ""

def menu_equipos():
    seguir = 0
    while seguir == 0:
        print("-----MENU EQUIPOS-----")
        print("1. Añadir Equipos")
        print("2. Listar Equipos")
        print("3. Buscar por id")
        print("4. Actualizar datos")
        print("5. Eliminar equipo")
        print("6. Volver al menú principal")

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
                mensaje = eliminar_equipo(lista_equipos)
            case "6":
                print("Volviendo al menú principal")
                seguir += 1
            case _:
                mensaje = "Opcion invalida"
        print(mensaje)

def menu_jugadores():
    seguir = 0
    while seguir == 0:
        print("-----MENU JUGADORES-----")
        print("1. Añadir Jugadores")
        print("2. Listar Jugadores")
        print("3. Buscar por id")
        print("4. Actualizar datos")
        print("5. Eliminar jugador")
        print("6. Volver al menú principal")

        opcion = input("Introduzca la opcion que desees: ")
        match opcion:
            case "1":
                mensaje = crear_jugador(lista_jugadores, lista_equipos)
            case "2":
                mensaje = listar_jugadores(lista_jugadores, lista_equipos)
            case "3":
                mensaje = buscar_jugador_por_id(lista_jugadores, lista_equipos)
            case "4":
                mensaje = actualizar_jugador(lista_jugadores, lista_equipos)
            case "5":
                mensaje = eliminar_jugador(lista_jugadores)
            case "6":
                print("Volviendo al menú principal")
                seguir += 1
            case _:
                mensaje = "Opcion invalida"
        print(mensaje)

def menu_partidos():
    seguir = 0
    while seguir == 0:
        print("-----MENU PARTIDOS-----")
        print("1. Crear Partido")
        print("2. Listar Partidos")
        print("3. Buscar Partido por ID")
        print("4. Reprogramar Partido")
        print("5. Eliminar Partido")
        print("6. Volver al menú principal")

        opcion = input("Introduzca la opcion que desees: ")
        match opcion:
            case "1":
                mensaje = crear_partido(partidos, lista_equipos)
            case "2":
                mensaje = listar_partidos(partidos, lista_equipos)
            case "3":
                mensaje = buscar_partido_por_id(partidos, lista_equipos)
            case "4":
                mensaje = reprogramar_partido(partidos)
            case "5":
                mensaje = eliminar_partido(partidos)
            case "6":
                print("Volviendo al menú principal")
                seguir += 1
            case _:
                mensaje = "Opcion invalida"
        print(mensaje)

def menu_ranking():
    seguir = 0
    while seguir == 0:
        print("-----MENU RESULTADOS Y CLASIFICACION-----")
        print("1. Registrar Resultado")
        print("2. Ver Clasificacion")
        print("3. Ver Estadisticas por Equipo")
        print("4. Volver al menú principal")

        opcion = input("Introduzca la opcion que desees: ")
        match opcion:
            case "1":
                mensaje = registrar_resultado(partidos)
            case "2":
                mensaje = generar_clasificacion(partidos, lista_equipos)
            case "3":
                mensaje = estadisticas_equipo(partidos, lista_equipos)
            case "4":
                print("Volviendo al menú principal")
                seguir += 1
            case _:
                mensaje = "Opcion invalida"
        print(mensaje)

def menu_principal():
    seguir = 0
    while seguir == 0:
        print("-----MENU PRINCIPAL-----")
        print("1. Gestión de Equipos")
        print("2. Gestión de Jugadores")
        print("3. Calendario de Partidos")
        print("4. Resultados y Clasificación")
        print("5. Salir")

        opcion = input("Introduzca la opcion que desees: ")
        match opcion:
            case "1":
                menu_equipos()
            case "2":
                menu_jugadores()
            case "3":
                menu_partidos()
            case "4":
                menu_ranking()
            case "5":
                print("Saliendo del programa")
                seguir += 1
            case _:
                print("Opcion invalida")

menu_principal()
