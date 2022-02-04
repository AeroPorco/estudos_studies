# Execute o terminal para interagir com o script

import math
print('='*30)
print('Olá!')
nome = input('Digite seu nome: ')
print('Prazer em te conhecer, {}!'.format(nome))
print('='*30)
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
m = n1 - n2
d = n1 / n2
di = n1 // n2 
e = n1 ** n2
sa = s - 1
ss = s + 1

print(' ')
print('Os resultados de {} com {} são:'.format(n1, n2))
print('Em soma: {}.'.format(s))
print('Em subtração: {}.'.format(m))
print('Em divisão: {}.'.format(d))
print('Divisão em inteiro: {}.'.format(di))
print('Exponenciação: {}.'.format(e))
print('O número antecessor ao da soma: {}.'.format(sa))
print('O número sucessor ao da soma: {}.'.format(ss))
print(' ')

n3 = 'y'
while type(n3) != int:
    try:
        n3 = int(input('Me diga mais um número: '))
        it_is = True
    except ValueError:
        it_is = False
        print('Isso não é um número.')

a = n3 - 1
sb = n3 + 1
m = n3 * 1000
cm = n3 * 10000
p = n3 * 3281
mi = n3 / 1,609
j = n3 * 1094
f = ( n3 * 9/5 ) + 32
k = n3 + 273,15
r = math.sqrt(n3)

print('Antecessor do número: {}.'.format(a))
print('Sucessor do número: {}.'.format(sb))
print('Raíz quadrada: {}.'.format(r))
print('Em distâncias, {}km fica: '.format(n3))
print('{} metros.'.format(m))
print('{} centímetros.'.format(cm))
print('Aproximadamente {} pés.'.format(p))
print('Aproximadamente {} milhas.'.format(mi))
print('Aproximadamente {} jardas.'.format(j))
print(' ')
print('Se {} fosse em temperatura de °C, ficaria: '.format(n3))
print('{}° em escala Fahrenheit.'.format(f))
print('{}° em escala Kelvin.'.format(k))
print(' ')
print('Vou mostrar a tabuada do próximo número que escolher.')
n4 = 'z'
while type(n4) != int:
    try:
        n4 = int(input('Qual o número?: '))
        it_is = True
    except ValueError:
        it_is = False
        print('Isso não é um número.')

print('A tabuada de {} é:'.format(n4))
print('{} x 1 = '.format(n4), n4*1)
print('{} x 2 = '.format(n4), n4*2)
print('{} x 3 = '.format(n4), n4*3)
print('{} x 4 = '.format(n4), n4*5)
print('{} x 5 = '.format(n4), n4*5)
print('{} x 6 = '.format(n4), n4*6)
print('{} x 7 = '.format(n4), n4*7)
print('{} x 8 = '.format(n4), n4*8)
print('{} x 9 = '.format(n4), n4*9)
print('{} x 10 = '.format(n4), n4*10)

print('Ufa. Coisa de louco.'.format(nome))
print(' ')
print('Gostou, {}? Legal, né?'.format(nome))


print('='*30)
qqr = (input('Agora, digita qualquer coisa aí: '))
print(qqr, 'é:')
print('Classe: ', type(qqr))
print('Numérico: ', qqr.isnumeric())
print('Alfabético: ', qqr.isalpha())
print('Alfanumérico: ', qqr.isalnum())
print('Essas são as classes de "{}"'.format(qqr))
print('='*30)