'''i = int(input('inicio:'))
f = int(input('fim:'))
p = int(input('passo:'))
for c in range(i, f+1, p):
    print(c)
print('fim')
s = 0
for c in range(0, 4):
    n = int(input('digite um numero:'))
    s += n
print(f'a soma de todos os valores é:{s}')'''
from playsound3 import playsound
caminho = 'C://Users//HP//Downloads//rupert-holmes-escape-the-pina-colada-song-1979-(mp3-made-with-Voicemod.mp3'
import emoji

sorrir = emoji.emojize('😊')
fogos = emoji.emojize('🎉')
print(f'feliz aniversario!{sorrir}')
enter = bool(input('para comemorar pressione enter'))
from time import sleep

for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print(fogos * 3)
playsound(caminho)
