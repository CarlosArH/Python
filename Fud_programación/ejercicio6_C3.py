try:
    entero1 = int(input("Primer número entero:"))
except: 
    print("El valor introducido no es considerado número entero")
    quit()
try:
    entero2 = int(input("Segundo número entero:"))
except:
    print("El valor introducido no es considerado número entero")
    quit()
try:
    entero3 = int(input("Tercer número entero:"))
except:
    print("El valor introducido no es considerado número entero")
    quit()
list = [entero1 , entero2 , entero3]
numeros = sorted(list)
print(numeros)