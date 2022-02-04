# Execute o script e dê o valor do produto e a porcentagem do desconto.
# O script vai aplicar o desconto e mostrar o resultado no terminal.
# Digite APENAS NÚMEROS para que o script entenda.
from distutils.log import error
from unittest.mock import seal


p = 'x'
d = 'y'
while type(p) != int:
    try:
        p = int(input('Diga o preço atual do produto: '))
        is_it = True
    except ValueError:
        is_it = False
        print('Isso não é um número.')

while type(d) != int:
    try:
        d = int(input('Agora, a porcentagem de desconto que quer colocar no produto: '))
        is_it = True
    except ValueError:
        is_it = False
        print('Isso não é um número.')

t = p - ( p * d / 100 )
print(' ')
print('O valor de R${} com  {}'.format(p, d), '% de desconto fica R${}.'.format(t))