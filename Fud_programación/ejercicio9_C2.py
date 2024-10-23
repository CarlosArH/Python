def suma(a,b,c,d):
    """float,float,float,float-->float
    OBJ:suma de números complejos"""
    real = a+c
    imag = b+d
    if imag > 0:
        return str(real) + "+" + str(imag) + "i"
    else:
        return str(real) + str(imag) + "i"
#probador
print("suma:" , suma(1,5,8,2))

def resta(a,b,c,d):
    """float,float,float,float-->float
    OBJ:resta de números complejos"""
    real = a-c
    imag = b-d
    if imag > 0:
        return str(real) + "+" + str(imag) + "i"
    else:
        return str(real) + str(imag) + "i"
#probador
print("resta:" , resta(1,7,4,-9))

def producto(a,b,c,d):
    """float,float,float,float-->float
    OBJ:producto de números complejos"""
    real = (a*c)-(b*d)
    imag = (a*d)+(b*c)
    if imag > 0:
        return str(real) + "+" + str(imag) + "i"
    else:
        return str(real) + str(imag) + "i"
#probador
print("producto" , suma(2,6,5,1))

def división(a,b,c,d):
    """float,float,float,float-->float
    OBJ: división de números complejos
    PRE: el denominador ha de ser distinto de 0"""
    denominador = ((c**2) + (d**2))
    real = ((a*c)+ (b*d)) / denominador
    imag = ((b*c)-(a*d)) / denominador
    if imag > 0:
        return str(real) + "+" + str(imag) + "i"
    else:
        return str(real) + str(imag) + "i"
#probador
print("divisiónm:" , división(8,4,2,7))


   