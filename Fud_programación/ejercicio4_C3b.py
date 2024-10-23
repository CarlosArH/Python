total = 0
positivos = 0
negativos = 0
while True:
    try:
        numero = int(input("Introduzca un número(si quiere salir del programa introduzca el -9999):"))
    except: print("El numero no es un entero")
    else:
        if numero == -9999:
            print("Adios")
            break
        elif numero > 0:
            total += 1
            positivos += 1
        elif numero < 0:
            total += 1
            negativos += 1
        elif numero == 0:
            total += 1
        else:
            continue
print("numeros totales:", total)
print("numeros positivos:", positivos)
print("numeros negativos:", negativos)

