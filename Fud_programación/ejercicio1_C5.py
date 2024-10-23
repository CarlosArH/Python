#1
def persona(nombre, sexo, edad):
    """str, str, int--> dict
    OBJ: crear un diccionario con los datos de una persona"""
    return {"nombre":nombre, "sexo":sexo, "edad":edad}
def datos():
    nombre = str(input("Introduzca el nombre de la persona: "))
    sexo = str(input("Introduzca el sexo de la persona(h/m):0 "))
    edad = int(input("Introduzca la edad de la persona: "))
    return persona(nombre, sexo, edad)
#2
def datos_persona(persona):
    print("Nombre:", persona["nombre"])
    print("Sexo:", persona["sexo"])
    print("Edad:", persona["edad"])
    return ""
def print_lista_personas(lista_personas):
    for i in range(numero_personas):
        print(f"---Persona{i+1}---")
        datos_persona(datos())
    return""
def media(lista_personas):
    suma = 0
    for persona in lista_personas:
        suma += persona["edad"]
    media_total = suma /len(lista_personas)
print(media(10))
