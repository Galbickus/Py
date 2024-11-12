#¿Qué es un diccionario?
#Un diccionario es como una lista, pero en lugar de usar índices (como 0, 1, 2) para acceder a los elementos, usamos claves que nosotros mismos definimos. Cada elemento tiene una clave y un valor, como esto:

diccionario = {
    "clave1": "valor1",
    "clave2": "valor2"
}

edades = {
    "Ana": 25,
    "Juan": 30,
    "Luis": 22
}

#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#Acceder a los valores de un diccionario
#Para obtener el valor asociado a una clave específica, usamos el nombre del diccionario y la clave entre corchetes [].

print(edades["Ana"])  # Esto imprimirá: 25
print(edades["Juan"]) # Esto imprimirá: 30

#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#Agregar y modificar valores
edades["Carlos"] = 28  # Agrega una nueva clave "Carlos" con valor 28
print(edades)  # Muestra: {'Ana': 25, 'Juan': 30, 'Luis': 22, 'Carlos': 28}

edades["Ana"] = 26  # Modifica el valor de la clave "Ana" a 26
print(edades)  # Muestra: {'Ana': 26, 'Juan': 30, 'Luis': 22, 'Carlos': 28}

#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#Eliminar elementos
del edades["Luis"]
print(edades)  # Muestra: {'Ana': 26, 'Juan': 30, 'Carlos': 28}

#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#Recorrer un diccionario
for nombre in edades:
    print(nombre, "tiene", edades[nombre], "años")
    