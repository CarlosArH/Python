def punto(x,y):
    """ float, float-->dict
    OBJ:crear un diccionario con los puntos dados"""
    return {"x":x, "y":y}
def suma(punto1, punto2):
    """dict, dict --> dict
    OBJ: sumar 2 puntos"""
    coord_x = punto1["x"] + punto2["x"]
    coord_y = punto1["y"] + punto2["y"]
    return punto(coord_x,coord_y)
punto_1 = punto(4,8)
punto_2 = punto(2,12)
print(suma(punto_1,punto_2))