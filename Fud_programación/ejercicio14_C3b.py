try:
    longitud_serie = int(input("Introduzca cuantos números tendrá su serie:"))
except: print("la longitud de la serie debe ser un número entero")
else:
    i = 0
    valores_convergencia = []
    for i in range(longitud_serie):
        try: 
            numeros = int(input("Introduzca los valores de forma creciente:"))
        except: print("Los números deben ser enteros")
        else:
            i += 1
            valores_convergencia.append(numeros)
    for j in (valores_convergencia):
        factorial = []
        con = []
        for k in range(1, j+1):
            factorial.append(k)
            convergencia = (sum(factorial)**2) / (2 **(2*j))
            con.append(convergencia)
        convergencia_2 = sum(con)
        print("convergencia hasta ", j, "=", convergencia_2)
            

