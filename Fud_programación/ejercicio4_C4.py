import random
numeros_en_lista = random.randint(0,15)
lista_numeros = []
for i in range(numeros_en_lista):
    numero = random.randint(0,20)
    lista_numeros.append(numero)
print(lista_numeros)
x = 0
for i in (lista_numeros):
    x += i
media = x/numeros_en_lista
mínimo = min(lista_numeros)
máximo = max(lista_numeros)
print(media)
print("máximo: ", máximo)
print("mínimo: ", mínimo)