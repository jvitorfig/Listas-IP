dicionario={'nomes':[], 'desempenhos':[],'tipo_analise':[], 'posicoes':[]}

nome_jogador=''
while nome_jogador!='FIM':

    nome_jogador = input()
    if nome_jogador!='FIM':

        dicionario['nomes'].append(nome_jogador)

        disposicao_percentual=int(input())

        posicao=input()
        dicionario['posicoes'].append(posicao)

        if disposicao_percentual>=85:
            chutes_ou_passes=int(input())
            dicionario['tipo_analise'].append('chutes ou passes')
            dicionario['desempenhos'].append(chutes_ou_passes)


        elif disposicao_percentual>=50:
            desempenho_ultimo_jogo=int(input())
            dicionario['tipo_analise'].append('desempenho ultimo jogo')
            dicionario['desempenhos'].append(desempenho_ultimo_jogo)
        
        else:
            desempenho_ultimo_treino=int(input())
            dicionario['tipo_analise'].append('desempenho ultimo treino')
            dicionario['desempenhos'].append(desempenho_ultimo_treino)


atacantes_prontos=0
meio_def_prontos=0  

qtd_jogadores=len(dicionario['nomes'])

for i in range (qtd_jogadores):

    #dados individuais pra analise
    nome_jogador=dicionario['nomes'][i]
    posicao=dicionario['posicoes'][i]
    tipo_analise=dicionario['tipo_analise'][i]
    desempenho=dicionario['desempenhos'][i]


    if tipo_analise == 'chutes ou passes':

        if posicao == 'atacante':

            if desempenho>10:
                print(f'{nome_jogador} está com um bom desempenho ofensivo.')
                atacantes_prontos+=1

            else:
                print(f'{nome_jogador} pode melhorar, Ancelotti pode usá-lo no segundo tempo.')

        else:
            if desempenho>=20:
                print(f'{nome_jogador} está com um bom desempenho de passes.')
                meio_def_prontos+=1

            else:
                print(f'{nome_jogador} pode melhorar, Ancelotti pode não colocá-lo no primeiro tempo.')

    elif tipo_analise == 'desempenho ultimo jogo':

        if desempenho>80:
            print(f'O jogador {nome_jogador} pode ser escalado para a próxima partida.')

            if posicao=='atacante':
                atacantes_prontos+=1
            else:
                meio_def_prontos+=1

        else:
            print(f'Ancelotti precisa analisar o desempenho do {nome_jogador} na partida.')

    elif tipo_analise == 'desempenho ultimo treino':

        if desempenho>70:
            print(f'Ancelotti deve colocar {nome_jogador} para treinar mais.')
        else:
            print(f'{nome_jogador} não deveria estar na próxima convocação.')

#PRINTS
print()
print('Relatório dos jogadores:')
print(f'Total de jogadores analisados: {qtd_jogadores}')
print(f'Atacantes prontos para começar: {atacantes_prontos}')
print(f'Meio-campistas e Defensores prontos para começar: {meio_def_prontos}')

