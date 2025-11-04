juegos = {
    "ea fc 25": (79.99, "Deportes"), 
    "minecraft": (19.99, "Aventura"),
    "rainbow six": (7.99, "Shooter"),
    "battlefield 6": (69.99, "Shooter"),
    "zelda breath of the wild": (59.99, "Aventura")
}

opcion = 0

while opcion != 5:
    print("\n------ MENÚ DE JUEGOS ------")
    print("1. Mostrar catálogo")
    print("2. Buscar juego por nombre")
    print("3. Añadir nuevo juego")
    print("4. Calcular precio medio")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))

    match opcion:
        case 1:
            print("\n--- CATÁLOGO DE JUEGOS ---")
            for nombre, datos in juegos.items():
                precio, genero = datos
                print(f"Nombre: {nombre}")
                print(f"Precio: {precio}€")
                print(f"Género: {genero}")
                print("--------------------------")

        case 2:
            nombre = input("Introduce el nombre del juego: ").lower()
            if nombre in juegos:
                precio, genero = juegos[nombre]
                print(f"\nNombre: {nombre}")
                print(f"Precio: {precio}€")
                print(f"Género: {genero}")
            else:
                print("\nEse juego no está en el catálogo.")

        case 3:
            nombre = input("Nombre del nuevo juego: ").lower()
            if nombre in juegos:
                print("\nEse juego ya existe en el catálogo.")
            else:
                precio = float(input("Precio: "))
                genero = input("Género: ")
                juegos[nombre] = (precio, genero)
                print("\nJuego añadido correctamente.")

        case 4:
            total = 0
            for precio, genero in juegos.values():
                total += precio
                media = total / len(juegos)
                print(f"\nEl precio medio de los juegos es: {media:.2f}€")


        case 5:
            print("\nSaliendo del programa...")

        case _:
            print("\nOpción no válida. Intenta de nuevo.")
