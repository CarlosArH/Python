def suma_edades_alumnos(lista_alumnos, indice=0):
    # Caso base: cuando el índice llega al final de la lista.
    if indice == len(lista_alumnos):
        return 0
    # Caso recursivo: sumar la edad del alumno actual y llamar a la función con el siguiente índice.
    else:
        return lista_alumnos[indice]['edad'] + suma_edades_alumnos(lista_alumnos, indice + 1)

# Ejemplo de uso con una lista de alumnos
alumnos = [
    {'nombre': 'Juan', 'edad': 25, 'titulacion': 'Informática'},
    {'nombre': 'María', 'edad': 22, 'titulacion': 'Matemáticas'},
    {'nombre': 'Carlos', 'edad': 28, 'titulacion': 'Física'}
]