def punto(x,y):
    """ float, float-->dict
    OBJ:crear un diccionario con los puntos dados"""
    return {"x":x, "y":y}
def distancia(punto1, punto2):
    """dict,dict-->float
    OBJ:averiguar la distancia entre 2 puntos del plano 2D"""
    distance = (((punto2["x"]-punto1["x"])**2)+(punto2["y"]-punto1["y"])**2)**0.5
    return distance
punto_1 = punto(4,8)
punto_2 = punto(2,12)
print(distancia(punto_1,punto_2))