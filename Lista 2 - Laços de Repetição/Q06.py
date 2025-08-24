num_rodadas = int(input(''))
print('Vamos dar início à disputa!!! TOMADA!!!')
verif=False
contador=1

pontosluvusier = 0
pontosjaob = 0
pontosjogador = 0

vencedor_tomada = str(input(''))

if contador==1:
    jogador=vencedor_tomada

if vencedor_tomada == 'Jaob':
    print('Jaob veio de Catende e está pronto para vencer!!!')

elif vencedor_tomada == 'Luvusier':
    print('Nada se cria, tudo se transforma, então Luvusier irá se transformar em um vencedor!!!')

while contador<=num_rodadas and verif==False:
    print(f'COMEÇA A {contador}ª RODADA!')
    contador+=1
    alvo='mesa'
    pontosjogador=0

    while alvo=='mesa':
        alvo=str(input(''))
        print(f'{jogador} jogou a bolinha no(a) {alvo}!')
        if jogador=='Jaob':
            jogador='Luvusier'
        else:
            jogador='Jaob'
    
    if jogador=='Jaob':
        jogador='Luvusier'
        pontosjogador=pontosluvusier
    else:
        jogador='Jaob'
        pontosjogador=pontosjaob
    
    if alvo=='Baralho de UNO' or alvo=='Armário de Homero e Elena' or alvo=='Peça de Dominó':

        if alvo == 'Baralho de UNO':
            pontosjogador += 2
        elif alvo == 'Armário de Homero e Elena':
            pontosjogador += 3
        elif alvo == 'Peça de Dominó':
            pontosjogador += 3

        print(f'{jogador} teve uma grande pontaria e acertou {alvo}! Agora está com {pontosjogador} pontos.')
        if jogador=='Jaob':
            pontosjaob=pontosjogador
        else:
            pontosluvusier=pontosjogador
        
    elif alvo=='Projetor' or alvo=='Computador' or alvo=='Cabeça do Amiguinho' or alvo=='Nada':

        if alvo=='Projetor':
            pontosjogador-=2
        elif alvo=='Computador':
            pontosjogador-=3
        elif alvo=='Cabeça do Amiguinho':
            pontosjogador-=5
        elif alvo=='Nada':
            pontosjogador-=1

        if pontosjogador<0:
            pontosjogador=0
        
        print(f'{jogador} teve mãos de alface e acertou o(a) {alvo}. Agora está com {pontosjogador} pontos.')

        if jogador=='Jaob':
            jogador='Luvusier'
            pontosjaob=pontosjogador
        else:
            jogador='Jaob'
            pontosluvusier=pontosjogador

    elif alvo == 'Baralho de Coup Desaparecido':
        verif = True
        pontosjogador += 100
        print(f'{jogador} teve uma grande pontaria e acertou {alvo}! Agora está com {pontosjogador} pontos.')
        print(f'{jogador} achou o Coup!!! Ele merece a vitória sem dúvidas!')
        if jogador=='Jaob':
            pontosjaob=pontosjogador
        else:
            pontosluvusier=pontosjogador

print('')
print('TEMOS O RESULTADO DA PARTIDA!')        

if pontosjaob>pontosluvusier:
    print(f'Jaob deu orgulho à Catende e ganhou a disputa com {pontosjaob} pontos!')

elif pontosluvusier>pontosjaob:
    print(f'A química está em festa, Luvusier ganha a disputa com {pontosluvusier} pontos!')

else:
    print('Jaob usou a sua autoridade como monitor-chefe e ganhou a disputa mesmo com o empate!')
