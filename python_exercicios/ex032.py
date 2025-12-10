from datetime import date
ano = int(input('\033[1;97;42mdigite um ano qualquer ou digite zero para o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'\033[1;97;40mo ano \033[4;30;107m{ano}\033[1;97;40m é bissexto')
else:
    print(f'\033[1;97;40mo ano \033[4;30;107m{ano}\033[1;97;40m é bissexto')
