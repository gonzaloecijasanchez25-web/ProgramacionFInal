productos = {}

while True:
    nombre = input("Introduzca el producto que quieras anotar (o 'fin' para terminar): ")

#ponemos primero el fin, para en caso de fin no pedir cantidad de fin que no tiene sentido
    if nombre.lower() == "fin":
        print("\nTerminaste tu lista, a continuación te la muestro:")
        break

#pedimos cantidad e introducimos en el diccionario el nombre = cantidad
    cantidad = int(input(f"Introduzca la cantidad de {nombre} que quieras añadir: "))
    productos[nombre] = cantidad

print("\nLista de productos y sus cantidades:")
#utilizamos un bucle for recorriendo los productos del diccionario mostrandolos
for nombre, cantidad in productos.items():
    print(f" - {nombre}: {cantidad}")


