try:
    año = int(input("Introduzca un año entre el 0 y el 2000 con 4 cifras(ej:0124):"))
except:
    print("el año no está entre 0 y 2000")
miles = str(año)[0]
centenas = str(año)[1]
decimas = str(año)[2]
unidades = str(año)[3]
if int(centenas) < 5:
    if int(decimas) < 5:
        if int(unidades) < 5:
            print(int(miles)*"M", int(centenas)*"C", int(decimas)*"X", int(unidades)*"I")
        else:
            unidades2: int(unidades) - 5
            print(int(miles)*"M", int(centenas)*"C", int(decimas)*"X", "V", int(unidades2)*"I")
    else:
        decimas2 = int(decimas) - 5
        if int(unidades) < 5:
            print(int(miles)*"M", int(centenas)*"C", "L", int(decimas2)*"X", int(unidades)*"I")
        else:
            unidades2: int(unidades) - 5
            print(int(miles)*"M", int(centenas)*"C", "L", int(decimas2)*"X", "V", int(unidades2)*"I")
else:
    centenas2 = int(centenas) - 5
    if int(decimas) < 5:
        if int(unidades) < 5:
            print(int(miles)*"M", "D", int(centenas2)*"C", int(decimas)*"X", int(unidades)*"I")
        else:
            unidades2: int(unidades) - 5
            print(int(miles)*"M", "D", int(centenas2)*"C", int(decimas)*"X", "V", int(unidades2)*"I")
    else:
        decimas2 = int(decimas) - 5
        if int(unidades) < 5:
            print(int(miles)*"M", "D", int(centenas2)*"C", "L", int(decimas2)*"X", int(unidades)*"I")
        else:
            unidades2: int(unidades) - 5
            print(int(miles)*"M", "D", int(centenas2)*"C", "L", int(decimas2)*"X", "V", int(unidades2)*"I")            
        