valordol=int(input(''))
cotdol=float(input(''))
racao=int(input(''))
aluguel=int(input(''))
onibus=int(input(''))

gastos=racao+aluguel+onibus
mesadareal=valordol*cotdol

maiorgasto=racao
if aluguel>maiorgasto:
    maiorgasto=aluguel
if onibus>maiorgasto:
    maiorgasto=onibus

if mesadareal>gastos:
    print('Me chama pra sua casa um dia pra gente comer Pedigree! Com essa grana dá pra alugar uma ManCão!')
elif mesadareal==gastos:
    print('Vai dar pra alugar sua casa, mas sugiro que você vá trabalhar se quiser gastar com outra coisa!')
else:
    print('Eu acho melhor você ir morar comigo no Cin! O RU é só 4 reais e lá no DA tem saco de dormir!')

if maiorgasto==racao:
    print('A inflaCão deu pros cachorros, viu! Sugiro que você vá no Coffee Break dos calouros e leve toda a comida!')
    nomemaiorgasto='Ração'
elif maiorgasto==aluguel:
    print('Não está fácil pra ninguém... Tenta dividir o aluguel com algum estudante aí!')
    nomemaiorgasto='Aluguel'
elif maiorgasto==onibus:
    print('Você consegue voar, por que quer orçamento de ônibus? Vai ser feliz!')
    nomemaiorgasto='Ônibus'

print(f'''MESADA (dólares): {valordol:.2f} dólares
MESADA (reais): {mesadareal:.2f} reais
MAIOR GASTO: {nomemaiorgasto}''')
