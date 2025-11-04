    # Modulo 1
    #variables usadas 
lista_equipos = []
equipo = {}
nombre = 0
ciudad = 0
estado = 0
id_busqueda = 0
nuevo_equipo = 0
nueva_ciudad = 0

    #definimos funciones
def generar_id(lista_equipos):
        return len(lista_equipos) + 1

def crear_equipo(lista_equipos):
        nombre = input("Introduce el nombre del equipo: ")
        ciudad = input(f"Introdue la ciudad donde se encuentre {nombre}: ")
        Estado = "Inactivo"
        if nombre == "" or ciudad == "":
            print("Ciudad y nombre no pueden estar vacíos")
            return
        
        for equipo in lista_equipos:
            if equipo["nombre"] == nombre:
                print ("Este equipo ya existe")
                return
        
        else:
            Estado = "Activo"

        equipo = {
            "id" : generar_id(lista_equipos),
            "nombre": nombre,
            "ciudad": ciudad,
            "estado": Estado
        }
        lista_equipos.append(equipo)
        return f"{equipo} creado correctamente"


def listar_equipos(lista_equipos):
    if len(lista_equipos) == 0:
        print("No hay equipos, vuelva a la primera opcion para añadir")
        return
    else:
        texto = ""
        for i in lista_equipos:
            estado = "Activo" if i["estado"] == "Activo" else "Inactivo"
            texto += f'ID:{i["id"]} | Equipo:{i["nombre"]} | Ciudad:{i["ciudad"]} | Estado:{estado}\n'
        return texto
    
def buscar_articulo_por_id(articulos):
    id_busqueda = int(input("Introduce el ID del artículo: "))
    for a in articulos:
        if a["id"] == id_busqueda:
            return f"Artículo encontrado: {a}"
    return "No se encontró un artículo con ese ID."
    
def buscar_equipo_por_id(lista_equipos):
     id_busqueda = int(input("Introduce el id del equipo que quieras buscar: "))
     for i in lista_equipos:
          if i["id"] == id_busqueda:
               return f"Artículo encontrado: {i}"
     return "No se encontro un artículo por ese id"

def eliminar_equipo(lista_equipos)
     id_busqueda = int(input("Introduce el id del equipo que quieras eliminar: "))
     for i in range(len(lista_equipos)):
          if lista_equipos[i]["id"] == id_busqueda:
               nombre = lista_equipos[i]["nombre"]
               lista_equipos.pop(i)
               return f"Equipo eliminado correctamente"
     return "No se encontro equipo por ese ID"

def actualizar(lista_equipos):
     id_busqueda = int(input("Introduce el id del equipo que quieras actualizar: "))
     for i in lista_equipos:
          if i["id"] == id_busqueda:
               nuevo_nombre = input("Introduce el nuevo nombre: ")
               nueva_ciudad = input("Introduce la nueva ciudad: ")
               i["nombre"] = nuevo_nombre
               i["ciudad"] = nueva_ciudad
               return f"Articulo con ID: {id_busqueda} actualizado"
     return "No se encontro articulo con ese ID"

     
