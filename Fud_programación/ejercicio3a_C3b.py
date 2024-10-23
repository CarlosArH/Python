def rectangulo(altura, anchura):
    """int, int --> None
    OBJ: dibujar un ractangulo con @ en las filas pares y # en la filas impares"""
    for i in range(altura):
        if i % 2 == 0:
            print("@"*anchura)
        else:
            print("#"*anchura)
rectangulo(15,10)
