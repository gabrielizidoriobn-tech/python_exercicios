while True:
    n = int(input('digite um numero entre 0 e 20:'))
    if 0 <= n <= 20:
        break
tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez' 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'voce digitou  o numero {tupla[n]}')
