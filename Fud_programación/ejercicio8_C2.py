def distancia(x1,y1,z1,x2,y2,z2):
    """float,float,float,float,float,float-->float
    OBJ: conserguir a partir de dos vectores el vector que los une, para hacer su modulo y sacar la distancia"""
    a = (x2-x1)
    b = (y2-y1)
    c = (z2-z1)
    return (a**2 + b**2 + c**2)**0.5
print("la distancia es de" , distancia(0,0,0,2,0,0) , "unidades")