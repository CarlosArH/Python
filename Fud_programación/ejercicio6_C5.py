import random
def lista_final(lista):
    seg_pos = lista[0]
    for pos in range(len(lista)-1):
        lista[pos]-=lista[pos+1]
    lista[(len(lista)-1)]-=seg_pos
    return lista
lista = []
for i in range(10):
    lista += [random.randint(-50,100)]
print(lista)       
print(lista_final(lista))
