def farenheit(TC):
    """float-->float
    OBJ: pasar de grados centígrados a grados farenheit"""
    return 9*TC/5 + 32
def kelvin(TC):
        """float-->float
    OBJ: pasar de grados centígrados a grados kelvin"""
        return TC + 273.15
print("son" , farenheit(30) , "grados farenheit y" , kelvin(30) , "grados kelvin")