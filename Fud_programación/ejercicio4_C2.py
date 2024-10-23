def tiempo_mn(h,min,s):
    """float,float,float-->float
    OBJ: clacular los segundos transcurridos desde la ultima medianoche"""
    a = h*3600 + min*60 + s
    return a
print("Han pasado" , tiempo_mn(2,0,0) , "segundos desde la última medianoche")