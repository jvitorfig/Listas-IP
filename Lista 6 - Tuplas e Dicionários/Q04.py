qtd_tecnicos=int(input())
tecnicos={}

#RANKING DEFINIÇAO
primeiro=''
pontos_primeiro=0
segundo=''
pontos_segundo=0
terceiro=''
pontos_terceiro=0

for i in range (qtd_tecnicos):

    nome_tecnico=input()

    if nome_tecnico=='Ancelotti':
        print('Será que Carleto irá continuar no cargo?')

    elif nome_tecnico=='Jorge Jesus':
        print('O mister finalmente retornará ao Brasil?')

    nacionalidade=input()

    if nacionalidade!='argentino':
        titulos_continentais=int(input())
        titulos_nacionais=int(input())
        aproveitamento=float(input())

        #calculo da pontuaçao
        pontuacao_tecnico=0
        pontuacao_tecnico= (titulos_continentais*100 + titulos_nacionais * 50) * aproveitamento
        
        if nacionalidade=='brasileiro':
            pontuacao_tecnico*=1.1
        elif nacionalidade=='alemão':
            print('Iremos mesmo perdoar o 7x1?')
            pontuacao_tecnico*=0.9
        if titulos_continentais==0:
            pontuacao_tecnico*=0.5

        interesse=input()

        tecnicos[nome_tecnico] = {'pontos': pontuacao_tecnico,
                                  'nacionalidade': nacionalidade,
                                  'interesse': interesse} #dicionario com dicionario dentro (uma chave por tecnico) 

        #calculo do ranking
        if pontuacao_tecnico>pontos_primeiro:
            terceiro=segundo
            pontos_terceiro=pontos_segundo
            segundo=primeiro
            pontos_segundo=pontos_primeiro
            primeiro=nome_tecnico
            pontos_primeiro=pontuacao_tecnico

        elif pontuacao_tecnico>pontos_segundo:
            terceiro=segundo
            pontos_terceiro=pontos_segundo
            segundo=nome_tecnico
            pontos_segundo=pontuacao_tecnico

        elif pontuacao_tecnico>pontos_terceiro:
            terceiro=nome_tecnico
            pontos_terceiro=pontuacao_tecnico
           
    else: #argentino
        print('Um hermano comandando a seleção? Sai fora!')
        
print('Lista de treinadores - CBF')
print(f'1º {primeiro} - {tecnicos[primeiro]["nacionalidade"]} - {pontos_primeiro:.2f} pontos')
print(f'2º {segundo} - {tecnicos[segundo]["nacionalidade"]} - {pontos_segundo:.2f} pontos')
print(f'3º {terceiro} - {tecnicos[terceiro]["nacionalidade"]} - {pontos_terceiro:.2f} pontos')

tecnico_escolhido=''

#ESCOLHA DO TECNICO PELO RANKING
if tecnicos[primeiro]["interesse"]=='sim':
    tecnico_escolhido=primeiro
    nacionalidade_escolhido=tecnicos[primeiro]["nacionalidade"]
else:
    print(f'O {primeiro} não aceitou a proposta da CBF e outros nomes serão analisados. Cuida, CBF!')

    if tecnicos[segundo]["interesse"]=='sim':
        tecnico_escolhido=segundo
        nacionalidade_escolhido=tecnicos[segundo]["nacionalidade"]

    else:
        print(f'O {segundo} não aceitou a proposta da CBF e outros nomes serão analisados. Cuida, CBF!')

        if tecnicos[terceiro]["interesse"]=='sim':
            tecnico_escolhido=terceiro
            nacionalidade_escolhido=tecnicos[terceiro]["nacionalidade"]
        else:
            print(f'O {terceiro} não aceitou a proposta da CBF e outros nomes serão analisados. Cuida, CBF!')
            print('Nenhum técnico aceitou a maior seleção do mundo!? Que humilhação, Sr. Samir Xaud!!!')


if tecnico_escolhido:

    if (primeiro=='Ancelotti' or segundo=='Ancelotti' or terceiro=='Ancelotti') and tecnicos["Ancelotti"]["interesse"]=='sim':
        print('Ancelotti será o quarto estrangeiro a treinar o Brasil. Que honra para o italiano!')
        print('Depois de uma longa novela, Carlo Ancelotti continuará como o treinador da Seleção Brasileira! Estamos bem servidos!')
        tecnico_escolhido='Ancelotti'

    elif tecnicos[tecnico_escolhido]["nacionalidade"]!='brasileiro':
        print(f'{tecnico_escolhido} será o quarto estrangeiro a treinar o Brasil. Que honra para o {tecnicos[tecnico_escolhido]["nacionalidade"]}!')

    if tecnico_escolhido=='Jorge Jesus':
        print('JESUS VOLTOU!!! Será que ele conseguirá repetir na seleção o sucesso que obteve no Flamengo?')
    
    elif tecnico_escolhido=='Felipão':
        print('FELIPÃO DE NOVO!? Vem mais um 7x1 por aí?')
    
    else:
        if tecnico_escolhido!='Ancelotti':
          print(f'O técnico {tecnicos[tecnico_escolhido]["nacionalidade"]} {tecnico_escolhido} irá treinar o Brasil. Não era o nome que esperávamos, mas torcemos para que faça um bom trabalho!')