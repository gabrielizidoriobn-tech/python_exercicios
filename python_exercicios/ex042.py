print('analise de triangulos')
print('informe o comprimento de cada segmento')
a = int(input('segmento 1:'))
b = int(input('segmento 2:'))
c = int(input('segmento 3:'))
triangulo = a + b > c and a + c > b and c + b > a
if triangulo and a == b == c:
    print(f'os segmentos {a}, {b} e {c} formam um triangulo  equilatero')
elif triangulo and a == b or b == c or c == a:
    print(f'os segmentos {a}, {b} e {c} formam um triangulo isoceles')
elif triangulo and a != b and b != c and c != a:
    print(f'os segmentos {a}, {b} e {c} formam um triangulo escaleno')
else:
    print(f'os segmentos {a}, {b} e {c} não formam um triangulo')
