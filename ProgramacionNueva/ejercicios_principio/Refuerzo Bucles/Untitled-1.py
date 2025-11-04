votos = {"Ana": 0, "Luis": 0, "Maria": 0}

while True:
    voto = input("Introduce el nombre del candidato (Ana, Luis, Maria) o 'fin' para terminar: ").capitalize()

    if voto == "Fin":
        break
    elif voto in votos:
        votos[voto] += 1
    else:
        print("Voto no válido. Intenta de nuevo.")

print("\nResultados de la votación:")
for candidato, cantidad in votos.items():
    print(f"{candidato}: {cantidad} votos")

# Sacar el ganador
max_votos = max(votos.values())
ganadores = [candidato for candidato, cantidad in votos.items() if cantidad == max_votos]

if len(ganadores) == 1:
    print(f"\nEl ganador es {ganadores[0]} con {max_votos} votos.")
else:
    print(f"\nHay un empate entre: {', '.join(ganadores)} con {max_votos} votos cada uno.")
