def sumador_listas(lista_1 , lista_2):
    lista_resultado = []
    for i in range(len(lista_1)):
        suma = lista_1[i] + lista_2[i]
        lista_resultado.append(suma)
    return lista_resultado
print(sumador_listas([1,3,-2,4],[3,-5,2,7]))