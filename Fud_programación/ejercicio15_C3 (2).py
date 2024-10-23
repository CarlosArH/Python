def monomio(coeficiente,exponente):
    if coeficiente == 0:
        return "0"
    elif coeficiente < 0:
        if exponente == 0:
            return str(coeficiente)
        else:
            return str(coeficiente) + "x**" + str(exponente) 
    elif coeficiente > 0:
        if exponente == 0:
            return "+" + str(coeficiente)
        else:
            return "+" + str(coeficiente) + "x**" + str(exponente) 
print(monomio(4,2))