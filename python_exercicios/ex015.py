print('digite os dias e a kilometragem rodada nesses dias para calcular o valor a ser pago')
d = int(input('dias ?'))
k = float(input('kilometragem ?'))
a = d*60+k*0.15
print(f'o valor total a ser pago é de {a:.2f}')
