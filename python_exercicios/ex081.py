lista = []
cont = 0
while True:
    n = int(input('digite um numero:'))
    s_n = str(input('deseja continuar? [S / N]:')).strip().lower()
    if not lista:
        lista.append(n)
    else:
        posição = 0
        while posição < len(lista) and n < lista[posição]:
            posição += 1
        lista.insert(posição, n)
    cont += 1
    if s_n == 'n':
        break
print(f'voce digitou {cont} elementos')
if 5 in lista:
    print(f'o numero 5 esta presente')
else:
    print(f'o numero 5 não esta presente')
print(f'esta é a forma decrescente {lista}')
