num = int(input('digite um numero de 0 a 9999, e eu mostrarei as casas numericas'))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'analisando o numero {num}')
print(f'unidade {u}')
print(f'dezena {d}')
print(f'centena {c}')
print(f'milhar {m}')
