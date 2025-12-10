from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opções
[ 1 ] pedra
[ 2 ] papel
[ 3 ] tesoura''')
jogador = int(input('sua escolha:'))
from time import sleep
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print(f'computador jogou {itens[computador]}')
print(f'jogador jogou {itens[jogador]}')
if computador == 0:#pedra
    if jogador == 0:#pedra
        print('empate')
    elif jogador == 1:#papel
        print('jogador vence')
    elif jogador == 2:#tesoura
        print('computador vence')
    else:
        print('jogada invalida')
elif computador == 1:#papel
    if jogador == 0:#pedra
        print('computador vence')
    elif jogador == 1:#papel
        print('empate')
    elif jogador == 2:#tesoura
        print('jogador vence')
    else:
        print('jogada invalida')
elif computador == 2:#tesoura
    if jogador == 0:#pedra
        print('jogador vence')
    elif jogador == 1:#papel
        print('computador vence')
    elif jogador == 2:#tesoura
        print('empate')
    else:
        print('jogada invalida')
