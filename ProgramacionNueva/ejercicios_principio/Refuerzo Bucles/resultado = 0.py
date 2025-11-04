resultado = 0
while True:

    print("Calculadora")

    print("\n1. Sumar 2. Restar 3. Multiplicar 4. Dividir 5. Salir")

    opcion = int(input("Introduzca el numero de la operacion que quieras realizar"))

    if opcion == 5:
        print("Has salido de la calculadora")
    break
 

num1 = float(input("Introduzca el primer numero: "))
num2 = float(input("Introduzca el primer numero: "))

match opcion:
    case 1:
        resultado = num1 + num2
        print(f"El resultado de {num1} + {num2} = {resultado}")

    case 2:
        resultado = num1 - num2
        print(f"El resultado de {num1} - {num2} = {resultado}")

    case 3:
        resultado = num1 * num2
        print(f"El resultado de {num1} * {num2} = {resultado}")

    case 4:
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} = {resultado}")

    case _:
        print("Operacion no valida, vuelve a elegir")