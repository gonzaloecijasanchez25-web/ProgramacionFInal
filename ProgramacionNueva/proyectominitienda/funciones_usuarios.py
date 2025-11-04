def usr_crear(usuarios):
    nombre = input("Introduce el nombre del usuario: ")
    email = input(f"Introduce el email de {nombre}: ")

    while "@" not in email or "." not in email:
        print("El email no es válido. Debe contener '@' y '.'")
        email = input("Introduce un email válido: ")

    usuario = {
        "id": generar_id(usuarios),
        "nombre": nombre,
        "email": email,
        "activo": True
    }

    usuarios.append(usuario)
    return f"Usuario '{nombre}' creado con éxito."

def usr_listar(usuarios):
    if len(usuarios) == 0:
        return "No hay usuarios registrados."
    texto = ""
    for u in usuarios:
        estado = "Activo" if u["activo"] else "Inactivo"
        texto += f'ID:{u["id"]} | {u["nombre"]} | Email:{u["email"]} | Estado:{estado}\n'
    return texto

def usr_buscar_por_id(usuarios):
    id_busqueda = int(input("Introduce el ID del usuario: "))
    for u in usuarios:
        if u["id"] == id_busqueda:
            return f"Usuario encontrado: {u}"
    return "No se encontró un usuario con ese ID."

#hecho con chatgpt
def usr_actualizar(usuarios):
    id_busqueda = int(input("Introduce el ID del usuario a actualizar: "))
    for u in usuarios:
        if u["id"] == id_busqueda:
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_email = input("Nuevo email: ")
            while "@" not in nuevo_email or "." not in nuevo_email:
                print("El email no es válido. Debe contener '@' y '.'")
                nuevo_email = input("Introduce un email válido: ")

            u["nombre"] = nuevo_nombre
            u["email"] = nuevo_email
            return f"Usuario con ID {id_busqueda} actualizado correctamente."
    return "No se encontró un usuario con ese ID."
#

def usr_eliminar(usuarios):
    id_busqueda = int(input("Introduce el ID del usuario a eliminar: "))
    for i in range(len(usuarios)):
        if usuarios[i]["id"] == id_busqueda:
            nombre = usuarios[i]["nombre"]
            usuarios.pop(i)
            return f"Usuario '{nombre}' eliminado correctamente."
    return "No se encontró un usuario con ese ID."

def usr_alternar_activo(usuarios):
    id_busqueda = int(input("Introduce el ID del usuario: "))
    for u in usuarios:
        if u["id"] == id_busqueda:
            u["activo"] = not u["activo"]
            estado = "activo" if u["activo"] else "inactivo"
            return f"El usuario '{u['nombre']}' ahora está {estado}."
    return "No se encontró un usuario con ese ID."