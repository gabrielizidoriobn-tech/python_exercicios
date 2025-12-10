cont = acum = 0
maior = menor = None
j = ''
while j != 'n':
    cont += 1
    n = int(input('digite um valor:'))
    acum += n
    j = str(input('deseja continuar? [S/N]:')).strip().lower()
    media = acum / cont
    if maior is None or menor is None:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'a quantidade de termos digitados foi {cont} a media deles é {media}')
print(f'o maior valor foi {maior} e o menor valor foi {menor}')
