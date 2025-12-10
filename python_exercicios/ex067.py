from time import sleep
print('taboada')
while True:
    n = int(input('digite um numero:'))
    if n < 0:
        break
    for t in range(1, 11):
        m = n * t
        sleep(0.3)
        print(f'{n} x {t} = {m}')
print('Fim')
