lista = []
while True:
    gols = []
    tot = 0
    partidas = []
    dados = {}
    dados['nome'] = str(input('Nome do jogador:'))
    partidas.append(int(input(f'quantas partidas {dados["nome"]} jogou ? :')))
    for c in range(0, partidas[0]):
        g = (int(input(f'numero de gols na partida {c + 1}:')))
        gols.append(g)
        tot += g
        dados['gols'] = gols[:]
        dados['total'] = tot
    lista.append(dados)
    while True:
        s_n = str(input('deseja continuar? [S/N] :')).strip().lower()
        if s_n in 'sn':
            break
        print('ERRO! Digite apenas S ou N.')
    if s_n in 'n':
        break
print(f'{"-=" * 21}')
print(f'{"pos"}', end=' ')
for i in dados.keys():
    print(f'{i:<15}', end=' ')
print()
print(f'_'* 42)
for d, l in enumerate(lista):
    print(f'{d}', end='   ')
    for k in l.values():
        print(f'{str(k):<15}', end='')
    print()
print(f'{"-" * 42}')
while True:
    opção = int(input('mostrar dados de qual jogador ?(999 para encerrar):'))
    while opção not in range(0, len(lista)):
        print(f'opção invalida, digite um numero entre {0, len(lista) - 1}')
        opção = int(input('mostrar dados de qual jogador ?(999 para encerrar):'))
        if opção in range(0,len(lista)) or opção == 999:
            break
    if opção == 999:
        break
    print(f'{"-" * 35}')
    print(f'levantamento do jogador {lista[opção]['nome']}')
    for f in range(0, len(lista[opção]['gols'])):
        print(f'no jogo {f + 1} ele fez {lista[opção]['gols'][f]} gols')
print('<<< ENCERRADO >>>')
