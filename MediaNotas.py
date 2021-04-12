a = int(input('Primeiro Bimestre: '))
if a > 10:
    
   a = int(input('Você digitou errado. Primeiro bimestre: '))
   
b = int(input('Segundo Bimestre: '))

c = int(input('Terceiro Bimestre: '))

d = int(input('Quarto Bimestre: '))

media = (a + b + c + d) / 4
##if a <= 10 and b <= 10 and c <= 10 and d <= 10:
##   print('media: {}'.format(media))
##else:
##    print('Foi informado alguma nota errada ')

print('media: {} '.format(media))
