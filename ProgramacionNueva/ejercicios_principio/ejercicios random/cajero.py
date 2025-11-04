saldo = 100

menu = "1. Consultar saldo\n2. Ingresar dinero\n3. Retirar dinero\n4. Salir"
print(menu)

while True:
    opcion = int(input("Introduce la opcion que desees: "))
    ingreso = 0
    retirada = 0
    dinerototal = 0
    if opcion == 4:
        print("Hasta pronto")
        break

    match opcion:
        case 1:
            print(f"Tu saldo es: {saldo}")
        case 2:
            ingreso = float(input("Introduce la cantidad de dinero que quieras ingresar: "))              
            if ingreso > 0:
                saldo += ingreso
                print(f"Has ingresado {ingreso}€. Tu saldo actual es: {saldo}€")
            else:
                print("Cantidad no valida")
        case 3:
            retirada = float(input("Introduce la cantidad de dinero que quieres retirar: "))
            if 0 < retirada <= saldo :
                saldo -= retirada
                print(f"Has retirado {retirada}€. Tu saldo actual es: {saldo}")
            else:
                print("Cantidad no valida")

