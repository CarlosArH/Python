#examen laboratorio 2021
import random

def es_correcto(n):
    valor_retorno = 0
    respuesta_correcta = False
    while not respuesta_correcta:
        respuesta = input("¿Es el numero "+str(n)+"?")
        if respuesta == "si":
            valor_retorno = 0
            respuesta_correcta = True
        elif respuesta == "menor":
            valor_retorno = -1
            respuesta_correcta = True
        elif respuesta == "mayor":
            valor_retorno = 1
            respuesta_correcta = True
        else:
            print("La entrada no es correcta")
    return valor_retorno

minimo = 1
maximo = 100
intentos = 0
he_acertado = False
while not he_acertado:
    intentos += 1
    aleatorio = random.randint(minimo,maximo)
    resultado = es_correcto(aleatorio)
    if resultado == 0:
        print("El número es", aleatorio, "y he utilizado", intentos, "intentos")
        he_acertado = True
    elif resultado == 1:
        minimo = aleatorio + 1
    else:
        maximo = aleatorio  - 1

