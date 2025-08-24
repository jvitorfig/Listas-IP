def batalha(turno, vitalidade_sekiro, postura_sekiro, cabacas_curativas_sekiro, vitalidade_genichiro, postura_genichiro):
    turno+=1
    print(f'--- Turno {turno} ---')

    arsenal_genichiro=['ataque', 'defesa', 'recuperação de postura', 'ataque kanji']
    arsenal_sekiro=['ataque', 'defesa', 'defesa perfeita', 'usar cabaça', 'desviar', 'contra ataque mikiri']

    acao_genichiro=input()
    #loop pra caso a ação seja inválida
    while acao_genichiro not in arsenal_genichiro:
        print('Genichiro não tem esse movimento em seu arsenal.')
        acao_genichiro=input()

    acao_sekiro=input()
    #loop pra caso a ação seja inválida
    while acao_sekiro not in arsenal_sekiro:
        print('O lobo não adquiriu esse movimento ainda.')
        acao_sekiro=input()


    if acao_genichiro=='ataque':

        if acao_sekiro=='ataque':
            vitalidade_sekiro-=25
            vitalidade_genichiro-=10
            postura_genichiro+=15
            print('Clima de tensão! Os dois atacam numa luta implacável!')
        
        elif acao_sekiro=='defesa':
            vitalidade_sekiro-=10
            postura_sekiro+=20
            print('Sekiro firma sua espada e se defende, absorvendo o impacto em sua postura!')
        
        elif acao_sekiro=='defesa perfeita':
            postura_genichiro+=25
            print('Lâminas se encontram! Um desvio perfeito de Sekiro desequilibra Genichiro!')
        
        elif acao_sekiro=='usar cabaça':
            if cabacas_curativas_sekiro>0:
                cabacas_curativas_sekiro-=1
                vitalidade_sekiro-=25
                print('Sekiro tenta curar, mas é punido pelo ataque impiedoso de Genichiro!')
            else:
                vitalidade_sekiro-=25
                print('Sekiro busca sua cabaça, mas ela está vazia!')
                print('Enquanto Sekiro se distrai, Genichiro avança com um ataque certeiro!')

        elif acao_sekiro=='desviar':
            print('O lobo desvia agilmente do ataque comum de Genichiro!')

        elif acao_sekiro=='contra ataque mikiri':
            postura_genichiro+=10
            print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro faz um movimento comum.')



    elif acao_genichiro=='defesa':

        if acao_sekiro=='ataque':
            postura_genichiro+=5
            print('Genichiro prevê o movimento e apara o golpe de Sekiro com sua lâmina!')

        elif acao_sekiro=='defesa':
            print('Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.')

        elif acao_sekiro=='defesa perfeita':
            print('Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.')

        elif acao_sekiro=='usar cabaça':
            if cabacas_curativas_sekiro>0:
                print('Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.')
                vitalidade_sekiro+=25

            else:
                print('Sekiro busca sua cabaça, mas ela está vazia!')
                print('Genichiro mantém a guarda, enquanto o lobo percebe seu erro.')

            cabacas_curativas_sekiro-=1

        elif acao_sekiro=='desviar':
            print('O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.')

        elif acao_sekiro=='contra ataque mikiri':
            print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.')



    elif acao_genichiro=='recuperação de postura':

        if acao_sekiro=='ataque':
            vitalidade_genichiro-=10
            postura_genichiro+=15
            print('Genichiro ia recuperar sua postura mas o lobo foi mais rápido, um grande ataque por parte do lobo!')

        elif acao_sekiro=='defesa':
            postura_genichiro=0
            print('Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.')
            print('Genichiro consegue recuperar sua postura, cuidado lobo!')
        
        elif acao_sekiro=='defesa perfeita':
            postura_genichiro=0
            print('Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.')
            print('Genichiro consegue recuperar sua postura, cuidado lobo!')

        elif acao_sekiro=='usar cabaça':
            postura_genichiro=0

            if cabacas_curativas_sekiro>0:
                vitalidade_sekiro+=25
                print('Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.')
                print('Genichiro consegue recuperar sua postura, cuidado lobo!')
            else:
                print('Sekiro busca sua cabaça, mas ela está vazia!')
                print('Genichiro aproveita a hesitação do lobo para recuperar sua postura.')
                print('Genichiro consegue recuperar sua postura, cuidado lobo!')

            cabacas_curativas_sekiro-=1


        elif acao_sekiro=='desviar':
            postura_genichiro=0
            print('O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.')
            print('Genichiro consegue recuperar sua postura, cuidado lobo!')
        
        elif acao_sekiro=='contra ataque mikiri':
            postura_genichiro=0
            print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.')
            print('Genichiro consegue recuperar sua postura, cuidado lobo!')



    elif acao_genichiro=='ataque kanji':

        if acao_sekiro=='contra ataque mikiri':
            postura_genichiro+=25
            print('O lobo utiliza a técnica de contra ataque mikiri e pisa na arma de Genichiro!')

        elif acao_sekiro=='desviar':
            print('O lobo desvia do ataque especial de Genichiro com muita agilidade!')

        elif acao_sekiro=='usar cabaça':
            vitalidade_sekiro-=50
            postura_sekiro+=20
            print('O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!')
            
            if cabacas_curativas_sekiro<=0:
                print('Para piorar, Sekiro nem sequer tinha uma cabaça para usar!')
            cabacas_curativas_sekiro-=1

        else:
            vitalidade_sekiro-=50
            postura_sekiro+=20
            print('O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!')

    
    #verificações de morte
    if vitalidade_genichiro<1 or postura_genichiro>=100:
        turno+=1
        print(f'--- Turno {turno} ---')

        print('Genichiro está de joelhos e vulnerável! Acabe com isso, Lobo!')
        acao_sekiro=input()

        if acao_sekiro=='ataque':
            print('Sekiro executa um Golpe Mortal em Genichiro!')
            print('====================================')
            print('Vitória de Sekiro: Golpe Mortal!')

        elif acao_sekiro=='hesitar':
            print('O lobo hesitou no seu golpe final, Genichiro recupera sua postura! Cuidado, Lobo!')
            if postura_genichiro>=100:
                postura_genichiro-=50

                if vitalidade_genichiro<50:
                    vitalidade_genichiro=50
                

            elif vitalidade_genichiro<1:
                vitalidade_genichiro+=50
                postura_genichiro=50
                
            return batalha(turno, vitalidade_sekiro, postura_sekiro, cabacas_curativas_sekiro, vitalidade_genichiro, postura_genichiro)


    elif vitalidade_sekiro<1:
        print('Sekiro cai de joelhos, derrotado...')
        print('====================================')
        print('Vitória de Genichiro: Morte.')

    elif postura_sekiro>=100:
        print('A postura do lobo foi quebrada! Ele não consegue se defender e é derrotado!')
        print('====================================')
        print('Vitória de Genichiro: Morte.')

    else:
        return batalha(turno, vitalidade_sekiro, postura_sekiro, cabacas_curativas_sekiro, vitalidade_genichiro, postura_genichiro)

#MAIN
turno=0
print('O duelo começa! Suas decisões determinarão o vencedor.')

vitalidade_sekiro=100
postura_sekiro=0
cabacas_curativas_sekiro=2

vitalidade_genichiro=100
postura_genichiro=0

#função recursiva
batalha(turno, vitalidade_sekiro, postura_sekiro, cabacas_curativas_sekiro, vitalidade_genichiro, postura_genichiro)

