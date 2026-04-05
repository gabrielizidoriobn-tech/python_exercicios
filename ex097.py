def escreva(txt):
    dis = len(txt) + 3
    print(f'-' * (dis))
    print(f'{txt:^{dis}}')
    print('-' * dis)

lista = []
for d in range(0, 3):
    frase = str(input('qual frase deseja centralizar ?:'))
    lista.append(frase)
for f in lista:
    escreva(f)
