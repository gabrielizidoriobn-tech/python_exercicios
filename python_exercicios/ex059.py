print('digite dois valores e eu vou listar as opções')
n1 = int(input('primeiro valor:'))
n2 = int(input('segundo valor:'))
print('''digite
1 para somar
2 para multiplicar
3 para mostrar o maior
4 para digitar novos valores
5 para finalizar''')
op = 'selecione a sua opção:'
o = 0
while o != 5:
    o = int(input(op))
    if o == 1:
        print(f'a soma dos valores [{n1}] e [{n2}] é [{n1 + n2}]')
    elif o == 2:
        print(f'a multiplicação dos valores [{n1}] e [{n2}] é [{n1 * n2}]')
    elif o == 3:
        if n1 > n2:
            print(f'entre [{n1}] e [{n2}], o maior valor é [{n1}]')
        elif n1 < n2:
            print(f'entre [{n1}] e [{n2}], o maior valor é [{n2}]')
        else:
            print(f'não a um valor maior que o outro, {n1} e {n2} são iguais')
    elif o == 4:
        n1 = int(input('digite um novo primeiro valor:'))
        n2 = int(input('digite um novo segundo valor:'))
    else:
        print(f'a opção [{o}] não é valida')
print(f'voce escolheu a opção {o}, obrigado por utilizar este programa')
