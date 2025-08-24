#funcao pra adicionar clubes ao campeonato
def adicionar_clube(times, clube, contador_de_times, num_times_regiao, regiao):

    if num_times_regiao < 2:
        times[clube] = {}
        times[clube]['pontos'] = 0
        times[clube]['saldo de gols'] = 0
        contador_de_times += 1
        num_times_regiao += 1

    else:
        print(f'Cota para a região {regiao} atingida. Por favor, insira um clube de outro estado, de outra região.')

    return times, contador_de_times, num_times_regiao


#funcao simulacao de partida do mata mata
def partida(time_A, time_B, artilharia, times_classificacao, tipo_partida):
    gols_time_A = 0
    gols_time_B = 0
    vencedor=''
    perdedor=''
    empate=False
    entrada = input()

    while entrada != 'FIM':
        jogador, time = entrada.split(' - ')
        print(f'Gol do {time}, {jogador} é o nome da emoção')

        if time==time_A:
            gols_time_A += 1

        elif time==time_B:
            gols_time_B += 1
        
        
        if (jogador, time) in artilharia: #se o jogador ja ta na lista de artilharia, ele fez mais um gol
            artilharia[(jogador, time)]['gols'] +=1
        else:
            artilharia[(jogador, time)] = {'gols': 1} #se nao, inicia com 1
            
        entrada=input()

    if gols_time_A > gols_time_B:
        vencedor = time_A
        perdedor = time_B

    elif gols_time_B > gols_time_A:
        vencedor = time_B
        perdedor = time_A
    
    elif gols_time_A == gols_time_B:
        empate=True
        #desempate pela posicao na fase de liga
        if times_classificacao[time_A]['posicao'] < times_classificacao[time_B]['posicao']:
            vencedor=time_A
            perdedor=time_B
        else:
            vencedor=time_B
            perdedor=time_A
            
    if vencedor==time_A:
        gols_vencedor=gols_time_A
        gols_perdedor=gols_time_B
    else:
        gols_vencedor=gols_time_B
        gols_perdedor=gols_time_A

    saldo_perdedor = gols_perdedor - gols_vencedor

    #PRINTS
    print('Fim de jogo.')
    print(f'Placar: {vencedor} {gols_vencedor} X {gols_perdedor} {perdedor}')

    if tipo_partida=='semifinal':
        if empate==True:
            print(f'O {vencedor} passa para a final após vencer nos pênaltis, será que vai ser campeão?')

        else:
            print(f'O {vencedor} venceu e foi para a final, será que vai ser campeão?')

    return vencedor, perdedor, saldo_perdedor, artilharia

 
#MAIN
times={} #2 times do sudeste, 2 do sul e 2 do nordeste

regioes = {
    'sul': ('RS', 'SC', 'PR'),
    'nordeste': ('BA', 'PE', 'CE', 'RN', 'PB', 'AL', 'MA', 'SE', 'PI'),
    'sudeste': ('SP', 'RJ', 'MG', 'ES')
}


clube=''
contador_de_times=0
num_times_sul=0
num_times_nordeste=0
num_times_sudeste=0

while contador_de_times<6 and clube != 'FIM':
    clube=input()

    if clube !='FIM':
        estado=input()

        #definindo os times por regiao
        #sul
        if estado in regioes['sul']:
            times, contador_de_times, num_times_sul = adicionar_clube(times, clube, contador_de_times, num_times_sul, 'Sul')

        #nordeste
        elif estado in regioes['nordeste']:
            times, contador_de_times, num_times_nordeste = adicionar_clube(times, clube, contador_de_times, num_times_nordeste, 'Nordeste')

        #sudeste
        elif estado in regioes['sudeste']:
            times, contador_de_times, num_times_sudeste = adicionar_clube(times, clube, contador_de_times, num_times_sudeste, 'Sudeste')


if contador_de_times <6:
    print(f'Ai não dá, com {contador_de_times} somente não dá para fazer um campeonato, essa ideia de Copa União foi um fiasco mesmo, #VOLTACBF')

