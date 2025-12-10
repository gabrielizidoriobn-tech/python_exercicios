cores = {'limpa': '\033[m', 'ciano': '\033[4;37;40m', 'verde': '\033[1;32;40m', 'azul': '\033[1;30;107m'}
numero = int(input(f'{cores['ciano']}digite um numero:'))
d = numero % 2
if d == 0:
    print(f'{cores['azul']}seu numero é par')
else:
    print(f'{cores['verde']}seu numero é impar')
