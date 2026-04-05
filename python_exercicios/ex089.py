tudo = []
while True:
    nomes_e_notas = []
    nome = str(input('nome do aluno:'))
    nota1 = float(input('nota 1:'))
    nota2 = float(input('nota 2:'))
    media = (nota1 + nota2) / 2
    nomes_e_notas.append(nome)
    nomes_e_notas.append(media)
    nomes_e_notas.append(nota1)
    nomes_e_notas.append(nota2)
    tudo.append(nomes_e_notas)
    s_n = str(input('quer continuar ?: [S/N] ')).strip().lower()
    if s_n == 'n':
        break
print('=' * 30)
print(f'{"N°     nome     nota":^30}')
print('-' * 30)
for i, a in enumerate(tudo):
    linha = f'{i}       {tudo[i][0]}       {tudo[i][1]:.1f}'
    print(f'{linha:^30}')
print('-' * 30)
while True:
    escolha = int(input('deseja ver a nota de qual aluno ?:'))
    if escolha == 999:
        break
    else:
        print(tudo[escolha][2:])
print('*' * 30)
print('obrigado e volte sempre')
