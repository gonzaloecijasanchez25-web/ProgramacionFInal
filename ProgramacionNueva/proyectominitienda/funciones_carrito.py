carrito_actual = []
usuario_activo = None
ventas = []

def ven_seleccionar_usuario(usuarios, usuario_activo):
    print(usr_listar(usuarios))
    id_usuario = int(input("Introduce el ID del usuario activo: "))
    for u in usuarios:
        if u["id"] == id_usuario and u["activo"]:
            usuario_activo = id_usuario
            return f"Usuario '{u['nombre']}' seleccionado como activo.", usuario_activo
    return "Usuario no encontrado o inactivo.", usuario_activo

def ven_añadir_carrito(articulos, carrito_actual, usuario_activo):
    if usuario_activo == None:
        return "Selecciona un usuario activo antes de añadir artículos.", carrito_actual
    print(listar_articulos(articulos))
    id_art = int(input("Introduce el ID del artículo: "))
    for a in articulos:
        if a["id"] == id_art and a["activo"]:
            cantidad = int(input(f"Introduce la cantidad (stock disponible {a['stock']}): "))
            if cantidad < 1:
                return "Cantidad mínima es 1.", carrito_actual
            if cantidad > a["stock"]:
                return "No hay suficiente stock.", carrito_actual
            for i in range(len(carrito_actual)):
                if carrito_actual[i][0] == id_art:
                    carrito_actual[i] = (id_art, carrito_actual[i][1] + cantidad)
                    return f"{cantidad} unidades añadidas al carrito.", carrito_actual
            carrito_actual.append((id_art, cantidad))
            return f"{cantidad} unidades añadidas al carrito.", carrito_actual
    return "Artículo no encontrado o inactivo.", carrito_actual

def ven_quitar_carrito(carrito_actual):
    if len(carrito_actual) == 0:
        return "El carrito está vacío.", carrito_actual
    id_art = int(input("Introduce el ID del artículo a quitar: "))
    for i in range(len(carrito_actual)):
        if carrito_actual[i][0] == id_art:
            carrito_actual.pop(i)
            return "Artículo eliminado del carrito.", carrito_actual
    return "El artículo no está en el carrito.", carrito_actual

def ven_ver_carrito(articulos, carrito_actual):
    if len(carrito_actual) == 0:
        return "El carrito está vacío."
    texto = ""
    total = 0
    for art_id, cantidad in carrito_actual:
        for a in articulos:
            if a["id"] == art_id:
                subtotal = a["precio"] * cantidad
                texto += f"{a['nombre']} x {cantidad} = {subtotal}€\n"
                total += subtotal
    texto += f"Total: {total}€"
    return texto

def ven_confirmar_compra(articulos, carrito_actual, usuario_activo, ventas):
    if usuario_activo == None:
        return "Selecciona un usuario activo antes de comprar.", carrito_actual, ventas
    if len(carrito_actual) == 0:
        return "El carrito está vacío.", carrito_actual, ventas
    for art_id, cantidad in carrito_actual:
        for a in articulos:
            if a["id"] == art_id:
                if cantidad > a["stock"]:
                    return f"No hay suficiente stock de {a['nombre']}.", carrito_actual, ventas
    items = []
    total = 0
    for art_id, cantidad in carrito_actual:
        for a in articulos:
            if a["id"] == art_id:
                a["stock"] -= cantidad
                items.append((art_id, cantidad, a["precio"]))
                total += a["precio"] * cantidad
    venta = {
        "id_venta": generar_id(ventas),
        "usuario_id": usuario_activo,
        "items": items,
        "total": total
    }
    ventas.append(venta)
    carrito_actual = []
    return f"Compra confirmada. Total: {total}€", carrito_actual, ventas

def ven_historial_usuario(usuario_activo, ventas):
    if usuario_activo == None:
        return "Selecciona un usuario activo primero."
    texto = ""
    for v in ventas:
        if v["usuario_id"] == usuario_activo:
            texto += f"Venta ID {v['id_venta']}: Total {v['total']}€ Items: {v['items']}\n"
    if texto == "":
        return "No hay ventas para este usuario."
    return texto

def ven_vaciar_carrito(carrito_actual):
    carrito_actual = []
    return "Carrito vaciado.", carrito_actual