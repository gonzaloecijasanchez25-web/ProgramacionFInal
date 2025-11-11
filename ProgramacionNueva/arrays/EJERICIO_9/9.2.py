import numpy as np
print("Introduce los valores del array 1: ")
array1 = np.array([int(input(f"Introduce el numero {i+1}: "))for i in range(6)])
print("Introduce los valores del array 2: ")
array2 = np.array([int(input(f"Introduce el numero {i+1}: "))for i in range(6)])

producto = array1 * array2
print(f"Los resultados son: {producto}")
