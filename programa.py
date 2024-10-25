from funcoes import *

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
        linha = int(input(''))
        coluna = int(input(''))
        tamanho = tamanhos[0]  #esse é o tamanho do návio (quantidade de espaços que o navio ocupa)
        if navios != 'submarino':
            orientacao =  int(input('[1] Vertical [2] Horizontal: '))
            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'
        verifica = posicao_valida(dicionario_frota, linha, coluna, orientacao, tamanho)

        if verifica == False:
            print('Esta posição não está válida!')
            print(f'Insira as informações referentes ao navio {navios} que possui tamanho {tamanhos[0]}')
        while verifica == False:
            linha = int(input(''))
            coluna = int(input(''))
            if navios != 'submarino':
                orientacao =  int(input('[1] Vertical [2] Horizontal: '))
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


print(dicionario_frota)