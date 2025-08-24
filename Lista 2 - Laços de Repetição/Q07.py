print('🎾🏆 Bem-vindo ao Torneio Fatorial Ping Pong Championship! 🧮🏓\nHoje, o jovem Lavoi enfrentará seu maior desafio: CÁLCULOS!')
print('')
print('Qual será o número que marcará o INÍCIO dessa tabuada fatorial?')

num_inicio = int(input(''))

while num_inicio < 0:
    print(f'O número {num_inicio} é inválido! O INÍCIO NÃO pode ser NEGATIVO.')
    num_inicio = int(input(''))
else:
    print(f'O número {num_inicio} é ótimo como número inicial!')
    print('')

print('Qual será o número que marcará o FIM dessa tabuada fatorial?')
num_final = int(input(''))
while num_final < num_inicio:
    print(
        f'O número {num_final} é inválido! O FIM NÃO pode ser MENOR que o número inicial {num_inicio}.')
    num_final = int(input(''))
else:
    print(f'O número {num_final} é ótimo como número final!')
    print()

print('Qual será o número cujo FATORIAL será calculado?')
num_sagrado = int(input(''))
while num_sagrado < 0:
    print(
        f'O número {num_sagrado} é inválido! Números válidos são maiores ou iguais a zero.')
    num_sagrado = int(input(''))
else:
    print(f'O número {num_sagrado} é ótimo para o cálculo do fatorial!')
    print('')

for c in range(num_inicio, num_final+1):
    contador = 1
    fatorial = 1
    while contador <= num_sagrado*num_inicio:
        fatorial *= contador
        contador += 1
    print(f'({num_inicio} * {num_sagrado})! = {fatorial}')
    num_inicio += 1

print()
print('🏁 Jornada Finalizada! Lavoi completou todos os estágios do desafio!\n🏓 Que sua energia vital continue brilhando nas próximas batalhas!')
