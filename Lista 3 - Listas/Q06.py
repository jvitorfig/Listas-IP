n=int(input())
vitoriasherois=0
vitoriasviloes=0
maiordiferenca=0
indicemaiordiferenca=0
ondamenosacirrada=[]
vencedor='' #vencedor da onda menos acirrada

for c in range (1, n+1):
    num_herois=0
    num_viloes=0
    personagens=input()

    lista=personagens.split(', ')
    listaoriginal=lista.copy()
    lista.remove(lista[0])
    lista.remove(lista[-1])

    for i in lista:
        if i[0]=='H':
            num_herois+=1
        elif i[0]=='V':
            num_viloes+=1
    diferenca=num_herois-num_viloes


    if abs(diferenca)>abs(maiordiferenca):
        maiordiferenca=diferenca
        indicemaiordiferenca=c
        ondamenosacirrada=listaoriginal
        if diferenca>0:
            vencedor='heróis'
        elif diferenca<0:
            vencedor='vilões'
            
    if diferenca>0:
        vitoriasherois+=1
    elif diferenca<0:
        vitoriasviloes+=1

#PRINTS
if maiordiferenca != 0:
    print(f'🌀Onda {indicemaiordiferenca} foi a menos acirrada e a mais favorável para os {vencedor}!')
    participantesmaior=', '.join(ondamenosacirrada)
    print(f'Participantes analisados: {participantesmaior}')
elif maiordiferenca==0:
    print('🌀Nenhuma onda foi selecionada como a menos acirrada e a mais favorável para nenhum do dois lados!')

print('Agora vamos ao resultado geral das ondas...')
print(f'Heróis: {vitoriasherois} | Vilões: {vitoriasviloes}')
if vitoriasherois>vitoriasviloes:
    print('Ufa, os heróis dominaram! Central City está seguro outra vez')
elif vitoriasviloes>vitoriasherois:
    print('Ah, não. Os vilões vão dominar Central City e mandar todos os heróis embora!')
else:
    print('Ninguém é mais forte que ninguém. Heróis e vilões vão ter que entrar em consenso para viverem no mesmo espaço')
