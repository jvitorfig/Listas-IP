nome=str(input())
acertos1=int(input())
acertos2=int(input())
acertos3=int(input())
acertos4=int(input())*5/3
acertos5=int(input())*5/3
acertos6=int(input())*5/3

media=round((acertos1+acertos2+acertos3+acertos4+acertos5+acertos6)/6,1)

print(f'A média de {nome} é {media}')

if acertos1<=acertos2<=acertos3<=acertos4<=acertos5<=acertos6:
    print('Progresso constante! Parabéns pelo esforço!')
else:
    print('Alerta! Queda no rendimento.')

naofeitas=0
if acertos1==0:
    naofeitas+=1
if acertos2==0:
    naofeitas+=1
if acertos3==0:
    naofeitas+=1
if acertos4==0:
    naofeitas+=1
if acertos5==0:
    naofeitas+=1
if acertos6==0:
    naofeitas+=1
if naofeitas>=2:
    print('Alerta! Múltiplas listas não respondidas.')

if media>=8:
    print('Parabéns pelo excelente desempenho! Continue "au" sim.')
elif media>=7:
    print('Parabéns pelo bom desempenho!')
else:
    print('Alerta! Desempenho abaixo do esperado.')
