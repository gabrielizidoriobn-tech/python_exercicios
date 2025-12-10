from random import sample

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
tupla = sample(numeros, 5)
maior = max(tupla)
menor = min(tupla)
print(tupla)
print(f'esse é o maior {maior}')
print(f'esse é o menor {menor}')

#forma do guanabara

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'os valores sorteados foram:', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\no maior valor foi:{max(numeros)}')
print(f'o menor valor foi:{min(numeros)}')
