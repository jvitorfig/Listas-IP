fome=str(input('O Byte está com fome?'))
if fome=='sim':
    comida=str(input('\nO que você vai dar para ele comer?'))
    if comida=='carne' or 'ração' or 'petisco':
        print(f'\nByte comeu {comida} e está feliz!')
        print('Depois desse banquete, Byte pode tirar um cochilo feliz')
    else:
        print(f'\nByte não gosta de {comida}')
        print('Byte se irritou e foi dormir pra ver se sonha com suas refeições prediletas...')
elif fome=='não':
    print('\nJá que Byte não está com fome, ele pode passear')
    chovendo=str(input('Está chovendo?'))
    if chovendo=='sim':
        print('\nJá que está chovendo, Byte vai ter que brincar em casa')
    elif chovendo=='não':
        print('\nByte está indo passear')
    else:
        print('\nInsira uma resposta válida')

else:
    print('\nInsira uma resposta válida')
    