#forma do guanabara
# não esta totalmente igual
# n = int(input('digite um numero para calcular seu fatorial:'))
# c = n
# f = 1
# print(f'calculando {n}! = ', end='')
# while c > 0:
#     print(c, end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1
#     print(f, end='')

import math

print('calculadora de fatorial')
n = False
while not n:
    n = int(input('digite um numero:'))
    print(f'o fatorial do numero [{n}] é {n}', end=' ')
    for a in range(n - 1, 0, -1):
        print(f'x {a}', end=' ')
f = math.factorial(n)
print(f'= {f}')
