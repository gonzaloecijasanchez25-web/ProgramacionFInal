votos_Ana = 0
votos_Luis = 0
votos_Maria = 0



while True:
    print("A quien de los 3 candidatos vas a votar: Ana, Luis o Maria")
    voto = input("Introduzca a quien vas a votar (o fin si ya han votado todos: )")

    if voto == "fin":
        print(f"Los resultados son los siguientes: Ana = {votos_Ana}, Luis = {votos_Luis}, Maria = {votos_Maria}")
        break

    match voto:
        case "Ana":
            votos_Ana += 1

        case "Luis":
            votos_Luis += 1

        case "Maria":
            votos_Maria += 1
