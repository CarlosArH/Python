def notas(lista):
    lista_notas = []
    for i in lista:
        i = float(i)
        if 0 <= i < 5:
            nota = "suspenso"
        elif 5 <= i < 6:
            nota = "suficiente"
        elif 6 <= i < 7:
            nota = "bien"
        elif 7 <= i < 9:
            nota = "notable"
        elif 9<= i <= 10:
            nota= "sobresaliente"
        else:
            nota = "nota no válida"
        lista_notas.append(nota)
    return lista_notas
print(notas([1,4,8,6,3,7,9,10,-11,15,8]))