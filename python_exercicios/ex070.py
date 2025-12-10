total = caro = menor = cont = 0
barato = ''
while True:
    nome = str(input('qual o produto escolhido:')).strip()
    preço = float(input('qual o preço do produto:'))
    cont += 1
    if preço > 1000:
        caro += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    total += preço
    continuar = str(input('deseja continuar ? [S/N]:')).strip().lower()
    while continuar != 'n' and continuar != 's':
        continuar = str(input('deseja continuar ? [S/N]:')).strip().lower()
    if continuar == 'n':
        break
print(f'''o total gasto foi de {total}, a quantidade de produtos a cima de 1000 foi {caro}
e o item mais barato foi o {barato} e ele custou {menor}''')
