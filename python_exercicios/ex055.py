peso = float(0)
maior = menor = None
for p in range(0, 5):
    peso = float(input(f'pessoa n {p + 1}, digite seu peso:'))
    if p == 1:
        maior = 1
        menor = 1
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'o maior peso é {maior} e o menor peso é {menor:.1f}')
