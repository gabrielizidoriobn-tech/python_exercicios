print('me mostre quantos reais voce tem, e eu lhe mostrarei quantos dolares, euros, ienes, ')
print('pesos argentinos, bolivares venezuelanos, pesos mexicanos e yuan chineses, voce pode comprar')
real = float(input('quantos reais voce tem ?'))
dolar = real / 5.42
euro = real / 5.93
ienes = real * 29.07
peso_argentino = real * 168.82
bolivar_venezuelano = real * 6.72
peso_mexicano = real * 3.24
yuan = real * 1.34
print('com {:.2f} reais voce pode comprar\n{:.2f} dolares'.format(real, dolar))
print('{:.2f} euros\n{:.2f} ienes\n{:.2f} pesos argentinos\n{:.2f} bolivares venezuelanos'.format(euro,ienes,peso_argentino,bolivar_venezuelano))
print('{:.2f} pesos mexicanos\n{:.2f} yuan'.format(peso_mexicano, yuan))
