from moeda import metade, dobro, aumentar, diminuir, formato

preço = int(input('digite o preço:'))
print(f'''a metade de {formato(preço)} é {metade(preço)}
o dobro de {formato(preço)} é {dobro(preço)}
{formato(preço)} mais 10% é {aumentar(preço, 10)}
{formato(preço)} menos 13% é {diminuir(preço, 13)}''')
