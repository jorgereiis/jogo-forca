from random import choice

with open('palavras.txt') as arquivo:
    arq = arquivo.read()
    lista = arq.split('\n')
passphrase = choice(lista).upper()
