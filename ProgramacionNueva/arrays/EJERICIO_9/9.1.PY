import numpy as np

print("Introduce los valores del array 1:")
array1 = np.array([int(input(f"Número {i+1}: ")) for i in range(5)])


print("Introduce los valores del array 2:")
array2 = np.array([int(input(f"Número {i+1}: ")) for i in range(5)])

suma_arrays = array1 + array2
print(f"Los resultados de la suma: {suma_arrays}")