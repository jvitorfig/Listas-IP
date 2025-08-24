dconcha=round((((500-400)**2+(500-100)**2)**(1/2))*2)
dlaguinho=round((((500-300)**2+(1000-100)**2)**(1/2))*2)
dhospital=round((((1000-500)**2+(1000-100)**2)**(1/2))*2)
dginasio=round((((800-500)**2+(0)**2)**(1/2))*2)

tconcha=round(15+(dconcha/120))
tlaguinho=round(15+(dlaguinho/120))
thospital=round(15+(dhospital/120))
tginasio=round(15+(dginasio/120))

lugar=str(input(''))

if lugar=='Concha Acústica da UFPE':
    print(f'Byte visitou {lugar}, caminhou {dconcha} metros e gastou {tconcha} minutos passeando!')
    print('Aqui é muito grande mesmo! Muitos eventos ocorrem por aqui!')

if lugar=='Laguinho da UFPE':
    print(f'Byte visitou {lugar}, caminhou {dlaguinho} metros e gastou {tlaguinho} minutos passeando!')
    print('Nossa, mas esse lago é longe hein?!')
    
if lugar=='Hospital das Clínicas':
    print(f'Byte visitou {lugar}, caminhou {dhospital} metros e gastou {thospital} minutos passeando!')
    print('Um dos hospitais mais importantes do estado também fica na área do Campus da UFPE!')

if lugar=='Ginásio e Pista de Atletismo da UFPE':
    print(f'Byte visitou {lugar}, caminhou {dginasio} metros e gastou {tginasio} minutos passeando!')
    print('Que legal! O Ginásio é bem perto do CIn!')
