#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#.get() te permite acceder a los valores sin riesgo de errores si la clave no existe.
#Si la clave no está, devuelve un valor por defecto.
edades = {
    "Ana": 25,
    "Juan": 30,
    "Luis": 22
}

print(edades.get("Ana", 0))   # Salida: 25
print(edades.get("Raul", 0))    # Salida: 0