print('\033[97mdigite dois numeros e eu direi qual é maior')
n1 = float(input('primeiro numero:'))
n2 = float(input('segundo numero :'))
if n1 > n2:
    print(f'mentre {n1} e {n2} o maior é {n1}')
elif n2 > n1:
    print(f'entre {n1} e {n2} o maior é {n2}')
else:
    print(f'{n1} e {n2} são iguais')
