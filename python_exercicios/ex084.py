lista = []
while True:
    sublista = [str(input('qual o seu nome ?:')), float(input('qual o seu peso ?:'))]
    lista.append(sublista)
    while True:
        s_n = str(input('deseja continuar ?[S_N]:')).strip().lower()
        if s_n in ['s', 'n']:
            break
        print('sua resposta é invalida tente de novo')
    if s_n == 'n':
        break
maiorpeso = max([pessoa[1] for pessoa in lista])
nome1 = [pessoa[0] for pessoa in lista if pessoa[1] == maiorpeso]
menorpeso = min([pessoa[1] for pessoa in lista])
nome2 = [pessoa[0] for pessoa in lista if pessoa[1] == menorpeso]
print(f'''o total de pessoas cadastradas foi de {len(lista)}
o maior peso é de {','.join(nome1)} pesando {maiorpeso}
o menor peso é de {','.join(nome2)} pesando {menorpeso}''')
print(lista)
