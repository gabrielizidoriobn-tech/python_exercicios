lista = []
listmax = 0
listmin = 0
maxi = mini = 0
for n in range(0, 5):
    lista.append(int(input(f'digite o {n}º valor:')))
    maxi = max(lista)
    mini = min(lista)
if maxi == mini:
    print(f'todos os numeros são iguais')
else:
    print(f'o maior numero {maxi} esta nas posições', end=' ')
    for pos, num in enumerate(lista):
        if num == maxi:
            print(f'{pos}', end='...')
    print(f'\no menor numero {mini} esta nas posições', end=' ')
    for pos, num in enumerate(lista):
        if num == mini:
            print(f'{pos}', end='...')
