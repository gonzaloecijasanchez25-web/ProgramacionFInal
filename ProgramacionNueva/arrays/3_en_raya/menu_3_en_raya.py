from funciones_3_en_raya import *

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

juego()
