try:
    a = float(input("primer coeficiente:"))
    b = float(input("segundo coeficiente:"))
    c = float(input("tercer coeficiente:"))
except: print("los valors introducidos no sirven para la ecuación")
raíz = b**2 - 4*a*c
denominador = 2*a
if raíz > 0 :
    solucion1 = (-b + (raíz**0.5)) / denominador
    solucion2 = (-b - (raíz**0.5)) / denominador
    print(solucion1 , "y" , solucion2)
elif raíz == 0:
    solucion3 = (-b) / denominador
    print(solucion3)
else:
    print("raíces imaginarias")
