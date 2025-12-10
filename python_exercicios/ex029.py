cores = {'limpa': '\033[m', 'branca': '\033[97;40m', 'verde': '\033[1;32;107m', 'vermelho': '\033[1;31m'}
v = int(input(f'{cores['branca']}qual a velocidade do carro ?{cores['limpa']}'))
v_l = (v - 80) * 7
from time import sleep

print('=' * 12)
print(f'{cores['branca']}processando{cores['limpa']}')
print('=' * 12)
sleep(3)
if v > 80:
    print(f'{cores['branca']}voce ultrapassou o limite, a sua multa sera de{cores['limpa']}\n==={cores['vermelho']}{v_l}{cores['limpa']}===')
# else:
#     print(f'voce ultrapassou o limite, sua multa sera de\n___{v_l}___')
print(f'{cores['verde']}tenha um bom dia e dirija com segurança{cores['limpa']}')
