try:
    kilometros = float(input("¿cuantos kilómetros ha hecho el coche?:"))
except: print("el dato aportado no se puede utilizar")
else:
    if 0 < kilometros <= 300:
        print("son 100 euros")
    elif 300 < kilometros <=1000:
        km_restantes1 = kilometros - 300
        factura1 = 100 + (0.3 * km_restantes1)
        print("son" , factura1 , "euros")
    elif kilometros > 1000:
        km_restantes2 = kilometros -1000
        factura2 = 100 + (0.3 * 700) + (0.2 * km_restantes2)
        print("son" , factura2 , "euros")
    else:
        print("el dato aportado no se puede utilizar")

