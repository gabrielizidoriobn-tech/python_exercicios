print('contador de numeros pares!')
n1 = int(input('digite o primeiro numero:'))
n2 = int(input('digite o segundo numero:'))
for p in range(n1, n2):
    if p % 2 == 0:
        print(p)
