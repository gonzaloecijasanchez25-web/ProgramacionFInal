contraseña1 = "hola12345"

while True:
    contraseña2 = input("Introduce la contraseña: ")
    if contraseña2 == contraseña1:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta, inténtalo de nuevo.")
