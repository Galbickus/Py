#MENÚ PPAL

productos=[] # lista de productos que vamos cargando

while True:
    #ENTRADA: MENÚ DE OPCIONES.
    print("Menú para la Gestión de Productos:\n")
    print("1. Registro: Alta de productos nuevos.")
    print("2. Visualización: Consulta de datos de productos.")
    print("3. Actualización: Modificar la cantidad en stock de un producto.")
    print("4. Eliminación: Dar de baja productos.")
    print("5. Listado: Listado completo de los productos e la base de datos.")
    print("6. Reporte de Bajo Stock: Lista de productos con cantidad bajo mínimo.")
    print("7. Salir.")

    try:
        #PROCESO: SOLICITUD DE OPCIÓN.
        opcion = int(input("Seleccione una opcion entre 1 y 7: "))
        if opcion == 1:
            print("Usted ha seleccionado la opción N°1: Registro")
        elif opcion ==2:
            print("Usted ha seleccionado la opción N°2: ")
        elif opcion ==3:
            print("Usted ha seleccionado la opción N°3: ")
        elif opcion ==4:
            print("Usted ha seleccionado la opción N°4: ")
        elif opcion ==5:
            print("Usted ha seleccionado la opción N°5: ")
        elif opcion ==6:
            print("Usted ha seleccionado la opción N°6: ")
        elif opcion ==7:
            print("Usted ha seleccionado la opción N°7: ")
            break
        else:
            print("Opción inválida, ingrese un número del (1 al 7) ")
    except ValueError:
        print("Entrada inválida. Ingrese un número de 1 a 7")
            
        