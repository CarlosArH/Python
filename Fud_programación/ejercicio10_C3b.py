try:
    importe = float(input("¿Cual es el importe?:"))
    cantidad_cliente = float(input("¿Cuanto ha pagado el cliente?:"))
except: print("Error")
cambio = cantidad_cliente - importe
if importe <= 0:
    print("Error")
elif cantidad_cliente <= 0:
    print("Error")
elif cambio < 0:
    print("El cliente te ha dado menos de lo que debería")
elif cambio == 0:
    print("No hay que dar cambio")
else:
    CANTIDADES = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
    for moneda in CANTIDADES:
        num_monedas = int(cambio // moneda)
        cambio = (cambio % moneda)
        if num_monedas > 0:
            if moneda > 5:
                print("Billetes de ", moneda,":", num_monedas )
            else:
                print("Monedas de ", moneda, ":", num_monedas)


