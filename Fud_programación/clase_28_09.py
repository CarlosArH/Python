def area_rectangulo(altura,anchura):
    """float-->float
    OBJ:Calcula el area de un rectángulo
    PRE: altura>=0, ancho>=0"""
    altura = 10
    return altura*anchura
altura = 5
anchura = 5
area = area_rectangulo(altura,anchura)
print(altura) #coje la altura 5 porque h=5 es la que tiene justo antes
print(area) #coje el area con altura 10 porque el return tiene la h=10 justo antes

