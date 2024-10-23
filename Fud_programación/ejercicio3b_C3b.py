def rectangulo(altura, anchura):
    """int, int --> None
    OBJ: dibujar un ractangulo con @ en las filas pares y # en la filas impares"""
    for i in range(altura):
            print((" @ # ") * anchura)
rectangulo(4,3)
