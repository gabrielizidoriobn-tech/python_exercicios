import urllib
import urllib.request

url = 'https://www.pudim.com.br'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
req = urllib.request.Request(url, headers=headers)

try:
    site = urllib.request.urlopen(req)
except urllib.error.HTTPError as erro:
    print(f'\033[31mO site retornou um erro HTTP: {erro.code}\033[m')
except urllib.error.URLError as erro:
    print(f'\033[31mFalha de rede. Motivo: {erro.reason}\033[m')
else:
    print(f'\033[32mSite acessado com sucesso!\033[m')
