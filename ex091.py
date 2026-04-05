from random import randint
from time import sleep
from operator import itemgetter
dados = {}
ranking = {}
for d in range(1, 5):
    dados[f'jogador {d}'] = randint(1, 6)
print('valores sorteados:')
for k, v in dados.items():
    sleep(0.5)
    print(f'O jogador {k} tirou {v} no dado.')
sleep(0.5)
print('ranking dos jogadores:')
ranking = dict(sorted(dados.items(), key=itemgetter(1), reverse=True))
contador = 0
for k,v in ranking.items():
    sleep(0.5)
    contador += 1
    print(f'em {contador}º lugar esta o {k} que tirou {v}')
