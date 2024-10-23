def división(numero1, numero2):
    if numero1 < 0 and numero2 > 0 or numero1 > 0 and numero2 < 0:
        if numero2 < 0:
            numero2, numero1 = numero1, numero2
        numero1 = -numero1
        if numero1 == 0 or numero2 == 0:
            return 0
        elif numero1 == 1 or numero2 == 1:
            return -numero1
        else:
            numero1 = numero1 - división(numero1, numero2 -1)
            return -numero1
    elif numero1 > 0 and numero2 > 0 or numero1 < 0 and numero2 < 0:
        if numero1 < 0 and numero2 < 0:
            numero2 = -numero2
            numero1 = -numero1
        if numero1 == 0 or numero2 == 0:
            return 0
        elif numero1 == 1 or numero2 == 1:
            return numero1
        else:
            numero1 = numero1 - división(numero1, numero2 -1)
            return numero1
print(división(10,2))