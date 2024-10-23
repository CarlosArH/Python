def contador_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contador_digitos(numero//10)
print(contador_digitos(15075654544657))