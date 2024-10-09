
#MULTIPLICAMOS TANTO CADENAS COMO NÚMEROS

risa= "ja"
carcajada= risa * 5 #jajajajaja
print('_______________________')
#CONCATENAMOS

nombre= input("Ingrese un nombre:")
saludo= "Hola " + nombre

print(saludo) #Hola nombre
print('_______________________')
var1 = 3 + 5          # 8 (entero)
var2 = "3" + "5"      # 35 (cadena)
#var3 = 3 + "5"        # TypeError
var4 = str(3) + "5"   # 35 (cadena)
var5 = 3 + int("5")   # 8 (entero)
print(var1)
print(var2)
print(var4)
print(var5)
print('_______________________')

#EJEMPLO LEN (LONGITUD DE CARACTERES)
nombre = 'Talento Tech Adultos'
print(len(nombre)) # se imprime 20

print('_______________________')
#ACCESO A LOS CARACTERES CON SUBÍNDICES
cadena = "Aprendemos Python"
print(cadena[0])     # A
print(cadena[5])     # d
print(cadena[-1])    # n
print(cadena[-2])    # o
#SUBÍNDICES NEGATIVOS COMIENZAN DEL FINAL PARA ATRAS