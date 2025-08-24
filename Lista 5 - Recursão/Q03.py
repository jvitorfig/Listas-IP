def tribonacci (num, a, b, c):

    t=a+b+c

    if num == t: #achou o numero em tribonacci
        return True
    
    elif t > num: #o valor atual passou de num, ent n tem na sequencia
        return False
    else:
        return tribonacci(num, t, a, b)


def fatorial (num, a, r):
    r *= a #r é o fatorial do antecessor de a

    if num == r: #achou o numero no fatorial
        return True
    
    elif r > num:
        return False

    else:
        return fatorial (num, a+1, r)
    

def catalan(n, lista_catalan=[]): #funçao que diz se um numero é catalan
    if lista_catalan ==[]:
        lista_catalan = [1]

    if n in lista_catalan:
        return [True, lista_catalan]

    if n < lista_catalan[-1]:
        return [False, lista_catalan]

    proximo = 0
    for i in range(len(lista_catalan)):
        proximo += lista_catalan[i] * lista_catalan[-i - 1]
    lista_catalan.append(proximo)
    
    return catalan(n, lista_catalan)


nome_e_vida=input().split(' - ')
qtd_acoes=int(input())

nome=nome_e_vida[0]
vida_maxima=int(nome_e_vida[1])

armas=[]
danos=[]
runa_ativa=''

for i in range(qtd_acoes):
    entrada=input()

    if '-' in entrada: #é arma
        entrada=entrada.split(' - ')
        nome_arma_atual=entrada[0]
        dano_arma_atual=int(entrada[1])
        tipo_arma_atual=entrada[2]

        print(f'Vou levar a/o {nome_arma_atual} ela/e vai ser de grande ajuda.')
     
        print('Hora de Aprimorar!!!')
        nivel=0
        while entrada !='fim':

            entrada=input()

            if entrada != 'fim':
                if tipo_arma_atual=='basica':
                    if tribonacci(int(entrada), 1, 0, 0)==True and nivel<20:
                        nivel+=1
                        print(f'Pronto, consegui mais um nível agora a/o {nome_arma_atual} está no nível {nivel}!')
                        dano_arma_atual=dano_arma_atual*1.1

                elif tipo_arma_atual=='especial':
                    if fatorial(int(entrada), 1, 1)==True and nivel<10:
                        nivel+=1
                        print(f'Pronto, consegui mais um nível agora a/o {nome_arma_atual} está no nível {nivel}!')
                        dano_arma_atual=dano_arma_atual*1.2

        if nivel>0:
            print(f'Agora sim! Acho que a/o {nome_arma_atual} está forte o suficiente, consegui colocar ele/a para o nível {nivel}')
        else:
            print(f'Droga não consegui aumentar o nível da/o {nome_arma_atual}')

        armas.append(nome_arma_atual)
        danos.append(dano_arma_atual)

    else: #runa
        print('A batalha vai ser difícil melhor tentar ativar uma runa!')

        #FRASE DE EFEITO
        if entrada=='Grande Runa de Godrick':
            frase_efeito='acho que um pouco de tudo não é nada mal.'
        elif entrada=='Grande Runa de Radahn':
            frase_efeito='mais vida vai ajudar muito.'
        elif entrada=='Grande Runa de Morgott':
            frase_efeito='quanto mais vida melhor.'
        elif entrada=='Grande Runa de Malenia':
            frase_efeito='ela foi tão difícil de conseguir, tenho que testar ela pelo menos uma vez.'

        print(f'Me decidi vou tentar ativar a {entrada}, {frase_efeito}')
        
        numeros=[]
        for i in range (10):
            num=int(input())
            numeros.append(num)
        
        maior=max(numeros) #maior dos inputs

        lista_catalan = catalan(maior)[1] #faz o algoritmo ate o numero maior

        catalans_do_input=[] #lista com os numeros do input q tbm sao de catalan
        for num in numeros:
            if num in lista_catalan:
                catalans_do_input.append(num)

        if len(catalans_do_input) >= 3:
            i = 0

            while i < len(catalans_do_input) - 2 and runa_ativa=='':
                trinca_usuario = catalans_do_input[i:i+3]

                for j in range(len(lista_catalan) - 2):
                    trinca_catalan = lista_catalan[j:j+3]

                    if runa_ativa=='' and trinca_usuario == trinca_catalan:
                        runa_ativa = entrada
                        print("Isso consegui ativar a Grande Runa.")
                        print(f"Acabei precisando apenas dos números: {trinca_usuario[0]} - {trinca_usuario[1]} - {trinca_usuario[2]}.")
                
                i += 1

        if not runa_ativa:
            print("Caramba não consegui ativar a Grande Runa, infelizmente vou ter que me contentar com as armas que vou levar.")

    print() #fim do processamento de arma/runa


