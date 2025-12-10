soma = cont = 0
while True:
    n = int(input('digite um numero [condição de parada 999]:'))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'a quantidade de numeros digitados foi {cont} e a soma deles é {soma}')
