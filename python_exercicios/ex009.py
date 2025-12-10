print('ola, me de um numero e eu irei mostrar a sua taboada')
a = float(input('qual o seu numero ?'))
print('-' * 15)
print('a sua taboada é')
print(
    '{:.0f}x1={:.0f}\n{:.0f}x2={:.0f}\n{:.0f}x3={:.0f}\n{:.0f}x4={:.0f}\n{:.0f}x5={:.0f}'.format(a, a * 1, a, a * 2, a,
                                                                                                 a * 3, a, a * 4, a,
                                                                                                 a * 5))
print(
    '{:.0f}x6={:.0f}\n{:.0f}x7={:.0f}\n{:.0f}x8={:.0f}\n{:.0f}x9={:.0f}\n{:.0f}x10={:.0f}'.format(a, a * 6, a, a * 7, a,
                                                                                                  a * 8, a, a * 9, a,
                                                                                                  a * 10))
print('-' * 15)
