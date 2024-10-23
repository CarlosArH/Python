try:
    compra = float(input("introduzca el importe:"))
except: print("El valor que has dado no es válido")
else:
    if compra >= 100:
        a = float(input("contado(pon 1), tarjeta(pon 0):"))
        if a == 1:
            b = compra * 0.95
            print("El total de su compra es de:" , b)
        elif a == 0:
            c = compra * 0.98
            print("El total de su compra es de:" , c)
    else:
        print("este importe no tiene descuento")