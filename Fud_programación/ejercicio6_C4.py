def es_palindromo(palabra):
    letra_inicio = 0
    letra_final = len(palabra)-1
    palindromo = True
    while palindromo and letra_inicio < letra_final:
        if palabra[letra_inicio] != palabra[letra_final]:
            palindromo = False
        else:
            letra_final += -1
            letra_inicio += 1
    return palindromo
cadena = input("intreoduce la palabra:")
print(es_palindromo(cadena))

