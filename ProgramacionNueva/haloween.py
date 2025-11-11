import random

monstruos = {
    'vampiro': 3,
    'momia': 2,
    'bruja': 4,
    'esqueleto': 1,
    'fantasma': 5
}

objetos = ['estaca', 'poción mágica', 'hechizo']

def seleccionar_monstruo():
    monstruo = random.choice(list(monstruos.keys()))
    dificultad = monstruos[monstruo]
    return monstruo, dificultad

def calcular_probabilidad(objeto, dificultad):
    efectividad = {
        'estaca': 0.6,
        'poción mágica': 0.7,
        'hechizo': 0.8
    }
    base = efectividad.get(objeto, 0.5)
    probabilidad = base - (dificultad * 0.1)
    return max(probabilidad, 0.1)

def intentar_captura(monstruo, dificultad):
    intentos = 3
    while intentos > 0:
        print(f"\nTienes {intentos} intentos restantes.")
        print(f"Elige un objeto para intentar capturar al {monstruo}: {', '.join(objetos)}")
        objeto = input("Escribe el nombre del objeto: ").lower().strip()
        
        if objeto not in objetos:
            print("Objeto no válido. Intenta de nuevo.")
            continue
        
        prob = calcular_probabilidad(objeto, dificultad)
        if random.random() < prob:
            print(f"Has capturado al {monstruo} con un/a {objeto}.")
            return True
        else:
            print(f"Fallaste al intentar capturar al {monstruo} con un/a {objeto}.")
        
        intentos -= 1

    print(f"El {monstruo} ha escapado.")
    return False

print("Bienvenido a la Caza de Monstruos de Halloween.")

monstruo, dificultad = seleccionar_monstruo()
print(f"\nUn {monstruo} ha aparecido con dificultad {dificultad}.")

capturado = intentar_captura(monstruo, dificultad)

if capturado:
    print("\nHas salvado Halloween.")
else:
    print("\nHas fallado la caza.")
