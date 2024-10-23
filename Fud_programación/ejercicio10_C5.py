def contar_longitudes_palabras():
    frecuencias = {}  # Diccionario para almacenar las frecuencias de las longitudes de palabras
    while True:
        palabra = input("Introduce una palabra (o escribe 'fin' para terminar): ")
        if palabra.lower() == 'fin':
            break

        longitud = len(palabra)
        if longitud in frecuencias:
            frecuencias[longitud] += 1
        else:
            frecuencias[longitud] = 1

    return frecuencias

# Ejemplo de uso
resultado = contar_longitudes_palabras()
print("Frecuencias de longitudes de palabras:")
for longitud, frecuencia in resultado.items():
    print(f"Palabras de longitud {longitud}: {frecuencia}")