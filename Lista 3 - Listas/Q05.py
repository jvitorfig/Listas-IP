doce=''
docesestragados=[]
qualidade=''
carro=[]
roda=''
volante=''
corpo=''
temroda=False
temvolante=False
temcorpo=False
temrodaboa=False
temvolantebom=False
temcorpobom=False
esgotou=False

print('Vamos lá, Vanellope! Vou te ajudar a montar um carro CINistro!')

while not esgotou:
    doce=input()

    if doce=='Recursos Esgotados':
        esgotou=True

    else:
        if doce=='O REI DOCE ESTÁ ROUBANDO TODOS OS INGREDIENTES!':
            print('Ah não!! Ele vai destruir seu carro, Vanellope! CUIDADO')
            if temroda==True:
                docesestragados.append(roda)
            if temcorpo==True:
                docesestragados.append(corpo)
            if temvolante==True:
                docesestragados.append(volante)
            #reseta o carro
            temroda=False
            temcorpo=False
            temvolante=False
            temcorpobom=False
            temrodaboa=False
            temvolantebom=False
            roda=''
            corpo=''
            volante=''
            carro=[]

        else:
            n=len(doce)
            for i in range(n):
                if doce[i]=='-':
                    doceatual=doce[0:i-1]
                    if doce[i+2:]=='estragado':
                        docesestragados.append(doceatual)
                        qualidade='estragado'
                    elif doce[i+2:]=='qualidade mediana':
                        qualidade='mediana'
                    elif doce[i+2:]=='alta qualidade':
                        qualidade='alta'

            #mudando o carro a cada doce recebido
            if qualidade=='alta': #pros doces de alta qualidade
                if doceatual=='Mentos' or doceatual=='Jujuba' and temrodaboa==False:
                    if temroda==True: #se já tiver um de media qualidade, ele vai pros estragados
                        docesestragados.append(roda)
                    roda=doceatual
                    temroda=True
                    temrodaboa=True

                elif doceatual=='Bolo de rolo' or doceatual=='Barra de chocolate' or doceatual=='Banda de ovo de Páscoa' and temcorpobom==False:
                    if temcorpo==True:
                        docesestragados.append(corpo)
                    corpo=doceatual
                    temcorpo=True
                    temcorpobom=True

                elif doceatual=='Pretzel' or doceatual=='Donuts' and temvolantebom==False:
                    if temvolante==True:
                        docesestragados.append(volante)
                    volante=doceatual
                    temvolante=True
                    temvolantebom=True

                else: #não usou o doce bom no carro
                    docesestragados.append(doceatual)

            if qualidade=='mediana': #pros doces de media qualidade
                if temroda==False and doceatual=='Mentos' or doceatual=='Jujuba':
                    roda=doceatual
                    temroda=True

                elif temcorpo==False and doceatual=='Bolo de rolo' or doceatual=='Barra de chocolate' or doceatual=='Banda de ovo de Páscoa':
                    corpo=doceatual
                    temcorpo=True

                elif temvolante==False and doceatual=='Pretzel' or doceatual=='Donuts':
                    volante=doceatual
                    temvolante=True
                
                else: #se não precisou usar, vai pros descartados
                    docesestragados.append(doceatual)

            carro=[roda,corpo,volante]

if temvolante==True and temroda==True and temcorpo==True and (temvolantebom==True or temcorpobom==True or temrodaboa==True):
    print('Conseguimos! Impossível você não ganhar essa corrida, Vanellope!')
    print(f'Para fazer o carro você utilizou {corpo} para ser a estrutura do carro, {volante} para o volante, {roda} para compor as rodas!')

elif temcorpo==True and temroda==True and temvolante==True:
    print('Pelo menos anda! Você consegue!')

else:
    print('Sinto muito, Vanellope. Não consegui te ajudar dessa vez.')

if docesestragados!=[]:
    print('Alguns doces foram descartados. São eles:')
    printdocesestragados=', '.join(docesestragados)
    print(printdocesestragados)
