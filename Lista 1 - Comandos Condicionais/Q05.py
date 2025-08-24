nome1 = ''
nome2 = ''
nome3 = ''
total1 = 0
total2 = 0
total3 = 0

nome1 = str(input(''))
if nome1 == 'Byte':
    print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')
else:
    nota1_1 = int(input(''))
    nota1_2 = int(input(''))
    nota1_3 = int(input(''))
    total1 = nota1_1 + nota1_2 + nota1_3

    if total1 == 30:
        print(f'Com uma pontuação perfeita, {nome1} conquista o título de mascote do CIn!')
    else:
        nome2 = str(input(''))
        if nome2 == ('Byte'):
            print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')
        else:
            nota2_1 = int(input(''))
            nota2_2 = int(input(''))
            nota2_3 = int(input(''))
            total2 = nota2_1 + nota2_2 + nota2_3

            if total2 == 30:
                print(f'Com uma pontuação perfeita, {nome2} conquista o título de mascote do CIn!')
            else:
                nome3 = str(input(''))
                if nome3 == 'Byte':
                    print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')
                else:
                    nota3_1 = int(input(''))
                    nota3_2 = int(input(''))
                    nota3_3 = int(input(''))
                    total3 = nota3_1 + nota3_2 + nota3_3

                    if total3 == 30:
                        print(f'Com uma pontuação perfeita, {nome3} conquista o título de mascote do CIn!')
                    else:
                        if nota1_1 + nota1_2 + nota1_3 < 15:
                            print(f'Infelizmente {nome1} está fora da disputa')
                        if nota2_1 + nota2_2 + nota2_3 < 15:
                            print(f'Infelizmente {nome2} está fora da disputa')
                        if nota3_1 + nota3_2 + nota3_3 < 15:
                            print(f'Infelizmente {nome3} está fora da disputa')

                        if max(total1, total2, total3) == total1:
                            print(f'Após uma disputa acirrada, o novo mascote do CIn é {nome1}!')
                        if max(total1, total2, total3) == total2:
                            print(f'Após uma disputa acirrada, o novo mascote do CIn é {nome2}!')
                        else:
                            print(f'Após uma disputa acirrada, o novo mascote do CIn é {nome3}!')
