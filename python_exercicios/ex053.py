print('detector de palindromos')
frase = str(input('digite uma frase:')).replace(' ', '').upper()
fr = frase[::-1]
print(f'a frase {frase} escrita ao contrario é {fr}', end=' ')
if frase == fr:
    print('e é um \033[32mpalindromo')
else:
    print('e não é um \033[31mpalindromo')
