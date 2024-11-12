#pop(clave): Elimina un elemento específico y devuelve su valor. Se puede proporcionar un valor predeterminado si la clave no existe.
#clear(): Vacía el diccionario por completo, dejándolo sin elementos.
#del clave: Elimina un elemento específico del diccionario. No devuelve valor.

edades = {
    "Ana": 25,
    "Juan": 30,
    "Luis": 22
}


#/////////////////////////////////////////////////////////////////////////////////////////////
#POP
# Eliminar el elemento con la clave "Juan"
edad_juan = edades.pop("Juan")
print("Edad de Juan eliminada:", edad_juan)
print("Diccionario después de pop:", edades)

#Si intentas hacer edades.pop("Carlos"), que no está en el diccionario, obtendrás un error. Si usas un valor por defecto, como en edades.pop("Carlos", "No encontrado"), devolverá "No encontrado" en lugar de un error.


#/////////////////////////////////////////////////////////////////////////////////////////////
#CLEAR
#vacía completamente el diccionario, pero sin eliminar el diccionario mismo.
# Vaciar el diccionario
edades.clear()
print("Diccionario después de clear:", edades)


#/////////////////////////////////////////////////////////////////////////////////////////////
#DEL
# Eliminar el elemento con la clave "Luis"
del edades["Luis"]
print("Diccionario después de del:", edades)
#A diferencia de pop, no devuelve el valor eliminado.

# Eliminar todo el diccionario
del edades
# Intentar acceder al diccionario después de eliminarlo causará un error
# print(edades)  # Esto dará un error porque el diccionario ya no existe




