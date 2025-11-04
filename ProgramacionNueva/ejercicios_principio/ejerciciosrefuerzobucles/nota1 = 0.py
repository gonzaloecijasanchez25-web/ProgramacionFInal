#inicamos todsa las variables que vamos a usar
nota1 = 0
nota2 = 0
nota3 = 0
media = 0
contador_a = 0
contador_b = 0

nombre = input("Introduzca su nombre: ")

while True:
    nota1 = input("Introduzca su primera nota (o 'fin' para acabar): ")
    if nota1 == "fin":
        break
#no usamos el float en el input, porque vamos a necesitar que funcione si ponemos fin, por eso ahora lo pasamos a float en caso de que no sea fin
    nota1 = float(nota1)
    nota2 = float(input("Introduzca su segunda nota: "))
    nota3 = float(input("Introduzca su tercera nota: "))

#comprobamos que las notas sean reales, calculamos sus medias y en caso de que sean aporbado o suspenso sumar a los contadores
    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
        media = (nota1 + nota2 + nota3) / 3

        if media >= 5:
            print(f"Tu media es {media}. Aprobado, enhorabuena!")
            contador_a += 1
        else:
            print(f"Tu media es {media}. Suspenso, la próxima será.")
            contador_b += 1
    else:
        print("Error: las notas deben estar entre 0 y 10")

print(f"\nHas tenido {contador_a} medias aprobadas y {contador_b} medias suspensas.")