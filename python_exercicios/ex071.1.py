print('=' * 30)
print(f'{'banco cev':^30}')
print('=' * 30)
valor = (int(input('que valor voce quer sacar ? S$:')))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'total de {totalced} cedulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 30)
print(f'volte sempre ao BANCO CEV! tenha um bom dia !')
