print(
    '\033[1;32mparabens, voce chegou ao seu exercicio numero 50, continue assim e não desista voce esta quase la\033[m')
print('contador de numeros pares')
cont = 0
soma = 0
for p in range(1, 7):
    num = int(input(f'digite o {p} valor :'))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'a soma dos {cont} numeros pares é {soma}')
