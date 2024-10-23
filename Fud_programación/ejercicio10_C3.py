try:
    año = int(input("introduzca el año:"))
except: print("el año no es válido")
else:
    if año < 1582:
        print("en ese año no se habían establecido los años bisiestos")
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                print("es bisiesto")
            else:
                print("no es bisiesto")
        else:
            print("es bisiesto")
    else:
        print("no es bisiesto")


