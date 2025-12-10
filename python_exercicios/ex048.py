print('soma de numeros impares de 1 ate 500')
soma = 0
cont = 0
for i in range(1, 500):
    if i % 2 == 1 and i % 3 == 0:
        cont += 1
        soma += i
print(f'a soma dos {cont} valores é igual a {soma}')
