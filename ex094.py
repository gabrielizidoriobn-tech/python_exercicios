lista = []
total = 0
while True:
    dicionario = {}
    dicionario['nome'] = str(input('nome:')).strip().lower()
    dicionario['idade'] = int(input('idade:'))
    while True:
        dicionario['sexo'] = str(input('sexo[M/F]:')).strip().lower()
        if dicionario['sexo'] == 'm' or dicionario['sexo'] == 'f':
            break
        print('digite apenas M ou F')
    lista.append(dicionario)
    s_n = str(input('deseja continuar?[S/N]')).strip().lower()
    if s_n != 's' and s_n != 'n':
        while True:
            print('digite apenas S ou N')
            s_n = str(input('deseja continuar?[S/N]')).strip().lower()
            if s_n == 's' or s_n == 'n':
                break
    elif s_n == 'n':
        break
print(f'A) o total de pessoas cadastradas foi: {len(lista)}')
for p in range(0, len(lista)):
    total += (lista[p]['idade'])
media = total / len (lista)
print(f'B) a media da idade das pessoas cadastradas foi: {media:.0f}')
print('C) as pessoas do sexo feminino cadastradas foram:', end=' ')
for f in range(0, len(lista)):
    if lista[f]['sexo'] == 'f':
        print(lista[f]['nome'], end=' ')
print(f'\nD) a lista das pessoas com idade acima da media :')
for i in range (0, len(lista)):
    if lista[i]['idade'] > media:
        print(f"nome = {lista[i]['nome']}, sexo = {lista[i]['sexo']}, idade = {lista[i]['idade']}")
print('<<< ENCERRADO >>>')
