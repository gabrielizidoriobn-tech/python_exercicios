def linha(t=30):
    return '-' * t

def cabeçalho(txt):
    print(linha())
    print(txt.center(len(linha())))
    print(linha())

def leiaint(inte):
    while True:
        try:
            inteiro = int(input(f'{inte}'))
        except ValueError:
            print('\033[31mERRO:\033[m digite um numero inteiro')
        except KeyboardInterrupt:
            print('\no programa foi interrompido')
            inteiro = 0
            break
        else:
            break
    return inteiro

def menu(options):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for o in options:
        print(f'{cores['amarelo']}{c}{cores['limpa']} - {cores['azul']}{o}{cores['limpa']}')
        c += 1
    print(linha())
    opc = leiaint('sua opção:')
    return opc

cores = {'vermelho': '\033[31m', 'amarelo': '\033[33m', 'azul': '\033[34m', 'limpa': '\033[m'}
