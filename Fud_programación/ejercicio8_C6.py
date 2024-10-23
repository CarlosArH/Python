def sumador(numero):
    if numero <= 0:
        return 0
    if numero % 2 == 1:
        return sumador(numero-1)
    else:
        return numero + sumador(numero-1)
print(sumador(998))