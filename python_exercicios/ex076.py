print(f'''{'-' * 20}
LISTAGEM DE PREÇOS
{'-' * 20}''')
tupla = ('lapis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo', 25.00, 'transferidor', 4.20,
         'compasso', 9.99, 'mochila', 120.32, 'canetas', 22.30, 'livro', 34.90)
itens = (tupla[0::2])
preço = (tupla[1::2])
for e in range(0, len(itens)):
    print(f'{itens[e]:.<30} R${preço[e]:>7.2f}')

#forma do guanabara

listagem = ('lapis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo', 25.00, 'transferidor', 4.20,
            'compasso', 9.99, 'mochila', 120.32, 'canetas', 22.30, 'livro', 34.90)
print('_' * 40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('_' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('_' * 40)
