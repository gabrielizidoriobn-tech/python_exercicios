print('conversor de bases numericas')
n = int(input('digite um numero decimal:'))
print('''digite 1 para converter para binario
digite 2 para converter para octal
digite 3 para converter para hexadecimal''')
opção = int(input('qual a sua opção?:'))
if opção == 1:
    print(f'o numero {n} em binario é {bin(n)[2:]}')
elif opção == 2:
    print(f'o numero {n} em octal é {oct(n)[2:]}')
elif opção == 3:
    print(f'o numero {n} em hexadecimal é {hex(n)[2:]}')
else:
    print(f'a escolha {n} não é valida')
