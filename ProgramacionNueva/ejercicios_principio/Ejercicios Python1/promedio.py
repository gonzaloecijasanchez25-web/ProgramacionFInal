suma = 0
contador = 0

while True:
    numero = int(input("Introduce un numero (0 para parar): "))
    if numero == 0:
        break
    suma += numero
    contador += 1

promedio = suma / contador
print("El promedio de los numeros es:", promedio)
