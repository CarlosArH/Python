alineaciones = {1:{1:"Pedro", 2:"Ramón", 3:"Julio", 4:"Javier"},
                2:{1:"Pedro", 2:"Ramón", 3:"Julio"},
                3:{1:"Pedro", 2:"Ramón", 3:"Javier"}}
alineaciones[1]
alineaciones[1].values
print(alineaciones[1])
dorsales = {1:{1:"Pedro", 2:"Ramón", 3:"Julio", 4:"Javier"}}
def lista_jornadas(alineaciones,dorsal):
    jornadas_en_las_que_jugo = []
    for jornada in alineaciones:
        jugadores_jornada = alineaciones[jornada]
        if dorsal in jugadores_jornada.keys():
            jornadas_en_las_que_jugo.append(jornada)
    return jornadas_en_las_que_jugo
print(lista_jornadas(alineaciones, 1))


def buscar_jugador_con_mas_partidos(dorsales,alineaciones):
    jugador_que_mas_jugo = None
    mayor_numero_de_partidos = 0
    todos_los_dorslaes = dorsales.keys()
    for dorsal in todos_los_dorslaes:
        jornadas_que_juego = len(lista_jornadas(alineaciones, dorsal))
        if jornadas_que_juego>mayor_numero_de_partidos:
            mayor_numero_de_partidos=jornadas_que_juego
            jugador_que_mas_jugo = dorsal
dorsal = buscar_jugador_con_mas_partidos(dorsales,alineaciones)
print("El jugador que más jugó fue ", dorsales[dorsal], "con dorsal", dorsal)