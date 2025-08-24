qtd_grupos=int(input())
grupos={}

for c in range(1, qtd_grupos+1): #pra cada grupo

    times_grupo_atual=[]

    for i in range (4): #processando os 4 times do grupo

        time=input()
        time=time.split(' - ')

        nome_time=time[0]
        pontuacao_time=int(time[1])
        times_grupo_atual.append((pontuacao_time,nome_time)) #tupla com a pontuaçao e o nome pra ordenar

        times_grupo_atual.sort() #ordena do grupo com menos pontos pro grupo com mais pontos
        times_grupo_atual.reverse() #inverte do lider pro lanterna


    grupos[c]=times_grupo_atual #o inteiro vai ser a chave de uma lista com os times


if qtd_grupos<2 or qtd_grupos%2==1: #sem cruzamento
    print(f'Mas como que vamos fazer um torneio com {qtd_grupos} grupos Samir!?')

else:
    print('Roda os dados Samir!')

    chaves=[] #lista com tuplas de dois inteiros que sao as keys do dicionario
    for i in range (qtd_grupos//2):
        n=input().split(' x ')
        n1=int(n[0])
        n2=int(n[1])
        chaves.append((n1, n2))

    for c in range (len(chaves)):

        primeiro_grupo=grupos[chaves[c][0]] #pega a primeira chave e acessa o primeiro indice (key do dicionario pra definir o primeiro grupo do confronto)
        segundo_grupo=grupos[chaves[c][1]] #mesma coisa

        print()
        print(f'Confrontos chave {c+1}:')
        print(f'{primeiro_grupo[0][1]} x {segundo_grupo[1][1]}') #tava guardado em tupla de (ponto, nome), entao tem que pegar o indice [1] pra printar so o nome
        print(f'{primeiro_grupo[1][1]} x {segundo_grupo[0][1]}')

    print()
    for i in range (1, qtd_grupos+1):
        print(f'O time {grupos[i][3][1]} ficou em último lugar em seu grupo e foi rebaixado!')

