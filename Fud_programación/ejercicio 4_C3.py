"""OBJ: convertir de una hora expresada en 24 horas en una hora expresada en 12 horas
PRE: la hora tiene que ser entre 0 y 24
PRE: hay que poner la hora como horas y luego los minutos"""
try:
    hora = int(input("¿Cuantas horas han pasado desde la última media noche?:"))
    minutos = int(input("¿Cuantos minutos han pasado desde la última hora punta?:"))
except: print("los valores introducidos no son válidos")
else:
    if 0 < hora < 24 + 0 < minutos < 60 :
        if hora <= 12:
            print(hora , ":" , minutos , "AM")
        else:
            a = hora - 12
            print(a , ":" , minutos , "PM")
    else: 
        print("los valores introducidos no son válidos")
    