# Define posições do navio no grid:
def define_posicoes(linha,coluna,orientacao,tamanho):
    posicao_navio = []
    if orientacao == "vertical":
        posicao_navio.append([linha,coluna])
        i = linha
        contador = 1
        while contador < tamanho:
            posicao_navio.append([i+1,coluna])
            contador +=1
            i +=1

    else:
        posicao_navio.append([linha,coluna])
        i = coluna
        contador = 1
        while contador < tamanho:
            posicao_navio.append([linha,i+1])
            contador +=1
            i +=1
    return posicao_navio

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if len(frota) != 0:
        if nome_navio in frota:
            lista_final = frota[nome_navio]
            lista_posicao = define_posicoes(linha,coluna, orientacao, tamanho)
            lista_final.append(lista_posicao)
            frota[nome_navio] = lista_final
        else:
            lista_final = []
            lista_posicao = define_posicoes(linha,coluna, orientacao, tamanho)
            lista_final.append(lista_posicao)
            frota[nome_navio] = lista_final
    else:
        lista_final = []
        lista_posicao = define_posicoes(linha,coluna, orientacao, tamanho)
        lista_final.append(lista_posicao)
        frota[nome_navio] = lista_final
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

