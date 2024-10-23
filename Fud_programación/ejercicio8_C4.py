def son_iguales(frase1, frase2):
    iguales = True
    if len(frase1) != len(frase2):
        iguales = False
    caracter= 0
    while iguales and caracter < len(frase1):
        if frase1[caracter] == frase2[caracter]:
            caracter += 1
        else:
            iguales = False
    return iguales
print(son_iguales("hola", "holo"))