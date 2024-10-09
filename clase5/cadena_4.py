#Slicing (rebanado) porciones de una cadena

#cadena= "Aprender Python es divertido"
#1 - [0:8] = Subcadena desde el principio hasta el índice 8.
#2 - [:8]  = Subcadena desde el principio hasta el índice 8.
#3 - [8:0] = Subcadena desde el índice 8 hasta el final
#4 - [::2] = Toma caracteres de 2 en 2 desde el inicio hasta el final.

#EJEMPLO 1
frase = "Aprender Python es divertido"
subcadena = frase[0:8]
print("Subcadena desde el inicio hasta el índice 8:", subcadena)

#EJEMPLO 2
frase = "Aprender Python es divertido"
subcadena = frase[:8]
print("Subcadena desde el inicio hasta el índice 8:", subcadena)

#EJEMPLO 3
frase = "Aprender Python es divertido"
subcadena = frase[8:]
print("Subcadena desde el inicio hasta el final:", subcadena)

#EJEMPLO 4
texto = "Talento Tech"
subcadena = texto[::2]
print("Subcadena obtenida:", subcadena)
# Imprime TlnoTc
