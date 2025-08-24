def forca_lutador(lutador): #vai receber uma lista de 2 elementos, o [0] é o nome do lutador e o [1] é a técnica dele
    tecnica=lutador[1]
    forca=len(tecnica)%8
    return forca

def verif_3_lutador(primeirolutador,segundolutador):
    lutadores=[] #nomes dos lutadores
    lutadores.append(primeirolutador[0])
    lutadores.append(segundolutador[0])
    terceirolutador=False
    n=0 #pra verificar se o ajudado será o primeiro ou o segundo lutador

    if 'Goku' in lutadores and 'Jiren' in lutadores:
        terceirolutador=True
        n=lutadores.index('Goku')
    
    elif 'Frieza' in lutadores and 'Jiren' in lutadores:
        terceirolutador=True
        n=lutadores.index('Frieza')

    elif 'Gohan' in lutadores and 'Namekuseijins' in lutadores:
        terceirolutador=True
        n=lutadores.index('Gohan')

    elif 'Androide 17' in lutadores and 'Ribrianne' in lutadores:
        terceirolutador=True
        n=lutadores.index('Androide 17')

    return [terceirolutador, n]

qtd_batalhas=int(input())
print(f'O torneio do poder irá começar com {qtd_batalhas} batalhas no dia de hoje! Vamos ver quais universos vão conseguir se manter vivos até o final do dia!')

for c in range(qtd_batalhas):
    lutadores=[]

    lutador1=input().split(' - ')
    forca1=forca_lutador(lutador1)

    lutador2=input().split(' - ')
    forca2=forca_lutador(lutador2)

    [verificacao, n] =verif_3_lutador(lutador1, lutador2)

    if verificacao:
        lutador3=input().split(' - ')
        print(f'A intensidade dos dois lutadores motivou {lutador3[0]} a entrar na batalha também!')
        forca3=forca_lutador(lutador3)

        if n==0: #se o lutador ajudado for o primeiro
            forca1=forca1+forca3
            if forca1>forca2:
                print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {lutador1[1]}, {lutador2[1]} e {lutador3[1]}! A batalha acaba com {lutador1[0]} e {lutador3[0]} no topo!')
            else:
                print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {lutador1[1]}, {lutador2[1]} e {lutador3[1]}! A batalha acaba com {lutador2[0]} no topo!')

        elif n==1:
            forca2=forca2+forca3
            if forca2>forca1:
                print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {lutador1[1]}, {lutador2[1]} e {lutador3[1]}! A batalha acaba com {lutador2[0]} e {lutador3[0]} no topo!')
            else:
                print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {lutador1[1]}, {lutador2[1]} e {lutador3[1]}! A batalha acaba com {lutador1[0]} no topo!')

    else:
        if forca1>forca2:
            print(f'Incrível! {lutador1[0]} mostrou sua força e defenderá seu universo até o final!')
        else:
            print(f'Incrível! {lutador2[0]} mostrou sua força e defenderá seu universo até o final!')
