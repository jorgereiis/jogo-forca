def salvar_ranking(nome_jogador, acertos, erros):

    if erros == 0 or erros == 1:
        pontos = 100
    elif erros == 2 or erros == 3:
        pontos = 60
    elif erros == 4 or erros == 5:
        pontos = 20
    elif erros == 6:
        pontos = 0    

    with open('ranking.txt', 'a') as arquivo:
        arquivo.write('{} Pontos - {} [{} acertos, {} erros]\n'.format(pontos, nome_jogador, acertos, erros))
        arquivo.close()
