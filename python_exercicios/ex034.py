s = int(input('\033[97minforme o seu salario:'))
if s > 1250:
    print(f'\033[97mo seu aumento é de \033[32m{s * (11 / 10):.2f}')
else:
    print(f'\033[97mo seu aumento é de \033[32m{s * (11.5 / 10):.2f}')
