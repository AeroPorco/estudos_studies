# Sendo que cada litro de tinta pinta uma área de 2m^2 de parede, quantos litros vou precisar?
# Execute o script e digite a largura e a altura da parede em m^2.
# O terminal mostrará quantos litros irá precisar para pintar a parede.

l = 'x'
a = 'y'

while type(l) != int:
    try:
        l = int(input('Digite a largura da parede com apenas números: '))
        is_it = True
    except ValueError:
        is_it = False
        print('Isso não é um número.')

while type(a) != int:
    try:
        a = int(input('Agora, a altura da parede somente com números: '))
        is_it = True
    except ValueError:
        is_it = False
        print('Isso não é um número.')
t = l * a
r = t / 2
print('Precisará de {} litros de tinta para pintar uma parede de {} metros quadrados.'.format(r, t))