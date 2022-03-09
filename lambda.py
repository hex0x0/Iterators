

calc_dano = (lambda atacante, atacado, x: max((atacante['FOR'] - atacado['DEF']/x), 1))

obj = {'nome': 'player', 'FOR': 20, 'DEF': 20, 'HP':20, 'SP':100, 'ATKS':{'FLEXADA':{'atk':'flexada', 'SP':0}}}




def Clavada(atacante, atacado):
    global calc_dano
    dano = calc_dano(atacante, atacado, 1)
    atacado['HP'] -= dano
    print('%s usou ESPADADA em %s'%(atacante['nome'], atacado['nome']))
    print('%s causou %.2f de dano!'%(atacante['nome'],dano))

Ogro = {'nome': 'Ogro',
            'FOR': 30, 'DEF': 5, 'HP': 100, 'SP': 5,
            'ATKS': {'Clavada': {'Atk': Clavada, 'SP': 0}}}


Clavada(Ogro, obj)

