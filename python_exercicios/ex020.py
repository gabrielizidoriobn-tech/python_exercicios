import random

print('para determinar a sequencia de alunos a apresentar o trabalho, digite os nomes')
a1 = input('aluno 1')
a2 = input('aluno 2')
a3 = input('aluno 3')
a4 = input('aluno 4')
# l = [a1, a2, a3, a4]
lr = random.sample([a1, a2, a3, a4],4)
print(f'a sequencia a ser apresentada é {lr}')
# ordem = random.choices(l,k=4)
# print(f'a ordem sera {ordem}')
