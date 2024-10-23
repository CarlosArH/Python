def decimal_a_base_menor(numero, base):
    # Caso base: si el número es menor que la base, devolver el número como cadena.
    if numero < base:
        return str(numero)
    # Caso recursivo: dividir el número por la base y llamar a la función con el cociente,
    # luego concatenar el residuo (resto) al resultado.
    else:
        return decimal_a_base_menor(numero // base, base) + str(numero % base)

# Solicitar al usuario un número decimal y una base desde el teclado
try:
    numero_decimal = int(input("Ingrese un número decimal: "))
    base_destino = int(input("Ingrese la base a la que desea convertir (menor que 10): "))

    if base_destino >= 10 or base_destino <= 1:
        raise ValueError("La base debe ser menor que 10 y mayor que 1.")

    # Llamar a la función para convertir a la base deseada
    resultado = decimal_a_base_menor(numero_decimal, base_destino)
    print(f"El número {numero_decimal} en base {base_destino} es: {resultado}")

except ValueError as e:
    print(f"Error: {e}")
