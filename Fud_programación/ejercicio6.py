km = float(input("¿Cuantos kilómetros ha realizado el conductor?:"))
L = float(input("¿Cuantos litros ha utilizado el conductor?:"))
eur_L = float(input("¿Cuanto cuesta el litro de gasoil?:"))
eur_mant = float(input("¿Cuanto ha costado el mantenimiento?:"))
k_l = km / L
coste_T = (eur_L * L) + eur_mant
eur_km = coste_T / km
print("Has recorrido" , k_l , "kilómetros por litro, el coste total del viaje ha sido de" , coste_T , "euros y el coste por kilómetros ha sido de" , eur_km , "euros")        
 