notas = {
    "Programación": [],
    "Sistemas": [],
    "Bases de datos": []
}

seguir = 0

while seguir == 0:
    print("\n--- MENÚ DE GESTIÓN DE NOTAS ---")
    print("1. Añadir nota a una asignatura")
    print("2. Ver notas de una asignatura")
    print("3. Calcular media por asignatura")
    print("4. Media general")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            asignatura = input("Introduce la asignatura: ")
            if asignatura in notas:
                nota = float(input("Introduce la nota: "))
                notas[asignatura].append(nota)
                print(f"Nota añadida a {asignatura}.")
            else:
                print("Asignatura no válida.")

        case "2":
            asignatura = input("Introduce la asignatura: ")
            if asignatura in notas:
                print(f"Notas de {asignatura}: {notas[asignatura]}")
            else:
                print("Asignatura no válida.")

        case "3":
            asignatura = input("Introduce la asignatura: ")
            if asignatura in notas:
                if len(notas[asignatura]) > 0:
                    total = 0
                    for nota in notas[asignatura]:
                        total += nota
                    media = total / len(notas[asignatura])
                    print(f"Media de {asignatura}: {media}")
                else:
                    print(f"No hay notas registradas en {asignatura}.")
            else:
                print("Asignatura no válida.")

        case "4":
            total_notas = 0
            contador = 0
            for asignatura in notas:
                for nota in notas[asignatura]:
                    total_notas += nota
                    contador += 1
            if contador > 0:
                media_general = total_notas / contador
                print(f"Media general de todas las asignaturas: {media_general:.2f}")
            else:
                print("No hay notas registradas aún.")

        case "5":
            print("Saliendo del programa...")
            seguir = 1

        case _:
            print("Opción no válida. Intenta de nuevo.")
