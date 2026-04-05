def dobro(p, format = False):
    """função dobro: função que dobra um valor numerico
    parametro p:(preço) valor numerico a ser calculado
    parametro format:(booleano) valor booleano; verdadeiro ou falso"""
    dobr = p * 2
    return dobr if format is False else formato(dobr)


def metade(p, format = False):
    """função metade: função que divide um valor numerico por 2 para calcular o metade
    parametro p:(preço) valor numerico a ser calculado
    parametro format:(booleano) valor booleano; verdadeiro ou falso"""
    metad = p / 2
    return metad if format is False else formato(metad)


def aumentar(p, i, format = False):
    """função aumentar: função que aumenta um valor numerico em uma porcentagem
    parametro i: parametro que define a porcentagem a ser aumentada
    parametro p:(preço) valor numerico a ser calculado
    parametro format:(booleano) valor booleano; verdadeiro ou falso"""
    aumento = p + (p * (i/100))
    return aumento if format is False else formato(aumento)


def diminuir(p, i, format = False):
    """função diminuir: função que diminui um valor numerico em uma porcentagem
    parametro i: parametro que define a porcentagem a ser diminuida
    parametro p:(preço) valor numerico a ser calculado
    parametro format:(booleano) valor booleano; verdadeiro ou falso"""
    diminuto = p - (p * (i/100))
    return diminuto if format is False else formato(diminuto)

def formato(p):
    """função formato: formata um valor numerico para monetario
    parametro p: valor numerico a ser formatado"""
    return f'R${p:.2f}'.replace('.', ',')
