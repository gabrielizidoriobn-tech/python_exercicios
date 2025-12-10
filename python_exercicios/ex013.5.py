print('escolha um produto e eu erei calcular um desconto a vista e um aumento a prazo')
p = float(input('qual o valor do seu produto ?'))
d = p*(20/100)
a = p*5/100
print(f'a vista o seu desconto é de {d:.2f} e o valor total a ser pago é de {p-d:.2f}')
print(f'e a prazo o seu aumento é de {a:.2f} e o valor total a ser pago é de {p+a:.2f}')
