def sumador_listas(lista_1 , lista_2):
    lista_corta = lista_1
    lista_larga = lista_2
    if len(lista_1) > len(lista_2):
        lista_corta = lista_2
        lista_larga = lista_1
    lista_resultado=[]
    for j in range(len(lista_corta)):
        suma = lista_larga[j] + lista_corta[j]
        lista_resultado.append(suma)
    for i in range(len(lista_corta), len(lista_larga)):
        suma = lista_larga[i]
        lista_resultado.append(suma)
    return lista_resultado
print(sumador_listas([1,3,-2,4],[3,-5,2,7,6]))