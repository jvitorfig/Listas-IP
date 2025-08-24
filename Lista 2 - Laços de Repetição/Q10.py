set_atual=0
vitoriashugo=0 #vitorias de set
vitoriaslin=0
pontoshugo=0 #pontos no set
pontoslin=0
set_acabou=False
partida_acabou=False
tiebreak=False #manda pro tiebreak
tiebreak1=True
sacador=input()
primeirosacador=sacador #pra usar no tiebreak
saqueshugo=0 #quantidade de saques no tiebreak
saqueslin=0

print('Bem amigos da Rede Globo, emoção no ar! Prepare o coração porque hoje é dia de decisão! É final de Copa do Mundo, mas não é futebol… é ping pong, meu amigo! A raquete vai cantar, a bolinha vai voar, e só um será campeão! Segura essa emoção porque vai começar!')

#-----------set-------------
while partida_acabou==False:
    set_atual+=1
    set_acabou=False
    print(f'Set {set_atual}:')

    while set_acabou==False: #----------------LOOP DOS SETS------------

        if tiebreak==True and tiebreak1==True: #é o primeiro saque do tiebreak
            sacador=primeirosacador
            print('Agora é hora da decisão! Vamos para o tie-break, quem errar, perde tudo! É emoção até o fim!')
            pontoshugo=0
            pontoslin=0
            
        elif tiebreak==True:
            if sacador=='hugo':
                saqueshugo+=1
            elif sacador=='lin':
                saqueslin+=1

        verificador=0
        contador=0
        jogador=sacador
        sacando=False
        atacando=False
        defendendo=False
        acao=input()
        for c in acao:
            if c == 's' and contador==verificador: #SAQUE
                verificador+=6 
                sacando=True

            if c =='a' and contador==verificador: #ATAQUE
                verificador+=7 
                if sacando==True: #ataque depois de saque
                    print(f'Uau, um ace! {jogador.capitalize()} solta o braço e deixa o adversário parado!')
                    if jogador=='hugo': #hugo tava sacando, então ele ganha ponto
                        pontoshugo+=1
                    else:
                        pontoslin+=1

                elif atacando==True: #ataque depois de ataque
                    if jogador=='hugo': #hugo tava atacando, então ele ganha ponto
                        pontoshugo+=1
                        print('Hugo acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!')
                    else:
                        pontoslin+=1
                        print('Lin acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!')

                elif jogador=='hugo':
                    jogador='lin' #lin passa a atacar
                    atacando=True
                    defendendo=False
                    sacando=False

                elif jogador=='lin':
                    jogador='hugo'
                    atacando=True
                    defendendo=False
                    sacando=False


            if c =='d' and contador==verificador: #DEFESA
                verificador +=7 #defesa-

                if defendendo==True:
                    if jogador=='hugo': #hugo mandou a anterior de defesa, então ele ganha ponto
                        pontoshugo+=1
                        print('Lin tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.') 
                    else:
                        pontoslin+=1
                        print('Hugo tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.')

                elif jogador=='hugo':
                    jogador='lin'
                    defendendo=True
                    sacando=False
                    atacando=False
                elif jogador=='lin':
                    jogador='hugo'
                    defendendo=True
                    sacando=False
                    atacando=False


            if c =='c' and contador==verificador: #CONTROLE
                verificador +=9 #controle-
                if atacando==True:
                    if jogador=='hugo': #hugo tava atacando, então ele ganha ponto
                        pontoshugo+=1
                        print('Hugo acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!')
                    else:
                        pontoslin+=1
                        print('Lin acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!')

                elif jogador=='hugo':
                    jogador='lin'
                    defendendo=False
                    sacando=False
                elif jogador=='lin':
                    jogador='hugo'
                    defendendo=False
                    sacando=False


            if c=='e' and contador==verificador:

                if contador==0: #erro como primeira ação
                    if jogador=='hugo': #hugo foi sacar e errou
                        pontoslin+=1
                        print('Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.')
                        jogador='lin'
                    else:
                        pontoshugo+=1
                        print('Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.')
                        jogador='hugo'

                elif sacando==True: #erro depois de saque
                    print(f'Uau, um ace! {jogador.capitalize()} solta o braço e deixa o adversário parado!')
                    if jogador=='hugo': #hugo tava sacando, então ele ganha ponto
                        pontoshugo+=1
                    else:
                        pontoslin+=1

                elif contador>0: #erro em controle saque ou defesa
                    if jogador=='hugo': #hugo tava jogando e lin errou
                        pontoshugo+=1
                        print('Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.')
                    else:
                        pontoslin+=1
                        print('Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.')            

            contador+=1

        print(f'Ponto para {jogador.capitalize()}!\nPlacar do {set_atual} set : {pontoshugo} x {pontoslin}')
                
