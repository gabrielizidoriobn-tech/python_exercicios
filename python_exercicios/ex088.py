import random
import time
todos_os_jogos = []
print('*' * 30)
print('MEGA SENA'.center(30))
print('*' * 30)
q = int(input('quantos jogos voce quer sortear?:'))
for n in range(0, q):
    jogo = random.sample(range(1, 61), 6)
    jogo.sort()
    todos_os_jogos.append(jogo)
for i, jogo in enumerate(todos_os_jogos):
    time.sleep(1)
    print(f'jogo {i + 1}: {jogo}')
time.sleep(1)
print('parabens e boa sorte!!')