#se tiver runa ativa
if runa_ativa=='Grande Runa de Radahn':
    vida_maxima+=vida_maxima * 0.15
elif runa_ativa=='Grande Runa de Morgott':
    vida_maxima+=vida_maxima * 0.25
elif runa_ativa=='Grande Runa de Godrick':
    for i in range (len(danos)):
        danos[i] = int(danos[i] * 1.1)
    vida_maxima=round(vida_maxima*1.1)

#BATALHA
inimigo=input().split(' - ') 
nome_inimigo=inimigo[0]
vida_inimigo=int(inimigo[1])
dano_inimigo=int(inimigo[2])

vida_maxima=int(vida_maxima)
vida=vida_maxima

for i in range (len(danos)): #arredondamento
    danos[i]=int(danos[i])

turno=0
while vida_inimigo>0 and vida>0 and len(armas)>0:

    turno+=1
    print(f'{turno}° TURNO')
    print(f'Melhor conferir meus status antes de lutar -> vida: ({vida}/{vida_maxima})')
    print(f'E o {nome_inimigo} ainda está com {vida_inimigo} pontos de vida')

    arma_utilizada=armas.pop(0)
    dano_causado=danos.pop(0)

    print(f'Atacando com {arma_utilizada}.')
    print(f'Consegui causar {dano_causado} de dano no/a {nome_inimigo}!!!')
    print(f'Acabei consumindo a/o {arma_utilizada}, hora de pegar outra arma do arsenal.')
    vida_inimigo-=dano_causado

    if vida_inimigo>0:
        if runa_ativa=='Grande Runa de Malenia' and vida<vida_maxima:
            cura=int(vida_maxima * 0.05)

            if vida+cura>vida_maxima:
                cura=vida_maxima-vida
                vida=vida_maxima

            else:
                vida+=cura

            print(f'Ainda bem que eu ativei a Grande Runa da Malenia, consegui recuperar {cura}')

        vida-=dano_inimigo
        print(f'Droga {nome_inimigo} ainda não morreu, acabei recebendo {dano_inimigo} de dano.')
        print()


if vida_inimigo <= 0:
    print()
    print('Great Enemy Felled')
    if len(armas)==0:
        print(f'Acabei usando tudo que eu trouxe, mas finalmente consegui derrotar a/o {nome_inimigo}.')
    else:
        print(f'Finalmente depois de tanto me preparar consegui derrotar a/o {nome_inimigo}.')
        print(f'Acho que me preparei bem eu ainda tenho {len(armas)} arma/as sobrando são ela/as: {", ".join(armas)}.')

elif vida <= 0 or len(armas) == 0:
    if len(armas)==0 and vida>0:
        print(f'Parece que eu não me preparei o suficiente, acabei usando tudo que tinha e a/o {nome_inimigo} ainda tem {vida_inimigo} pontos de vida, vou ter que me preparar mais da próxima vez.')
    else:
        print('You Died')
        print(f'Droga acabei morrendo para a/o {nome_inimigo} e ele ainda tem {vida_inimigo} pontos de vida, vou ter que trazer armas mais fortes da próxima vez.')
    