#----------VERIFICANDO SE O SET ACABOU------
        if tiebreak==False:

            if pontoshugo==5 and pontoslin<=3:
                vitoriashugo+=1
                set_acabou=True

                if pontoshugo==5 and pontoslin==0:
                    print('Fim de set! Domínio total: 5 a 0, sem chance para o adversário — Hugo passeia na mesa')
                    
                else:
                    print('E o set vai para Hugo!')

                pontoshugo=0
                pontoslin=0
                print(f'Placar do jogo: {vitoriashugo} x {vitoriaslin}')

            elif pontoslin==5 and pontoshugo<=3:
                vitoriaslin+=1
                set_acabou=True
                if pontoslin==5 and pontoshugo==0:
                    print('Fim de set! Domínio total: 5 a 0, sem chance para o adversário — Lin passeia na mesa')
                else:
                    print('E o set vai para Lin!')

                pontoshugo=0
                pontoslin=0
                print(f'Placar do jogo: {vitoriashugo} x {vitoriaslin}')

            elif pontoshugo>=4 and pontoslin>=4: #-----------VAI A 2
                if pontoshugo==4 and pontoslin==4:
                    print('O set está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva — é decisão na mesa!')
                if abs(pontoshugo-pontoslin)<2:
                    set_acabou=False
                else:
                    set_acabou=True
                    if pontoshugo>pontoslin:
                        vitoriashugo+=1
                        print('E o set vai para Hugo!')
                        print(f'Placar do jogo: {vitoriashugo} x {vitoriaslin}')
                    else:
                        vitoriaslin+=1
                        print('E o set vai para Lin!')
                        print(f'Placar do jogo: {vitoriashugo} x {vitoriaslin}')
                    pontoshugo=0
                    pontoslin=0

#----------------TIEBREAK--------------------
        if tiebreak==True:

            if tiebreak1==True: #primeiro saque do tiebreak
                tiebreak1=False
                if sacador=='hugo':
                    sacador='lin'
                else:
                    sacador='hugo'
            elif tiebreak1==False: #outros saques do tiebreak
                if sacador=='hugo' and saqueshugo==2:
                    sacador='lin'
                    saqueshugo=0
                elif sacador=='lin' and saqueslin==2:
                    sacador='hugo'
                    saqueslin=0
        
            if pontoshugo==7 and pontoslin<=5:
                vitoriashugo+=1
                set_acabou=True

                if pontoshugo==7 and pontoslin==0:
                    print('Fim de tie-break! Hugo arrasa com um 7 a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!')
                    
                else:
                    print('E o set vai para Hugo!')

                print(f'Placar do jogo: {vitoriashugo} x {vitoriaslin}')

            elif pontoslin==7 and pontoshugo<=5:
                vitoriaslin+=1
                set_acabou=True
                if pontoslin==7 and pontoshugo==0:
                    print('Fim de tie-break! Lin arrasa com um 7 a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!')
                else:
                    print('E o set vai para Lin!')

                print(f'Placar do jogo: {vitoriashugo} x {vitoriaslin}')

            elif pontoshugo>=6 and pontoslin>=6: #-----------VAI A 2
                if pontoshugo==6 and pontoslin==6:
                    print('O tie-break está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva, é a reta final da disputa! Quem será o grande campeão?')
                if abs(pontoshugo-pontoslin)<2:
                    set_acabou=False
                else:
                    set_acabou=True
                    if pontoshugo>pontoslin:
                        vitoriashugo+=1
                        print('E o set vai para Hugo!')
                        print(f'Placar do jogo: {vitoriashugo} x {vitoriaslin}')
                    else:
                        vitoriaslin+=1
                        print('E o set vai para Lin!')
                        print(f'Placar do jogo: {vitoriashugo} x {vitoriaslin}')


    if tiebreak==False:
        if sacador=='hugo': #inverte o sacador pro proximo set
            sacador='lin'
        elif sacador=='lin':
            sacador='hugo'

# VERIFICAÇÃO DAS VITÓRIAS

    if vitoriashugo==3 and tiebreak==False:
        print('Hugo garantiu a vitória sem precisar de tie-break! Uma performance sólida e sem erros, ele dominou o jogo do início ao fim e se sagrou campeão do mundo!')
        partida_acabou=True
    elif vitoriaslin==3 and tiebreak==False:
        print('Hugo não conseguiu segurar a pressão e acabou perdendo sem precisar do tie-break. Foi uma grande final, mas hoje não foi o seu dia. Vitória do chinês!')
        partida_acabou=True

    elif vitoriashugo==vitoriaslin==2:
        tiebreak=True

    elif vitoriashugo==3 and tiebreak==True:
        print('Hugo é o grande vencedor! Ele conquista o tie-break com uma performance impecável e leva a vitória!')
        partida_acabou=True

    elif vitoriaslin==3 and tiebreak==True:
        print('Hugo lutou até o fim, mas no tie-break, o adversário levou a melhor. Uma derrota apertada, mas ainda assim, uma grande batalha!')
        partida_acabou=True
