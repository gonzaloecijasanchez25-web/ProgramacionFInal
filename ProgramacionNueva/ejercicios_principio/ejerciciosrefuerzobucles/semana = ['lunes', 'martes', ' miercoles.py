# inicializamos variables y creamos la lista
semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
contador_S = 0
contador_N = 0
porcentaje = 0

# recorremos la lista y pedimos datos al usuario
for dias in semana:
    asistencia = input(f"Has venido a clase el {dias} (pon S o N): ")  

    if asistencia == "S":
            contador_S += 1

    elif asistencia == "N":
            contador_N +=1
           
    else:
        print("Respuesta no valida, por favor pon S o N")
        asistencia = input(f"Has venido a clase el {dias} (pon S o N): ")

# calculamos el porcentaje y mostramos resultados
porcentaje = (contador_S / len(semana)) * 100
print(f"Has tenido {contador_N} ausencias y {contador_S} dias has venido a clase durante esta semana")
print(f"Tu porcentaje de asistencia ha sido {porcentaje} %")