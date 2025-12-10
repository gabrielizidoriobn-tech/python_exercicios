print('digite o comprimento de tres seguimentos de reta')
a = float(input('\033[33m seguimento 1:'))
b = float(input('\033[34m seguimento 2:'))
c = float(input('\033[35m seguimento 3:'))
if a + b > c and a + c > b and b + c > a:
    print('\033[1;32m os seguimentos acima formam um triangulo')
else:
    print('\033[4;31m os seguimentos acima não formam um triangulo')
