productos = { "bolígrafo": {"precio": 1.2, "stock": 10}, "cuaderno": {"precio": 3.5, "stock": 5}, "carpeta": {"precio": 2.8, "stock": 8}}
producto_pedir = 0
carrito = []
opcion = 0
seguir = 0

while seguir ==  0:
    print("\n PAPELERIA")
    print("1. Mostrar productos")
    print("2. Añadir productos al carrito")
    print("3. Ver totald de la compra")
    print("4. Salir")
    opcion = int(input("Introduzca la opcion que desees:"))
    
    match opcion:
        case 1:
            print("\nProductos disponibles")
            for nombre, info in productos.items():
                print(f"{nombre} - {info['precio']}€ - (Stock: {info['stock']})")


        case 2:
            producto_pedir = input("Que producto deseas añadir al carrito?: ")
            if producto_pedir in productos:
                if productos[producto_pedir]["stock"] > 0:
                    carrito.append(producto_pedir) 
                    productos[producto_pedir]["stock"] -= 1
                    print(f"{producto_pedir} fue añadido al carrito")

                else:
                    print("No tenemos en stock el producto que quiere")

            else:
                print("Producto no encontrado")

        case 3:
            if not carrito:
                print("El carrito está vacío.")
            else:
                total = sum(productos[i]["precio"] for i in carrito)
                print("\nProductos en el carrito:")
                for i in carrito:
                    print(f"- {i} ({productos[i]['precio']}€)")
                print(f"Total: {total}€")
        
        case 4:
            print("Saliendo del menu...")
            seguir += 1
