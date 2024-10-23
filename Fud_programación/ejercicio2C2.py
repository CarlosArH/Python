def barns_metros2 (Barn):
    """float-->float
    OBJ: pasar de Barn a metros cuadrados"""
    return Barn * 10**-28
print("Son" , barns_metros2(4000) , "metros cuadrados")
def metros2_barns (M):
    """float-->float
    OBJ: pasar de metros cuadrados a Barn"""
    return M / 10**-28
print("Son", metros2_barns(3 * 10**-24) , "Barns")
    