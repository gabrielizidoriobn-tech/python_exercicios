import random
m = random.randint(1, 10)
j = int(input('eu estou pensando em um numero de 1 a 10, adivinhe qual é:'))
p = 0
while m != j:
    if j > m:
        j = int(input('voce errou, tente mais para baixo:'))
    elif j < m:
        j = int(input('voce errou, tente mais para cima:'))
    p += 1
print(f'parabens voce acertou, o numero em que eu estava pensando era {m}')
print(f'voce precisou ao todo de {p} palpites para acertar')

#forma do guanabara
# from random import randint
# computador = randint(0, 10)
# print('''sou seu computador... acabei de pensar em um numero entre 0 e 10.
# sera que voce consegue adivinhar qual foi ?''')
# acertou = False
# palpites = 0
# while not acertou:
#     jogador = int(input('quel é seu palpite:'))
#     palpites += 1
#     if jogador == computador:
#         acertou = True
#     else:
#         if jogador < computador:
#             print('Mais... tente mais uma vez')
#         elif jogador > computador:
#             print('Menos... tente mais uma vez')
# print(f'acertou com {palpites} tentativas, parabens')
