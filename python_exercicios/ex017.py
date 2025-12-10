'''from math import sqrt as r
from math import pow as p'''
from math import hypot as h
co = float(input('qual o cateto oposto'))
ca = float(input('qual o cateto adjacente'))
#s = p(2,co) + p(2,ca)
hi = h(co,ca)
print(f'a hipotenusa é igual raiz quadrada da soma do seu cateto oposto{co}')
print(f'mais o seu cateto adjacente {ca}')
#print(f'que é igual a {r(s)}')
print(f'é igual a {hi}')
