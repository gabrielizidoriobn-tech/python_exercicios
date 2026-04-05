def dobro(p):
    dobr = p * 2
    return formato(dobr)


def metade(p):
    metad = p / 2
    return formato(metad)


def aumentar(p, i):
    aumento = p + (p * (i/100))
    return formato(aumento)


def diminuir(p, i):
    diminuto = p - (p * (i/100))
    return formato(diminuto)

def formato(p):
    return f'R${p:.2f}'.replace('.', ',')
