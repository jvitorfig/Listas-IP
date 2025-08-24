niveljinwoo=int(input())
qtd=int(input())
exercito=[] #exercito inteiro
exercitonomes=[] #nomes das criaturas, sem repetiçao
morreu=False
contador=0 #quantidade de criaturas enfrentadas

while contador<qtd and not morreu:
    contador+=1
    nome_criatura=input()
    nivel_criatura=int(input())

    if niveljinwoo>nivel_criatura:
        resposta=input()

        if resposta=='Erga-se':

            if nome_criatura in exercito: #se uma criatura de mesmo nome já está no exército
                exercito.append(nome_criatura)
            else:
                exercito.append(nome_criatura)
                exercitonomes.append(nome_criatura)

            niveljinwoo+=(nivel_criatura//3)

    else:
        morreu=True
        print(f'Jin-Woo foi derrotado por {nome_criatura}...')

if not morreu:
    print('Jin-Woo sobreviveu à caçada, um verdadeiro Monarca das Sombras mesmo!')
print('===== Exército das Sombras de Jin-Woo =====')
if exercito==[]:
    print('Jin-Woo não conseguiu formar seu exército...')

else:
    for criatura in exercitonomes:
        qtd_criatura=0
        for i in exercito:
            if criatura==i:
                qtd_criatura+=1
        print(f'{criatura}: {qtd_criatura}')
