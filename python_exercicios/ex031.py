distancia = int(input('\033[4;30;45mqual a distancia da sua viagem:'))
# if distancia > 200:
#     print(f'o valor da sua passagem é de {distancia*0.45:.2f}$R')
# else:
#     print(f'o valor da sua passagem é de {distancia*0.50:.2f}$R')
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'\033[4;97mo valor da sua passagem é de \033[1;32m{preço:.2f} $R\033[m')
