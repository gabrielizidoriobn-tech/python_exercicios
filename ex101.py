def voto(y):
    if 17 < y < 66:
        return 'OBRIGATORIO'
    elif y < 16:
        return 'PROIBIDO'
    else:
        return 'OPCIONAL'


#programa principal
from datetime import date
hj = date.today().year
ano = int(input('digite seu ano de nascimento: '))
idade = hj - ano
print(f'se a sua idade é {idade}, o seu voto é {voto(idade)}')
