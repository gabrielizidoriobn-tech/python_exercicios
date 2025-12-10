print('=' * 10)
print('olimpiedas')
print('=' * 10)
from datetime import date

nascimento = int(input('informe o seu ano de nascimento para saber a sua categoria:'))
data = date.today().year
idade = data - nascimento
print(f'voce tem {idade} anos e ', end='')
if idade <= 9:
    print('a sua categoria é mirim')
elif idade < 15:
    print('a sua categoria é infantil')
elif idade < 20:
    print('a sua categoria é junior')
elif idade < 26:
    print('a sua categoria é senior')
else:
    print('a sua categoria é master')
