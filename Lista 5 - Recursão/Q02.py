def batalha(vida_jogador, dps_jogador, vida_boss, dps_boss, tentativas, nome_boss):
    #iniciais pra usar na recursão
    vida_inicial_jogador=vida_jogador
    vida_inicial_boss=vida_boss

    gravemente_ferido=False

    #loop dos ataques
    while vida_jogador > 0 and vida_boss > 0:

        vida_boss-=dps_jogador


        #SIF GRAVEMENTE FERIDA
        if nome_boss=='Sif, a Grande Loba Cinzenta':
            if vida_boss<3432*0.1 and gravemente_ferido==False:
                print('Sif, a Grande Loba Cinzenta está gravemente ferida! Essa é sua chance, acabe com o sofrimento dela!')
                dps_boss-=15
                gravemente_ferido=True

        #GWYN EM CHAMAS
        elif nome_boss=='Gwyn, Lorde das Cinzas':
            if vida_boss<4185*0.5:
                vida_jogador-=10

        #se o boss não morreu, ele ataca
        if vida_boss>0:
            vida_jogador-=dps_boss

    #boss morreu
    if vida_boss<=0:
        return tentativas
    
    #jogador morreu
    else:
        tentativas+=1
        return batalha(vida_inicial_jogador, dps_jogador*aumento_dps, vida_inicial_boss, dps_boss*reducao_dps, tentativas, nome_boss)



nivel_experiencia = input()

if nivel_experiencia=='Iniciante':
    aumento_dps=1.05
    reducao_dps=0.90

elif nivel_experiencia=='Veterano':
    aumento_dps=1.10
    reducao_dps=0.80

elif nivel_experiencia=='Mestre do Souls':
    aumento_dps=1.20
    reducao_dps=0.67


tentativas=1
stats=input().split(' ')
vitalidade=int(stats[0])
forca=int(stats[1])


nome_boss=input()


if nome_boss=='Sif, a Grande Loba Cinzenta':
    vida_boss=3432
    dps_inicial_boss=35
    print('Venha até mim guardiã do túmulo de Artorias... Vamos acabar logo com isso!')

elif nome_boss=='Gwyn, Lorde das Cinzas':
    vida_boss=4185
    dps_inicial_boss=55
    print('Enfim estou de frente ao Senhor das Cinzas! Nossa batalha será lendária e ecoará em todos os cantos de Lordran!!!')


vida_jogador=vitalidade * 20
dps_jogador=forca * 5

#loop da batalha
tentativas = batalha(vida_jogador, dps_jogador, vida_boss, dps_inicial_boss, tentativas, nome_boss)

#PRINTS
print(f'Você precisou de {tentativas} tentativas para vencer o(a) {nome_boss}!')


if nivel_experiencia=='Iniciante':
    if tentativas<=5:
        print('Esse iniciante teve muita sorte, no próximo boss ele vai conhecer a verdadeira DOR!!!')
    elif tentativas<=10:
        print('Até que não foi tão ruim assim, continue assim novato!')
    else:
        print('Bem vindo a Dark Souls.')

elif nivel_experiencia=='Veterano':
    if tentativas <=5:
        print('Você já andou por Lordran antes, não é? Impressionante.')
    elif tentativas <=10:
        print('Nada mal, guerreiro. Mas os próximos desafios não terão piedade.')
    else:
        print('Mesmo os veteranos sangram em Dark Souls...')

elif nivel_experiencia=='Mestre do Souls':
    if tentativas <=5:
        print('Inacreditável. Um verdadeiro Mestre do Souls. Está destinado a se tornar o Dark Lord!')
    elif tentativas <=10:
        print('Seu conhecimento sobre o ciclo é profundo. Quase como se já tivesse vivido isso mil vezes...')
    else:
        print('Nem mesmo os Mestres escapam ilesos da chama...')

if nome_boss=='Sif, a Grande Loba Cinzenta':
    print('A grande loba cai com honra. No fundo dos seus olhos, havia apenas lealdade.')

elif nome_boss=='Gwyn, Lorde das Cinzas':
    print('A chama se apaga, e o silêncio reina em Lordran. Você derrotou o Senhor das Cinzas...')
    if tentativas==1:
        print('O ciclo foi quebrado... Você se tornou o verdadeiro Senhor das Cinzas. Um novo destino começa...')
    else:
        print('Mas o ciclo... o ciclo continua.')
