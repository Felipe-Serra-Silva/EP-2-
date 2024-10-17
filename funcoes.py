# Define posições do navio:
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

