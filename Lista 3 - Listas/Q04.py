entrada=input()
robos=entrada.split('-')
n=int(len(robos))
nomeszords=[]
nivelzords=[]
megazord=True

for c in range (n): #separando em 2 listas
    if c % 2==0:
        nomeszords.append(robos[c])
    elif c %2==1:
        nivelzords.append(int(robos[c]))

for i in range(1,len(nivelzords)): #algoritmo pra ordenar em ordem decrescente
    nivel=nivelzords[i]
    nome=nomeszords[i]
    j=i-1

    while j>=0 and nivelzords[j]<nivel:
        nivelzords[j+1]=nivelzords[j]
        nomeszords[j+1]=nomeszords[j]
        j-=1

    nivelzords[j+1]=nivel
    nomeszords[j+1]=nome

#separando em tipos
zordstipo1=[]
zordstipo2=[]
zordstipo3=[]

if 'robocin' in robos:
    print('Go! Go! Power Rangers!')
    print('Os rangers encontraram o zord lendário!!!! O Robocin!!!! Eles não precisam mais de outros zords!')
else:
    print('Go! Go! Power Rangers!')
    for i in range (len(nomeszords)):
        zord=nomeszords[i]
        numzord=int(nivelzords[i])
        if numzord<=10:
            zordstipo3.append(zord)
        elif numzord<=30:
            zordstipo2.append(zord)
        elif numzord>30:
            zordstipo1.append(zord)

#PRINTS
    if zordstipo1!=[]:
        if len(zordstipo1)>=2:
            print(f'Zord do Ranger Vermelho: {zordstipo1[0]}')
            print(f'Zord do Ranger Verde: {zordstipo1[1]}')
        elif len(zordstipo1)==1:
            print(f'Zord do Ranger Vermelho: {zordstipo1[0]}')
            print(f'Ranger Verde ficou sem zord!')
            megazord=False
    else:
        print('Ranger Vermelho ficou sem zord!\nRanger Verde ficou sem zord!')
        megazord=False

    if zordstipo2!=[]:
        if len(zordstipo2)>=2:
            print(f'Zord da Ranger Rosa: {zordstipo2[0]}')
            print(f'Zord do Ranger Preto: {zordstipo2[1]}')
        elif len(zordstipo2)==1:
            print(f'Zord da Ranger Rosa: {zordstipo2[0]}')
            print(f'Ranger Preto ficou sem zord!')
            megazord=False
    else:
        print('Ranger Rosa ficou sem zord!\nRanger Preto ficou sem zord!')
        megazord=False

    if zordstipo3!=[]:
        if len(zordstipo3)>=2:
            print(f'Zord do Ranger Azul: {zordstipo3[0]}')
            print(f'Zord da Ranger Amarela: {zordstipo3[1]}')
        elif len(zordstipo3)==1:
            print(f'Zord do Ranger Azul: {zordstipo3[0]}')
            print(f'Ranger Amarela ficou sem zord!')
            megazord=False
    else:
        print('Ranger Azul ficou sem zord!\nRanger Amarela ficou sem zord!')
        megazord=False



    if zordstipo1!=[]:
        zords1=', '.join(zordstipo1)
        print(f'Zords do tipo 1: {zords1}')
    else:
        print('Não temos nenhum zord do tipo 1 :(')

    if zordstipo2!=[]:
        zords2=', '.join(zordstipo2)
        print(f'Zords do tipo 2: {zords2}')
    else:
        print('Não temos nenhum zord do tipo 2 :(')

    if zordstipo3!=[]:
        zords3=', '.join(zordstipo3)
        print(f'Zords do tipo 3: {zords3}')
    else:
        print('Não temos nenhum zord do tipo 3 :(')



    if megazord==True:
        print('Os Rangers estão prontos para montar o Megazord e derrotar Rita!')
    else:
        print('Ai ai ai, essa não!! Não temos zords suficientes para formar o Megazord! Os ranger não vão conseguir derrotar Rita!')