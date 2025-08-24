def busca_melhor_caminho(matriz, custos, linha_atual, coluna_atual, numero_linhas, numero_colunas):

    if matriz[linha_atual][coluna_atual] == 1 or matriz[linha_atual][coluna_atual] == 3: #anda so 1 casa no mapa
        movimentos_possiveis = [[1, 0], [-1, 0], [0, 1], [0, -1]] 

        # TESTE DAS 4 DIREÇÕES
        for c in range(4):
            nova_linha = linha_atual + movimentos_possiveis[c][0]
            nova_coluna = coluna_atual + movimentos_possiveis[c][1]

            if (-1 < nova_linha < numero_linhas) and (-1 < nova_coluna < numero_colunas): #range da matriz

                if matriz[nova_linha][nova_coluna] != 0: #barreira

                    if matriz[linha_atual][coluna_atual] == 1: #saiu da casa 1, custo 1 movimento
                        custo_movimento = custos[linha_atual][coluna_atual] + 1

                    elif matriz[linha_atual][coluna_atual] == 3: #saiu da casa 3, custo 3 movimentos
                        custo_movimento = custos[linha_atual][coluna_atual] + 3

                    if custos[nova_linha][nova_coluna] == -1 or custo_movimento < custos[nova_linha][nova_coluna]:
                        custos[nova_linha][nova_coluna] = custo_movimento #se o custo for menor troca o antigo

                        #busca os caminhos a partir do novo de menor custo (recursao
                        busca_melhor_caminho(matriz, custos, nova_linha, nova_coluna, numero_linhas, numero_colunas)

    elif matriz[linha_atual][coluna_atual] == 2: #viga, msm algoritmo soq pulando 2 casas
        movimentos_possiveis = [[2, 0], [-2, 0], [0, 2], [0, -2]]

        for c in range(4):
            nova_linha = linha_atual + movimentos_possiveis[c][0]
            nova_coluna = coluna_atual + movimentos_possiveis[c][1]

            if (-1 < nova_linha < numero_linhas) and (-1 < nova_coluna < numero_colunas):
                if matriz[nova_linha][nova_coluna] != 0:
                    custo_movimento = custos[linha_atual][coluna_atual] + 1

                    if custos[nova_linha][nova_coluna] == -1 or custo_movimento < custos[nova_linha][nova_coluna]:
                        custos[nova_linha][nova_coluna] = custo_movimento

                        busca_melhor_caminho(matriz, custos, nova_linha, nova_coluna, numero_linhas, numero_colunas)


# MAIN
print('=== SEKIRO: O RESGATE DE CESAR ===')
print('Wolf deve resgatar CESAR!')

numero_linhas = int(input())
numero_colunas = int(input())

# formacao da matriz
matriz = []

for i in range(numero_linhas):
    linha = input().split()

    for c in range(numero_colunas):  # loop pra transformar os numeros de string pra int
        linha[c] = int(linha[c])

    matriz.append(linha)

custos = []  # matriz com o mesmo tamanho da original, contendo os menores custos de movimentos pra chegar em cada casa

for i in range(numero_linhas): #gerando a matriz de custos
    custos.append([-1] * numero_colunas)  # as casas com -1 sao as que nao foram visitadas

custos[0][0] = 0  # zera o ponto de partida

#FUNÇAO RECURSIVA
busca_melhor_caminho(matriz, custos, 0, 0, numero_linhas, numero_colunas)

total_movimentos=custos[numero_linhas-1][numero_colunas-1]

if total_movimentos == -1:  # não conseguiu chegar no final
    print('MORTE! Wolf não conseguiu resgatar Cesar... ele nunca saberá quem venceu Satoru Gojo ou Sukuna!')

else:
    print(f'SUCESSO! Wolf resgatou o Cesar em {total_movimentos} movimentos!')

    if total_movimentos <= 4:
        print('PERFEITO! Verdadeiro Shinobi! Cesar está ORGULHOSO!!')
    elif total_movimentos < 8:
        print('BOM! Caminho eficiente! Mas você quase decepcionou Cesar')
    else:
        print('Wolf chegou, mas pode melhorar... Cesar está decepcionado, quase morreu de tédio!')
