print('progressão aritimetica')
p1 = int(input('digite o primeiro termo:'))
r = int(input('digite a razão:'))
cont = 0
print(f'a progressão aritmetica do termo {p1} com razão {r} é')
print(f'{p1} ', end=' ')
while cont != 9:
    cont += 1
    p1 += r
    print('=', end='  ')
    print(f'{p1} ', end=' ')
