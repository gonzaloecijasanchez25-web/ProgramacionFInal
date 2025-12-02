"""
Gestor de Clientes
Programa de consola para gestionar clientes usando arrays paralelos
Autor: [Tu Nombre]
Fecha: [Fecha]
"""

# ============================================================================
# CONSTANTES Y VARIABLES GLOBALES
# ============================================================================
MAX_CLIENTES = 100  # Máximo número de clientes que se pueden almacenar
NOMBRE_FICHERO = "clientes.txt"  # Nombre del archivo para guardar los datos

# Arrays paralelos para almacenar los datos de los clientes
dni = [""] * MAX_CLIENTES
nombre = [""] * MAX_CLIENTES
apellidos = [""] * MAX_CLIENTES
telefono = [""] * MAX_CLIENTES

# Variable para controlar el número actual de clientes
num_clientes = 0

# ============================================================================
# FUNCIONES AUXILIARES
# ============================================================================

def buscar_cliente_por_dni(dni_buscar):
    """
    Busca un cliente por su DNI.
    
    Args:
        dni_buscar (str): DNI a buscar
        
    Returns:
        int: Índice del cliente si se encuentra, -1 si no se encuentra
    """
    for i in range(num_clientes):
        if dni[i] == dni_buscar:
            return i
    return -1


def mostrar_cliente(indice):
    """
    Muestra la información de un cliente.
    
    Args:
        indice (int): Índice del cliente a mostrar
    """
    print("\n" + "="*50)
    print("INFORMACIÓN DEL CLIENTE")
    print("="*50)
    print(f"DNI: {dni[indice]}")
    print(f"Nombre: {nombre[indice]}")
    print(f"Apellidos: {apellidos[indice]}")
    print(f"Teléfono: {telefono[indice]}")
    print("="*50)


