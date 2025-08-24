num1=int(input(''))
num2=int(input(''))
num3=int(input(''))
num4=int(input(''))
num5=int(input(''))

resto=(num1+num2+num3+num4+num5)%5
#Arthur com o resto 0, Bruna com 1, César com 2, Daniel com 3 e Eduarda com 4.
monitor=''
if resto==0:
    monitor='Arthur'
if resto==1:
    monitor='Bruna'
if resto==2:
    monitor='César'
if resto==3:
    monitor='Daniel'
if resto==4:
    monitor='Eduarda'
    
print(f'{monitor} vai ter a honra de passear com Byte hoje!')
