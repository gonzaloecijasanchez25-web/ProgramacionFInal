lista_jugadores = []
jugador = {}
nombre = 0
posicion = 0
equipo_id = 0
id_busqueda = 0
nuevo_jugador = 0
nueva_posicion = 0
nuevo_equipo = 0

def generar_id(lista_jugadores):
    return len(lista_jugadores) + 1

def crear_jugador(lista_jugadores, lista_equipos):
    nombre = input("Introduce el nombre del jugador: ")
    posicion = input(f"Introduce la posicion de {nombre}: ")
    equipo_id = int(input("Introduce el id del equipo al que pertenece: "))

    if nombre == "" or posicion == "":
        print("Nombre y posicion no pueden estar vacíos")
        return

    equipo_valido = False
    for equipo in lista_equipos:
        if equipo["id"] == equipo_id and equipo.get("estado", "Inactivo") == "Activo":
            equipo_valido = True

    if not equipo_valido:
        print("No existe un equipo activo con ese ID")
        return

    jugador = {
        "id": generar_id(lista_jugadores),
        "nombre": nombre,
        "posicion": posicion,
        "equipo_id": equipo_id,
        "activo": True
    }
    lista_jugadores.append(jugador)
    return f"{jugador} creado correctamente"

def listar_jugadores(lista_jugadores, lista_equipos):
    if len(lista_jugadores) == 0:
        print("No hay jugadores, vuelva a la primera opcion para añadir")
        return
    else:
        texto = ""
        for j in lista_jugadores:
            equipo_nombre = ""
            for e in lista_equipos:
                if e["id"] == j["equipo_id"]:
                    equipo_nombre = e["nombre"]
            estado = "Activo" if j["activo"] == True else "Inactivo"
            texto += f'ID:{j["id"]} | Jugador:{j["nombre"]} | Posicion:{j["posicion"]} | Equipo:{equipo_nombre} | Estado:{estado}\n'
        return texto

def buscar_jugador_por_id(lista_jugadores, lista_equipos):
    id_busqueda = int(input("Introduce el id del jugador que quieras buscar: "))
    for j in lista_jugadores:
        if j["id"] == id_busqueda:
            equipo_nombre = ""
            for e in lista_equipos:
                if e["id"] == j["equipo_id"]:
                    equipo_nombre = e["nombre"]
            return f"Jugador encontrado: {j} | Equipo: {equipo_nombre}"
    return "No se encontro un jugador por ese id"

def eliminar_jugador(lista_jugadores):
    id_busqueda = int(input("Introduce el id del jugador que quieras eliminar: "))
    for i in range(len(lista_jugadores)):
        if lista_jugadores[i]["id"] == id_busqueda:
            nombre = lista_jugadores[i]["nombre"]
            lista_jugadores[i]["activo"] = False
            return f"Jugador {nombre} desactivado correctamente"
    return "No se encontro jugador por ese ID"

def actualizar_jugador(lista_jugadores, lista_equipos):
    id_busqueda = int(input("Introduce el id del jugador que quieras actualizar: "))
    for j in lista_jugadores:
        if j["id"] == id_busqueda:
            nuevo_nombre = input("Introduce el nuevo nombre: ")
            nueva_posicion = input("Introduce la nueva posicion: ")
            nuevo_equipo = int(input("Introduce el nuevo id de equipo: "))

            equipo_valido = False
            for e in lista_equipos:
                if e["id"] == nuevo_equipo and e.get("estado", "Inactivo") == "Activo":
                    equipo_valido = True

            if not equipo_valido:
                return "No existe un equipo activo con ese ID"

            j["nombre"] = nuevo_nombre
            j["posicion"] = nueva_posicion
            j["equipo_id"] = nuevo_equipo
            return f"Jugador con ID: {id_busqueda} actualizado"
    return "No se encontro jugador con ese ID"