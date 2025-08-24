tecnicos={} #dicionario com tecnico, boole se ele fez substituiçao ou nao e pontuaçao
numero_tecnitos=int(input())

def processar_jogadores(comando):

    if comando=='titulares':
        titulares=[] #lista de dicionarios, um dicionario pra cada jogador titular

        for i in range (11):
            jogador=input().split(',')
            nome_jogador, pontos_jogador, posicao_jogador = calcular_pontos(jogador)

            titular={'nome': nome_jogador,
                     'pontos':pontos_jogador,
                     'posicao':posicao_jogador}
            
            titulares.append(titular)

        return titulares

    elif comando=='reservas':
        reservas=[] #lista de dicionarios

        for i in range (5):
            jogador=input().split(',')
            nome_jogador, pontos_jogador, posicao_jogador = calcular_pontos(jogador)

            reserva={'nome': nome_jogador,
                     'pontos': pontos_jogador,
                     'posicao': posicao_jogador}
            
            reservas.append(reserva)

        return reservas



def calcular_pontos(jogador):
    nome=jogador[0]
    posicao=jogador[1]

    pontuacao_total= (8 * int(jogador[2])) + (5 * int(jogador[3])) + (-1 * int(jogador[4])) + (-3 * int(jogador[5]))

    if (posicao == 'goleiro' or posicao == 'zagueiro' or posicao == 'lateral') and int(jogador[6])==0:
        pontuacao_total+=5

    return nome, pontuacao_total, posicao



#MAIN
for i in range(numero_tecnitos):
    nome_tecnico=input()

    comando=input()
    grupo1 = processar_jogadores(comando)

    comando=input()
    grupo2 = processar_jogadores(comando)

    if len(grupo1)>len(grupo2):
        titulares=grupo1
        reservas=grupo2
    else:
        titulares=grupo2
        reservas=grupo1

    #SUBSTITUIÇAO:
    substituicao=False
    nome_substituido=''
    ganho_substituido=0
    prioridade_substituido=6 

    prioridades = {'goleiro': 1, 'lateral': 2, 'zagueiro': 3, 'meia': 4, 'atacante': 5} #prioridades para comparacao
    trocas_campeas=[] #lista com as trocas campeas por posicao

    for i in range(5): #percorre os reservas (UM POR POSICAO)

        titulares_da_posicao=[] #lista com os titulares de uma posicao

        for c in range (11): #percorre os titulares
            if reservas[i]['posicao'] == titulares[c]['posicao']:
                titulares_da_posicao.append(titulares[c])

        candidatos_a_sair=[] #lista dos titulares a sair de uma mesma posicao

        pior_pontuacao_da_posicao = titulares_da_posicao[0]['pontos']
        for titular in titulares_da_posicao:
            if titular['pontos'] < pior_pontuacao_da_posicao:
                pior_pontuacao_da_posicao = titular['pontos']


        for titular in titulares_da_posicao:
            if titular['pontos'] == pior_pontuacao_da_posicao:
                candidatos_a_sair.append(titular)


        #DESEMPATE PELA LEXICOGRAFIA (entre os da mesma posição)
        titular_escolhido=''
        if len(candidatos_a_sair)>0:
                if len(candidatos_a_sair)==1:
                    titular_escolhido=candidatos_a_sair[0]

                else:
                    titular_escolhido=candidatos_a_sair[0]

                    for j in range (1, len(candidatos_a_sair)):
                        if candidatos_a_sair[j]['nome'] > titular_escolhido['nome']:
                            titular_escolhido=candidatos_a_sair[j]

        #se tiver uma troca boa, adiciona na lista de trocas por posicao
        if titular_escolhido and reservas[i]['pontos'] > titular_escolhido['pontos']:
            ganho=reservas[i]['pontos'] - titular_escolhido['pontos']
            troca_campea={'ganho': ganho,
                          'reserva': reservas[i],
                          'titular': titular_escolhido,
                          'prioridade': prioridades[reservas[i]['posicao']]}
            
            trocas_campeas.append(troca_campea)


    #entre as trocas campeas por posicao, decide uma
    if trocas_campeas != []:
        substituicao=True
        reserva_substituto={}
        titular_substituido={}
        ganho_substituido=0
        prioridade_substituido=6 #quanto menor melhor e é de 1 a 5 (5 posiçoes), entao o 6 ta fora do range

        for troca in trocas_campeas:
            if troca['ganho']>ganho_substituido:
                reserva_substituto=troca['reserva']
                titular_escolhido=troca['titular']
                ganho_substituido=troca['ganho']
                prioridade_substituido=troca['prioridade']
                titular_substituido = titular_escolhido


            #DESEMPATE PELA PRIORIDADE
            elif troca['ganho']==ganho_substituido:
                if troca['prioridade'] < prioridade_substituido:
                    reserva_substituto=troca['reserva']
                    titular_escolhido=troca['titular']
                    ganho_substituido=troca['ganho']
                    prioridade_substituido=troca['prioridade']
                    titular_substituido = titular_escolhido

        indice_para_remover=titulares.index((titular_substituido))
        titulares[indice_para_remover] = reserva_substituto

    #processamento da pontuacao do tecnico
    pontos_tecnico=0
    for jogador in titulares:
        pontos_tecnico+=jogador['pontos']

    #dicionario dentro do de tecnicos, com os dados do tecnico
    if substituicao==True:
        tecnicos[nome_tecnico]={'substituicao': substituicao,
                                'titular substituido': titular_substituido['nome'],
                                'reserva substituto': reserva_substituto['nome'],
                                'pontuacao': pontos_tecnico}
        
    else:
        tecnicos[nome_tecnico]={'substituicao': substituicao,
                                'pontuacao': pontos_tecnico}
        
    

#VENCEDOR E PRINTS
vencedor=''
pontuacao_vencedor=0

nomes_tecnicos=list(tecnicos.keys())

print(f'Os técnicos que participarão da avaliação da rodada serão {", ".join(nomes_tecnicos)}.')

for i in range (len(tecnicos)):
    nome_tecnico=list(tecnicos.keys())[i]

    if tecnicos[nome_tecnico]['substituicao']==True:
        print(f'{nome_tecnico} é um gênio da bola mesmo, a substituição de {tecnicos[nome_tecnico]["titular substituido"]} por {tecnicos[nome_tecnico]["reserva substituto"]} fez ele ganhar pontos!')
    
    else:
        print(f'Pode cortar {nome_tecnico} dos candidatos a técnico da amarelinha, nem fazer uma substituição ele consegue...')
    
    if tecnicos[nome_tecnico]['pontuacao'] > pontuacao_vencedor:
        vencedor=nome_tecnico
        pontuacao_vencedor=tecnicos[nome_tecnico]['pontuacao']

print(f'{vencedor} é incrível ganhou essa rodada com {pontuacao_vencedor} pontos!')


if tecnicos[vencedor]['substituicao']==False:
    print(f'Temos que pedir desculpas a {vencedor}, mesmo sem fazer uma substituição ele foi o melhor da rodada, talvez ele deva assumir a amarelinha depois do Ancelotti!')

