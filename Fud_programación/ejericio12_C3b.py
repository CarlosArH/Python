def media(x, y):
    return sum(x) / y
try:
    n = int(input("Introduzca el numero de elementos de la población:"))
except: 
    print("no es un número válido de elementos")
    exit()
población = []
i = 0
while i in range(n):
    try:
        numeros = float(input("Introduzca los datos para los cuales hay que determinar la varianza:"))
    except: 
        print("El valor introducido no es valido")
        exit()
    else:
        población.append(numeros)
        i += 1
n_2 = n - 1
numeradores = []
for j in (población):
    numerador = (j - media(población,n))**2
    numeradores.append(numerador)
def varianza (a,b):
    var = sum(a) / b
    return var
print(varianza(numeradores, n_2))



    

