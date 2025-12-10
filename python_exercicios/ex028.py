cores = {'limpa': '\033[m', 'verde': '\033[32m', 'vermelho': '\033[31m', 'branco': '\033[97m'}
import random
print(f'{cores['branco']}eu estou pensando em um numero de 1 a 5')
n = int(input(f'{cores['branco']}adivinhe em que numero estou pensando:'))
na = random.randint(1,5)
print('-=-'*20)
print(f'{cores['branco']}processando')
print('-=-'*20)
import time
time.sleep(3)
if n == na:
    print(f'{cores['verde']}parabens, voce acertou')
else:
    print(f'{cores['vermelho']}sinto muito voce errou\no numero em que eu estava pensando era ___{na}___')
