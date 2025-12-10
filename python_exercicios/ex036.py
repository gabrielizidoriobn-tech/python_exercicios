cores = {'limpo': '\033[m', 'branco': '\033[97m', 'verde': '\033[32m', 'vermelho': '\033[31m'}
print(f'{cores['branco']}informe o valor da casa de sua escolha e o seu salario para uma avaliação de emprestemo')
valor_da_casa = float(input('qual o valor da casa ?:'))
salario = float(input('qual o seu salario ?:'))
porcentagem = salario * 30/100
tempo = int(input(f'em quantos anos sera financiada ?:{cores['limpo']}'))
valor_da_prestação = valor_da_casa / (tempo * 12)
if valor_da_prestação < porcentagem:
    print(f'{cores['verde']}parabens, o seu financiamento foi aprovado{cores['limpo']}')
else:
    print(f'{cores['vermelho']}sinto muito, a sua renda é insuficiente{cores['limpo']}')
print(f'{cores['branco']}o valor da prestação de uma casa de {cores['verde']}{valor_da_casa:.2f}{cores['branco']} financiado em {tempo} anos, é de {cores['verde']}{valor_da_prestação:.2f}')
