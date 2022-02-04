# Execute o script e faça o reajuste salarial em porcentagem.
# Quando exigido, digite apenas números.

a = 'x'
b = 'y'
c = 'w'
d = 'z'

print('O reajuste é para aumentar ou reduzir o salário?: ')
opcao = int(input('1- Aumentar em porcentagem \n2- Reduzir em porcentagem\n>> '))
if opcao == 1:
    while type(a) != int:
        try:
            a = int(input('Digite o salário atual: '))
            is_it = True
        except ValueError:
            is_it = False
            print('Isso não é um número.')
    while type(b) != int:
        try:
            b = int(input('Agora, digite a porcentagem que quer aumentar: '))
            is_it = True
        except ValueError:
            is_it = False
            print('Isso não é um número.')
    r = a + ( a * b / 100 )
    print('O salário de R${} aumentado em {} % é de R${}.'.format(a, b, r))

elif opcao == 2:
    while type(c) != int:
        try:
            c = int(input('Digite o salário atual: '))
            is_it = True
        except ValueError:
            is_it = False
            print('Isso não é um número.')
    while type(d) != int:
        try:
            d = int(input('Agora, digite a porcentaquem que quer reduzir: '))
            is_it = True
        except ValueError:
            is_it = False
            print('Isso não é um número.')
    rr = c - ( c * d / 100 )
    print('O salário de R${} reduzido em {} % é de R${}.'.format(c, d, rr))
elif opcao != 1 or 2:
    print('Não é nenhuma das opções. Execute o script novamente.')