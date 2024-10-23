import random
sustantivos = ["perro", "niño", "nube", "padre"]
verbos = ["es", "está", "come", "mira", "ama"]
determinantes = ["el", "la"]
preposiciones = ["al", "en"]
def frases():
    for i in range(5):
        i +=1
        palabras = random.randint(3,10)
        if palabras == 3:
            verbo_3 = random.choice(verbos)
            determinante_3 = random.choice(determinantes)
            sustantivo_3 = random.choice(sustantivos)
            print(determinante_3 ,"",  sustantivo_3,"", verbo_3)
        elif palabras == 4:
            verbo_4 = random.choice(verbos)
            determinante_4 = random.choice(determinantes)
            sustantivo_4 = random.choice(sustantivos)
            determinante_4_2 = random.choice(determinantes)
            print(determinante_4 ,"",  sustantivo_4,"",determinante_4_2,"", verbo_4)
        elif palabras == 5:
            verbo_5 = random.choice(verbos)
            determinante_5 = random.choice(determinantes)
            sustantivo_5 = random.choice(sustantivos)
            preposicion_5 = random.choice(preposiciones)
            sustantivo_5_2 = random.choice(sustantivos)
            print(determinante_5 ,"",  sustantivo_5,"", verbo_5, "", preposicion_5,"", sustantivo_5_2)
        elif palabras == 6:
            verbo_6 = random.choice(verbos)
            determinante_6 = random.choice(determinantes)
            sustantivo_6 = random.choice(sustantivos)
            preposicion_6 = random.choice(preposiciones)
            sustantivo_6_2 = random.choice(sustantivos)
            determinante_6_2 = random.choice(determinantes)
            print(determinante_6 ,"",  sustantivo_6,"", verbo_6, "", preposicion_6,"", determinante_6_2,"", sustantivo_6_2)
        elif palabras == 7:
            verbo_7 = random.choice(verbos)
            determinante_7 = random.choice(determinantes)
            sustantivo_7 = random.choice(sustantivos)
            preposicion_7 = random.choice(preposiciones)
            sustantivo_7_2 = random.choice(sustantivos)
            determinante_7_2 = random.choice(determinantes)
            print(determinante_7 ,"",  verbo_7,"", "al", sustantivo_7, "", "en","", determinante_7_2,"", sustantivo_7_2)
        elif palabras == 8:
            
frases()