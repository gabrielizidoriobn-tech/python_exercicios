soma_idade = 0
velho = 0
F = 0
nomevelho = ''
for c in range(0, 4):
    print('_' * 10, end='')
    print(f'{c + 1}ª pessoa', end='')
    print('_' * 10)
    nome = str(input(f'nome   :'))
    idade = int(input('idade:'))
    sexo = str(input(f'sexo [M / F]:')).strip().upper()
    soma_idade += idade
    if c == 1 and sexo == 'M':
        velho = idade
        nomevelho = nome
    if sexo == 'M' and idade > velho:
        velho = idade
        nomevelho = nome
    media = idade / 4
    if sexo == 'F' and idade < 20:
        F += 1
print(f'o mais velho tem {velho} anos de idade e seu nome é {nomevelho}')
print(f'a media de idade é de {media}')
print(f'a quantidade de mulheres com menos de vinte anos é {F}')
