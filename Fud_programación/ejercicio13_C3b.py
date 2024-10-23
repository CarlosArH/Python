print('Intente adivinar el símbolo oculto')
def juego(max_intentos):
    simbolo = input('Haga su apuesta: ')
    intentos = 1
    while simbolo != '#' and intentos <= max_intentos:
        simbolo = input('Ese no es el símbolo oculto. Haga su apuesta: ')
        intentos += 1
    if simbolo == "#":
        print(f'Por fin! Ha necesitado {intentos} intentos para adivinarlo.')
    elif intentos > max_intentos:
        print("Te has pasado de intentos")
juego(5)
    