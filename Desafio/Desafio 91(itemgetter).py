import random
import time
from operator import itemgetter
#key = itemgetter(1)

jogo = {'jogador1': random.randint(1,6),
        'jogador2': random.randint(1,6),
        'jogador3': random.randint(1,6),
        'jogador4': random.randint(1,6)}

ranking = list()

for k,v in jogo.items():
    print(f'o {k} tirou {v}')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for c, v in enumerate(ranking):
    print(f'{c+1}º {v[0]} tirou {v[1]}')

