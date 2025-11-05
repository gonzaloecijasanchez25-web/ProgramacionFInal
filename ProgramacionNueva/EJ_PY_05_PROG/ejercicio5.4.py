#Ejercicio 4: Redondear una Lista de Números Decimales

numeros = []
seguir = 0

while seguir == 0:
    entrada = input("Introduce el numero que quieras redonder (o fin para acabar):")
    if entrada.lower() == "fin":
        seguir +=1
    else:
        numeros.append(float(entrada))


resultado = list(map(round, numeros))
print("EL resultado es:", resultado) 