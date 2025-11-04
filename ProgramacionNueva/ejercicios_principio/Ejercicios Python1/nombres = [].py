nombres = []

while True:
    nombre = input("Ingresa un nombre (o escribe 'fin' para terminar): ")
    if nombre == "fin":
        break
    nombres = nombres + [nombre]

print("Los nombres ingresados son:", nombres)
print("Lista de nombres:")
for nombre in nombres:
    print("-", nombre)