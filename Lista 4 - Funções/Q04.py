herois = ['Gohan',    'Goku',       'Goten',     'Kuririn',     'Piccolo',  
     'Tenshinhan',   'Trunks',      'Uub',       'Vegeta',      'Yamcha']

viloes = ['Babidi',    'Baby',     'Broly',     'Buu',     'Cell',     
          'Cooler',   'Frieza',    'Hit',     'Janemba',   'Zamasu']

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']


def arredondamento(num):
    inteiro=int(num)
    if inteiro==num:
        return inteiro
    else:
        return inteiro+1


def fusao(nome1, nome2):
    nome_fusao=''
    fusao_perfeita=False
    fusao_especial=False

    if (nome1 in herois and nome2 in viloes) or (nome2 in herois and nome1 in viloes):
        print('Heróis e vilões não se misturam! As auras dos dois participantes são incompatíveis.')

    elif (nome1=='Vegeta' and nome2=='Goku') or (nome1=='Goku' and nome2=='Vegeta'):
        nome_fusao='Vegito'
        fusao_perfeita=True
        fusao_especial=True
    elif  (nome1=='Goten' and nome2=='Trunks') or (nome1=='Trunks' and nome2=='Goten'):
        nome_fusao='Gotenks'
        fusao_perfeita=True
        fusao_especial=True

    else:
        #PRIMEIRA TENTATIVA
        #primeiro nome
        if len(nome1)<=4:
            pedaco1fusao=nome1[0] 
        else:
            num1=len(nome1)/2
            num1=arredondamento(num1)
            pedaco1fusao=nome1[0:num1]

        nome_fusao+=pedaco1fusao
        
        #segundo nome
        if len(nome2)<=4:
            if len(nome2)==3:
                pedaco2fusao=nome2[len(nome2)-2:len(nome2)]
            else:
                pedaco2fusao=nome2[len(nome2)-3:len(nome2)]
        else:
            num2=len(nome2)/2
            num2=arredondamento(num2)-1
            pedaco2fusao=nome2[len(nome2)-num2:len(nome2)]

        nome_fusao+=pedaco2fusao

        #SEGUNDA TENTATIVA
        if len(nome_fusao)<=3 or (pedaco1fusao[-1].lower() in consoantes and pedaco2fusao[0].lower() in consoantes) or (pedaco1fusao[-1].lower() in vogais and pedaco2fusao[0].lower() in vogais):
            print(f'A sincronização foi um desastre... {nome_fusao} é uma fusão imperfeita!')

            if len(nome1)<=4:
                pedaco1fusao=nome1[0:2]
            else:
                num1=len(nome1)/2
                num1=arredondamento(num1)+1
                pedaco1fusao=nome1[0:num1]

            nome_fusao=pedaco1fusao+pedaco2fusao

            #TERCEIRA TENTATIVA
            if len(nome_fusao)<=3 or (pedaco1fusao[-1].lower() in consoantes and pedaco2fusao[0].lower() in consoantes) or (pedaco1fusao[-1].lower() in vogais and pedaco2fusao[0].lower() in vogais):
                print(f'A sincronização foi um desastre... {nome_fusao} é uma fusão imperfeita!')

                if len(nome1)>4:
                    num1=len(nome1)/2
                    num1=arredondamento(num1)
                    pedaco1fusao=nome1[0:num1]

                if len(nome2)<=4:
                    pedaco2fusao=nome2[len(nome2)-3:len(nome2)].lower()
                else:
                    num2=len(nome2)/2
                    num2=arredondamento(num2)
                    pedaco2fusao=nome2[len(nome2)-num2:len(nome2)]

                nome_fusao=pedaco1fusao+pedaco2fusao

                if len(nome_fusao)<=3 or (pedaco1fusao[-1].lower() in consoantes and pedaco2fusao[0].lower() in consoantes) or (pedaco1fusao[-1].lower() in vogais and pedaco2fusao[0].lower() in vogais):
                    print(f'A sincronização foi um desastre... {nome_fusao} é uma fusão imperfeita!')
                    print('Aparentemente essa combinação é incompatível...')
                else:
                    fusao_perfeita=True
            else:
                fusao_perfeita=True
        else:
            fusao_perfeita=True
    
    if fusao_perfeita==True:
        if nome1 in herois:
            print(f'Fusão realizada com sucesso! {nome_fusao} entra em combate para derrotar o exército de vilões!')
        else:
            print(f'Fusão realizada com sucesso! {nome_fusao} entra em combate com sede de destruir Satan City!')

    return nome_fusao, fusao_perfeita, fusao_especial
            
def calculo_poder(nome_fusao):
    if len(nome_fusao)==4:
        poder=2000
    elif len(nome_fusao)==5:
        poder=2250
    elif len(nome_fusao)==6:
        poder=2500
    elif len(nome_fusao)==7:
        poder=2750
    else:
        poder=3000

    return poder

#INPUTS
poder_herois = 0
poder_viloes = 0
personagens_fundidos=[]

while poder_herois<=8000 and poder_viloes<=8000:

    nome1=input()
    print(f'{nome1} se elege para participar da fusão!')
    nome2=input()
    print(f'{nome2} se elege para participar da fusão!')

    while nome1 in personagens_fundidos or nome2 in personagens_fundidos:#se ja fundiu, pede outros nomes
        
        if nome1 in personagens_fundidos:
            print(f'{nome1} já participou de uma fusão. Fusão inválida.')
        if nome2 in personagens_fundidos:
            print(f'{nome2} já participou de uma fusão. Fusão inválida.') 

        nome1=input()
        print(f'{nome1} se elege para participar da fusão!')
        nome2=input()
        print(f'{nome2} se elege para participar da fusão!')

    fusaoatual, fusao_perfeita, fusao_especial = fusao(nome1, nome2)

    if fusao_perfeita:
        if not fusao_especial:
            personagens_fundidos.append(nome1)
            personagens_fundidos.append(nome2)

        if nome1 in herois:
            poder_herois+=calculo_poder(fusaoatual)
        else:
            poder_viloes+=calculo_poder(fusaoatual)

if poder_herois>poder_viloes:
    print('O poder dos heróis... É mais de 8000! Eles derrotam os vilões e conseguem selar o portal.')
else:
    print('Os vilões são fortes demais! Satan City está em apuros!')
