#Ejercicio 3: Calcular el Doble de Cada Número en una Lista
def calcular_doble(numero):
    return numero * 2

numeros = []
seguir = 0

while seguir == 0:
    entrada = input("Introduce el numero del que quieras calcular el dobe (o fin para acabar):")
    if entrada.lower() == "fin":
        seguir += 1
    else:
        numeros.append(int(entrada))
        

resultado = list(map(calcular_doble, numeros))
print("Resultado:", resultado)
