lista_productos = []

while True:
    producto = input("Introduzca los artículos que quieras comprar (fin para terminar): ")

    if producto.lower() == "fin":
        break

    if producto not in lista_productos:
        lista_productos.append(producto)
        print(f"{producto} añadido a la lista")

    else:
        print(f"{producto} ya ha sido introduce")

print("\nLista de la compra:")
for item in lista_productos:
    print(f"{item}")