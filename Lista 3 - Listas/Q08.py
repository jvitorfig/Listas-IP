alfabeto=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
codigo=['k', 'q', 'f', 'm', 'x', 'e', 't', 'z', 'r', 'h', 'v', 'n', 'd', 'l', 'j', 'a', 's', 'u', 'y', 'b', 'g', 'w', 'p', 'o', 'i', 'c', ' ']
nomedecodificado=''
acao=''
teenteamcompleto=False

n=int(input()) #numero de equibes
matriz=[]

for c in range (n):
    matriz.append([])

while acao!='FIM':
    acao=input()
    nomedecodificado=''

    if acao=='adicionar':
        print('Quem será o próximo integrante do time?')

        heroi=input()
        for c in range (len(heroi)):
            if heroi[c] =='-': #separando a string

                nomeheroi=heroi[0:c-1]

                #DECODIFICAÇÃO
                for i in nomeheroi:
                    indice=codigo.index(i)
                    letra=alfabeto[indice]
                    nomedecodificado+=letra

                nivelheroi=int(heroi[c+1:])

        if nomedecodificado=='rex splode':
            print('Eu vou te detonar!')
        elif nomedecodificado=='atom eve':
            print('Eu reescrevo a matéria... incluindo a SUA.')
        elif nomedecodificado=='duplikate':
            print('Quantas de mim você acha que consegue lidar?')
        elif nomedecodificado=='robot':
            print('Minha lógica diz que você vai perder.')
        
        time=int(input())

        matriz[time].append(nomedecodificado)
        matriz[time].append(nivelheroi)


    if acao=='metamorfo':
        print('Atenção!!! Metamorfo encontrado, quem deverá ser removido do time?')
        heroifalso=input()
        print('Quem você gostaria de colocar no lugar?')
        heroi=input()
        time=int(input())

        index=matriz[time].index(heroifalso)
        matriz[time].remove(matriz[time][index]) #remove o metamorfo e seu nível
        matriz[time].remove(matriz[time][index])

        for c in range (len(heroi)):
            if heroi[c] =='-': #separando a string

                nomeheroi=heroi[0:c-1]

                #DECODIFICAÇÃO
                for i in nomeheroi:
                    indice=codigo.index(i)
                    letra=alfabeto[indice]
                    nomedecodificado+=letra

                nivelheroi=int(heroi[c+1:])

        if nomedecodificado=='rex splode':
            print('Eu vou te detonar!')
        elif nomedecodificado=='atom eve':
            print('Eu reescrevo a matéria... incluindo a SUA.')
        elif nomedecodificado=='duplikate':
            print('Quantas de mim você acha que consegue lidar?')
        elif nomedecodificado=='robot':
            print('Minha lógica diz que você vai perder.')

        matriz[time].append(nomedecodificado)
        matriz[time].append(nivelheroi)


# aumento de 10%
for c in range (len(matriz)):
    if 'rex splode' in matriz[c] and 'duplikate' in matriz[c] and 'atom eve' in matriz[c] and 'robot' in matriz[c]:
        teenteamcompleto=True
        for i in range (1, len(matriz[c])+1, 2):
            matriz[c][i]=(matriz[c][i])*1.1

# escolha do melhor time
melhortime=0
pontosmelhortime=0

for c in range (len(matriz)):
    pontos=0
    for i in range (1, len(matriz[c])+1, 2):
        pontos+=(matriz[c][i])
    if pontos>pontosmelhortime:
        pontosmelhortime=pontos
        melhortime=matriz[c]

#ordem decrescente
niveismelhortime=[]
nomesmelhortime=[]
for c in range (0, len(melhortime), 2):
    nomesmelhortime.append(melhortime[c])
for c in range (1, len(melhortime), 2):
    niveismelhortime.append(melhortime[c])

for i in range(1,len(niveismelhortime)): #algoritmo pra ordenar em ordem decrescente
    nivel=niveismelhortime[i]
    nome=nomesmelhortime[i]
    j=i-1

    while j>=0 and niveismelhortime[j]<nivel:
        niveismelhortime[j+1]=niveismelhortime[j]
        nomesmelhortime[j+1]=nomesmelhortime[j]
        j-=1

    niveismelhortime[j+1]=nivel
    nomesmelhortime[j+1]=nome


if teenteamcompleto==True:
    print('O teen team esta completo, Cecil esta muito contente!')

print(f'Aqui está o poderoso time da terra: {nomesmelhortime[0]}, {nomesmelhortime[1]}, {nomesmelhortime[2]}')

#batalha
vitoriasterra=0
vitoriasinimigos=0
viltrumita=[['general kregg',110],['conquista',100], ['anissa', 90]]

for c in range (0, 3):
    print(f'{c+1} Duelo: {nomesmelhortime[c]} X {viltrumita[c][0]}')
    if niveismelhortime[c]>viltrumita[c][1]:
        vitoriasterra+=1
    elif viltrumita[c][1]>niveismelhortime[c]:
        vitoriasinimigos+=1

if vitoriasterra>vitoriasinimigos:
    print('A terra venceu!')
else:
    print('Infelizmente o imperio viltrumita conquistou a terra!')
