cidade = str(input('digite o nome de uma cidade que tenha santo no nome')).strip()
c = cidade.lower()
cs = 'santo' in c
print(f'a sua cidade é {cs}')
