#MENU PRINCIPAL
#////////////////////////////////////////////////////////////////////////////////////
#ENTRADA: MENÚ DE OPCIONES.
print("Menú para la Gestión de Productos:\n")
print("1. Registro: Alta de productos nuevos.")
print("2. Visualización: Consulta de datos de productos.")
print("3. Actualización: Modificar la cantidad en stock de un producto.")
print("4. Eliminación: Dar de baja productos.")
print("5. Listado: Listado completo de los productos e la base de datos.")
print("6. Reporte de Bajo Stock: Lista de productos con cantidad bajo mínimo.")
print("7. Salir.")

print("\n")#SALTO DE LINEA

#PROCESO: SOLICITUD DE OPCIÓN.
opcion = int(input("Seleccione una opcion entre 1 y 7: "))

#SALIDA: NRO DE OPCIÓN SOLICITADA.

print("Ud ha seleccionado la opción Nro: " , opcion)

print("\n")#SALTO DE LINEA

#////////////////////////////////////////////////////////////////////////////////////

#PRECIO TOTAL CON IVA
print("PRECIO TOTAL CON IVA: \n")
#ENTRADA: Solicitud de Precio del Producto con el Porcentaje del IVA.
nombre_producto_iva = str(input("Ingrese el nombre del producto: "))
precio_producto_iva = float(input("Ingrese el precio del producto: "))
porcentaje_iva =  float(input("Ingrese el porcentaje del IVA (por ejemplo 21 para el 21%): "))

#PROCESO: Calcular el monto del IVA con el Precio Final.
monto_iva = (precio_producto_iva * porcentaje_iva) /100
precio_total_iva = precio_producto_iva + monto_iva

print("\n")#SALTO DE LINEA

#SALIDA: Mostrar en pantalla el precio total incluyendo el IVA.
print("El precio total del producto con el IVA es de: $" , precio_total_iva)

#////////////////////////////////////////////////////////////////////////////////////

#CÁLCULO DE DESCUENTO
print("PRECIO TOTAL CON DESCUENTO: \n")
#ENTRADA: Solicitud del Precio del Producto y el Porcentaje del Descuento.
nombre_producto_desc = str(input("Ingrese el nombre del producto: "))
precio_producto_desc = float(input("Ingrese el precio del producto: "))
porcentaje_desc =  int(input("Ingrese el porcentaje del descuento (por ejemplo, 5 para el 5%): "))

#PROCESO: Calcular el Descuento y el Precio Final.
monto_desc= (precio_producto_desc * porcentaje_desc) /100
precio_total_desc = precio_producto_desc - monto_desc

print("\n")#SALTO DE LINEA

#SALIDA: Mostrar el Precio Final del Producto con el Descuento Aplicado.
print("El precio total del producto con el descuento queda en: $" , precio_total_desc)

#////////////////////////////////////////////////////////////////////////////////////

#COMPRA DE VARIOS ARTÍCULOS
print("COMPRA DE VARIOS ARTÍCULOS: \n")
#ENTRADA: Solicitud del Precio Unitario del Producto y la Cantidad que lleva.
nombre_producto_unidad = str(input("Ingrese el nombre del producto: "))
precio_unitario = float(input("Ingrese el precio unitario del producto: $"))
cantidad_producto = int(input("Ingrese la cantidad de productos que lleva: "))
 
#PROCESO: Calcular Costo Total del Producto con la Cantidad de Unidades que lleva.
precio_total_productos = precio_unitario * cantidad_producto

print("\n")#SALTO DE LINEA

#SALIDA: MOSTRAR EL MONTO TOTAL DE LA COMPRA
print("El precio total de los productos es de: $" , precio_total_productos)