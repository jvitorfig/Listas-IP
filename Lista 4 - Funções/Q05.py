def calcular_expressao_prefixa(expressao):
    expressao = expressao.split(' ')
    operadores = []
    lista_operadores_possiveis = ['+', '-', '*', '/']
    pilha_numeros = [] #separa em operadores e em numeros

    for c in range(len(expressao)-1, -1, -1): #percorre de trás pra frente

        if expressao[c] in lista_operadores_possiveis:
            operador = expressao.pop(c)
            operadores.append(operador) #guarda os operadores na ordem normal

        else:
            num = expressao.pop(c)
            pilha_numeros.insert(0, num) #guarda os numeros na ordem contrária

    for c in range(len(operadores)):
        if c == 0:
            operando1 = int(pilha_numeros[0])
            operando2 = int(pilha_numeros[1])
            operador = operadores[0]

        else:
            operando1 = int(resultado_operacao)
            operando2 = int(pilha_numeros[c+1])
            operador = operadores[c]

        c += 1

        if operador == '+':
            resultado_operacao = operando1+operando2
        elif operador == '-':
            resultado_operacao = operando1-operando2
        elif operador == '*':
            resultado_operacao = operando1*operando2
        elif operador == '/':
            resultado_operacao = operando1//operando2

    return resultado_operacao


def verif_primo(num):
    primo = False
    lista_divisores = []

    if num<=1:
        primo=False
    
    else:
        for c in range(1, num+1):
            teste = num/c
            if int(teste) == teste:
                lista_divisores.append(c)

        if len(lista_divisores) == 2:
            primo = True

    return primo


def conversao_binario_p_decimal(num):
    num_decimal=0
    cont=len(num)-1

    for c in num:
        if c == '1':
            num_decimal+=2**cont
        cont-=1

    return num_decimal


def processar_coordenada(n):
    cadeia_binaria=''
    entrada='string temporária'

    while entrada != '': #recebe varias entradas ate chegar no input vazio
        entrada=input()

        if entrada !='':

            resultado=calcular_expressao_prefixa(entrada)

            primo=verif_primo(resultado)

            if primo:
                cadeia_binaria+='1'
            else:
                cadeia_binaria+='0' #forma as cadeias binarias pelos bits recebidos

    valor_decimal=conversao_binario_p_decimal(cadeia_binaria)

    coordenada=valor_decimal%n

    return coordenada, cadeia_binaria


def calcular_distancia(esfera, goku_x, goku_y):
    esfera_x=esfera[0]
    esfera_y=esfera[1]

    distancia=(((esfera_x-goku_x)**2)+((esfera_y-goku_y)**2))**(1/2)

    return distancia


def ordenar_esferas(esferas, goku_x, goku_y):

    trajetoria=[f'({goku_x}, {goku_y})'] #onde vai ser formada a trajetória do goku
    x_atual=goku_x
    y_atual=goku_y

    while len(esferas)>0:
        esfera_mais_proxima=esferas[0]
        indice_esfera_mais_proxima=0
        menor_distancia = calcular_distancia(esferas[0], x_atual, y_atual)

        for i in range (1, len(esferas)): #compara com as distâncias das esferas restantes
            esfera_comparativa=esferas[i]
            distancia_comparativa=calcular_distancia(esfera_comparativa, x_atual, y_atual)

            if menor_distancia > distancia_comparativa: #se for menor, substitui
                menor_distancia= distancia_comparativa
                esfera_mais_proxima=esfera_comparativa
                indice_esfera_mais_proxima = i

        x_atual = esfera_mais_proxima[0]
        y_atual = esfera_mais_proxima[1]

        trajetoria.append(f'({x_atual}, {y_atual})')
        esferas.pop(indice_esfera_mais_proxima) #remove a mais próxima

    return trajetoria


print('🟠 Vamos conquistar as esferas do dragão! 🟠')
print('--------------------------------------------------------------------------')
print('')

fim=False #fim da decodificaçao
matriz=[]
n=int(input())


for c in range (n):
    linha=[]
    for c in range (n):
        linha.append('.')
    matriz.append(linha) #forma a matriz já com os pontos


coordenadas_goku=input()
coordenadas_goku=coordenadas_goku[1:len(coordenadas_goku)-1].split(', ') #tira os parenteses e transforma em lista
goku_x=int(coordenadas_goku[0])
goku_y=int(coordenadas_goku[1])


input() #pra linha vazia
divisao=input()
esferas=[] #lista com as coordenadas das esferas
numero_esfera=0 #contagem de esferas


while not fim:
    numero_esfera+=1
    esfera_atual=[] #lista pras 2 coordenadas da esfera atual


    coordenada_x, cadeia_binaria =processar_coordenada(n)
    print(f'Coordenada x da {numero_esfera}ª esfera do dragão obtida pelo código binário {cadeia_binaria}: {coordenada_x}')
    esfera_atual.append(coordenada_x)


    coordenada_y, cadeia_binaria=processar_coordenada(n)
    print(f'Coordenada y da {numero_esfera}ª esfera do dragão obtida pelo código binário {cadeia_binaria}: {coordenada_y}')
    esfera_atual.append(coordenada_y)

    esferas.append(esfera_atual)


    print(f'As coordenadas da {numero_esfera}ª esfera do dragão são: ({coordenada_x}, {coordenada_y})')
    print('')

    divisao=input() #recebe string vazia ou todos os bits foram decodificados
    if divisao=='Todos os bits foram decodificados':
        print('--------------------------------------------------------------------------')
        print('')
        fim=True

for c in range (0, n):

    for i in esferas: #percorre a lista de esferas
        esfera_x=i[0]
        esfera_y=i[1]
        if esfera_x==c:
            matriz[c][esfera_y]='☆'

    if goku_x==c:
        matriz[c][goku_y]='G'

    print(" ".join(matriz[c])) #print das linhas da matriz

print('')


trajetoria = ordenar_esferas(esferas, goku_x, goku_y)
 
print(f'Trajetória completa de Goku: {" -> ".join(trajetoria)}')

print('Missão cumprida! Conseguimos todas as esferas do dragão!🟠🐉')