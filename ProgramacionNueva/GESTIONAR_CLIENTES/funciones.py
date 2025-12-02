import numpy as np

#Inicializamos los arrays
dni_list = []
nombre_list = []
apellidos_list = []
telefono_list = []


def pedir_dni_existente(dni_list):
    dni = input("DNI: ")

# Sirve para comprobar si el DNI existe en la lista y para devolver el indice (utili para actualizar, eliminar )
    if dni not in dni_list:
        print("Ese DNI no existe.")
        return None
    
    return dni_list.index(dni)


def dar_de_alta(dni_list, nombre_list, apellidos_list, telefono_list):
    print("---Creacion de usuario---")
    dni = input("DNI: ")

    if dni in dni_list:
        print("Ese DNI ya existe.")
        return None
    
    return dni

    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    telefono = input("Teléfono: ")

    if telefono in telefono_list:
        print("Ese numero ya existe. ")
        return None

    dni_list.append(dni)
    nombre_list.append(nombre)
    apellidos_list.append(apellidos)
    telefono_list.append(telefono)

    print("---Cliente dado de alta.---")



def listar_clientes(dni_list)




