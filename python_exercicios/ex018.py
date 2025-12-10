from math import radians,sin,cos,tan
angulo = float(input('digite um angulo'))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))
cosseno = cos(radians(angulo))
print(f'os valores do seu angulo são\nseno {seno:.2f}\ncosseno {cosseno:.2f}\n tangente {tangente:.2f}')
