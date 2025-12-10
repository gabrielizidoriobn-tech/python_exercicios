expressão = str(input('digite uma expressão:'))
parentese_e = expressão.count('(')
parentese_a = expressão.count(')')
if parentese_e != parentese_a:
    print(f'sua expressão esta errada')
else:
    balanceando = 0
    for caractere in expressão:
        if caractere == '(':
            balanceando += 1
        elif caractere == ')':
            balanceando -= 1
            if balanceando < 0:
                break
    if balanceando == 0:
        print(f'sua expressão esta correta')
    else:
        print(f'sua expressão esta errada')
