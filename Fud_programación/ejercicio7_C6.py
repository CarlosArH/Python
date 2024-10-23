def sumador_listas(lista):
    ini = 0
    fin = len(lista)-1
    if len(lista) % 2 == 1:
        if len(lista) != 1:
            print(lista[ini]+lista[fin])
            return sumador_listas(lista[1:len(lista)-1])
        else:
            print(lista[0])
    else:
        print(lista[ini]+lista[fin])
        return sumador_listas(lista[1:len(lista)-2])
    return ""
print(sumador_listas([1,2,3,4,7,8,9]))


