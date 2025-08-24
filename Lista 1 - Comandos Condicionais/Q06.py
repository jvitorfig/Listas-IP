nome1=str(input(''))
qi1=str(input(''))

if qi1=='felino espião':
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')

if 'cin' in nome1 and qi1 != 'felino espião':
    print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')

nome2=str(input(''))
qi2=str(input(''))

if qi2=='felino espião':
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')

if 'cin' in nome2 and qi2 != 'felino espião':
    print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')

nome3=str(input(''))
qi3=str(input(''))

if qi3=='felino espião':
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')

if 'cin' in nome3 and qi3 != 'felino espião':
    print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')

pontos1=len(nome1)
pontos2=len(nome2)
pontos3=len(nome3)

if 'cin' in nome1:
    pontos1+=10
if 'cin' in nome2:
    pontos2+=10
if 'cin' in nome3:
    pontos3+=10


if 'gato' in nome1 or qi1=='felino espião':
    pontos1=0
if 'gato' in nome2 or qi2=='felino espião':
    pontos2=0
if 'gato' in nome3 or qi3=='felino espião':
    pontos3=0

primeiro=0
segundo=0
terceiro=0

if pontos1>pontos2>pontos3:
    primeiro=nome1
    segundo=nome2
    terceiro=nome3

if pontos1>pontos3>pontos2:
    primeiro=nome1
    segundo=nome3
    terceiro=nome2

if pontos2>pontos1>pontos3:
    primeiro = nome2
    segundo = nome1
    terceiro = nome3

if pontos2>pontos3>pontos1:
    primeiro=nome2
    segundo=nome3
    terceiro=nome1

if pontos3>pontos2>pontos1:
    primeiro=nome3
    segundo=nome2
    terceiro=nome1

if pontos3>pontos1>pontos2:
    primeiro=nome3
    segundo=nome1
    terceiro=nome2

print(f'''RANKING DOS NOMES:
Primeiro lugar: {primeiro}
Segundo lugar: {segundo}
Terceiro lugar: {terceiro}''')
