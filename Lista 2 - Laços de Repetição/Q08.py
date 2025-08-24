nacionalidade_atleta = str(input(''))
nome_atleta = str(input(''))
print('A partida de revanche de Hugo Calderano contra a China, Potência Mundial do Tênis de Mesa, está prestes a começar!')

numero_hugo = 0
numero_adversario = 0
pontos_hugo = 0
pontos_adversario = 0
pontoextra = False

while nacionalidade_atleta != 'Chinês':
    print(f'O {nome_atleta} não poderá disputar a partida, pois sua nacionalidade não é chinesa!')
    nacionalidade_atleta = str(input(''))
    nome_atleta = str(input(''))

else:
    print(f'{nome_atleta} foi convocado para vingar o massacre feito durante o mundial de Tênis de Mesa!')


while abs(pontos_hugo-pontos_adversario) < 3:
    numero_adversario = int(input(''))
    numero_hugo = int(input(''))

    if numero_adversario >= (2*numero_hugo):
        pontos_adversario += 2
        pontoextra = True
    if numero_hugo >= (2*numero_adversario):
        pontos_hugo += 2
        pontoextra = True
    if pontoextra == True:
        print('Que bela jogada, essa merece ponto extra!')

    elif numero_adversario > numero_hugo:
        pontos_adversario += 1
        print('Vamos Hugo, não deixe ele vencer!')

    elif numero_hugo > numero_adversario:
        pontos_hugo += 1
        print('Hugo Calderano marcou um ponto de maneira esplendida!')

    elif numero_hugo == numero_adversario:
        pontos_hugo += 1
        print('A bola bateu na rede e felizmente caiu no lado adversário!!! Hugo marca mais um ponto!')

    pontoextra = False

if pontos_hugo == 3:
    print('Hugo Calderano mostrou o porquê ele é o atual campeão mundial, uma partida relâmpago!')
elif 3 < pontos_hugo <= 10:
    print('Não demorou muito, mas o resultado era esperado, Hugo Calderano vence!')
elif pontos_hugo > 10:
    print('Demorou, mas o previsto aconteceu! Hugo Calderano não deixa dúvidas do porquê ele é o Campeão Mundial!')

print(f'Placar Final: {pontos_hugo}x{pontos_adversario}')
print('')
print('Aqui está o merecido prêmio de Hugo Calderano:')

largura = pontos_hugo
comprimento = pontos_adversario
if comprimento % 2 == 0:
    comprimento -= 1

superficiemesa = '|'+' '*(largura-2)+'|'
rededamesa = '|'+'#'*(largura-2) + '|'

print('-'*largura)
for c in range(1, ((comprimento-2)//2)+1):
    print(superficiemesa)
print(rededamesa)
for c in range(((comprimento//2))+1, comprimento-1):
    print(superficiemesa)
print('-'*largura)
