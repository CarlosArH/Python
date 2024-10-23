import math
angulo = float(input("introduzca el coeficiente de pi según el ángulo escogido:"))
radianes = math.pi * angulo
print("1.seno")
print("2.coseno")
print("3.tangente")
print("4.cosecante")
print("5.secante")
print("6.cotangente")
print("0.exit")
función = int(input("Elige una opción:"))
if función == 1:
    seno = math.sin(radianes)
    print(seno)
if función == 2:
    coseno = math.cos(radianes)
    print(coseno)
if función == 3:
    tangente = math.tan(radianes)
    print(tangente)
if función == 4:
    cosecante = 1 / seno
    print(cosecante)
if función == 5:
    secante = 1 / coseno
    print(secante)
if función == 6:
    cotangete = 1 / tangente
    print(cotangete)
if función == 0:
    exit()