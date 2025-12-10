cont = acum = 0
n = int(input('digite um numero [999 para encerrar]:'))
while n != 999:
    cont += 1
    acum += n
    n = int(input('digite um numero [999 para encerrar]:'))
print(f'o numero de termos digitados foi {cont} e a soma é {acum}')
