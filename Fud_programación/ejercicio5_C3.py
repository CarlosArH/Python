try:
    nota = float(input("Introduzca la calificación del alumno:"))
except: print("El valor introducido no es considerado una calificación valida")
else:
    if 10>=nota>=8.5:
        print("A")
    elif 8.5>nota>=6.5:
        print("B")
    elif 6.5>nota>=5:
        print("C")
    elif 5>nota>=3.5:
        print("D")
    elif 3.5>nota>=0:
        print("F")
    else:
        print("El valor introducido no es considerado una calificación valida")