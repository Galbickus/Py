#1° INICIAMOS UNA FUNCIÓN - Estructura básica:

def nombre_funcion(parametros_opcionales):
    #LINEAS / BLOQUES DE CÓDIGO.
    return resultado_opcional

#Ejemplo N°1: Función sin parámetros ni retorno
def saludo():
    print("Hola bienvenidos a Python")
#llamado a la función "saludo"
saludo()

#Ejemplo N°2: Función con parámetros
def saludar_persona(nombre):
    print(f"Hola {nombre.lower()} bienvenido a Python")

saludar_persona("SERGIO")

#Ejemplo N°3: Función con retorno

def dividir_por_dos(numero):
    return numero // 2

resultado= dividir_por_dos(10)
print(f"La division es de: {resultado}")

#Ejemplo N°4: Función con múltiples parámetros

def suma(numero, numero2, numero3):
    return numero + numero2 + numero3

print(suma(2,4,3))

#Ejemplo N°5: Función con valores predeterminados
def saludar_persona2(nombre="sergio"):
    print(f"Hola {nombre} bienvenido a Python")

saludar_persona2("MARIA")
saludar_persona2()

#Ejemplo N°6: Función práctica (calcular promedio)
def calcular_promedio(lista):
    suma= sum(lista)
    cantidad= len(lista)
    return suma / cantidad

notas= [8,6,4,5]
promedio= calcular_promedio(notas)

print(f"El promedio de las notas es de: {promedio:.2f}")

# Resumen de puntos clave:

# 1° Una función se define con def.
# 2° Se pueden usar parámetros para que la función reciba datos.
# 3° El valor retornado con return puede ser reutilizado.
# 4° Las funciones hacen el código más limpio, reutilizable y fácil de entender.