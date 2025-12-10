palavras = (
'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'\nna palavra {p} temos as vogais :', end=' ')
    for l in p:
        if l in 'AEIOU':
            print(f'{l}', end=' ')
