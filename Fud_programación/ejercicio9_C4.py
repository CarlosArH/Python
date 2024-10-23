def vocales_palabra(palabra):
    vocales = ["a", "e", "i", "o", "u"]
    vocales_in = []
    caracter = 0
    todas_vocales = True
    n_vocales = 0
    for caracter in range(len(palabra)):
        x = palabra[caracter]
        if x in vocales:
            if x in vocales_in:
                n_vocales += 0
            else:
                n_vocales += 1  
                vocales_in.append(x)
    if n_vocales < 5:
        todas_vocales = False
    else:
        todas_vocales = True
    return todas_vocales
palabra = str(input("Introduce una palabra:"))
print(vocales_palabra(palabra))