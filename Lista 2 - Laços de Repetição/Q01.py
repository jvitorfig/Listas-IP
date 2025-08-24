ataque = defesa = 0
erro = False
print('------- Início do Treino -------')

qtd_bolas = int(input(''))

for c in range(0, qtd_bolas):
    bola_lancada = str(input(''))
    golpe_executado = str(input(''))

    if golpe_executado == 'Errou':
        erro = True
        if bola_lancada == 'Ataque':
            ataque -= 10
        if bola_lancada == 'Defesa':
            defesa -= 10
        print('Você errou! Levanta a cabeça que ainda tem mais.')

    if bola_lancada == 'Defesa' and golpe_executado != 'Errou':
        if golpe_executado == 'Push':
            defesa += 5
        if golpe_executado == 'Chop':
            defesa += 10
        print(
            f'Você conseguiu rebater uma bola de {bola_lancada}! Golpe executado: {golpe_executado}.')
    if bola_lancada == 'Ataque' and golpe_executado != 'Errou':
        if golpe_executado == 'Topspin':
            ataque += 5
        if golpe_executado == 'Smash':
            ataque += 10
        print(
            f'Você conseguiu rebater uma bola de {bola_lancada}! Golpe executado: {golpe_executado}.')

if ataque < 0:
    ataque = 0
if defesa < 0:
    defesa = 0

if ataque > defesa:
    print('Ter um bom jogo ofensivo será fundamental para ganhar o InterCin!')
elif defesa > ataque:
    print('Defesa ganha campeonatos! Agora sim estou preparado.')
elif defesa == ataque:
    print('Foi um treino equilibrado.')

if erro == True:
    print('Infelizmente não foi um treino perfeito, mas pude melhorar muito.')

print(f'''------- Atributos -------
Ataque: {ataque}
Defesa: {defesa}''')
