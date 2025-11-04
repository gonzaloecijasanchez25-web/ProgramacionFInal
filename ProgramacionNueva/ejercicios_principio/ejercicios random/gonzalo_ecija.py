#Prueba evaluable 1-1t-dam1-getafe
#Gonzalo Ecija 
#Tipo A
#21for nombre, cantidad in productos.items(): print(f" - {nombre}: {cantidad}")

alumnos = {}
orden_registro = []
media_alumno = {}

opcion = 0
nota1 = 0
nota2 = 0
nota3 = 0
media = 0
media_t = 0
media_g = 0
contador_a = 0
contador_b = 0
contador_c = 0
contador_d = 0
porcentaje_a = 0
nomb_pedir = 0
seguir = 0

while seguir == 0:
        print("Menu: 1. Añadir alumno 2. Listar alumnos 3. Media de un alumno 4. Estadísticas del grupo 5. Salir")
        opcion = int(input("Introduzca la opcion que desees: "))
        match opcion:
            case 1:
                nombre = input("Introduzca el nombre del alumno: ")
                if nombre in orden_registro:
                    print("Este nombre ya esta dentro de la lista:")
                
                else:
                    orden_registro.append(nombre)
                    nota1 = float(input("Introduzca su primera nota"))
                    nota2 = float(input("Introduzca su segunda nota"))
                    nota3 = float(input("Introduzca su tercera nota"))
                    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10 and 0 <= nota3 <= 10:
                        media = (nota1 + nota2 + nota3) / 3
                        media_t += media
                        alumnos[nombre] = nota1,nota2,nota3
                        media_alumno[nombre] = media

                        if media >= 5:
                            contador_a += 1
                        else:
                            contador_b += 1

                    else:
                        print("Error, las notas tienen que estar entre 0 y 10.")

            case 2:
                print(f"La lista de alumnos es:{orden_registro}")

            
            case 3:
                nomb_pedir = input("Introduce el nombre del que quieras saber su media: ")
                if nomb_pedir in media_alumno:
                    if media >= 5:
                        print(f"La media de {nombre} es {media}, estas aprobado enhorabuena!!")
                    else:
                        print(f"La media de {nombre} es {media}, estas suspenso la proxima sera")

            case 4:
                media_g = media_t / len(orden_registro)
                porcentaje_a = (contador_a / len(orden_registro)) * 100
                print(f"El numero total de alumnos es: {len(orden_registro)}")
                print(f"La media global es: {media_g}")
                print(f"El porcentaje de aprobados es {porcentaje_a} %")

            case 5:
                print("Saliendo del programa.......")
                seguir += 1