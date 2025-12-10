lista = []
numeros = soma = terceiracoluna = maiorvalor = 0
for n in range(0, 3):
    for m in range(0, 3):
        numeros = (int(input(f'digite um valor para a posição {n},{m}:')))
        if numeros % 2 == 0:
            soma += numeros
        lista.append(numeros)
for t in range(2, 9, 3):
    terceiracoluna += (lista[t])
maiorvalor = max(lista[3:6])
for i in range(0, 9, 3):
    print(lista[i:i + 3])
print(f'''a soma dos valores pares é igual a: {soma} :
a soma dos valores da terceira coluna é igual a: {terceiracoluna} :
o maior valor da segunda linha é: {maiorvalor} :''')
