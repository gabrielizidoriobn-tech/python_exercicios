cores = {'branco': '\033[97;40m',
         'azul': '\033[34;43m',
         'verde': '\033[32;35',
         'amarelo': '\033[33;41m',
         'limpa': '\033[M'}
n1 = int(input(f'{cores['azul']}digite o primeiro numero:'))
n2 = int(input(f'{cores['verde']}digite o segundo numero :'))
n3 = int(input(f'{cores['amarelo']}digite o terceiro numero:'))

# l = [n1, n2, n3]
# l.sort()
# print(f'o maior numero é {l[2]}')
# print(f'o menor numero é {l[0]}')

# if n1 > n2 and n1 > n3:
#     print(f'o maior numero é {n1}')
# if n2 > n1 and n2 > n3:
#     print(f'o maior numero é {n2}')
# if n3 > n1 and n3 > n2:
#     print(f'o maior numero é {n3}')
# if n1 < n2 and n1 < n3:
#     print(f'o menor numero é {n1}')
# if n2 < n1 and n2 < n3:
#     print(f'o menor numero é {n2}')
# if n3 < n1 and n3 < n2:
#     print(f'o menor numero é {n3}')

menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'{cores['branco']}o maior numero é {maior}')
print(f'{cores['branco']}o menor numero é {menor}')
