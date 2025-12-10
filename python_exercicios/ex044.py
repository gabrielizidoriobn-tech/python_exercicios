valor = float(input('qual o valor da sua compra:'))
forma = int(input('''selecione a sua forma de pagamento abaixo
digite:
1 para a vista no dinheiro ou cheque
2 para a vista no debito
3 para em ate 2x no credito
4 para 3x ou mais no credito:'''))
print(f'voce escolheu a opção {forma} para forma de pagamento')
if forma == 1:
    print(f'a sua compra de {valor} vai custar {valor * (90/100)}')
elif forma == 2:
    print(f'a sua compra de {valor} vai custar {valor * (95/100)}')
elif forma == 3:
    print(f'a sua compra vai custar {valor}')
elif forma == 4:
    parcelas = int(input('em quantas parcelas voce gostaria de dividir:'))
    print(f'''a sua compra de {valor} vai custar {valor * (120/100):.2f}
e sera parcelado em {parcelas} vezes no valor de {valor / parcelas} por parcela''')
else:
    print(f'a escolha {forma} não é uma opção valida')
