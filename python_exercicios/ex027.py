nome = str(input('digite o seu nome completo:')).strip()
# print(f'ola {nome}\no seu primeiro nome é {nome[:nome.find(' ')]}\ne o seu ultimo nome é {nome[nome.rfind(' '):]}')
nomes = nome.split()
print(f'ola {nome}\no seu primeiro nome é {nomes[0]}\ne o seu ultimo nome é {nomes[len(nomes)-1]}')
