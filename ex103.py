def ficha(n = False, g = 0):
    if n:
        print(f'o jogador {n} fez {g} gols')
    else:
        print(f' o jogador <desconhecido> fez {g} gols')

numeros = '1234567890'
nome = str(input('nome do jogador:')).strip()
for n in nome:
    if n in numeros:
        nome = ''

letras = 'asdfghjklçqwertyuiopzxcvbnm'
gols = (input('gols feitos:')).strip()
for g in gols:
    if g in letras:
        gols = 0
if gols == '':
    gols = 0

ficha(nome, gols)
