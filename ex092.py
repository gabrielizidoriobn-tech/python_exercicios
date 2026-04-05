dados = {}
dados['nome'] = str(input('nome:'))
dados['nascimento'] = int(input('ano de nascimento:'))
dados['numero'] = int(input('numero da cartira de trabalho:'))
if dados['numero'] == 0:
    print(f'''nome tem o valor {dados['nome']}
    ano de nascimento tem o valor {dados['nascimento']}''')
    print(f'ctps tem o valor {dados["numero"]}.')
else:
    dados['contrato'] = int(input('ano de contratação:'))
    dados['salario'] = float(input('salario:'))
    dados['aposentadoria'] = (dados['contrato'] - dados['nascimento']) +35
    print(f'''nome tem o valor {dados['nome']}
ano de nascimento tem o valor {dados['nascimento']}''')
    print(f'''aposentadoria tem o valor {dados['aposentadoria']}''')
