numeros = []
num = 0
for n in range(1, 8):
    num = int(input(f'digite o {n}º valor:'))
    if num % 2 == 1:
        numeros.insert(0, num)
    else:
        numeros.append(num)
numeros.sort()
print('os numeros pares são:', end=' ')
for nu in numeros:
    if nu % 2 == 0:
        print(f'{nu}', end=' ')
print('\nos numeros impares são:', end=' ')
for nu in numeros:
    if nu % 2 == 1:
        print(f'{nu}', end=' ')
