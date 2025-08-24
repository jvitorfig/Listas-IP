n=int(input())
armas=[]
armas_usadas=[]
solicitacao=''
golpes=0
qtd_armas_usadas=0

for c in range (n): #loop pra receber as armas
    arma=input()
    armas.append(arma)

while solicitacao!='fim': #loop das solicitações de armas
    solicitacao=input()
    if solicitacao in armas and not (solicitacao in armas_usadas):
        armas_usadas.append(solicitacao)
        qtd_armas_usadas+=1
        print(f'{solicitacao} usado(a) com sucesso!')
    elif solicitacao in armas and solicitacao in armas_usadas:
        print(f'{solicitacao} já foi usado(a)!')
        golpes+=1
    elif solicitacao!='fim':
        print(f'{solicitacao} não está disponível!')
        golpes+=1

print(f'Batalha encerrada! Os Vingadores utilizaram {qtd_armas_usadas} arma(s).')

if golpes==0:
    print('''Vitória! Os Vingadores salvaram o UNIVERSO!

Tony Stark:
Salvar o mundo de novo? Vou precisar de um aumento.

Thor:
Espero que tenha cerveja depois disso!

Homem-Aranha:
Posso dizer que ajudei, né? Tipo… oficialmente?
Dá pra postar isso no Insta dos Vingadores?''')

elif golpes==1:
    print('''Os Vingadores sofreram um golpe do Thanos!
Vitória por pouco! Os Vingadores ganharam...

Tony Stark:
Quase que eu fico sem troco para o cafezinho.

Thor:
Esse quase foi o meu momento de “não consegui”. Mas consegui, então vale cerveja!

Peter Quill (Star-Lord):
Cara, quase perdi o ritmo do meu walkman!''')

elif golpes>=2:
    print(f'''Os Vingadores sofreram {golpes} golpes do Thanos!
Derrota... Os Vingadores não conseguiram todas as armas necessárias.

Tony Stark:
Essa não foi das melhores ideias...

Thor:
Culpa do humano. Eu sabia que devíamos ter chamado o Hulk.''')