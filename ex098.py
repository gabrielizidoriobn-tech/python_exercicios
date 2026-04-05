from time import sleep

def contador(i, f, p):
    menor = 0
    sleep(0.5)
    print(f'contagem de {i} ate {f} de {p} em {p}')
    if i < f:
        for d in range(i, f + 1, p):
            sleep(0.5)
            print(d, end=' ')
    if i > f:
        menor = i
        print(f'{i}', end=' ')
        for d in range(i, f + 1, p):
            sleep(0.5)
        for d in range(f, i + 1):
            if menor - p < menor:
                menor -= p
                if menor >= f:
                    sleep(0.5)
                    print(f'{menor}', end=' ')
            if menor - p > menor:
                menor += p
                if menor >= f:
                    sleep(0.5)
                    print(f'{menor}', end=' ')


for s in range(1, 3):
    sleep(0.5)
    print(f'_-' * 20)
    print(f'contagem de 1 ate 10 pulando de {s}')
    for a in range(1, 11, s):
        sleep(0.5)
        print(f'{a}', end=' ')
        if a == 10:
            print()
sleep(0.5)
print(f'\nagora voce vai personalizar a contagem')
inicio = int(input('inicio:'))
fim = int(input('fim:'))
passo = int(input('passo:'))
contador(i = inicio, f = fim, p = passo)

sleep(0.5)
print('\n>>> encerrado <<<')
