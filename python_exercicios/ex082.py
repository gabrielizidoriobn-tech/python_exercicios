lista = []
par = []
impar = []
while True:
    n = int(input('digite um numero:'))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    s_n = str(input('deseja continuar? [S / N]:')).strip().lower()
    if s_n == 'n':
        break
print(f'''a lista completa é {lista}
os numeros pares são {par}
e os numeros impares são {impar}''')
