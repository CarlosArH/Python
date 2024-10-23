lista_gasolina = []
lista_tienda = []
for i in range(10):
    gasolina = float(input("¿Cuanto dinero ha gastado en la gasolina?: "))
    tienda = float(input("¿Cuanto dinero ha gastado en la tienda?: "))
    lista_gasolina += [gasolina]
    lista_tienda += [tienda]
lista_total = []
for pos in range(10):
    lista_total += [lista_gasolina[pos]+lista_tienda[pos]]
print("dinero gastado en tienda: ", lista_tienda)
print("dinero gastado en gasolina: ", lista_gasolina)
print("dinero gastado en total: ", lista_total)


