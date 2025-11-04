def generar_id(articulos):
    return len(articulos) + 1

def crear_articulo(articulos):
    nombre = input("Introduce el nombre del artículo: ")
    precio = float(input(f"Introduce el precio de {nombre}: "))
    while precio <= 0:
        print("El precio debe ser superior a 0")
        precio = float(input("Introduce de nuevo el precio: "))
    stock = int(input(f"Introduce el stock de {nombre}: "))
    while stock < 0:
        print("El stock no puede ser negativo")
        stock = int(input("Introduce de nuevo el stock: "))

    producto = {
        "id": generar_id(articulos),
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "activo": True
    }

    articulos.append(producto)
    return f"Artículo '{nombre}' creado con éxito."
# 
def listar_articulos(articulos):
    if len(articulos) == 0:
        return "No hay artículos registrados."
    else:
        texto = ""
        for a in articulos:
            estado = "Activo" if a["activo"] else "Inactivo"
            texto += f'ID:{a["id"]} | {a["nombre"]} | Precio:{a["precio"]}€ | Stock:{a["stock"]} | Estado:{estado}\n'
        return texto

def buscar_articulo_por_id(articulos):
    id_busqueda = int(input("Introduce el ID del artículo: "))
    for a in articulos:
        if a["id"] == id_busqueda:
            return f"Artículo encontrado: {a}"
    return "No se encontró un artículo con ese ID."

def leer_float(mensaje, minimo=None):
    valor = float(input(mensaje))
    if minimo != None and valor < minimo:
        print("El valor no puede ser menor que", minimo)
        valor = minimo
    return valor

def actualizar_articulo(articulos):
    id_busqueda = int(input("Introduce el ID del artículo a actualizar: "))
    for a in articulos:
        if a["id"] == id_busqueda:
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_precio = leer_float("Nuevo precio: ", 0)
            nuevo_stock = int(leer_float("Nuevo stock: ", 0))
            a["nombre"] = nuevo_nombre
            a["precio"] = nuevo_precio
            a["stock"] = nuevo_stock
            return f"Artículo con ID {id_busqueda} actualizado correctamente."
    return "No se encontró un artículo con ese ID."

def eliminar_articulo(articulos):
    id_busqueda = int(input("Introduce el ID del artículo a eliminar: "))
    for i in range(len(articulos)):
        if articulos[i]["id"] == id_busqueda:
            nombre = articulos[i]["nombre"]
            articulos.pop(i)
            return f"Artículo '{nombre}' eliminado correctamente."
    return "No se encontró un artículo con ese ID."

def alternar_activo(articulos):
    id_busqueda = int(input("Introduce el ID del artículo: "))
    for a in articulos:
        if a["id"] == id_busqueda:
            a["activo"] = not a["activo"]
            estado = "activo" if a["activo"] else "inactivo"
            return f"El artículo '{a['nombre']}' ahora está {estado}."
    return "No se encontró un artículo con ese ID."
