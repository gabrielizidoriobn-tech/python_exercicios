def notas(*n, sit = False):
    """notas: função para calcular total, maior, menor, media e (opcional) situação das notas
    parametro n: parametro que recebe uma quantidade variavel de notas
    parametro sit (opcional): parametro para mostrar situação das notas
    return: retorna um dicionario com os dados da notas"""
    resp = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n) / len(n)}
    if sit:
        if resp['media'] >= 8:
            resp['situação'] = 'boa'
        elif resp['media'] >= 6:
            resp['situação'] = 'razoável'
        else:
            resp['situação'] = 'ruim'
    return resp


resp = notas(8.3, 7.6, 9.5, 9, sit=True)
print(resp)
help(notas)
