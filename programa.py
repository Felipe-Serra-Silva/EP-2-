from funcoes import *
import random
random.seed(2)

#cria dicionario para facilitar o while rodar para cada tipo de navio:
dicionario_tamanho = {
    "porta-aviões":[4,1] ,
    "navio-tanque": [3,2],
    "contratorpedeiro": [2,3],
    "submarino": [1,4],
}  

dicionario_frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}     


for navios, tamanhos in dicionario_tamanho.items():

    contador = 0
    while contador < tamanhos[1]:  #vai rodar até o tamanho do navio ser atingido (quantidade de navios)
        print(f'Insira as informações referentes ao navio {navios} que possui tamanho {tamanhos[0]}')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        tamanho = tamanhos[0]  #esse é o tamanho do návio (quantidade de espaços que o navio ocupa)
        if navios != 'submarino':
            orientacao =  int(input('Orientação: [1] Vertical [2] Horizontal '))
            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'
        verifica = posicao_valida(dicionario_frota, linha, coluna, orientacao, tamanho)

        if verifica == False:
            print('Esta posição não está válida!')
            print(f'Insira as informações referentes ao navio {navios} que possui tamanho {tamanhos[0]}')
        while verifica == False:
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            if navios != 'submarino':
                orientacao =  int(input('Orientação: [1] Vertical [2] Horizontal '))
                if orientacao == 1:
                    orientacao = 'vertical'
                elif orientacao == 2:
                    orientacao = 'horizontal'
            verifica = posicao_valida(dicionario_frota, linha, coluna, orientacao, tamanho)
            if verifica == False:
                print('Esta posição não está válida!')
                print(f'Insira as informações referentes ao navio {navios} que possui tamanho {tamanhos[0]}') 
        
        posicoes_escolhidas = define_posicoes(linha,coluna,orientacao,tamanho)
        preenchendo = preenche_frota(dicionario_frota, navios, linha, coluna, orientacao, tamanho)

        contador +=1


#Jogadas de ataque do jogador:
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(dicionario_frota)

# a função monta_tabuleiros foi adicionada no arquivo: funcoes.py
# Printa o tabuleiro atualizado:
print(monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente))

jogando = True
jogadas_feitas = []
jogadas_oponentes = []

while jogando == True:
    #pergunta linha e coluna, com validação:

    valida = - 1
    while valida == -1:
        linha = int(input('Jogador, qual linha deseja atacar? '))
        quebra = 0
        if linha < 0 or linha > 9:
            print('Linha inválida!')
            quebra = -1
        while quebra == -1:
            linha = int(input('Jogador, qual linha deseja atacar? '))
            quebra = 0
            if linha < 0 or linha > 9:
                print('Linha inválida!')
                quebra = -1
        
        coluna = int(input('Jogador, qual coluna deseja atacar? '))
        quebra = 0
        if coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            quebra = -1
        while quebra == -1:
            coluna = int(input('Jogador, qual coluna deseja atacar? '))
            quebra = 0
            if coluna < 0 or coluna > 9:
                print('Coluna inválida!')
                quebra = -1
        
        #verifica se a jogada ja foi feita:
        jogado = [linha,coluna]
        if jogado not in jogadas_feitas:
            jogadas_feitas.append(jogado)
            valida = 0
        else:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
    
    #atualiza tabuleiro do oponete:
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente,linha,coluna)
    #verifica se atingiu todos:
    quantidade_afundados = afundados(frota_oponente,tabuleiro_oponente)
    if quantidade_afundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    else:

        #oponente ataca jogador:
        oponete = 0
        while oponete == 0:
            linha_sorteada = random.randint(0,9)
            coluna_sorteada = random.randint(0,9)

            jogada_oponente = [linha_sorteada,coluna_sorteada]
            if jogada_oponente not in jogadas_oponentes:
                jogadas_oponentes.append(jogada_oponente)
                oponete = -1
        
        print(f'Seu oponente está atacando na linha {linha_sorteada} e coluna {coluna_sorteada}')

        #Verifica se oponente eliminou o jogador:
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador,linha_sorteada,coluna_sorteada)
        oponente_atacou =  afundados(dicionario_frota, tabuleiro_jogador)

        if oponente_atacou == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False
        else:
            #atualiza o tabuleiro:
            print(monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente))

        