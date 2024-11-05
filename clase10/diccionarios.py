
diccionario= {
    "Clave1": "valor1",
    "Clave2": "valor2",
    "Clave3": "valor3"
}

eddades = {
    "Ana": 26,
    "Andres": 18,
    "Analia": 58
}
#print(eddades)

#para acceder a distintos valores del diccionario

print(eddades["Analia"])
print(eddades["Andres"])
print(eddades["Ana"])

# si quiero agregar y modificar los valores del diccionario

eddades["Ana"]=30
print(eddades["Ana"])

eddades["Joaquin"]=80
print(eddades)

# eliminar

del eddades["Ana"]
print(eddades)

#
for nombre, edad in eddades.items():
    print(f"{nombre} tiene: {edad}")