n = 0
numeros = 0
try:
    numero_limite = int(input("Introduzca un límite:"))
except: print("El numero no es valido")
while numeros <= numero_limite:
    if numero_limite <= 0:
        print("El numero no es valido")
    else:
        n += 1
        numeros += 1/n
        continue
    break
print(n)