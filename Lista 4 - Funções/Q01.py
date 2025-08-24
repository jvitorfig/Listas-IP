def calcular_distancia(X, Y):
    distancia=(((X)**2+(Y**2))**(1/2))
    return distancia

detectou_esfera=False
n_objetos=int(input())
menordistancia=0
esferaproxima=0


for c in range(1,n_objetos+1):
    nome=input()
    coordenada_x=int(input())
    coordenada_y=int(input())
    dist=calcular_distancia(coordenada_x, coordenada_y)


    if nome=='rocha':
        print("Radar: Rocha detectada! Bulma resmunga: 'Só um pedregulho cósmico... Sem valor para mim!'")
    elif nome=='árvore':
        print("Radar: Árvore à vista! Bulma comenta: 'Interessante, mas não brilha como uma esfera. Próximo alvo!'")
    elif nome=='nave':
        print("Radar: Sinal de nave! Bulma alerta: 'Pode ser Pilaf ou a Patrulha Vermelha! Melhor ficar atenta, mas o foco são as esferas!'")
    elif nome!='esfera':
        print(f"Radar: Detectado um(a) {nome}. Não parece ser uma esfera... Continuando a busca.")
    elif nome=='esfera':
        detectou_esfera=True
        if menordistancia==0:
            menordistancia=dist
            esferaproxima=c
        else:
            if dist<menordistancia:
                menordistancia=dist
                esferaproxima=c


if not detectou_esfera:
    print('Radar varreu a área. Nenhuma esfera do dragão à vista desta vez!')

else:
    print(f'ALVO PRIORITÁRIO: Esfera | Distância: {menordistancia:.2f}m | Detecção Original: {esferaproxima}°')