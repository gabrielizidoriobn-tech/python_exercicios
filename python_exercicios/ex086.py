lista = []
zero = 0
for n in range(0, 3):
    for nu in range(0, 3):
        numeros = int(input(f'digite o {n},{nu} numero:'))
        lista.append(numeros)
for i in range(0, 9, 3):
    print(f'{lista[i:i + 3]:^5}')
