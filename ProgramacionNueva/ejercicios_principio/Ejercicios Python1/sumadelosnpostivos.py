numero = int(input("Introduce un numero:  "))
i = 0
suma = 0

if numero > 0:
    for i in range(1, numero):
        suma = suma + i
    print("La suma de los numeros desde el 0 hasta ", numero, "es: ", suma)

else:
    print("El numero debe ser mayor que 0")
