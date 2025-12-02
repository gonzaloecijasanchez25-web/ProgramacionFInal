import numpy as np
import random

def crear_tablero():
    return np.zeros((3,3), dtype=int)

def mostrar_tablero(tablero):
    s = {0:" ",1:"X",2:"O"}
    print("\n 0 1 2")
    for i,fila in enumerate(tablero):
        print(f"{i} " + " ".join(s[x] for x in fila))

def turno_jugador(tablero,j):
    while True:
        f = int(input(f"Jugador {j} - fila: "))
        c = int(input(f"Jugador {j} - columna: "))
        if 0<=f<3 and 0<=c<3:
            if tablero[f,c]==0:
                tablero[f,c]=j
                return tablero
            else:
                print("Casilla ocupada")
        else:
            print("Fuera de rango")

def turno_cpu(tablero):
    vacias = [(i,j) for i in range(3) for j in range(3) if tablero[i,j]==0]
    if vacias:
        f,c = random.choice(vacias)
        tablero[f,c]=2
    return tablero

def comprobar_victoria(tablero,j):
    for i in range(3):
        if all(tablero[i,:]==j) or all(tablero[:,i]==j):
            return True
    if all(np.diag(tablero)==j) or all(np.diag(np.fliplr(tablero))==j):
        return True
    return False

def comprobar_empate(tablero):
    return np.all(tablero!=0)

def juego():
    print("Tres en Raya")
    modo = input("Modo 1=PvP 2=PvCPU: ")
    t = crear_tablero()
    turno = 1
    while True:
        mostrar_tablero(t)
        if modo=="1" or (modo=="2" and turno==1):
            t = turno_jugador(t,turno)
        else:
            t = turno_cpu(t)
        if comprobar_victoria(t,turno):
            mostrar_tablero(t)
            print(f"¡Jugador {turno} gana!")
            break
        if comprobar_empate(t):
            mostrar_tablero(t)
            print("Empate")
            break
        turno = 2 if turno==1 else 1

if __name__=="__main__":
    juego()
