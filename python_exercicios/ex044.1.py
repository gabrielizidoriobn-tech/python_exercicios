valor = float(input('digite o valor da sua compra:'))
opção = int(input('''selecione a sua opção de pagamento abaixo
digite 1 para a vista no dinheiro ou cheque
digite 2 para a vista no debito
digite 3 para parcelar em 2x
digite 4 para parcelar em 3x ou mais
:'''))
if opção == 1:
    total = valor * (90/100)
elif opção == 2:
    total = valor * (95/100)
elif opção == 3:
    total = valor
elif opção == 4:
    total = valor * (120/100)
    parcelas = int(input('quantas parcelas?:'))
    valpar = total / parcelas
    print(f'a sua compra sera parcelada em {parcelas} parcelas de {valpar}')
else:
    print(f'a opção {opção} não é valida')
print(f'''voce escolheu a opção {opção} como forma de pagamento, a sua compra de {valor}
vai custar {total:.2f}''')
