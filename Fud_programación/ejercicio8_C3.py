try:
    mes = int(input("introduzca el número del mes:"))
except:
    print("El dato aportado no es válido")
else:
    if mes == 10:
        print("octubre")
    elif mes == 1:
        print("enero")
    elif mes == 2:
        print("febrero")
    elif mes == 3:
        print("marzo")
    elif mes == 4:
        print("abril")
    elif mes == 5:
        print("mayo")
    elif mes == 6:
        print("junio")
    elif mes == 7:
        print("julio")
    elif mes == 8:
        print("agosto")
    elif mes == 9:
        print("septimbre")
    elif mes == 11:
        print("noviembre")
    elif mes == 12:
        print("diciembre")
    else:
        print("el número aportado no se corresponde con ningún mes")
