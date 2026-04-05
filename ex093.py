dados = {}
gols = []
tot = 0
dados['nome'] = str(input('Nome do jogador:'))
dados['partidas'] = int(input(f'quantas partidas {dados["nome"]} jogou ? :'))
for c in range(0, dados['partidas']):
    g = (int(input(f'numero de gols na partida {c + 1}:')))
    gols.append(g)
    tot += g
dados['gols'] = gols[:]
dados['total'] = tot
del dados['partidas']
print(f'=-'*15)
print(dados)
print(f'=-'*15)
for k,v in dados.items():
    print(f'o campo {k} tem o valor {v}')
print(f'=-' * 15)
print(f'o jogador {dados['nome']} jogou {len(gols)} partidas')
cont = 0
for g in gols:
    cont += 1
    print(f'na partida {cont}, fez {g} gols')
