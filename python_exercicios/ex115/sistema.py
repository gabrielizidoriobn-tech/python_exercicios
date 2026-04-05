from lib.interface import *
from lib.arquivo import *

cores = {'vermelho': '\033[31m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'limpa': '\033[m'}
arq = 'cadastro.txt'
if not arquivoexiste(arq):
    criararquuivo()

while True:
    resposta = menu(['ver pessoas cadastradas', 'cadastrar nova pessoa', 'sair do sistema'])
    if resposta == 1:
        lerarquivo('cadastro.txt')
    elif resposta == 2:
        with open('cadastro.txt', 'a', encoding='utf-8') as arquivo:
            nome = (str(input('Digite o nome: ')))
            idade = leiaint('Digite a idade: ')
            cadastrar('cadastro.txt',nome, idade)
    elif resposta == 3:
        break
    else:
        print(f'{cores['vermelho']}ERRO{cores['limpa']}: {resposta} não é uma opção valida!')
cabeçalho('programa encerrado')
