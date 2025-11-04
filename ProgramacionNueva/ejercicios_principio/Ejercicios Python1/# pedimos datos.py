# pedimos datos

numero1 =float(input("Introduce el primer numero de la operacion: "))
numero2 = float(input("Introduce el segundo numero de la operacion: "))
operacion = (input("Que operacion harás: + - x / "))

# realizamos operacion

if operacion == "+":
    resultado = numero1 + numero2   
    print("El resultado de la suma es: ", resultado)

elif operacion == "-":
    resultado = numero1 - numero2   
    print("El resultado de la resta es: ", resultado)   

elif operacion == "x":
    resultado = numero1 * numero2   
    print("El resultado de la multiplicacion es: ", resultado)

elif operacion == "/":
    if numero2 == 0:
        print("No se puede dividir entre 0")
    else:
        resultado = numero1 / numero2   
        print("El resultado de la division es: ", resultado)

        