def invertir(palabra):
    if len(palabra) <= 1:
        return palabra
    else:
        return palabra[-1] + invertir(palabra[1:-1]) + palabra[0]
print(invertir("palabra"))