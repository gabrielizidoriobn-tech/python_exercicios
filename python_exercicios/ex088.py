import random
lista = []
print('*' * 30)
print('MEGA SENA'.center(30))
print('*' * 30)
q = int(input('quantos jogos voce quer sortear?:'))
for n in range(0, q):
    # print(f'jogo {n + 1}:', end=' ')
    for m in range(0, 6):
        lista.append(random.randint(0, 61))
        print(lista)
