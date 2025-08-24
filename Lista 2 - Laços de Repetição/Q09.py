
jogador1 = str(input(''))
jogador2 = str(input(''))
pontos1 = 0
pontos2 = 0
vitorias1 = 0
vitorias2 = 0

rebatida = 0
contador = 0  # pra contar as rebatidas
contadorsets = 1  # pra contar os sets

verifpartida = False  # pra sair do loop da partida
verifrebatida = True  # pra sair do loop da rebatida

if (jogador1=='Luis' or jogador1=='Lavoisier' or jogador1=='Joab' or jogador1=='Renan') and (jogador2=='Luis' or jogador2=='Lavoisier' or jogador2=='Joab' or jogador2=='Renan'):
    print('Essa partida vai ser épica! O jogo vai ser emocionante!')
jogador = jogador1
pontojogador = 0
acao2 = ''  # oponente rebateu

num_sets = int(input(''))

nivel = str(input('')) #define maximo de rebatidas
if nivel == 'aprendizes':
    rebatida = 1
elif nivel == 'básicos':
    rebatida = 2
elif nivel == 'amostradinhos':
    rebatida = 3


while contadorsets <= num_sets: #Loop dos sets
    pontos1=0
    pontos2=0
    contador=0
    jogador=jogador1
    print(f'Iniciando o {contadorsets}º set')
    contadorsets += 1
    verifpartida = False

    while verifpartida == False: #Loop das partidas
        verifrebatida= True
        print(f'O saque é de {jogador}')
        acao = str(input('')) #provavelmente vai ser saque

        if acao == 'saque':
            entrada1 = str(input('')) #SA OU AO
            entrada2 = str(input('')) #SA OU AO

            if entrada1 == 'SA' and entrada2 == 'AO':
                print(f'Um saque PERFEITO!!')
                contador=0

                acao = str(input(''))
                if acao == 'rebatida':

                    while contador<rebatida and verifrebatida:
                        acao2=input()

                        if acao2==f'{jogador1} deixou a bola cair':
                            verifrebatida=False
                            pontos2+=1
                            jogador=jogador2

                        elif acao2==f'{jogador2} deixou a bola cair':
                            verifrebatida=False
                            pontos1+=1
                            jogador=jogador1

                        elif acao2=='oponente rebateu':
                            contador+=1
                            if jogador == jogador1:
                                jogador=jogador2
                            else:
                                jogador=jogador1

                    else:
                        if contador == rebatida:
                            velocidade1 = int(input(''))
                            velocidade2 = int(input(''))

                            if velocidade1 < velocidade2:
                                pontos1 += 1
                                jogador = jogador1
                            elif velocidade2 < velocidade1:
                                pontos2 += 1
                                jogador = jogador2

 
            elif entrada1 == 'SA' and entrada2 == 'SA':
                print(
                    f'{jogador}, a bola quicou duas vezes na sua própria área! Que saque feio foi esse??')
                if jogador == jogador1:
                    jogador = jogador2
                    pontos2 += 1
                else:
                    jogador = jogador1
                    pontos1 += 1

            elif entrada1 == 'AO' and entrada2 == 'AO':
                if jogador == jogador1:
                    print(
                        f'Boa, {jogador}! Deu ponto de graça pro oponente!! Agora quem saca é {jogador2}')
                    jogador = jogador2
                    pontos2 += 1
                else:
                    print(
                        f'Boa, {jogador}! Deu ponto de graça pro oponente!! Agora quem saca é {jogador1}')
                    jogador = jogador1
                    pontos1 += 1
            elif entrada1 == 'REDE' or entrada2 == 'REDE':
                print('Vish, ainda bateu na rede')
                if jogador == jogador1:
                    jogador = jogador2
                    pontos2 += 1
                else:
                    jogador = jogador1
                    pontos1 += 1

        if pontos1>=3 or pontos2>=3:
            if abs(pontos1-pontos2)>=2:
                verifpartida=True
                if pontos1>pontos2:
                    vitorias1+=1 
                else:
                    vitorias2+=1

if vitorias1 > vitorias2:
    print(f'''Depois de {num_sets} set(s) vibrante(s), o grande vencedor é {jogador1}!!
Fim do jogo!''')

elif vitorias2 > vitorias1:
    print(f'''Depois de {num_sets} set(s) vibrante(s), o grande vencedor é {jogador2}!!
Fim do jogo!''')
    