print('calculadora de IMC')
altura = float(input('qual a sua altura:'))
peso = float(input('qual o seu peso:'))
imc = peso / altura ** 2
print(f'de acordo com a sua altura de {altura} metros, e o seu peso de {peso}KG o seu IMC é {imc:.2f} e voce esta')
if imc < 18.5:
    print('abaixo do peso')
elif imc < 26:
    print('no seu peso ideal')
elif imc < 31:
    print('com sobrepeso')
elif imc < 41:
    print('com obesidade\nprocure ajuda rapido')
else:
    print('com obesidade morbida\nALERTA DE RISCO\nprocure ajuda urgentemente')
