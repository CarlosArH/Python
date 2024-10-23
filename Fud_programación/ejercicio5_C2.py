def circunferencia(x,y):
    """float,float-->float
    OBJ: averiguar si un punto en el plano está en la cicunferencia dada"""
    return x**2 + y**2
if circunferencia(10,30)==1000:
    print("El punto está en la circunferencia")
else:
    print("El punto no está en la circunferencia")    
