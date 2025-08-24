ascii_chars = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
    '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
    '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
]

def descriptografar(nome_criptografado, ascii_chars):

    #divide as metades
    if len(nome_criptografado)%2==0: #par
        indice=int(len(nome_criptografado)/2)
        primeira_metade=list(nome_criptografado[:indice])
        segunda_metade=list(nome_criptografado[indice:])
    else: #impar
        indice=len(nome_criptografado)//2
        primeira_metade=list(nome_criptografado[:indice])
        segunda_metade=list(nome_criptografado[indice:])

    #desloacmento de -1 na segunda metade
    for i in range(len(segunda_metade)):
        n = ascii_chars.index(segunda_metade[i])

        if ascii_chars[n]==ascii_chars[-1]: #se é o ultimo elemento, volta ro inicio
            segunda_metade[i]=ascii_chars[0]
        else:
            segunda_metade[i]=ascii_chars[n+1]

    nome_criptografado=primeira_metade+segunda_metade #concatena
    #inversão
    nome_criptografado.reverse()

    #deslocamento de +3 em tudo
    for i in range (len(nome_criptografado)):
        n = ascii_chars.index(nome_criptografado[i])

        if ascii_chars[n]==ascii_chars[2]:
            nome_criptografado[i]=ascii_chars[-1]
        elif ascii_chars[n]==ascii_chars[1]:
            nome_criptografado[i]=ascii_chars[-2]
        elif ascii_chars[n]==ascii_chars[0]:
            nome_criptografado[i]=ascii_chars[-3]
        else:
            nome_criptografado[i]=ascii_chars[n-3]

    #junção em string
    nome=''.join(nome_criptografado)

    return nome


qtd_nomes=int(input())
dicionario={'nomes_criptografados':[],
            'nomes_descriptografados':[]}

for i in range (qtd_nomes):
    nome_criptografado=input()
    nome_descriptografado=descriptografar(nome_criptografado, ascii_chars)

    print(f'''Criptografada: {nome_criptografado}
Descriptografada: {nome_descriptografado}
--------------------------------------------------''')

    dicionario['nomes_criptografados'].append(nome_criptografado)
    dicionario['nomes_descriptografados'].append(nome_descriptografado)

for nome in dicionario['nomes_descriptografados']:
    if nome=='Ronaldo':
        print('Ronaldo Fenômeno detectado! Autor dos gols na final!')
    elif nome=='Ronaldinho':
        print('Ronaldinho Gaúcho chegou! Chamem o inglês que ele vai chutar do meio-campo...')
    elif nome=='Cafu':
        print('Capitão Cafu presente! O único a jogar 3 finais de Copa seguidas!')
    elif nome=='Marcos':
        print('Marcos está na área! O paredão do Brasil em 2002!')
    elif nome=='Luiz Felipe Scolari':
        print('Técnico reconhecido: Luiz Felipe Scolari — o comandante do penta!')
    else:
        print(f'{nome} está confirmado na escalação!')

print()

tem_tecnico=False

if 'Luiz Felipe Scolari' in dicionario['nomes_descriptografados']:
    qtd_jogadores=qtd_nomes-1
    tem_tecnico=True
    dicionario['nomes_descriptografados'].remove('Luiz Felipe Scolari')
else:
    qtd_jogadores=qtd_nomes

if qtd_jogadores<11:
    print('!!!!!!!!!! Escalação incompleta! !!!!!!!!!!')
    print(f'Só foram encontrados {qtd_jogadores} jogadores. Faltam jogadores para completar o time.')
    
elif qtd_jogadores>=11:
    print('++++++++++ Escalação Confirmada ++++++++++')
    print('Escalação Oficial da Seleção Brasileira — Copa do Mundo 2002')
    print('==================================================')
    for c in range(qtd_jogadores):
        print(f'->{dicionario["nomes_descriptografados"][c]}')
    print('==================================================')

if tem_tecnico:
    print('========== Técnico ==========')
    print('Luiz Felipe Scolari (Felipão)')
    if qtd_jogadores>=11:
        print('===== Tudo pronto! Rumo ao Penta! =====')
        print('Escalação completa com técnico confirmado.')
        print('Que comece o espetáculo, Brasil rumo ao penta!')
else:
    print('!!!!!!!!!! Técnico não encontrado! !!!!!!!!!!')
    print('Como vamos jogar sem treinar? Como vamos ganhar o penta?')

