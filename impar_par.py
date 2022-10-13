import random
x = random.randint(1, 2)
opção = input('Par ou ímpar? ')

if opção == 'par' or opção == 'Par':
    print('Ok, você escolheu par')
else:
    print('Ok, você escolheu ímpar')

numero = int(input('Agora digite um número: '))
print('O computador escolheu o número: {}'.format(x))

if opção == 'par' or opção == 'Par':
    if numero % 2 == 0 and x == 1:
        print('VOCÊ PERDEU')
else:
    if numero % 2 == 0 and x == 1:
        print('VOCÊ VENCEU!')
if opção == 'par' or opção == 'Par':
    if numero % 2 != 0 and x == 2:
        print('VOCÊ PERDEU')
else:
    if numero % 2 != 0 and x == 1:
        print('VOCÊ PERDEU')
if opção == 'par' or opção == 'Par':
    if numero % 2 == 0 and x == 2:
        print('VOCÊ VENCEU!')
else:
    if numero % 2 != 0 and x == 2:
        print('VOCÊ VENCEU!')
if opção == 'par' or opção == 'Par':
    if numero % 2 != 0 and x == 1:
        print('VOCÊ VENCEU!')
else:
    if numero % 2 == 0 and x == 2:
        print('VOCÊ PERDEU')