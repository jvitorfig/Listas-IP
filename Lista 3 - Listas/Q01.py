entrada=''
listadecompras=[]

while entrada!='E por hoje é só, pessoal!':
    entrada=input()
    if entrada=='Anotar ingrediente':
        ingrediente=input()
        listadecompras.append(ingrediente)

    elif entrada=='Ingrediente Urgente!':
        ingrediente=input()
        listadecompras.insert(0, ingrediente)
    
    elif entrada=='Saci disse que já tem':
        ingrediente=input()
        listadecompras.remove(ingrediente)
    
    elif entrada=='Saci trocou a ordem':
        indice1=int(input())
        indice2=int(input())
        listadecompras[indice1], listadecompras[indice2] = listadecompras[indice2], listadecompras[indice1]
    
    elif entrada=='Organizar a lista':
        ingrediente1=input()
        ingrediente2=input()
        a=listadecompras.index(ingrediente1)
        b=listadecompras.index(ingrediente2)
        listadecompras[a], listadecompras[b] = listadecompras[b], listadecompras[a]

    elif entrada=='Deixar para depois':
        ingrediente=input()
        listadecompras.remove(ingrediente)
        listadecompras.append(ingrediente)

    elif entrada=='Ler a lista para a vovó':
        print(', '.join(listadecompras))

listafinal=', '.join(listadecompras)
print(f'Pronto, vovó! A lista de compras para o bolo de Narizinho está pronta. Podemos ir ao mercado. A lista final é: {listafinal}')
