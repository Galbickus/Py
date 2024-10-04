#el programa solicite nombre, cantidad y valor unitario de productos
#Solicitud de datos primer producto
producto1= input("Ingrese el nombre del primer producto: ")
cantidad1= int(input("Ingrese la cantidad del producto1: "))
valor_unitario_1=float(input("Ingrese el precio unitario del producto1: "))
#Solicitud de datos segundo producto
producto2= input("Ingrese el nombre del segundo producto: ")
cantidad2= int(input("Ingrese la cantidad del producto2: "))
valor_unitario_2=float(input("Ingrese el precio unitario del producto2: "))
#Solicitud de datos primer producto
producto3= input("Ingrese el nombre del tercer producto: ")
cantidad3= int(input("Ingrese la cantidad del producto3: "))
valor_unitario_3=float(input("Ingrese el precio unitario del producto3: "))

#calculo de totales
#producto#1

total1= cantidad1 * valor_unitario_1
iva1=total1* 0.21
total_con_iva1=iva1 + total1

#producto#2

total2= cantidad2 * valor_unitario_2
iva2=total1* 0.21
total_con_iva2=iva2 + total2

#producto#3

total3= cantidad2 * valor_unitario_3
iva3=total3* 0.21
total_con_iva3=iva1 + total3

#Salida
print("\n ---TICKET DE COMPRA ---\n")

#producto 1
print("---PRODUCTO #1")
print(f"producto : {producto1}")
print(f"cantidad : {cantidad1}")
print(f"Valor Unitario: $ {valor_unitario_1}")
print(f"Total sin IVA: ${total1}" )
print(f"IVA(%21): ${iva1:.2f}")
print(f"Total de Compra con IVA: $ {total_con_iva1:.2f} ")

#producto 2
print("---PRODUCTO #2")
print(f"producto : {producto2}")
print(f"cantidad : {cantidad2}")
print(f"Valor Unitario: $ {valor_unitario_2}")
print(f"Total sin IVA: ${total2}" )
print(f"IVA(%21): ${iva1:.2f}")
print(f"Total de Compra con IVA: $ {total_con_iva2:.2f} ")

#producto 3
print("---PRODUCTO #3")
print(f"producto : {producto3}")
print(f"cantidad : {cantidad3}")
print(f"Valor Unitario: $ {valor_unitario_3}")
print(f"Total sin IVA: ${total3}" )
print(f"IVA(%21): ${iva1:.2f}")
print(f"Total de Compra con IVA: $ {total_con_iva3:.2f} ")

#Proceso:
#CALCULO DE TOTALES
#PRODUCTO1


