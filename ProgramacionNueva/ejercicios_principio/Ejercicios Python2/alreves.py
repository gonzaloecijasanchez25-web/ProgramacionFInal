palabra = input("Introduce una palabra: ")
invertida = ""

for i in range(len(palabra) - 1, -1, -1):
    invertida += palabra[i]

print("La palabra invertida es:", invertida)