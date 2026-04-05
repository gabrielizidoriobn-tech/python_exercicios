def area(a, b):
    c = a * b
    print(f'a area do seu terreno de {a} x {b} é {c} M²')

print('consulta de area de terrenos')
print(f'_'*30)
largura = float(input('qual a largura do terreno:'))
comprimento = float(input('qual o comprimento da terreno:'))
print(f'_'*30)
area(largura, comprimento)
