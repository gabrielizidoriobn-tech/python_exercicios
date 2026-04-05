

def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True

def criararquuivo(nome):
    try:
        with open('cadastro.txt', 'wt+', encoding='utf-8') as arquivo:
            for nome in arquivo:
                print(nome)
    except:
        print(f'\033[31mERROmna criação do arquivo\033[')
    else:
        print(f'\033[32marquivo criado com sucesso\033[m')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler arquivo')
    else:
        print(f'-'*30)
        print(f'{'pessoas cadastradas':^30}')
        print(f'-' * 30)
        for n in a:
            dado = n.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mERRO ao cadastrar\033[')
    else:
        try:
            a.write(f'{nome} ; {idade}\n')
        except:
            print('\033[31mERRO ao escrever\033[')
        else:
            print(f'novo registro de {nome} cadastrado com sucesso')
