from random import randint

def sorteio(num):
    for i in range(1, 6):
        numeros.append(randint(1, 10))
    print(f'lista sorteada, os valores sorteados foram {numeros}')


def somapar(num):
    par = 0
    for n in num:
        if n % 2 == 0:
            par += n
    print(f'a soma dos valores pares é {par}')


#programa principal
numeros = []
sorteio(numeros)
somapar(numeros)