def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    """
    print("\n" * 2)


# ============================================================================
# FUNCIONES PRINCIPALES DEL MENÚ
# ============================================================================

def alta_cliente():
    """
    Opción 1: Da de alta un nuevo cliente.
    Solicita los datos del cliente y los añade a los arrays.
    """
    global num_clientes
    
    print("\n" + "="*50)
    print("ALTA DE CLIENTE")
    print("="*50)
    
    # Verificar si hay espacio disponible
    if num_clientes >= MAX_CLIENTES:
        print("¡Error! No se pueden añadir más clientes. Límite alcanzado.")
        return
    
    # Solicitar datos del cliente
    dni_cliente = input("Introduce el DNI: ").strip()
    
    # Verificar si el DNI ya existe
    if buscar_cliente_por_dni(dni_cliente) != -1:
        print("¡Error! Ya existe un cliente con ese DNI.")
        return
    
    nombre_cliente = input("Introduce el nombre: ").strip()
    apellidos_cliente = input("Introduce los apellidos: ").strip()
    telefono_cliente = input("Introduce el teléfono: ").strip()
    
    # Validar que no se introduzcan campos vacíos
    if not dni_cliente or not nombre_cliente or not apellidos_cliente:
        print("¡Error! DNI, nombre y apellidos son campos obligatorios.")
        return
    
    # Añadir el cliente a los arrays
    dni[num_clientes] = dni_cliente
    nombre[num_clientes] = nombre_cliente
    apellidos[num_clientes] = apellidos_cliente
    telefono[num_clientes] = telefono_cliente
    
    num_clientes += 1
    print(f"\n✅ Cliente {nombre_cliente} {apellidos_cliente} añadido correctamente.")


def listar_clientes():
    """
    Opción 2: Lista todos los clientes almacenados.
    """
    print("\n" + "="*50)
    print("LISTADO DE CLIENTES")
    print("="*50)
    
    if num_clientes == 0:
        print("No hay clientes registrados.")
        return
    
    print(f"Total de clientes: {num_clientes}\n")
    
    # Mostrar todos los clientes
    for i in range(num_clientes):
        print(f"Cliente {i+1}:")
        print(f"  DNI: {dni[i]}")
        print(f"  Nombre: {nombre[i]}")
        print(f"  Apellidos: {apellidos[i]}")
        print(f"  Teléfono: {telefono[i]}")
        print("-" * 30)


def buscar_cliente():
    """
    Opción 3: Busca un cliente por su DNI.
    """
    print("\n" + "="*50)
    print("BUSCAR CLIENTE POR DNI")
    print("="*50)
    
    if num_clientes == 0:
        print("No hay clientes registrados.")
        return
    
    dni_buscar = input("Introduce el DNI a buscar: ").strip()
    
    indice = buscar_cliente_por_dni(dni_buscar)
    
    if indice != -1:
        mostrar_cliente(indice)
    else:
        print(f"\n❌ Cliente con DNI {dni_buscar} no encontrado.")


def modificar_telefono():
    """
    Opción 4: Modifica el teléfono de un cliente.
    """
    print("\n" + "="*50)
    print("MODIFICAR TELÉFONO DE CLIENTE")
    print("="*50)
    
    if num_clientes == 0:
        print("No hay clientes registrados.")
        return
    
    dni_buscar = input("Introduce el DNI del cliente: ").strip()
    
    indice = buscar_cliente_por_dni(dni_buscar)
    
    if indice != -1:
        print(f"\nCliente encontrado: {nombre[indice]} {apellidos[indice]}")
        print(f"Teléfono actual: {telefono[indice]}")
        
        nuevo_telefono = input("\nIntroduce el nuevo teléfono: ").strip()
        
        if nuevo_telefono:
            telefono[indice] = nuevo_telefono
            print("✅ Teléfono actualizado correctamente.")
        else:
            print("❌ El teléfono no puede estar vacío.")
    else:
        print(f"\n❌ Cliente con DNI {dni_buscar} no encontrado.")


def eliminar_cliente():
    """
    Opción 5: Elimina un cliente por su DNI.
    """
    global num_clientes
    
    print("\n" + "="*50)
    print("ELIMINAR CLIENTE")
    print("="*50)
    
    if num_clientes == 0:
        print("No hay clientes registrados.")
        return
    
    dni_buscar = input("Introduce el DNI del cliente a eliminar: ").strip()
    
    indice = buscar_cliente_por_dni(dni_buscar)
    
    if indice != -1:
        # Mostrar información del cliente a eliminar
        print(f"\nCliente a eliminar:")
        mostrar_cliente(indice)
        
        # Confirmar eliminación
        confirmacion = input("\n¿Estás seguro de que quieres eliminar este cliente? (s/n): ").strip().lower()
        
        if confirmacion == 's':
            # Desplazar los clientes siguientes una posición hacia arriba
            for i in range(indice, num_clientes - 1):
                dni[i] = dni[i + 1]
                nombre[i] = nombre[i + 1]
                apellidos[i] = apellidos[i + 1]
                telefono[i] = telefono[i + 1]
            
            # Limpiar la última posición y reducir el contador
            dni[num_clientes - 1] = ""
            nombre[num_clientes - 1] = ""
            apellidos[num_clientes - 1] = ""
            telefono[num_clientes - 1] = ""
            
            num_clientes -= 1
            print("✅ Cliente eliminado correctamente.")
        else:
            print("❌ Eliminación cancelada.")
    else:
        print(f"\n❌ Cliente con DNI {dni_buscar} no encontrado.")


def guardar_clientes():
    """
    Opción 6: Guarda los clientes en un fichero de texto.
    """
    print("\n" + "="*50)
    print("GUARDAR CLIENTES EN FICHERO")
    print("="*50)
    
    if num_clientes == 0:
        print("No hay clientes para guardar.")
        return
    
    try:
        with open(NOMBRE_FICHERO, 'w', encoding='utf-8') as archivo:
            for i in range(num_clientes):
                # Formato: DNI;Nombre;Apellidos;Telefono
                linea = f"{dni[i]};{nombre[i]};{apellidos[i]};{telefono[i]}"
                archivo.write(linea + "\n")
        
        print(f"✅ {num_clientes} clientes guardados correctamente en '{NOMBRE_FICHERO}'.")
    
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")


def cargar_clientes():
    """
    Opción 7: Carga los clientes desde un fichero de texto.
    """
    global num_clientes
    
    print("\n" + "="*50)
    print("CARGAR CLIENTES DESDE FICHERO")
    print("="*50)
    
    try:
        with open(NOMBRE_FICHERO, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            
            if not lineas:
                print("El archivo está vacío.")
                return
            
            # Reiniciar los arrays
            for i in range(MAX_CLIENTES):
                dni[i] = ""
                nombre[i] = ""
                apellidos[i] = ""
                telefono[i] = ""
            
            num_clientes = 0
            
            # Cargar los clientes desde el archivo
            for linea in lineas:
                if num_clientes >= MAX_CLIENTES:
                    print(f"¡Advertencia! Se alcanzó el límite de {MAX_CLIENTES} clientes.")
                    break
                
                linea = linea.strip()
                if linea:  # Ignorar líneas vacías
                    partes = linea.split(';')
                    
                    if len(partes) >= 4:
                        dni[num_clientes] = partes[0]
                        nombre[num_clientes] = partes[1]
                        apellidos[num_clientes] = partes[2]
                        telefono[num_clientes] = partes[3]
                        num_clientes += 1
        
        print(f"✅ {num_clientes} clientes cargados correctamente desde '{NOMBRE_FICHERO}'.")
    
    except FileNotFoundError:
        print(f"❌ El archivo '{NOMBRE_FICHERO}' no existe.")
    except Exception as e:
        print(f"❌ Error al cargar el archivo: {e}")


def mostrar_menu():
    """
    Muestra el menú principal del programa.
    """
    print("\n" + "="*50)
    print("GESTOR DE CLIENTES")
    print("="*50)
    print("1. Alta de cliente")
    print("2. Listar todos los clientes")
    print("3. Buscar cliente por DNI")
    print("4. Modificar teléfono de un cliente")
    print("5. Eliminar cliente")
    print("6. Guardar clientes en fichero")
    print("7. Cargar clientes desde fichero")
    print("8. Salir")
    print("="*50)


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal del programa.
    Controla el flujo principal y el menú interactivo.
    """
    print("BIENVENIDO AL GESTOR DE CLIENTES")
    print("Versión 1.0 - Desarrollado en Python")
    
    # Cargar clientes automáticamente al iniciar si el archivo existe
    try:
        with open(NOMBRE_FICHERO, 'r', encoding='utf-8') as archivo:
            print(f"\n📁 Archivo '{NOMBRE_FICHERO}' detectado. Usa la opción 7 para cargar los datos.")
    except:
        print(f"\n📁 Archivo '{NOMBRE_FICHERO}' no encontrado. Puedes crear uno nuevo.")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSelecciona una opción (1-8): ").strip()
            
            if opcion == "1":
                alta_cliente()
            elif opcion == "2":
                listar_clientes()
            elif opcion == "3":
                buscar_cliente()
            elif opcion == "4":
                modificar_telefono()
            elif opcion == "5":
                eliminar_cliente()
            elif opcion == "6":
                guardar_clientes()
            elif opcion == "7":
                cargar_clientes()
            elif opcion == "8":
                print("\n" + "="*50)
                print("GRACIAS POR USAR EL GESTOR DE CLIENTES")
                print("¡Hasta pronto!")
                print("="*50)
                break
            else:
                print("\n❌ Opción no válida. Por favor, introduce un número del 1 al 8.")
        
        except ValueError:
            print("\n❌ Error: Debes introducir un número válido.")
        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
        
        # Pausa para que el usuario pueda ver los resultados
        input("\nPresiona Enter para continuar...")
        limpiar_pantalla()


# ============================================================================
# EJECUCIÓN DEL PROGRAMA
# ============================================================================
if __name__ == "__main__":
    main()