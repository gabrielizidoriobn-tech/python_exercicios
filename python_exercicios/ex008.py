print('ola, me de uma medida em metros e eu irei converter para cm, mm, km, dam, dm e hm')
a = float(input('qual a sua medida ?'))
# km hm dam m dm cm mm
b = a*100
c = a*1000
d = a/1000
e = a/10
f = a*10
g = a/100
print(f'em cm é {b}')
print(f'em mm é {c}')
print(f'em km é {d}')
print(f'em dam é {e}')
print(f'em dm é {f}')
print(f'em hm é {g}')
