entrada=''
uniforme=0
isotonico=0
raquete=0
toalha=0
sabotagem=0

while entrada != 'FIM':
    entrada=str(input(''))

    if entrada=='Uniforme':
        uniforme+=1
        print(f'Tava faltando camisa! Agora temos {uniforme} uniforme(s)')
    if entrada=='Isotônico':
        isotonico+=1
        print(f'Bora garantir a hidratação! Agora temos {isotonico} isotônico(s)')
    if entrada=='Raquete':
        raquete+=1
        print(f'Mais uma raquete saindo! Agora temos {raquete} raquete(s)')
    if entrada=='Toalha':
        toalha+=1
        print(f'Mais uma toalha saindo! Agora temos {toalha} toalha(s)')

    if entrada=='Sabotagem':
        material=str(input(''))
        if material=='Uniforme' and uniforme>0:
            uniforme-=1
            sabotagem+=1
            print('O sueco está roubando as camisas de Hugo!')
        if material=='Isotônico' and isotonico>0:
            isotonico-=1
            sabotagem += 1
            print('O sueco está sabotando a hidratação de Hugo!')
        if material=='Raquete' and raquete>0:
            raquete-=1
            sabotagem += 1
            print('O sueco está roubando as raquetes de Hugo!')
        if material=='Toalha' and toalha>0:
            toalha-=1
            sabotagem += 1
            print('O sueco está roubando as toalhas de Hugo!')

else:
    print(f'''Bora ver o relatório final dos materiais!
Uniforme: {uniforme} unidade(s).
Isotônico: {isotonico} unidade(s).
Raquete: {raquete} unidade(s).
Toalha: {toalha} unidade(s).''')
    if uniforme+isotonico+raquete+toalha==0 and sabotagem>0:
        print('Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!')
    elif uniforme+isotonico+raquete+toalha==0 and sabotagem==0:
        print('Vish... Parece que vão faltar materiais para garantir a vitória do nosso atleta.')
    elif uniforme==0 or isotonico==0 or raquete==0 or toalha==0:
        print('Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!')
    else:
        print('Tudo pronto! Não vai faltar nada para mais um título de Hugo Calderano!')
        