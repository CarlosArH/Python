try:
    n = int(input("Introduzca un entero, que será la potencia máxima del numero:"))
except: print("error")
for i in range(0, n+1):
    print(2**i, end=" ")
print(" ")
for i in range(0, n+1):
    print(3**i, end=" ")
print(" ")
for i in range(0, n+1):
    print(5**i, end=" ")
