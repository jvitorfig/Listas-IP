cidade1=str(input(''))
adversario1=str(input(''))
resultado1=str(input(''))
partidasjogadas=1
vitorias=0
derrotas=0
roubo='Não!!!! :D'
cidadesvisitadas=cidade1
adversarios=adversario1

print('Byte, o cachorro mais promissor do futebol nordestino, acaba de calçar suas quatro chuteiras e está pronto para entrar em campo!')

if cidade1=='Catende' or cidade1=='Tabira':
    print('É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.')

if 's' in adversario1 and 'p' in adversario1 and 'o' in adversario1 and 'r' in adversario1 and 't' in adversario1:
    print('Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!')

if resultado1=='VENCEU':
    print('TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!')
    vitorias+=1
if resultado1=='perdeu':
    print('Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...')
    derrotas+=1



if resultado1=='Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
    roubo='sim :('
    vitorias+=1
    print('Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!')
    expressao1=str(input(''))
    a,b,c=expressao1
    a=int(a)
    c=int(c)
    if '+' in expressao1:
        total1=a+c
        print(f'A expressão resolvida é: {total1:.2f}')
    elif '-' in expressao1:
        total1=a-c
        print(f'A expressão resolvida é: {total1:.2f}')
    elif '*' in expressao1:
        total1=a*c
        print(f'A expressão resolvida é: {total1:.2f}')
    elif '/' in expressao1:
        total1=a/c
        print(f'A expressão resolvida é: {total1:.2f}')
    print('Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!')
else:
    cidade2 = str(input(''))
    adversario2 = str(input(''))
    resultado2 = str(input(''))
    partidasjogadas=2
    cidadesvisitadas=cidade1+' e '+cidade2
    adversarios=adversario1+' e '+adversario2

    if cidade2 == 'Catende' or cidade2 == 'Tabira':
        print('É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.')

    if (cidade1== 'Catende' and cidade2=='Tabira') or (cidade1=='Tabira' and cidade2=='Catende'):
        print('Não dá mais! Jogar nessas duas cidades é sinal de que o Santa Cruz precisa mais de magia do que de reforços...')

    if 's' in adversario2 and 'p' in adversario2 and 'o' in adversario2 and 'r' in adversario2 and 't' in adversario2:
        print('Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!')

    if resultado2 == 'VENCEU':
        print('TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!')
        vitorias+=1
    if resultado2 == 'perdeu':
        print('Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...')
        derrotas+=1

    if resultado2 == 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!':
        roubo='sim :('
        vitorias+=1
        print('Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!')
        expressao2 = str(input(''))
        d, e, f = expressao2
        d = int(d)
        f = int(f)
        if '+' in expressao2:
            total2 = d + f
            print(f'A expressão resolvida é: {total2:.2f}')
        elif '-' in expressao2:
            total2 = d - f
            print(f'A expressão resolvida é: {total2:.2f}')
        elif '*' in expressao2:
            total2 = d * f
            print(f'A expressão resolvida é: {total2:.2f}')
        elif '/' in expressao2:
            total2 = d / f
            print(f'A expressão resolvida é: {total2:.2f}')
        print('Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!')

print('')
print('RELATÓRIO DA PRÉ-TEMPORADA DO BYTE:')
print(f'- Partidas jogadas: {partidasjogadas}')
print(f'- Vitórias: {vitorias}')
print(f'- Derrotas: {derrotas}')
print(f'- Tentaram roubar o bixinho: {roubo}')
print(f'- Cidades visitadas: {cidadesvisitadas}')
print(f'- Adversários enfrentados: {adversarios}')
print('')
print('E assim termina a pré-temporada do Byte pelos gramados. Anotar tudo isso na mão dá uma trabalheira! Nas próximas férias o Byte deve esperar saber laços, listas, funções e muito mais pra registrar tudo com mais facilidade :)')
