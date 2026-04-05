aluno = {}
aluno['nome'] = (input('nome do aluno:')).strip().lower()
aluno['media'] = float(input(f'media do {aluno['nome']}:'))
if aluno['media'] >= 7:
    situação = 'aprovado'
else:
    situação = 'reprovado'
print(f'+-+'*15)
print(f'''o nome do aluno é: {aluno['nome']}
a media do aluno é: {aluno['media']}
e a situação do aluno é: {situação}''')
if aluno['media'] >= 7:
    print(f'parabens, aproveite as ferias')
else:
    print(f'sinto muito, boa sorte na recuperação')
