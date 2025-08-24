f_max=int(input(''))
f_inicial=int(input(''))
nivel=str(input(''))
f_mediajogador=int(input(''))
incremento=0
tempo=0
contador=0
f_acumulada=0
f_rebatida = f_inicial + (tempo*incremento)

print('Robô Hugo 4.0 foi inicializado…')
if nivel=='facil':
    incremento=1
    print('Iniciando no modo iniciante... Ótimo para aquecer os motores!')
elif nivel=='medio':
    incremento=3
    print('Você escolheu o modo intermediário. Hora de mostrar técnica e estratégia!')
elif nivel=='dificil':
    incremento=5
    print('Modo lendário ativado! Hugo 4.0 está a todo vapor — prepare-se para o combate definitivo!')

while f_acumulada<=f_max and f_rebatida<=150:
    tempo+=1
    contador+=1
    f_rebatida=f_inicial + (tempo*incremento)
    if f_rebatida>150:
      print('Bola fora! A força da rebatida excedeu os limites da mesa.')
      
    else:
      f_acumulada=f_acumulada+f_rebatida
      print(f'Rebatida {contador}: força = {f_rebatida}, força acumulada = {f_acumulada}')

else:
    if f_acumulada>f_max:
        print('Energia do robô esgotada! Encerrando o confronto…')

f_mediarobo=f_acumulada//tempo

print('Partida finalizada! Estas são as estatísticas do embate:')
print(f'''O robô realizou {contador} rebatidas em {tempo} segundos, com força total de {f_acumulada}.
Força média do robô: {f_mediarobo}
Força média do jogador: {f_mediajogador}''')

if f_mediarobo>f_mediajogador:
    print('Vitória do Hugo 4.0! O robô mostrou quem manda na quadra!')
elif f_mediarobo<f_mediajogador:
    print('Vitória do jogador! O talento humano ainda é imbatível!')
elif f_mediarobo==f_mediajogador:
    print('Empate técnico! Um duelo digno de mestres do tênis de mesa.')
