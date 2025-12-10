print('sequencia de fibonacci')
n = int(input('quantos termos da sequencia de fibonacci voce quer ver?:'))
t1 = 0
t2 = 1
cont = 3
# t1  t2  t3
# 0 - 1 - 1
#     t1  t2  t3
print(f'{t1} - {t2}', end=' - ')
while cont <= n:
    t3 = t1 + t2
    print(f'{t3}', end=' - ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
