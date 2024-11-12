#Para recorrer un diccionario podemos utilizar bucles. Hay tres métodos muy útiles:
#.items(): Devuelve clave-valor como tuplas.
#.keys(): Devuelve sólo las claves.
#.values(): Devuelve solo los valores.

diccionario = {
    "clave1": "valor1",
    "clave2": "valor2"
}
edades = {
    "Ana": 25,
    "Juan": 30,
    "Luis": 22
}

#////////////////////////////////////////////////////////////////////////////////////////
#ITEMS
for nombre, edad in edades.items():
    print(nombre, "tiene", edad, "años")

#Aquí, nombre toma cada clave y edad toma el valor asociado en cada iteración.

#////////////////////////////////////////////////////////////////////////////////////////
#KEYS
for nombre in edades.keys():
    print("Nombre:", nombre)

#Este método es útil si solo queremos ver las claves sin los valores.

#////////////////////////////////////////////////////////////////////////////////////////
#VALUES
for edad in edades.values():
    print("Edad:", edad)

#Este método es útil si solo queremos trabajar con los valores y no necesitamos las claves.