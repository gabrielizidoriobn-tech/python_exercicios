def leiaint(numero):
    print('_'*20)
    while not numero.isnumeric():
        numero = (input('digite um numero:'))
        if numero.isnumeric():
            break
        else:
            while not numero.isnumeric():
                print('\033[1;31;40merro, digite um numero inteiro valido')
                numero = (input('\033[mdigite um numero:'))
    return numero


#programa principal
n = leiaint('digite um numero:')
print(f'\033[1;32;40mvoce digitou o numero {n}')

#forma do guanabara
# def leiaint(msg):
#     ok = False
#     valor = 0
#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('\033[0;31mERRO! Digite um numero inteiro valido\033[m')
#         if ok:
#             break
#     return valor
# n = leiaint('digite um numero:')
# print(f'voce acabou de digitar o numero {n}')
