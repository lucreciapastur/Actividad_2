def inicializo_acumulado ():
    acumulado={}
    for jugador in ['Shadow', 'Blaze', 'Viper', 'Frost', 'Reaper']:
        acumulado[jugador]={'kills':0, 'assists':0, 'deaths':0, 'mvps':0, 'puntos':0}
    return acumulado

def calculo_puntos (kills, assists, deaths):
    puntos = kills * 3 + assists * 1 + deaths * -1
    return puntos

def encuentro_mvp (puntos):
    max_puntos=0
    for jugador in puntos:
        punt = puntos[jugador]
        if punt > max_puntos:
            max_puntos = punt
            mvp = jugador
    return mvp

def calculo_acumulado (acumulado, ronda):
    puntos = {}
    for jugador in ronda:
        acumulado[jugador]['kills'] += ronda[jugador]['kills']
        acumulado[jugador]['assists'] += ronda[jugador]['assists']
        acumulado[jugador]['deaths'] += 1 if ronda[jugador]['deaths'] else 0
        puntos[jugador] = calculo_puntos(ronda[jugador]['kills'], ronda[jugador]['assists'], ronda[jugador]['deaths'])
        acumulado[jugador]['puntos'] += puntos[jugador]
    acumulado[encuentro_mvp(puntos)]['mvps'] += 1
    return acumulado    

def impresion_ronda (acumulado, num_ronda):
    print(f"Ranking ronda {num_ronda}:")
    print(f"{'Jugador':<12} {'Kills':<12} {'Asistencias':<12} {'Muertes':<12} {'MVPs':<12} {'Puntos':<12}")
    print("-" * 72)
    ordenado=sorted(acumulado.items(), key=lambda elem: elem[1]['puntos'], reverse=True) 
    for jugador, info in ordenado:
        print(f"{jugador:<12} {info['kills']:<12} {info['assists']:<12} {info['deaths']:<12} {info['mvps']:<12} {info['puntos']:<12}")
    print("-" * 72)
    print()

def procesando_rondas (rounds):
    acumulado = inicializo_acumulado()
    num_ronda = 1
    for ronda in rounds:
        acumulado = calculo_acumulado (acumulado, ronda)
        impresion_ronda (acumulado, num_ronda)
        num_ronda += 1