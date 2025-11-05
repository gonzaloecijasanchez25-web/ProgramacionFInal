# Ejercicio 2: Convertir una Lista de Frases a Títulos

frases = []
seguir = 0

while seguir == 0:
    entrada = input("Introduce una frase (o fin para acabar): ")
    if entrada.lower() == "fin":
        seguir += 1
    else:
        frases.append(entrada)

resultado = list(map(str.title, frases))
print("Resultado:", resultado)
