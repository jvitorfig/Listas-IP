qtd_pessoas=int(input(''))
classica=0
caneta=0
classineta=0

for c in range (0,qtd_pessoas):
    voto=str(input(''))
    if voto=='Clássica':
        classica+=1
    if voto=='Caneta':
        caneta+=1
    if voto=='Classineta':
        classineta+=1

print('Estamos calculando... tão rápido quanto dar Run no Dikastis...')

votos1=0
votos2=0
votos3=0

if classica>caneta>classineta:
    primeiro='Clássica'
    votos1=classica
    segundo='Caneta'
    votos2=caneta
    terceiro='Classineta'
    votos3=classineta

elif classica>classineta>caneta:
    primeiro='Clássica'
    votos1=classica
    segundo='Classineta'
    votos2=classineta
    terceiro='Caneta'
    votos3=caneta

elif classineta>classica>caneta:
    primeiro='Classineta'
    votos1=classineta
    segundo='Clássica'
    votos2=classica
    terceiro='Caneta'
    votos3=caneta

elif classineta>caneta>classica:
    primeiro='Classineta'
    votos1=classineta
    segundo='Caneta'
    votos2=caneta
    terceiro='Clássica'
    votos3=classica

elif caneta>classica>classineta:
    primeiro='Caneta'
    votos1=caneta
    segundo='Clássica'
    votos2=classica
    terceiro='Classineta'
    votos3=classineta

elif caneta>classineta>classica:
    primeiro='Caneta'
    votos1=caneta
    segundo='Classineta'
    votos2=classineta
    terceiro='Clássica'
    votos3=classica

print(f'''1º lugar: {primeiro} ({votos1} votos)
2º lugar: {segundo} ({votos2} votos)
3º lugar: {terceiro} ({votos3} votos)''')

if primeiro=='Clássica' and votos1-votos2>=5:
    print('Podemos ver que a influência do grande Hugo Calderano foi disseminada pelos corredores do CIn!')
