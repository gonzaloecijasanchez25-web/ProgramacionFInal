#Ejercicio 1: Filtrar productos perecederos
productos = [
    {"nombre": "Manzanas", "perecedero": True},
    {"nombre": "Arroz", "perecedero": False},
    {"nombre": "Leche", "perecedero": True},
    {"nombre": "Pasta", "perecedero": False},
    {"nombre": "Zanahorias", "perecedero": True}
]

def es_perecedero(producto):
    return producto["perecedero"]

perecederos = list(filter(es_perecedero, productos))

for producto in perecederos:
    print(producto["nombre"])
