seguir = 0

def suma_hasta_limite(limite):
    suma = 0
    for i in range(1, limite + 1):
        suma += i
    return suma

while seguir == 0:
    numero = input("Introduce un número (o fin para acabar): ")

    if numero == "fin":
        print("Saliendo del programa")
        seguir += 1
    else:
        numero = int(numero)
        print(f"La suma desde 1 hasta {numero} es: {suma_hasta_limite(numero)}")
