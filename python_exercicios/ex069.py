maiores = masculino = mm = 0
while True:
    idade = int(input('quantos anos voce tem ?:'))
    sexo = str(input('qual o seu sexo ? [M / F]:')).strip().lower()
    if idade > 18:
        maiores += 1
    if sexo == 'm':
        masculino += 1
    if sexo == 'f' and idade > 20:
        mm += 1
    c = str(input('deseja continuar? [S / N]')).strip().lower()
    if c == 'n':
        break
print(f'''entre as pessoas cadastradas ha 
{maiores} pessoas maiores de 18 anos
{masculino} homens
{mm} mulheres com mais de 20 anos
fim''')
