productos = [{'nombre': "Iphone 14",'categoria':'movil','clave':['5g', 
'iphone','apple'], 'precio':600, 'stock': 100},
{'nombre': "Altavoz JBL Flip 4", 'categoria':'altavoz','clave':['flip', 
'bluetooth','JBL'], 'precio':100, 'stock': 50},
{'nombre': "Xiaomi 13T", 'categoria':'movil','clave':['5g', 'xiaomi','13t'], 
'precio':400, 'stock': 200},
{'nombre': "Apple Watch 8", 'categoria':'reloj','clave':['nfc', 
'apple','watch'], 'precio':400, 'stock': 100},
{'nombre': "Samsung Watch",'categoria':'reloj','clave':['nfc', 
'samsung','watch'], 'precio':200, 'stock': 100},
{'nombre': "Nintendo Switch", 'categoria':'consola','clave':['nintendo', 
'switch','oled'], 'precio':300, 'stock': 200},
{'nombre': "Alexa Echo Show 8", 'categoria':'altavoz','clave':['alexa', 
'show','bluetooth'], 'precio':150, 'stock': 100},
{'nombre': "Mi Smart Band 6",'categoria':'reloj','clave':['bluetooth', 
'xiaomi','smartband'], 'precio':40, 'stock': 100},
{'nombre': "Samsung S22", 'categoria':'movil','clave':['5g', 'samsung','s22'], 
'precio':600, 'stock': 100},
{'nombre': "Playstation 5", 'categoria':'consola','clave':['playstation', 
'hdmi','sony'], 'precio':800, 'stock': 100},
{'nombre': "Apple Airpods 14", 'categoria':'altaoz','clave':['apple', 
'airpods','bluetooth'], 'precio':400, 'stock': 50}]
def funcion_1(productos, categoría):
    print("Productos de esta categoría:")
    lista_2 = []
    for i in range(len(productos)):
        if productos[i]["categoria"] == categoría:
            lista_2 += productos[i]
    return lista_2 

def funcion_2(productos, p_clave):
    for i in range(len(productos)):
        for j in range(len(productos[i]["clave"])):
            if productos[i]["clave"][j] == p_clave:
                print("Nombre:",productos[i]["nombre"],"categoria:", productos[i]["categoria"], "clave:", productos[i]["clave"], "precio:", productos[i]["precio"], "stock:", productos[i]["stock"])
    return ""
print(funcion_2(productos, "apple"))

lista = funcion_1(productos, "reloj")
print(funcion_2(lista, "nfc"))












