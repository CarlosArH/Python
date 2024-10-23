try:
    ingresos = float(input("Ingresos mensuales de la unidad familiar:"))
except: print("el valor introducido no se puede utilizar como ingreso")
else:
    if ingresos < 0:
        print("el valor introducido no se puede utilizar como ingreso")
    elif 0 <= ingresos < 1800:
        print("4 puntos")
    elif 1800 <= ingresos < 3500:
        print("3 puntos")
    elif 3500 <= ingresos < 5000:
        print("2 puntos")
    else:
        print("1 punto")