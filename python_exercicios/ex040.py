n1 = float(input('digite sua primeira nota:'))
n2 = float(input('digite sua segunda nota :'))
m = (n1 + n2) / 2
print(f'a media de {n1} e {n2} é {m:.1f}')
if m >= 7:
    print('parabens voce esta aprovado')
elif 7 > m >= 5:
    print('voce esta de recuperação, estude mais')
else:
    print('sinto muito, voce esta reprovado')
