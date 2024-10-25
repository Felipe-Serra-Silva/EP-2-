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

#ataca o návio e modifica o grid:
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

#modifica o grid: 1 - para posição do barco
def posiciona_frota (dicionario_frota):
    grid = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    for lista in dicionario_frota.values():
        for lista_int in lista:
            for elemento in lista_int:
                linha = elemento[0]
                coluna = elemento[1]
                grid[linha][coluna] = 1
    return grid

#Verifica o numero de navios atingidos pelo inimigo:
def afundados (dicionario_frota, tabuleiro):

    navios_atingidos = 0
    for lista in dicionario_frota.values():
        for lista_int in lista:
            tiros = 0
            for elemento in lista_int:
                if tabuleiro[elemento[0]][elemento[1]] == 'X':
                    tiros +=1
            if tiros == len(lista_int):
                navios_atingidos += 1

    return(navios_atingidos)

#Verficia se a posição desejada pelo jogador, para alocar seu navio, está disponível:
def posicao_valida(dicionario_frota, linha, coluna, orientacao, tamanho):

    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)

    posicao_ocupada = 0
    for lista in dicionario_frota.values():
        for lista_int in lista:
            for elemento in lista_int:
                for lugar in posicoes:
                    if lugar == elemento:
                        posicao_ocupada +=1
    for lugar in posicoes:
        if lugar[0] > 9 or lugar[0] < 0:
            posicao_ocupada +=1
        if lugar[1] > 9 or lugar[1] < 0:
            posicao_ocupada +=1

    if posicao_ocupada == 0:
        return(True)
    else:
        return(False)

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto