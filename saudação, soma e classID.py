nome = input('Digite seu nome: ')
print('Prazer em te conhecer, {}!'.format(nome))
n1 = 'a'
n2 = 'x'
while type(n1) != int:
    try:
        n1 = int(input('Dá um número ae: '))
        it_is =True
    except ValueError:
        it_is = False
        print('Isso não é um número.')
while type(n2) != int:
    try:
        n2 = int(input('Outro número: '))
        it_is =True
    except ValueError:
        it_is = False
        print('Isso não é um número.')

s = n1 + n2
print('A soma de {} com {} resulta em {}, ó grande {}.'.format(n1, n2, s, nome))
qqr = input('Agora, digita qualquer coisa aí: ')
print(qqr, 'é:')
print('classe: ', type(qqr))
print('Numérico: ', qqr.isnumeric())
print('Alfabético: ', qqr.isalpha())
print('Alfanumérico: ', qqr.isalnum())
print('Essas são as classes de "{}"'.format(qqr))