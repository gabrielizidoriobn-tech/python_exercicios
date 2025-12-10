print('progressão aritmetica')
p = int(input('primeiro termo:'))
r = int(input('razão:'))
d = p + (10 - 1) * r
for pa in range(p, d + r, r):
    print(f'-> {pa} ', end='')
print('->acabou')
