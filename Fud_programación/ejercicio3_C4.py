def divisor_de_listas(lista_original):
    lista_pares_1 = []
    lista_impares_1=[]
    for i in (lista_original):
        if i % 2 == 0:
            lista_pares_1.append(i)
        else:
            lista_impares_1.append(i)

    return (lista_pares_1) , (lista_impares_1)
print(divisor_de_listas([1,2,3,4,5,6,7,8,9,15,30,41]))