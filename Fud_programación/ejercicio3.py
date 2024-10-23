lado = float(input("Lado del cuadrado a calcular:"))  #datos del usuario
area = lado * lado   #cálculo del area
if(lado > 0):
    print("El area del cuadrado es" , area)  #resultado
else:
    print("No se puede calcular el area de un cuadrado con el dato proporcionado")   #si el resultado es incoherente