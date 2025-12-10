print('super progressão aritimetica')
p1 = int(input('digite o primeiro termo:'))
r = int(input('digite a razão:'))
cont = 0
total = 0
mais = 9
print(f'a progressão aritmetica do termo {p1} com razão {r} é')
print(f'{p1} ', end=' ')
while mais != 0:
    total += mais
    while cont != total:
        cont += 1
        p1 += r
        print('=', end='  ')
        print(f'{p1} ', end=' ')
    mais = int(input('\nquantos termos voce quer mostrar a mais?:'))
print(f'progressão finalizada com {total} termos')
