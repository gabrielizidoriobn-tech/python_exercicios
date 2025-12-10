#forma do guanabara
# sexo = str(input('informe seu sexo [F/M]:')).strip().upper()[0]
# while sexo not in 'FM':
#     sexo = str(input('dados invalidos, por favor informe seu sexo:')).strip().upper()[0]
# print(f'sexo {sexo} registrado com sucesso')

s = ''
while s != 'm' and s != 'f':
    s = str(input('informe o seu sexo, escolha entre as opções [M / F]:')).lower().strip()
    if s == 'f':
        print('voce escolheu o sexo femenino')
    elif s == 'm':
        print('voce escolheu o sexo masculino')
    else:
        print(f'a opção [{s}] não é valida')
print(f'obrigado por colaborar')
