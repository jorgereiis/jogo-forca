#!/user/bin/env python3
"""Jogo da Forca - Projeto Infernal
Como usar:
Rodar o programa, escolher a opção desejada e passar as letras para acertar a palavra da forca.
"""
__version__ = '0.0.1'
__author__ = 'Jorge Reis'
__license__ = 'Unlicense'

# Importando as bibliotecas necessárias
from palavras import passphrase
from layout_forca import inicial, chances
import ranking
import os

# Variáveis globais
print('-=-=-=-=-=-=-\nJOGO DA FORCA\n-=-=-=-=-=-=-\n')
op = int(input('ESCOLHA UMA OPÇÃO:\n1 - JOGAR\n2 - VER RANKING\n3 - CADASTRAR PALAVRA\n4 - SAIR\n'))
sair = True
acertos = 0
erros = 0
l_erradas = ''
l_certas = ''

# Loop principal
while acertos < len(passphrase) and erros != 6:
    palavra = ''
    for letra in passphrase:
        if letra in l_certas:
            palavra += letra + ' '
        else:
            palavra += '_ '
    print('{}{}'.format(inicial, chances[erros]))
    print('\n\nPALAVRA:',palavra)
    
    letra = input('\n\n\n\nDigite uma letra: ').upper()
    os.system('cls')
    
    if letra in l_certas+l_erradas:
        print('Você já tentou essa letra. Escolha uma diferente!')
        continue

    if letra in passphrase:
        print('ACERTOOOOOOOU!')
        l_certas = l_certas + letra
        acertos = acertos + passphrase.count(letra)
    else:
        print('Que pena. Letra errada!')
        l_erradas = l_erradas + letra
        erros = erros + 1
if acertos == len(passphrase):
    print('VOCÊ ESCAPOU DA FORCA. PARABÉNS!!')
    print('A palavra completa é: {}'.format(passphrase))
elif erros == 6:

    print(inicial+chances[erros])
    print('VOCÊ PERDEU E POR ISSO FOI ENFORCADO!!!!\nHAHAHAHAHAHAHAHA!!!\n>>>>>>> S3 f#d#u <<<<<<<<')
