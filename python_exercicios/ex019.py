import random
print('para realizar um sorteio, digite os nomes dos alunos')
a1 = str(input('aluno 1'))
a2 = str(input('aluno 2'))
a3 = str(input('aluno 3'))
a4 = str(input('aluno 4'))
l = [a1,a2,a3,a4]
print(f'o sorteado foi {random.choice(l)}')
