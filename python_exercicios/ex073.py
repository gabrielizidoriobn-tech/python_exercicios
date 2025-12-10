colocados = ('BOTA FOGO', 'PALMEIRAS', 'FLAMENGO', 'FORTALEZA', 'INTERNACIONAL', 'SÃO PAULO'
             , 'CORINTHIANS', 'BAHIA', 'CRUZEIRO', 'VASCO DA GAMA', 'EC VITORIA', 'ATLETICO-MG',
             'FLUMINENSE', 'GREMIO', 'JUVENTUDE', 'BRAGANTINO', 'ATLETICO-PR', 'CRICIUMA',
             'ATLETICO-GO', 'CUIABA')
chapecoense = str('o chapecoense se encontra no 15° lugar da serie B do brasileirão')
print(f'os primeiros 5 colocados são:{colocados[0:5]}')
print(f'os ultimos 5 colocados são:{colocados[15:21]}')
print(f'aqui esta uma lista em ordem alfabetica')
tupla_ordenada = tuple(sorted(colocados))
print(tupla_ordenada)
print(chapecoense)
