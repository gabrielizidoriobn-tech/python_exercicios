somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'-----{p}ª pessoa-----')
    nome = str(input('nome:')).strip().upper()
    idade = int(input('idade:'))
    sexo = str(input('F / M :')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'a media de idade do grupo é de {mediaidade:.0f} anos')
print(f'o nome do homem mais velho é {nomevelho} e ele tem {maioridadehomem} anos')
print(f'a quantidade de mulheres com menos de vinte anos é {totmulher20}')
