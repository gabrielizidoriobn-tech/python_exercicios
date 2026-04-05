def maior(*numeros):
    print('-=' * 30)
    print('Analisando os valores passados...')
    print(f'{numeros} foram informados {len(numeros)} valores ao todo')
    if not numeros:
        print(f'o maior valor informado foi 0')
    else:
        print(f'o maior valor informado foi {max(numeros)}')


maior(5, 3, 6, 1, 8, 2)
maior(9, 6, 2)
maior(1, 5)
maior(9)
maior()
