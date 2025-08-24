qtd_atletas=int(input(''))

if qtd_atletas==1:
    atleta1=str(input(''))
    pos_atleta1=int(input(''))
    rank_atleta1=int(input(''))
    vel_atleta1=float(input(''))
    print(f'Não há dúvidas... {atleta1} é o culpado!')

else:
    if qtd_atletas==2:
        atleta1=str(input(''))
        pos_atleta1=int(input(''))
        rank_atleta1=int(input(''))
        vel_atleta1=float(input(''))
        atleta2=str(input(''))
        pos_atleta2=int(input(''))
        rank_atleta2=int(input(''))
        vel_atleta2=float(input(''))
        print(f'Caso encerrado: {atleta1} e {atleta2} roubaram o troféu!')

    else:
        primeiro=''
        segundo=''
        terceiro=''
        pontosprimeiro=0
        pontossegundo=0
        pontosterceiro=0
        pontosnovo=0
        vogaisnovo=0
        atletanovo=''

        for c in range (1, qtd_atletas+1):
            print(f'COMEÇANDO A {c}ª RODADA DE INVESTIGAÇÃO')

            atletanovo=str(input(''))
            nomeverific=atletanovo.lower()
            for h in nomeverific:
                if h=='a' or h=='e' or h=='i' or h=='o' or h=='u':
                    vogaisnovo+=1
            if vogaisnovo%2==0:
                pontosnovo+=10
            elif vogaisnovo%2==1:
                pontosnovo+=5 

            pos_atletanovo=int(input(''))
            if 45<=pos_atletanovo<=135:
                pontosnovo+=10 
                print(f'{atletanovo} estava em posição estratégica para pegar o troféu... muito suspeito!')
            elif 225<=pos_atletanovo<=315:
                pontosnovo+=5
            else:
                pontosnovo+=2

            rank_atletanovo=int(input(''))
            if rank_atletanovo<=10:
                pontosnovo+=10
                print(f'{atletanovo} é um dos melhores do mundo... e também um dos principais suspeitos!')
            elif 11<=rank_atletanovo<=50:
                pontosnovo+=5
            else:
                pontosnovo+=2

            vel_atletanovo=float(input(''))
            if vel_atletanovo>140:
                pontosnovo+=10
                print(f'Alta velocidade detectada! {atletanovo} pode ter fugido rapidamente com o troféu!')
            elif 100<=vel_atletanovo<=140:
                pontosnovo+=5
            else:
                pontosnovo+=2
            
            if (45>pos_atletanovo or pos_atletanovo>135) and (rank_atletanovo>10) and (vel_atletanovo<140):
                print(f'Hum, esse {atletanovo} sei não viu... Deve tá escondendo alguma coisa.')


            if pontosnovo>pontosprimeiro:
                pontosterceiro=pontossegundo
                terceiro=segundo
                pontossegundo=pontosprimeiro
                segundo=primeiro
                pontosprimeiro=pontosnovo
                primeiro=atletanovo
            
            elif pontosprimeiro>=pontosnovo>pontossegundo:
                pontosterceiro=pontossegundo
                terceiro=segundo
                pontossegundo=pontosnovo
                segundo=atletanovo

            elif pontossegundo>=pontosnovo>pontosterceiro:
                pontosterceiro=pontosnovo
                terceiro=atletanovo


            pontosnovo=0
            vogaisnovo=0

        print(f'''
RESULTADOS DAS INVESTIGAÇÕES:

Os 3 principais suspeitos são:
1. {primeiro} - {pontosprimeiro} pontos
2. {segundo} - {pontossegundo} pontos
3. {terceiro} - {pontosterceiro} pontos
''')

        if pontosprimeiro==pontossegundo:
            print(f'Que absurdo... {primeiro} e {segundo} roubaram o troféu juntos!')
        else:
            print(f'Mistério resolvido: O culpado é {primeiro}! Ele roubou o troféu de Calderano.')