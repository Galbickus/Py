#ENTRADA:Solicitud de datos al usuario
 
consumo_lts_x_100km= float(input("Ingresá el consumo en Lts. cada 100km: "))
precio_x_lt= float(input("Ing costo por Lt. de combustible: "))
distancia_a_recorrer= float(input("Ingresá la distancia a cubrir en Km: "))

#PROCESO: Calculo de litros consumidos e Importe

litros_consumidos=(consumo_lts_x_100km/100)*distancia_a_recorrer
costo_de_viaje= litros_consumidos * precio_x_lt
#SALIDA: Datos de consumo en litros y costo de combustible

print("\n --- DETSLLE DEL VIAJE ---")
print(f"Litros consumidos: {litros_consumidos} Lts.")
print(f"Costo del viaje: ${costo_de_viaje}")