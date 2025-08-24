jogoacabou=False
dia=0
quarteiroes_restaurados=0
diasemrestaurar=0
restaurou=False

tamanho=int(input()) #ordem da matriz

matriz=[]

for c in range (tamanho):
    linha=input()
    linha=linha.split(' ')
    matriz.append(linha)
    if 'H' in linha: #posição do homem aranha
        linha_h=c
        coluna_h=linha.index('H')

while jogoacabou==False:
    quarteiroes_destruidos=0
    quarteiroes_corrompidos=0

    mensagemespecial=''
    dia+=1
    comando=input()
    if comando=='FIM':
        jogoacabou=True
        print('Ainda existem quarteirões corrompidos! O Miranha não pode ir embora agora!')
    else:

        novalinha=linha_h
        novacoluna=coluna_h


        if comando=='Direita':
            novacoluna+=1
        elif comando=='Esquerda':
            novacoluna-=1
        elif comando=='Cima':
            novalinha-=1
        elif comando=='Baixo':
            novalinha+=1


        if -1 < novalinha < tamanho and -1 < novacoluna < tamanho: #dentro do range

            if matriz[novalinha][novacoluna]=='X': #lugar destruído
                mensagemespecial='Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!'

            else:
                if matriz[novalinha][novacoluna]=='E':
                    quarteiroes_restaurados+=1
                    diasemrestaurar=0
                    mensagemespecial='O Miranha restaurou um quarteirão!'
                else:
                    mensagemespecial='O Electro está ganhando espaço!'
                    diasemrestaurar+=1


                matriz[linha_h][coluna_h]='.'
                matriz[novalinha][novacoluna]='H'
                linha_h=novalinha
                coluna_h=novacoluna
            
        else: #fora do range
            mensagemespecial='Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!'

        if diasemrestaurar==3:
            destruiu=False
            diasemrestaurar=0
            while not destruiu:
                for c in range(tamanho):
                    for i in range(len(matriz[c])):
                        if not destruiu and matriz[c][i]=='E':
                            matriz[c][i]='X'
                            destruiu=True

        #PRINTS
        print(f'Dia {dia}')
        for c in range (tamanho):
            print(' '.join(matriz[c])) #matriz

            for i in matriz[c]: #contadores da matriz a cada dia
                if i =='E':
                    quarteiroes_corrompidos+=1
                if i =='X':
                    quarteiroes_destruidos+=1

        print(f'Posição atual do Homem-Aranha: ({linha_h}, {coluna_h})')
        print(f'Quarteirões restaurados: {quarteiroes_restaurados} | Quarteirões destruídos: {quarteiroes_destruidos}')
        print(mensagemespecial)
        print()

        if quarteiroes_corrompidos==0:
            jogoacabou=True
            print('Missão cumprida! Nova York está segura e o Miranha faz tudo novamente!')

        if dia==7 and quarteiroes_corrompidos>0:
            jogoacabou=True
            print('O Miranha não conseguiu restaurar a cidade a tempo, o Electro venceu!')