#campeonado normal
else:
    for i in range (15): #15 partidas das ligas
        placar=input()
        #PROCESSAMENTO DE PARTIDA DA LIGA
        time_1, time_2 = placar.split(' X ')

        time_1 = time_1.split(' ')
        gols_1 = int(time_1[-1])
        time_1 = ' '.join(time_1[:len(time_1)-1]) #usei .join pq não sabia outro jeito já q não dá pra saber quantas palavras vai ter o nome de um time

        time_2 = time_2.split(' ')
        gols_2 = int(time_2[0])
        time_2 = ' '.join(time_2[1:len(time_2)])

        #empate
        if gols_1 == gols_2:
            times[time_1]['pontos'] += 1
            times[time_2]['pontos'] += 1

        #primeiro ganhou
        elif gols_1 > gols_2:
            times[time_1]['pontos'] +=3
            times[time_1]['saldo de gols'] += (gols_1 - gols_2)
            times[time_2]['saldo de gols'] += (gols_2 - gols_1)

        #segundo ganhou
        elif gols_2 > gols_1:
            times[time_2]['pontos'] +=3
            times[time_1]['saldo de gols'] += (gols_1 - gols_2)
            times[time_2]['saldo de gols'] += (gols_2 - gols_1)


    times_classificacao = {} #pra ordenar os times

    for i in range (6):
        melhor_time=''
        melhor_pontuacao=0
        melhor_saldo=0

        for time in times:
            if time not in times_classificacao:
                pontos = times[time]['pontos']
                saldo = times[time]['saldo de gols']

                if not melhor_time:
                    melhor_time = time
                    melhor_pontuacao = pontos
                    melhor_saldo = saldo
                else:
                    if pontos > melhor_pontuacao or (pontos == melhor_pontuacao and saldo > melhor_saldo):
                        melhor_time = time
                        melhor_pontuacao = pontos
                        melhor_saldo = saldo

        times_classificacao[melhor_time] = times[melhor_time]

    contador=1
    for time in times_classificacao:
        print(f'{time} - {times_classificacao[time]["pontos"]} pontos') #classificacao final

        times_classificacao[time]['posicao'] = contador #guarda a posicao da fase de liga no dict pra usar depois

        #guardando os 4 primeiros times que vao pra semifinal
        if contador==1:
            primeiro_time = time
        elif contador==2:
            segundo_time = time
        elif contador==3:
            terceiro_time = time
        elif contador==4:
            quarto_time = time

        contador+=1

    artilharia={} #onde ficarao guardados os jogadores que fizerem gols

    #SEMIFINAL
    print('Os confrontos foram definidos:')
    print(f'{primeiro_time} X {quarto_time}')
    print(f'{segundo_time} X {terceiro_time}')

    print('Vai começar o confronto, quem será que vence?')
    finalista_1, perdedor_1, saldo_perdedor_1, artilharia = partida(primeiro_time, quarto_time, artilharia, times_classificacao, 'semifinal')
    print('Vai começar o confronto, quem será que vence?')
    finalista_2, perdedor_2, saldo_perdedor_2, artilharia = partida(segundo_time, terceiro_time, artilharia, times_classificacao, 'semifinal')

    if saldo_perdedor_1 > saldo_perdedor_2:
        terceiro_lugar=perdedor_1
    else:
        terceiro_lugar=perdedor_2

    #FINAL
    print('Vai começar a grande decisão, quem será o campeão brasileiro de 1987?')
    vencedor, perdedor_final, saldo_perdedor_final, artilharia = partida(finalista_1, finalista_2, artilharia, times_classificacao, 'final')

    #prints finais
    if vencedor=='Sport':
        print("Quem deixou o Sport participar, a Copa União só permite clubes grandes de participarem, tirem ele daqui que do jeito que eles são é capaz de irem no tribunal pedir o reconhecimento do 'Brasileiro de Questão de IP'")
        vencedor = perdedor_final
        if vencedor == 'Santa Cruz':
            print('O terror do Nordeste agradece o reconhecimento, porém recusa o titulo, diferente do seu rival ele prefere ganhar o título em campo, e não em imaginação')
            vencedor = terceiro_lugar

    elif vencedor=='Santa Cruz':
        print('O terror do Nordeste agradece o reconhecimento, porém recusa o titulo, diferente do seu rival ele prefere ganhar o título em campo, e não em imaginação')
        vencedor = perdedor_final
        if vencedor == 'Sport':
            print("Quem deixou o Sport participar, a Copa União só permite clubes grandes de participarem, tirem ele daqui que do jeito que eles são é capaz de irem no tribunal pedir o reconhecimento do 'Brasileiro de Questão de IP'")
            vencedor = terceiro_lugar

    if vencedor == 'Flamengo':
        print('Em 1987, o Flamengo é o campeão inquestionável! Conquistou na bola e com o reconhecimento merecido. Qualquer outra conversa é história para boi dormir.')

    else:
        print(f'E o campeão do real Campeonato Brasileiro de 1987 foi o {vencedor}, ouvi dizer que a CBF tava querendo fazer um outro campeonato chamado módulo amarelo, ainda bem que todo mundo entendeu que aquilo é somente uma serie B')


    if artilharia == {}:
        print('Esse ano o nivel foi fraco, não tivemos um artilheiro')
    else:
        #DEFININDO O ARTILHEIRO:
        artilheiro=''
        time_artilheiro=''
        gols_artilheiro=-1

        for jogador_e_time in artilharia: #LEMBRAR as chaves de artilharia sao tuplas de (jogador, time)

            if artilharia[jogador_e_time]['gols']>gols_artilheiro:
                artilheiro=jogador_e_time[0]
                time_artilheiro=jogador_e_time[1]
                gols_artilheiro=artilharia[jogador_e_time]['gols']

            elif artilharia[jogador_e_time]['gols']==gols_artilheiro:
                if jogador_e_time[0]<artilheiro:
                    artilheiro=jogador_e_time[0]
                    time_artilheiro=jogador_e_time[1]

        
        if time_artilheiro==vencedor:
            print(f'{artilheiro} garantiu o título do campeonato e a artilharia, que ano feliz para ele')
        else:
            print(f'Apesar de não ter sido campeão, pelo menos {artilheiro} foi o artilheiro, a culpa não foi dele')
