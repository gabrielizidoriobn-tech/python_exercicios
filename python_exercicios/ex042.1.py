print('analise de triangulos')
print('informe o comprimento de cada segmento')
a = int(input('segmento 1:'))
b = int(input('segmento 2:'))
c = int(input('segmento 3:'))
triangulo = a + b > c and a + c > b and c + b > a
if triangulo:
    print(f'os segmentos {a}, {b} e {c} formam um triangulo ', end='')
    if a == b == c:
        print('equilatero')
    elif a == b or b == c or c == a:
        print('escaleno')
    else:
        print('isoceles')
else:
    print(f'os segmentos {a}, {b} e {c} não formam um triangulo')
