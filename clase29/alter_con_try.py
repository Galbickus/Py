productos = []  # Lista de productos que vamos cargando

while True:
    # ENTRADA: MENÚ DE OPCIONES.
    print("\nMenú para la Gestión de Productos:\n")
    print("1. Registro: Alta de productos nuevos.")
    print("2. Visualización: Consulta de datos de productos.")
    print("7. Salir.")
    
    opcion = input("Seleccione una opción entre 1 y 7: ").strip()  #el strip() me dijo un compañero que iba pero en este caso es igual

    if opcion == "1":
        print("Usted ha seleccionado la opción N°1: Registro")
        while True:
            # Validación del nombre del producto
            nombre = input("Nombre del producto: ").strip().upper()
            if not nombre:
                print("El nombre no puede estar vacío. Intente nuevamente.")
                continue
            # Petición y validación del precio del producto
            while True:
                try:
                    precio = float(input("Precio del producto: "))
                    if precio <= 0:
                        print("Por favor, ingrese un valor mayor a 0.")
                    else:
                        break
                except ValueError:
                    print("Ingrese un valor numérico válido para el precio.")
            
            # Petición y validación del stock del producto
            while True:
                try:
                    stock = int(input("Cantidad en stock del producto: "))
                    if stock < 0:
                        print("El stock debe ser 0 o mayor.")
                    else:
                        break
                except ValueError:
                    print("Ingrese un número entero válido para el stock.")

            # Guardar producto en la lista
            producto = {'nombre': nombre, 'precio': precio, 'stock': stock}
            productos.append(producto)
            print("Producto cargado exitosamente.")

            # Preguntar si desea agregar más productos
            agregar_mas = input("¿Desea agregar más productos? (S/N): ").strip().upper()
            if agregar_mas != "S":
                break  # Salir del ciclo de registro y volver al menú principal

    elif opcion == "2":
        print("Usted ha seleccionado la opción N°2: Visualización")
        if productos:
            print("Lista de productos registrados:")
            for producto in productos:
                print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")
        else:
            print("No hay productos registrados aún.")

    elif opcion == "7":
        print("Usted ha seleccionado la opción N°7: Salir")
        break

    else:
        print("Opción inválida. Por favor, ingrese un número válido (1, 2 o 7).")

#SALIDA: NRO DE OPCIÓN SOLICITADA.
#////////////////////////////////////////////////////////////////////////////////////