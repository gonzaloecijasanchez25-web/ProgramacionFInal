resultados = []
clasificacion = []
id_partido = 0
goles_local = 0
goles_visitante = 0

def registrar_resultado(partidos):
    id_partido = int(input("Introduce el id del partido: "))
    for p in partidos:
        if p["id"] == id_partido:
            if p["jugado"]:
                return "Este partido ya tiene resultado"
            goles_local = int(input("Introduce los goles del equipo local: "))
            goles_visitante = int(input("Introduce los goles del equipo visitante: "))
            p["resultado"] = (goles_local, goles_visitante)
            p["jugado"] = True
            return f"Resultado registrado correctamente: {p}"
    return "No se encontró un partido con ese ID"

#hecho con chatgpt, no sabia como hacerlo
def generar_clasificacion(partidos, lista_equipos):
    clasificacion = []
    for e in lista_equipos:
        equipo = {
            "id": e["id"],
            "nombre": e["nombre"],
            "PJ": 0,
            "G": 0,
            "E": 0,
            "P": 0,
            "GF": 0,
            "GC": 0,
            "DG": 0,
            "PTS": 0
        }
        clasificacion.append(equipo)

    for p in partidos:
        if p["jugado"] and p["resultado"] is not None:
            gL, gV = p["resultado"]
            for eq in clasificacion:
                if eq["id"] == p["local_id"]:
                    eq["PJ"] += 1
                    eq["GF"] += gL
                    eq["GC"] += gV
                    if gL > gV:
                        eq["G"] += 1
                        eq["PTS"] += 3
                    elif gL == gV:
                        eq["E"] += 1
                        eq["PTS"] += 1
                    else:
                        eq["P"] += 1
                if eq["id"] == p["visitante_id"]:
                    eq["PJ"] += 1
                    eq["GF"] += gV
                    eq["GC"] += gL
                    if gV > gL:
                        eq["G"] += 1
                        eq["PTS"] += 3
                    elif gV == gL:
                        eq["E"] += 1
                        eq["PTS"] += 1
                    else:
                        eq["P"] += 1

    for eq in clasificacion:
        eq["DG"] = eq["GF"] - eq["GC"]

    clasificacion.sort(key=lambda x: x["PTS"], reverse=True)

    texto = ""
    for eq in clasificacion:
        texto += f'{eq["nombre"]} | PJ:{eq["PJ"]} | G:{eq["G"]} | E:{eq["E"]} | P:{eq["P"]} | GF:{eq["GF"]} | GC:{eq["GC"]} | DG:{eq["DG"]} | PTS:{eq["PTS"]}\n'
    return texto

def estadisticas_equipo(partidos, lista_equipos):
    id_equipo = int(input("Introduce el id del equipo: "))
    nombre_equipo = ""
    for e in lista_equipos:
        if e["id"] == id_equipo:
            nombre_equipo = e["nombre"]

    if nombre_equipo == "":
        return "No se encontró un equipo con ese ID"

    pj = 0
    gf = 0
    gc = 0
    pts = 0

    for p in partidos:
        if p["jugado"] and p["resultado"] is not None:
            gL, gV = p["resultado"]
            if p["local_id"] == id_equipo:
                pj += 1
                gf += gL
                gc += gV
                if gL > gV:
                    pts += 3
                elif gL == gV:
                    pts += 1
            if p["visitante_id"] == id_equipo:
                pj += 1
                gf += gV
                gc += gL
                if gV > gL:
                    pts += 3
                elif gV == gL:
                    pts += 1

    return f"Equipo: {nombre_equipo} | PJ:{pj} | GF:{gf} | GC:{gc} | PTS:{pts}"
