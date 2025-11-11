import numpy as np  # Importa la librería numpy para trabajar con arrays y funciones matemáticas

def linea():
    print("---------------------")  # Función que imprime una línea separadora

# Convertir una lista de Python a un array de numpy y mostrar ambos
mi_lista = [1, 2, 3, 4]
mi_array = np.array(mi_lista)
print(mi_array)  # Muestra el array: [1 2 3 4]
print(mi_lista)  # Muestra la lista original: [1, 2, 3, 4]
linea()

# Crear y mostrar una matriz 2x3
mi_matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(mi_matriz)
linea()

# Crear y mostrar una matriz de ceros 3x5
ceros = np.zeros((3,5))
print(ceros)
linea()

# Crear y mostrar una matriz de unos 3x5
unos = np.ones((3,5))
print(unos)
linea()

# Sumar las matrices de ceros y unos y modificar un valor
nueva = ceros + unos
print(nueva)
linea()
nueva[1,2] = 5
linea()

# Crear y mostrar un array con valores de 0 a 8 de 2 en 2
secuencia = np.arange(0, 10, 2)
print(secuencia)
linea()

# Crear y mostrar 5 valores equidistantes entre 0 y 1
valores = np.linspace(0, 1, 5)
print(valores)
linea()

# Filtrar números mayores a 10 usando lista de Python
lista = [5, 12, 3, 18, 7, 20, 9]
nuevalista = []
for numero in lista:
    if numero > 10:
        nuevalista.append(numero)
linea()
print(list(nuevalista))

# Filtrar números mayores a 10 usando array de numpy
array = np.array(lista)
nuevo_array = array[array > 10]
linea()
print(list(nuevo_array))
