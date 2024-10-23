def entero_pedido(min, max):
    """none --> int 
    OBJ:Solicita un entero al usuario, lo valida y lo retorna sólo cuando se ha asegurado de que es realmente un entero que esta dentrop del rango"""
    while True:
        try:
            entero = int(input("Introduce un número entero:"))
        except:
            print("El valor introducido no es un número entero. Por favor, inténtalo de nuevo.")
            continue
        if min<=entero<=max:
            break
        else:
            print("el número no está entre" , min , "y" , max)
            continue
    print("el numero", entero , "es entero")
#Probador
min = 1
max = 12
entero_pedido(min, max)

