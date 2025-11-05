# Ejercicio 1: Sumar 5 a Cada Número de una Lista
def sumar_cinco(numero):
    return numero + 5

numeros = []
seguir = 0

while seguir == 0:
    entrada = input("Introduce un número(o fin para acabar): ")
    if entrada.lower() == "fin":
        seguir += 1
    else:
        numeros.append(int(entrada))

resultado = list(map(sumar_cinco, numeros))
print("Resultado:", resultado)

