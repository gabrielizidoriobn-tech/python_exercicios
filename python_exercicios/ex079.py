lista = []
while True:
    numero = (int(input(f'digite um numero:')))
    if numero in lista:
        print(f'valor duplicado, não posso adicionar !')
    else:
        lista.append(numero)
    s_n = str(input(f'deseja continuar ? [S/N]:')).strip().upper()
    if s_n == 'N':
        break
lista.sort()
print(lista)
