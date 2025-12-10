numeros = []
PARES = []
TRES = []
for t in range(1, 5):
    numero = int(input(f'Digite o {t}º número:'))
    if numero % 2 == 0:
        pares = numero
        PARES.append(pares)
    numeros.append(numero)
    if numero == 3:
        tres = t
        TRES.append(tres)
tupla = tuple(numeros)
NOVE = tupla.count(9)
print(f'o NOVE apareceu {NOVE} vezes')
print(f'o TRES apareceu primeiro na {TRES[0]}ª posição')
print(f'os numeros pares são {PARES}')

# forma do guanabara

num = (int(input('digite o primeiro numero:')),
       int(input('digite o segundo numero:')),
       int(input('digite o terceiro numero:')),
       int(input('digite o quarto numero:')))
print(f'voce digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('o valor 3 não foi digitado em nenhuma posição')
print(f'os valores pares digitados foram',end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end='')
