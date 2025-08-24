humor=str(input(''))
qtdsenta=int(input(''))
qtdpatinha=int(input(''))
qtdfica=int(input(''))
qtdpega=int(input(''))
proximo=str(input(''))

if proximo=='Senta':
    qtdsenta = qtdsenta + 1
if proximo=='Dá a patinha':
    qtdpatinha = qtdpatinha + 1
if proximo=='Fica':
    qtdfica=qtdfica+1
if proximo=='Pega':
    qtdpega=qtdpega+1


if proximo=='Senta' and humor !='Brincalhão' and qtdsenta>2:
    print('Byte é o melhor')
elif proximo=='Senta' and humor=='Brincalhão':
    print('Ele parece estar muito animado para isso!')

elif proximo=='Dá a patinha' and qtdpatinha>2:
    print('Ele é um bom garoto!')

elif proximo=='Fica' and humor !='Brincalhão' and qtdfica>2:
    print('Ele está aprendendo')
elif proximo=='Fica' and humor=='Brincalhão':
    print('Ele não consegue ficar parado')

elif proximo=='Pega' and humor!='Preguiçoso' and qtdpega>2:
    print('Ele é muito ágil!')
elif proximo=='Pega' and humor=='Preguiçoso':
    print('Quem não tem seu momento de preguiça?')

else:
    print('Parece que ele não aprendeu esse truque ainda')

if qtdsenta>2 or qtdpatinha>2 or qtdfica>2 or qtdpega>2:
    print(f'O nosso novo mascote estava {humor} e aprendeu o(s) seguinte(s) truque(s):')




if qtdsenta>2:
    print('Senta')
if qtdpatinha>2:
    print('Dá a patinha')
if qtdfica>2:
    print('Fica')
if qtdpega>2:
    print('Pega')
