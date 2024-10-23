def leer_entero_valido():
    """none --> int 
    OBJ:Solicita un entero al usuario, lo valido y lo retorna sólo cuando se ha asegurado de que es realmente un entero"""
    while True:
        try:
            entero = int(input("Introduce un número entero: "))
        except:
            print("El valor introducido no es un número entero. Por favor, inténtalo de nuevo.")
            continue
        break
    print("el numero", entero , "es entero")

leer_entero_valido()

