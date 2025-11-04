gastos = {"Lunes": [], "Martes": [], "Miercoles": [], "Jueves": [], "Viernes": []}
gasto_total = 0
mayor_gasto = 0
dia_mayor = ""
seguir = 0
while seguir == 0:

    print("---Menu de gastos---")
    print("1.Añadir gasto a un dia")
    print("2.Mostrar gastos de un dia")
    print("3.Ver gasto total")
    print("4.Dia con mayor gasto")
    print("5.Salir")

    opcion = input("Elige una opcion: ")

    match opcion:
        case "1":
            dia = input("Introduce el dia:")
            if dia in gastos:
                gasto = float(input("Introduce el gasto en euros:"))
                gasto_total += gasto
                gastos[dia].append(gasto)
                print(f"Gasto añadido a {dia}")
            else:
                print("Error, vuelve a introducirlo")
        
        case "2":
            dia = input("Elige el día que quieras ver los gastos:")
            if dia in gastos:
                print(f"Gasto del {dia}: {gastos[dia]}")
            else:
                print("Error, vuelve a introducirlo")

        case "3":
            print(f"Gasto toal de la semana: {gasto_total}")

        #hecho con chatgpt
        case "4":
            for dia in gastos:
                total_dia = sum(gastos[dia])

                if total_dia > mayor_gasto:
                    mayor_gasto = total_dia
                    dia_mayor = dia

            if dia_mayor == "":
                print("No hay gastos registrados aún.")
            else:
                print(f"El día con más gasto es {dia_mayor} con {mayor_gasto} €.")

        case "5":
            print("Saliendo del programa:")
            seguir += 1

        case _:
            print("\nOpción no válida. Intenta de nuevo.")
