locaisparis=['Torre Eiffel', 'Museu do Louvre', 'Catacumbas de Paris', 'Biblioteca Nacional', 'Galeria Lafayette', 'Parque dos Príncipes', 'Catedral de Notre-Dame', 'Jardim de Luxemburgo', 'Padaria Dupain Cheng']
horarios=['09:00 23:00', '08:00 18:00', '10:00 20:00', '07:00 22:00', '10:00 21:00', '06:00 23:00', '08:00 18:30', '07:00 19:00', '04:00 20:00']

local_nao_existe=False
locais_qn_existem=[] #lista de locais que nao existem
nomes_mentiu_locais=[] #lista de mentirosos sobre os locais

hora_errada=False
horarios_errados=[]
local_horario_errado=[]
nomes_mentiu_horario=[]

seguranca_baixa=False
nomes_seguranca_baixa=[]

sem_testemunha=False
nomes_sem_testemunha=[]

for c in range (1,7):
    lista=[]
    suspeito=input()
    lista=suspeito.split(' - ')
    nome_suspeito=lista[0]
    horario_suspeito=lista[1]
    local_suspeito=lista[2]
    testemunha_suspeito=lista[3]

    if local_suspeito not in locaisparis: #verifica o local
        local_nao_existe=True
        locais_qn_existem.append(local_suspeito)
        nomes_mentiu_locais.append(nome_suspeito)



    else: #local existe, verifica os horários
        for c in range (len(locaisparis)):
            if locaisparis[c]==local_suspeito:
                horario_abre=horarios[c][0:5] #horario que ele vai verificar
                horario_fecha=horarios[c][6:11]

        if int(horario_suspeito[0:2])<int(horario_abre[0:2]) or int(horario_suspeito[0:2])>int(horario_fecha[0:2]) or (int(horario_suspeito[0:2])==int(horario_fecha[0:2]) and int(horario_suspeito[3:5])>int(horario_fecha[3:5])):
            hora_errada=True
            horarios_errados.append(horario_suspeito)
            nomes_mentiu_horario.append(nome_suspeito)
            if local_suspeito not in local_horario_errado:
                local_horario_errado.append(local_suspeito)



        else: #local existe e horário bate, verifica a segurança
            if local_suspeito=='Catacumbas de Paris' or local_suspeito=='Parque dos Príncipes' or local_suspeito=='Padaria Dupain Cheng':
                seguranca_baixa=True
                nomes_seguranca_baixa.append(nome_suspeito)



            else: #verifica as testemunhas
                if testemunha_suspeito=='nenhuma':
                    sem_testemunha=True
                    nomes_sem_testemunha.append(nome_suspeito)

#ordem alfabetica:
locais_qn_existem.sort()
nomes_mentiu_locais.sort()
local_horario_errado.sort()
nomes_mentiu_horario.sort()
nomes_seguranca_baixa.sort()
nomes_sem_testemunha.sort()

if local_nao_existe==True:
    if len(nomes_mentiu_locais)==1:
        print(f'Esse lugar {locais_qn_existem[0]} nem existe! {nomes_mentiu_locais[0]} com certeza foi akumatizado!')
    elif len(nomes_mentiu_locais)>1:
        print(f'{", ".join(locais_qn_existem)} nem existem! {", ".join(nomes_mentiu_locais)} estão mentindo!')

elif hora_errada==True:
    if len(horarios_errados)==1:
        print(f'{local_horario_errado[0]} nem estava aberto às {horarios_errados[0]}! {nomes_mentiu_horario[0]} recebeu memórias falsas!')
    elif len(nomes_mentiu_horario)>1:
        print(f'{", ".join(local_horario_errado)} estavam fechados nesse horário! {", ".join(nomes_mentiu_horario)} podem ter sido manipulados pelo Hawk Moth!')

elif seguranca_baixa==True:
    if len(nomes_seguranca_baixa)==1:
        print(f'{nomes_seguranca_baixa[0]} estava em um local de segurança baixa... Ele pode ter mentido!')
    elif len(nomes_seguranca_baixa)>=1:
        print(f'{", ".join(nomes_seguranca_baixa)} estavam em locais de segurança baixa... Eles podem estar forjando um álibi!')

elif sem_testemunha==True:
    if len(nomes_sem_testemunha)==1:
        print(f'{nomes_sem_testemunha[0]} não teve testemunha para confirmar o álibi. É o mais suspeito até agora.')
    elif len(nomes_sem_testemunha)<6:
        print(f'{", ".join(nomes_sem_testemunha)} não foram confirmados por ninguém. O Hawk Moth pode vir atrás deles de novo')
    elif len(nomes_sem_testemunha)==6:
        print('Ninguém viu ninguém… estranho!!')

else:
    print('Poxa vida, todos os àlibis parecem válidos… mas algo continua errado')
