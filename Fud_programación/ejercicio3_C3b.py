try:
    cantidad_numeros = int(input("¿Cuantos números quiere introducir?:"))
except:
    print("no se puede introducir esa cantidad de números")
else:
    if cantidad_numeros>=2:
        numeros = []
        for i in range(cantidad_numeros):
            while True:
                numero = float(input(f"Introduce el número {i+1}: "))
                numeros.append(numero)
                break
        media= sum(numeros)/cantidad_numeros
        minimo = min(numeros)
        mayor = max(numeros)
        print("el mínimo es", minimo)
        print("el máximo es" , mayor)
        print("la media es" ,  media)
    else:
        print("error")




