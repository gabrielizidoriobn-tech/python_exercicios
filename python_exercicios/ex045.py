import emoji

pedra = emoji.emojize('✊')
papel = emoji.emojize('✋')
tesoura = emoji.emojize('✌️')
from random import choice

lista = [pedra, papel, tesoura]
aleatorio = choice(lista)
print('jo ken po')
print(f'''selecione a sua opção, digite
1 para {pedra}
2 para {papel}
3 para {tesoura}''')
opção = str(input('qual a sua opção:'))
if opção == '1' and aleatorio == pedra:
    print(f'{pedra} com {aleatorio} da empate')
elif opção == '2' and aleatorio == papel:
    print(f'{papel} com {papel} da empate')
elif opção == '3' and aleatorio == tesoura:
    print(f'{tesoura} com {aleatorio} da empate')
elif opção == '1' and aleatorio == papel:
    print(f'a sua {pedra} perde para o meu {aleatorio}')
elif opção == '2' and aleatorio == tesoura:
    print(f'o seu {papel} perde para minha {aleatorio}')
elif opção == '3' and aleatorio == pedra:
    print(f'a sua {tesoura} perde para minha {aleatorio}')
elif opção == '1' and aleatorio == tesoura:
    print(f'parabens, a sua {pedra} ganhou da minha {aleatorio}')
elif opção == '2' and aleatorio == pedra:
    print(f'parabens, o seu {papel} ganha da minha {aleatorio}')
elif opção == '3' and aleatorio == papel:
    print(f'parabens, a sua {tesoura} ganha do meu {papel}')
else:
    print(f'a opção {opção} não é uma escolha valida')
