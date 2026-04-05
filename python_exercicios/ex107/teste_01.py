import moeda

preço = int(input('digite o preço:'))
print(f'''a metade de {preço} é {moeda.metade(preço)}
o dobro de {preço} é {moeda.dobro(preço)}
{preço} mais 10% é {moeda.aumentar(preço, 10)}
{preço} menos 13% é {moeda.diminuir(preço, 13)}''')
