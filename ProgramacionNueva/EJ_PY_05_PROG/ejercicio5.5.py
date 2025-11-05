# Ejercicio 5: Calcular la Longitud de Cada Palabra en una Lista

def calcular_longitud(palabra):
    return len(palabra)

palabras = []
seguir = 0

while seguir == 0:
    entrada = input("Introduce una palabra (o fin para acabar): ")
    if entrada.lower() == "fin":
        seguir += 1
    else:
        palabras.append(entrada)

resultado = list(map(calcular_longitud, palabras))
print("El resultado es:", resultado)
