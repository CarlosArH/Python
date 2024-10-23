def codificador(cadena):
    caracter = 0
    for caracter in range(len(cadena)):
        x = cadena[caracter]       
        if x == "a" or x == "A":
            print("4", end = "")
        elif x == "e" or x == "E":
            print("3", end = "")
        elif x == "i" or x == "I":
            print("1", end = "")
        elif x == "o" or x == "O":
            print("0", end = "")
        elif x == "u" or x == "U":
            print("#", end ="")
        else:
            print(x, end = "")
    return ""
print(codificador("Un perro del hortelano"))
