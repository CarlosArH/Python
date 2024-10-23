fila1_A = []
fila2_A=[]
fila3_A=[]
fila1_B=[]
fila2_B=[]
fila3_B=[]
fila1=[]
fila2=[]
fila3=[]
for i in range(4):
    fila1_a = float(input(f"Introducir el numero {i+1} de la matriz A:"))
    fila1_b = float(input(f"Introducir el numero {i+1} de la matriz B:"))
    fila1_A += [fila1_a]
    fila1_B += [fila1_b]
for i in range(4):
    fila2_a = float(input(f"Introducir el numero {i+5} de la matriz A:"))
    fila2_b = float(input(f"Introducir el numero {i+5} de la matriz B:"))
    fila2_A += [fila2_a]
    fila2_B += [fila2_a]
for i in range(4):
    fila3_a = float(input(f"Introducir el numero {i+9} de la matriz A:"))
    fila3_b = float(input(f"Introducir el numero {i+9} de la matriz B:"))
    fila3_A += [fila3_a]
    fila3_B += [fila3_a]
for pos in range(4):
    fila1 += [fila1_A[pos]+fila1_B[pos]]
    fila2 += [fila2_A[pos]+fila2_B[pos]]
    fila3 += [fila3_A[pos]+fila3_B[pos]]
print("Matriz A:")
print(fila1_A)
print(fila2_A)
print(fila3_A)
print("Matriz B:")
print(fila1_B)
print(fila2_B)
print(fila3_B)
print("Matriz Suma:")
print(fila1)
print(fila2)
print(fila3)