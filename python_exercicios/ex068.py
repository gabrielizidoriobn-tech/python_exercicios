from random import randint
while True:
    print('vamos jogar par ou impar')
    j = int(input('digite um numero de 1 a 10:'))
    ip = str(input('escolha impar ou par [I/P]')).strip().lower()
    c = randint(1, 10)
    s = j + c
    if s % 2 == 0:
        print(f'''o jogador jogou {j} e o computador jogou {c}
a soma dos valores é {s} par''')
        if ip == 'p':
            print('jogador venceu')
        elif ip == 'i':
            print('computador venceu')
            break
    elif s % 2 == 1:
        print(f'''o jogador jogou {j} e o computador jogou {c}
a soma dos valores é {s} impar''')
        if ip == 'i':
            print('jogador venceu')
        elif ip == 'p':
            print('computador venceu')
            break
print('jogo encerrado')
