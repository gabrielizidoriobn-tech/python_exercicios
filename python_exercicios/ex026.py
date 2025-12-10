frase = str(input('digite uma frase')).strip().lower()
print(f'a letra A aparece {frase.count('a')} vezes')
print(f'ela se encontra primeiro na posição {frase.find('a')+1}')
print(f'e aparece por ultimo na posição {frase.rfind('a')+1}')
