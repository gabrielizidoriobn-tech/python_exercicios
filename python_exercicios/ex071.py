print('caixa eletronico')
totc = 0
while True:
    n = int(input('quanto dinheiro voce gostaria de sacar:'))
    print('o seu saque sera de')
    if n >= 50:
        n1 = n // 50
        print(f'{n1} notas de 50')
        if 0 < n % 50 < 10:
            n12 = n % 50 // 1
            print(f'{n12} notas de 1')
    if 10 <= n % 50 < 20:
        n13 = n % 50 // 10
        print(f'{n13} notas de 10 ')
        if 10 > n % 50 % 10 > 0:
            n14 = n % 50 % 10 // 1
            print(f'{n14} notas de 1')
    if 50 > n % 50 >= 20:
        n15 = n % 50 // 20
        print(f'{n15} notas de 20')
        if n % 50 % 20 >= 10:
            n17 = n % 50 % 20 // 10
            print(f'{n17} notas de 10')
            if 10 > n % 50 % 20 % 10 > 1:
                n18 = n % 50 % 20 % 10 // 1
                print(f'{n18} notas de 1')
        if 0 < n % 50 % 20 < 10:
            n16 = n % 50 % 20 // 1
            print(f'{n16} notas de 1')
        if 70 > n and n % 50 >= 20:
            n2 = n % 50 // 20
            print(f'{n2} notas de 20 a')
            if n % 50 % 20 >= 10:
                n3 = n % 50 % 20 // 10
                print(f'{n3} notas de 10')
                if n % 50 % 20 % 10 >= 1:
                    n4 = n % 50 % 20 % 10 // 1
                    print(f'{n4} notas de 1')
    if 20 <= n < 50:
        n5 = n // 20
        print(f'{n5} notas de 20')
        if n % 20 >= 10:
            n6 = n % 20 // 10
            print(f'{n6} notas de 10')
            if n % 20 % 10 >= 1:
                n7 = n % 20 % 10 // 1
                print(f'{n7} notas de 1')
        if 10 > n % 20 > 0:
            n11 = n % 20 // 1
            print(f'{n11} notas de 1')
    if 10 <= n < 20:
        n8 = n // 10
        print(f'{n8} notas de 10')
        if n % 10 >= 1:
            n9 = n % 10 // 1
            print(f'{n9} notas de 1')
    if 1 <= n < 10:
        n10 = n // 1
        print(f'{n10} notas de 1')
    if totc == totc:
        break
print('''obrigado por utilizar o banco python
fim''')
