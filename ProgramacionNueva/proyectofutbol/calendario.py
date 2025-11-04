partidos = []
partido = {}
jornada = 0
local_id = 0
visitante_id = 0
fecha = 0
hora = 0
jugado = False
resultado = ()
id_busqueda = 0
nuevo_partido = 0

def generar_id(partidos):
    return len(partidos) + 1

def crear_partido(partidos, lista_equipos):
    jornada = int(input("Introduce el número de jornada: "))
    local_id = int(input("Introduce el id del equipo local: "))
    visitante_id = int(input("Introduce el id del equipo visitante: "))
    fecha = input("Introduce la fecha del partido (YYYY-MM-DD): ")
    hora = input("Introduce la hora del partido (HH:MM): ")

    if local_id == visitante_id:
        print("Los equipos no pueden ser iguales")
        return

    local_valido = False
    visitante_valido = False

    for e in lista_equipos:
        if e["id"] == local_id and e.get("estado", "Inactivo") == "Activo":
            local_valido = True
        if e["id"] == visitante_id and e.get("estado", "Inactivo") == "Activo":
            visitante_valido = True

    if not local_valido or not visitante_valido:
        print("Uno o ambos equipos no existen o no están activos")
        return

    partido = {
        "id": generar_id(partidos),
        "jornada": jornada,
        "local_id": local_id,
        "visitante_id": visitante_id,
        "fecha": fecha,
        "hora": hora,
        "jugado": False,
        "resultado": None
    }
    partidos.append(partido)
    return f"{partido} creado correctamente"

def listar_partidos(partidos, lista_equipos):
    if len(partidos) == 0:
        print("No hay partidos creados")
        return
    else:
        texto = ""
        for p in partidos:
            local_nombre = ""
            visitante_nombre = ""
            for e in lista_equipos:
                if e["id"] == p["local_id"]:
                    local_nombre = e["nombre"]
                if e["id"] == p["visitante_id"]:
                    visitante_nombre = e["nombre"]
            jugado = "Sí" if p["jugado"] else "No"
            texto += f'ID:{p["id"]} | Jornada:{p["jornada"]} | Local:{local_nombre} | Visitante:{visitante_nombre} | Fecha:{p["fecha"]} | Hora:{p["hora"]} | Jugado:{jugado} | Resultado:{p["resultado"]}\n'
        return texto

def buscar_partido_por_id(partidos, lista_equipos):
    id_busqueda = int(input("Introduce el id del partido que quieras buscar: "))
    for p in partidos:
        if p["id"] == id_busqueda:
            local_nombre = ""
            visitante_nombre = ""
            for e in lista_equipos:
                if e["id"] == p["local_id"]:
                    local_nombre = e["nombre"]
                if e["id"] == p["visitante_id"]:
                    visitante_nombre = e["nombre"]
            return f"Partido encontrado: {p} | Local: {local_nombre} | Visitante: {visitante_nombre}"
    return "No se encontró un partido con ese ID"

def reprogramar_partido(partidos):
    id_busqueda = int(input("Introduce el id del partido que quieras reprogramar: "))
    for p in partidos:
        if p["id"] == id_busqueda:
            if p["jugado"]:
                return "No se puede reprogramar un partido jugado"
            nueva_fecha = input("Introduce la nueva fecha: ")
            nueva_hora = input("Introduce la nueva hora: ")
            p["fecha"] = nueva_fecha
            p["hora"] = nueva_hora
            return f"Partido con ID: {id_busqueda} reprogramado"
    return "No se encontró partido con ese ID"

def eliminar_partido(partidos):
    id_busqueda = int(input("Introduce el id del partido que quieras eliminar: "))
    for i in range(len(partidos)):
        if partidos[i]["id"] == id_busqueda:
            if partidos[i]["jugado"]:
                return "No se puede eliminar un partido jugado"
            partidos.pop(i)
            return f"Partido eliminado correctamente"
    return "No se encontró partido con ese ID"
