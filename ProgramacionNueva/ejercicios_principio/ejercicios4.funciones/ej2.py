seguir = 0
numero_nuevo = 0
numeros = []


def encontrar_maximo(numeros):
    maximo = numeros[0]
    for numero in numeros[1:]:
        if numero > maximo:
            maximo = numero
    return maximo


while seguir == 0:
    numero_nuevo = input("introduzca un numero a la lista, o fin para acabar: ")
    if numero_nuevo == "fin":
        seguir += 1
    else:
        numeros.append(int(numero_nuevo))
        # int sacado de chatgpt, me daba error y no sabia el porque

print(f"El numero maximo es: {encontrar_maximo(numeros)}")