# variables
articulos = []
usuarios = []
ventas = []
carrito_actual = []
usuario_activo = None
seguir = 0
opcion = ""
nombre = ""
precio = 0.0
stock = 0
email = ""
id_busqueda = 0
mensaje = ""
texto = ""
estado = ""
cantidad = 0
total = 0
subtotal = 0
i = 0
u = {}
a = {}
venta = {}
producto = {}
usuario = {}
items = []
carrito_actual = []
usuario_activo = None
ventas = []

#funciones arituclos
from funciones_articulos import generar_id, leer_float, crear_articulo, listar_articulos, buscar_articulo_por_id, actualizar_articulo, eliminar_articulo, alternar_activo

#funciones usario
from funciones_usuarios import usr_crear, usr_listar, usr_buscar_por_id, usr_actualizar, usr_eliminar, usr_alternar_activo

#funciones carrito
from funciones_carrito import ven_seleccionar_usuario, ven_añadir_carrito, ven_quitar_carrito, ven_ver_carrito, ven_confirmar_compra, ven_historial_usuario, ven_vaciar_carrito


#menus

def menu_articulos():
    seguir = 0
    while seguir == 0:
        print("\n--- MENÚ DE GESTIÓN DE ARTÍCULOS ---")
        print("1. Crear artículo")
        print("2. Listar artículos")
        print("3. Buscar artículo por ID")
        print("4. Actualizar artículo")
        print("5. Eliminar artículo")
        print("6. Alternar activo/inactivo")
        print("7. Salir")

        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                mensaje = crear_articulo(articulos)
                print(mensaje)
            case "2":
                mensaje = listar_articulos(articulos)
                print(mensaje)
            case "3":
                mensaje = buscar_articulo_por_id(articulos)
                print(mensaje)
            case "4":
                mensaje = actualizar_articulo(articulos)
                print(mensaje)
            case "5":
                mensaje = eliminar_articulo(articulos)
                print(mensaje)
            case "6":
                mensaje = alternar_activo(articulos)
                print(mensaje)
            case "7":
                print("Saliendo del programa...")
                seguir = 1
            case _:
                print("Opción no válida.")

def menu_usuarios():
    seguir = 0
    while seguir == 0:
        print("\n--- MENÚ DE USUARIOS ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Buscar usuario por ID")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Alternar activo/inactivo")
        print("7. Volver")

        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                print(usr_crear(usuarios))
            case "2":
                print(usr_listar(usuarios))
            case "3":
                print(usr_buscar_por_id(usuarios))
            case "4":
                print(usr_actualizar(usuarios))
            case "5":
                print(usr_eliminar(usuarios))
            case "6":
                print(usr_alternar_activo(usuarios))
            case "7":
                seguir = 1
            case _:
                print("Opción no válida.")

def menu_ventas(articulos, usuarios, ventas, carrito_actual, usuario_activo):
    seguir = 0
    while seguir == 0:
        print("\n--- MENÚ DE VENTAS / CARRITO ---")
        print("1. Seleccionar usuario activo")
        print("2. Añadir artículo al carrito")
        print("3. Quitar artículo del carrito")
        print("4. Ver carrito")
        print("5. Confirmar compra")
        print("6. Historial de ventas por usuario")
        print("7. Vaciar carrito")
        print("8. Volver")

        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                mensaje, usuario_activo = ven_seleccionar_usuario(usuarios, usuario_activo)
                print(mensaje)
            case "2":
                mensaje, carrito_actual = ven_añadir_carrito(articulos, carrito_actual, usuario_activo)
                print(mensaje)
            case "3":
                mensaje, carrito_actual = ven_quitar_carrito(carrito_actual)
                print(mensaje)
            case "4":
                print(ven_ver_carrito(articulos, carrito_actual))
            case "5":
                mensaje, carrito_actual, ventas = ven_confirmar_compra(articulos, carrito_actual, usuario_activo, ventas)
                print(mensaje)
            case "6":
                print(ven_historial_usuario(usuario_activo, ventas))
            case "7":
                mensaje, carrito_actual = ven_vaciar_carrito(carrito_actual)
                print(mensaje)
            case "8":
                seguir = 1
            case _:
                print("Opción no válida.")
    return carrito_actual, usuario_activo, ventas

def menu_principal():
    seguir = 0
    while seguir == 0:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestión de artículos")
        print("2. Gestión de usuarios")
        print("3. Menu ventas")
        print("4. Para salir")

        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                menu_articulos()
            case "2":
                menu_usuarios()
            case "3":
                print("Saliendo del programa...")
                menu_ventas()
            case "4":
                seguir += 1
            case _:
                print("Opción no válida.")




menu_principal()
