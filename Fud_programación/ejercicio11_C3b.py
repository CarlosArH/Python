import math
try:
    angulo = float(input("introduzca el coeficiente de pi según el ángulo en radianes escogido:"))
except:
    print("No es un ángulo")
else:
    radianes = math.pi * angulo
    print("1.seno")
    print("2.coseno")
    print("3.tangente")
    print("4.cosecante")
    print("5.secante")
    print("6.cotangente")
    print("0.exit")
    comando = 1
    while comando != 0:
        try:
            comando = int(input("Elige una opción:"))
        except: print("este carácter no corresponde a ninguna operación")
        else:
            COMANDOS = [1,2,3,4,5,6]
            if comando in COMANDOS:
                if comando == 1:
                    seno = math.sin(radianes)
                    print(seno)
                elif comando == 2:
                    coseno = math.cos(radianes)
                    print(coseno)
                elif comando == 3:
                    try:
                        tangente = math.tan(radianes)
                        print(tangente)
                    except: print("no existe")
                elif comando == 4:
                    seno = math.sin(radianes)
                    try:
                        cosecante = 1 / seno
                        print(cosecante)
                    except: print("no existe")
                elif comando == 5:
                    coseno = math.cos(radianes)
                    try:    
                        secante = 1 / coseno
                        print(secante)
                    except: print("no existe")
                elif comando == 6:
                    try:
                        tangente = math.tan(radianes)
                    except: print("no existe")
                    cotangente = 1 / tangente
                    print(cotangente)
            else:        
                print("Este valor no tiene asignado ninguna operación")
    print("Adios")

