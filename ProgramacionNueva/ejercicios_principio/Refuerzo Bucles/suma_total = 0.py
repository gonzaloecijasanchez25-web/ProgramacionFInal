#inicializamos las variables que vamos a usar
suma_total = 0
contador_p = 0
numero = 0
positivostotal = []

while True:
    numero = int(input("Introduce un numero positivo (o 0 para acabar): "))
    if numero == "0":
        break
#cuando numero es positivo, lo añadimos a la lista y ademas lo sumamos a sumatotal
    if numero > 0:
        suma_total += numero
        positivostotal.append(numero)

    elif numero < 0:
        print("Los numeros deben de ser positivos, vuelve a probar")

#una vez pulsamos 0, mostramos la suma total y el numero de positivos que hay, (los que se encuentran dentro de la lista en la que ibamos añadiendo si eran positivos)      
    if numero == 0:
            print(f"La suma total da: {suma_total}")
            print(f"El numero total de positivos es: {len(positivostotal)}")
            break