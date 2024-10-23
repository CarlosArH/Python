def encontrar_numero(lista, numero):
    if len(lista) <= 0:
        return "No está en la lista"
    else:
        if lista[0] == numero:
            return "está en la lista"
        else:
            return encontrar_numero(lista[1:], numero)
print(encontrar_numero([1,2,3,4,5,6,7,8,9,0], 10))