codigos=[]
for i in range(1,5):
    codigo=input("Ingrese el codigo a agregar: ")
    codigos.append(codigo)
    
#print(codigos)

for i in range(4):
    print(f"Producto {i + 1}: {codigos[i]}")
