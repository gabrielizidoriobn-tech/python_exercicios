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

def leiafloat(flo):
    while True:
        try:
            real = float(input(f'{flo}'))
        except ValueError:
            print('\033[31mERRO:\033[m digite um numero real')
        except KeyboardInterrupt:
            print('\no programa foi interrompido')
            real = 0
            break
        else:
            break
    return real


#programa principal
i = leiaint('digite um numero inteiro:')
r = leiafloat('digite um numero real:')
print(f'\033[1;32;40mo numero inteiro digitado foi {i} e o real foi {r}')
