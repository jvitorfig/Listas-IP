vida_piccolo=100
vida_gohan=100
vida_goku=200

def batalha(vida_oponente, oponente):
    vida_vegeta=100
    vegeta_morreu=False
    oponente_morreu=False
    desmaio=False
    numero_do_turno=1
    golpe_anterior_vegeta=''


    print(f'--- Iniciando o combate contra {oponente} ---')

    while vegeta_morreu==False and oponente_morreu==False:
        print()
        print(f'--- Turno {numero_do_turno} ---')
        numero_do_turno+=1

        ataque_vegeta=input()
        if golpe_anterior_vegeta=='Potente' and ataque_vegeta=='Potente':
            vegeta_morreu=True
            desmaio=True
            print('Vegeta usou dois Golpes Potentes seguidos e desmaiou com o esforço!')

        else:
            golpe_anterior_vegeta=ataque_vegeta
            dano_vegeta=ataque(ataque_vegeta,motivacao_vegeta)
            vida_oponente=vida_oponente-dano_vegeta
            print(f'Vegeta usou Golpe {ataque_vegeta} e causou {dano_vegeta} de dano!')

            if vida_oponente>0:
                ataque_oponente=input()
                dano_oponente=ataque(ataque_oponente, motivacao_oponente)
                vida_vegeta=vida_vegeta-dano_oponente
                print(f'{oponente} usou Golpe {ataque_oponente} e causou {dano_oponente} de dano!')

                if vida_vegeta<=0:
                    vegeta_morreu=True

            else:
                oponente_morreu=True

        if not vegeta_morreu and not oponente_morreu:
            print(f'|Vegeta: {vida_vegeta} HP vs {oponente}: {vida_oponente} HP|')

    #derrota do vegeta
    if vegeta_morreu==True:
        vida_vegeta=0
        print(f'|Vegeta: {vida_vegeta} HP vs {oponente}: {vida_oponente} HP|')
        #if desmaio==False:
        print()
        print(f'Vegeta foi derrotado! A Terra está a salvo graças a {oponente}!')
    
    #vegeta derrotou um oponente
    else:
        print(f'|Vegeta: {vida_vegeta} HP vs {oponente}: 0 HP|')
        print()
        print('Vitória de Vegeta!')
        print(f'Vegeta venceu a batalha contra {oponente} com {vida_vegeta} HP restantes!')
        print()

    return [vegeta_morreu, vida_vegeta]
        

def ataque(golpe,motivacao): #calcula o dano
    if golpe=='Normal':
        dano=20
    elif golpe=='Potente':
        dano=40
    dano=int(dano*motivacao)
    return dano


print('A saga de Vegeta começa!')
print()

#PRIMEIRA BATALHA
motivacao_vegeta=float(input())
motivacao_oponente=float(input())

[vegeta_morreu, vida_vegeta]=batalha(100, 'Piccolo') 

#SEGUNDA BATALHA
if vegeta_morreu==False:
    motivacao_oponente=float(input())
    motivacao_vegeta=motivacao_vegeta * (1+(vida_vegeta/100))
    [vegeta_morreu, vida_vegeta]=batalha(100,'Gohan')

#TERCEIRA BATALHA
    if vegeta_morreu==False:
        motivacao_oponente=float(input())
        motivacao_vegeta=motivacao_vegeta * (1+(vida_vegeta/100))
        [vegeta_morreu, vida_vegeta]=batalha(200,'Goku')
        
        if vegeta_morreu==False:
            print('Vegeta derrotou todos os Guerreiros Z! A Terra foi conquistada!')

