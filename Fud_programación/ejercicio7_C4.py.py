
def titulo(cadena):
    """ str -> str
    OBJ: Pone en mayúsculas la primera letra de cada palabra """
    res = ''
    anterior = ' '
    for caracter in cadena:
        if anterior == ' ' and caracter != ' ':
            res += caracter.upper()
        else:
            res += caracter
        anterior = caracter
    return res

print(titulo('   hola   '))
print(titulo('frase de    cuatro palabras'))
