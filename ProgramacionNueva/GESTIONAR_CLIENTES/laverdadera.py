import pickle

# Arrays
nombre = []
apellidos = []
telefono = []
dni = []

# Funciones
def alta_cliente(dni_arr, noms, apes, tels):
    d = input("DNI: ")
    if d in dni_arr:
        print("Ya existe un cliente con ese DNI")
        return

    nom = input("Nombre: ")
    ape = input("Apellidos: ")
    tel = input("Telefono: ")

    dni_arr.append(d)
    noms.append(nom)
    apes.append(ape)
    tels.append(tel)

    print("Cliente añadido")


def listar_clientes(dni_arr, noms, apes, tels):
    if not dni_arr:
        print("No hay clientes")
        return
    for i in range(len(dni_arr)):
        print(f"DNI: {dni_arr[i]}, Nombre: {noms[i]}, Apellidos: {apes[i]}, Teléfono: {tels[i]}")


def buscar_por_dni(dni_arr, d):
    for i in range(len(dni_arr)):
        if dni_arr[i] == d:
            return i
    return -1


def buscar_cliente(dni_arr, noms, apes, tels):
    d = input("DNI a buscar: ")
    pos = buscar_por_dni(dni_arr, d)
    if pos == -1:
        print("Cliente no encontrado")
        return
    print(f"DNI: {dni_arr[pos]}, Nombre: {noms[pos]}, Apellidos: {apes[pos]}, Teléfono: {tels[pos]}")


def modificar_telefono(dni_arr, tels):
    d = input("DNI a modificar: ")
    pos = buscar_por_dni(dni_arr, d)
    if pos == -1:
        print("Cliente no encontrado")
        return
    nuevo = input("Nuevo teléfono: ")
    tels[pos] = nuevo
    print("Teléfono actualizado")


def eliminar_cliente(dni_arr, noms, apes, tels):
    d = input("DNI a eliminar: ")
    pos = buscar_por_dni(dni_arr, d)
    if pos == -1:
        print("Cliente no encontrado")
        return
    dni_arr.pop(pos)
    noms.pop(pos)
    apes.pop(pos)
    tels.pop(pos)
    print("Cliente eliminado")


def guardar(dni_arr, noms, apes, tels):
    try:
        # Crear una tupla con todos los arrays para guardarlos juntos
        datos = (dni_arr, noms, apes, tels)
        
        with open("clientes.pkl", "wb") as f:
            pickle.dump(datos, f)
        print("Guardado realizado (formato pickle)")
    except Exception as e:
        print(f"Error al guardar: {e}")


def cargar(dni_arr, noms, apes, tels):
    try:
        with open("clientes.pkl", "rb") as f:
            # Cargar la tupla con los 4 arrays
            datos = pickle.load(f)
            
            # Limpiar los arrays actuales
            dni_arr.clear()
            noms.clear()
            apes.clear()
            tels.clear()
            
            # Recuperar los datos de la tupla
            dni_arr.extend(datos[0])
            noms.extend(datos[1])
            apes.extend(datos[2])
            tels.extend(datos[3])
            
        print("Datos cargados (formato pickle)")
    except FileNotFoundError:
        print("No existe el archivo 'clientes.pkl'")
    except Exception as e:
        print(f"Error al cargar: {e}")


def mostrar_menu():
    """Función que muestra el menú y gestiona todas las opciones"""
    while True:
        print("\n--- MENÚ GESTIÓN DE CLIENTES ---")
        print("1. Alta de cliente")
        print("2. Listar todos los clientes")
        print("3. Buscar cliente por DNI")
        print("4. Modificar teléfono de un cliente")
        print("5. Eliminar cliente")
        print("6. Guardar clientes en fichero (pickle)")
        print("7. Cargar clientes desde fichero (pickle)")
        print("8. Salir")

        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                alta_cliente(dni, nombre, apellidos, telefono)
            case "2":
                listar_clientes(dni, nombre, apellidos, telefono)
            case "3":
                buscar_cliente(dni, nombre, apellidos, telefono)
            case "4":
                modificar_telefono(dni, telefono)
            case "5":
                eliminar_cliente(dni, nombre, apellidos, telefono)
            case "6":
                guardar(dni, nombre, apellidos, telefono)
            case "7":
                cargar(dni, nombre, apellidos, telefono)
            case "8":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, elige una opción del 1 al 8.")


# Punto de entrada principal del programa
print("=== SISTEMA DE GESTIÓN DE CLIENTES ===")
print("Usando serialización con pickle")
mostrar_menu()