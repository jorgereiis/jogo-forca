#!/user/bin/env python3
"""Jogo da Forca - Projeto Infernal
Como usar:
Rodar o programa no console, escolher a opção desejada e passar as letras para acertar a palavra da forca.
EX: python3 jogo.py, ./jogo.py ou jogo.py
"""
__version__ = '0.1.1'
__author__ = 'Jorge Reis'
__license__ = 'Unlicense'

# Importando as bibliotecas necessárias
from time import sleep
from unicodedata import numeric
from layout_forca import inicial, chances
from random import choice
from ranking import salvar_ranking
import os

# Variáveis globais
sair = True

# Laço de repetição principal
while sair:
    # Variáveis locais
    passphrase = None
    acertos = 0
    erros = 0
    l_erradas = ''
    l_certas = ''

    # Menu de opções do jogo
    os.system('cls')
    print('-=-=-=-=-=-=-=-=-=-\n🎮 JOGO DA FORCA 🎮\n-=-=-=-=-=-=-=-=-=-\n')
    op = input('ESCOLHA UMA OPÇÃO:\n\n1️⃣  - JOGAR\n2️⃣  - VER RANKING\n3️⃣  - CADASTRAR PALAVRA\n4️⃣  - SOBRE\n5️⃣  - SAIR\n\n OPÇÃO: ')

    # Opção 1 (JOGAR)
    if op == '1':
        # Recebendo nome do jogador e iniciando o jogo
        os.system('cls')
        nome_jogador = input('Me diga aí, qual o seu nome❔❔\n')
        os.system('cls')
        print('Olá, {}!\n'.format(nome_jogador))
        print('Se prepare para a forca! 🙃\n')
        sleep(2)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        os.system('cls')
        
        # Carregando uma palavra aleatória de palavras.txt
        with open('palavras.txt') as arquivo:
            arq = arquivo.read()
            lista = arq.split('\n')
        passphrase = choice(lista).upper()

        # Laço de repetição interno de execução do jogo
        while acertos < len(passphrase) and erros != 6:
            palavra = ''
            for letra in passphrase:
                if letra in l_certas:
                    palavra += letra + ' '
                else:
                    palavra += '_ '
            print('{}{}'.format(inicial, chances[erros]))
            print('\n\nPALAVRA:',palavra)
            letra = input('\n\n\nDigite uma letra, {}: '.format(nome_jogador)).upper()
            
            # Verificando se a letra digitada já foi utilizada
            if letra in l_certas+l_erradas:
                os.system('cls')
                print('Você já tentou essa letra. Escolha uma diferente! 🤔')
                continue
            # Se a letra informada estiver na palavra, ela é adicionada ao acertos
            if letra in passphrase:
                os.system('cls')
                print('ACERTOOOOOOOU! 🥰🥰')
                l_certas = l_certas + letra
                acertos = acertos + passphrase.count(letra)
            # Se a letra informada não estiver na palavra, ela é adicionada ao erros
            else:
                os.system('cls')
                print('Que pena. Letra errada! ☹️☹️')
                l_erradas = l_erradas + letra
                erros = erros + 1
        # Se o jogador ganhou o jogo
        if acertos == len(passphrase):
            print('VOCÊ ESCAPOU DA FORCA. PARABÉNS!! 🤩🤩')
            print('A palavra completa é: {}'.format(passphrase))
            seguir = input('\nPressione ENTER para continuar...')
        # Se o jogador perdeu o jogo
        elif erros == 6:
            print(inicial+chances[erros])
            print('A palavra completa é: {}\n'.format(passphrase))
            print('>>>>>>> S3 f#d#u <<<<<<<<\nHAHAHAHAHAHAHAHA!!! 😂\nVOCÊ PERDEU E POR ISSO FOI ENFORCADO!!!!\n')
            seguir = input('Pressione ENTER para continuar...')
        
        # Salvando informações do jogador no ranking
        salvar_ranking(nome_jogador, acertos, erros)


    # Opção 2 (VER RANKING)
    elif op == '2':
        os.system('cls')
        print('-=-=-=-=-=-=-=-=-=-=-\n🏆 RANKING DO JOGO 🏆\n-=-=-=-=-=-=-=-=-=-=-\n')
        with open('ranking.txt') as arquivo:
            arq = arquivo.read()
            lista = arq.split('\n')
            lista = sorted(lista, reverse=True)

        for i in range(len(lista)):
            print(lista[i])
        seguir = input('Pressione ENTER para continuar...')


    # Opção 3 (CADASTRAR PALAVRA)
    elif op == '3':
        os.system('cls')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n📝 CADASTRAR NOVA PALAVRA 📝\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
        passphrase = input('Digite a palavra que deseja cadastrar: ').upper().strip(' ')

        # Abrindo arquivo palavras.txt, buscando as informações existes e atribuindo á uma variável para verificar se a palavra informada já existe.
        with open('palavras.txt') as arquivo:
            palavras = arquivo.read()
        if passphrase in palavras:
            print('Essa palavra já existe!\n')
            seguir = input('Pressione ENTER para continuar...')
        # Se for for espaço, em branco ou numérico, não cadastra.
        elif passphrase == None or passphrase is numeric or passphrase == '':
            print('Oxe? Você não digitou nenhuma palavra.\n')
            seguir = input('Pressione ENTER para continuar...')
        else:
            # Escrevendo a palavra nova no arquivo palavras.txt
            with open('palavras.txt', 'a') as arquivo:
                arquivo.write('\n' + passphrase)
                arquivo.close()
            print('Palavra cadastrada com sucesso!')
            seguir = input('Pressione ENTER para continuar...')

    # Opção 4 (SOBRE)
    elif op == '4':
        os.system('cls')
        print('-=-=-=-=-=-\n⚠️  SOBRE ⚠️\n-=-=-=-=-=-\n')
        print('Versão: {}\nDesenvolvedores: Jorge Reis Galvão e Werner Barbosa de Lima\n'.format(__version__))
        seguir = input('Pressione ENTER para continuar...')

    # Opção 5 (SAIR)
    elif op == '5':
        print('\nAté mais!')
        sleep(2)
        sair = False

    # Se a opção não for válida
    else:
        print('\nOpção inválida!')
        sleep(1)

# Fim do programa
