from datetime import date

print('alistamento militar')
genero = str(input('''informe o seu genero:
masculino
femenino
''')).strip().lower()
data = date.today().year
nascimento = int(input('informe o seu ano de nascimento:'))
idade = data - nascimento
if genero == 'femenino':
    print('voce não pode se alistar')
elif genero == 'masculino' and idade > 18:
    print(f'voce nasceu no ano {nascimento} e tem {idade} anos')
    print(f'o ano em que voce devia ter se alistado foi {data - (idade - 18)} e voce esta {idade - 18} anos atrasado')
elif genero == 'masculino' and idade < 18:
    print(f'voce nasceu no ano {nascimento} e tem {idade} anos')
    print(f'o ano em que voce vai se alistar é {18 - idade + data} e ainda falta {18 - idade} anos para o seu alistamento')
elif genero == 'masculino':
    print(f'esse é o ano do seu alistamento, compareça a junta militar')
