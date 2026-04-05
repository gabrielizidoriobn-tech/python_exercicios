def fatorial(num, show=False):
    """def fatorial: faz o fatorial do numero digitado
    parametro num: numero do fatorial a ser calculado
    parametro show: (opcional) True, mostra o calculo
    parametro show: (opcional) False, mostra apenas o resultado """
    resp = 1
    lista = []
    for a in range(1, num + 1):
        resp *= a
        lista.append(a)
        lista.append('x')
    del lista[len(lista) - 1]
    lista.insert(len(lista), '=')
    print(f'_'*25)
    if show:
            for n in lista:
                print(f'{n}', end=' ')
            return resp
    else:
        return resp


#programa principal
print(fatorial(7, show = True))
help(fatorial)
