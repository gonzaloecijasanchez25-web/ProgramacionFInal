import numpy as np

def crear_tablero():
    tablero = np.zeros((20, 20))
    return tablero

def colocar_barcos(tablero):
    barcos = [2, 3, 4]
    for tamaño in barcos:
        colocado = False
        while colocado == False:
            fila = np.random.randint(0, 20)
            columna = np.random.randint(0, 20)
            orientacion = np.random.choice(['H', 'V'])
            if orientacion == 'H' and columna + tamaño <= 20:
                if np.all(tablero[fila, columna:columna+tamaño] == 0):
                    tablero[fila, columna:columna+tamaño] = 1
                    colocado = True
            elif orientacion == 'V' and fila + tamaño <= 20:
                if np.all(tablero[fila:fila+tamaño, columna] == 0):
                    tablero[fila:fila+tamaño, columna] = 1
                    colocado = True
    return tablero

#hecho con chatgpt aparecian muy mal los numeros
def mostrar_tablero(tablero_visible):
    print("    ", end="")
    for i in range(20):
        if i < 10:
            print(" " + str(i) + " ", end="")
        else:
            print(str(i) + " ", end="")
    print()
    print("   " + "---" * 20)

    for i in range(20):
        if i < 10:
            print(" " + str(i) + "|", end=" ")
        else:
            print(str(i) + "|", end=" ")
        for j in range(20):
            if tablero_visible[i, j] == 0:
                print("~", end="  ")
            elif tablero_visible[i, j] == -1:
                print("O", end="  ")
            elif tablero_visible[i, j] == 2:
                print("X", end="  ")
        print()

def partida_ganada(tablero):
    return np.count_nonzero(tablero == 1) == 0

def jugar():
    tablero = colocar_barcos(crear_tablero())
    tablero_visible = np.zeros((20, 20))
    print("¡Comienza la partida de Hundir la Flota!")
    contador = 0

    while contador == 0:
        mostrar_tablero(tablero_visible)
        fila = int(input("Introduce la fila (0-19): "))
        columna = int(input("Introduce la columna (0-19): "))

        if fila < 0 or fila > 19 or columna < 0 or columna > 19:
            print("Coordenadas no válidas.\n")
        else:
            if tablero[fila, columna] == 1:
                tablero[fila, columna] = 2
                tablero_visible[fila, columna] = 2
                print("¡Tocado!\n")
            elif tablero[fila, columna] == 0:
                tablero[fila, columna] = -1
                tablero_visible[fila, columna] = -1
                print("Agua.\n")
            else:
                print("Ya habías probado esa posición.\n")

            if partida_ganada(tablero):
                mostrar_tablero(tablero_visible)
                print("¡Has hundido todos los barcos!")
                contador = contador + 1

jugar()
