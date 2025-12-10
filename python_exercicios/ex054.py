from datetime import date
hoje = date.today().year
jovem = 0
adulto = 0
for a in range(0, 7):
    idade = int(input('digite o seu ano de nascimento:'))
    maioridade = hoje - idade
    if maioridade >= 18:
        adulto += 1
    else:
        jovem += 1
print(f'o seu grupo é formado por {adulto} adultos e {jovem} jovens')
