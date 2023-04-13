import random
x = random.randint(1, 2)
option = input('Par ou ímpar? ')

if option == 'par' or option == 'Par':
    print('Ok, você escolheu par')
    n = int(input('Agora digite um número: '))
    if n % 2 == 0 and x % 2 != 0:
        print('VOCÊ PERDEU')
        print('O computador escolheu o número: {}'.format(x))
    if n % 2 != 0 and x % 2 == 0:
        print('VOCÊ PERDEU')
    if n % 2 == 0 and x % 2 == 0:
        print('VOCÊ VENCEU!')
    if n % 2 != 0 and x % 2 != 0:
        print('VOCÊ VENCEU!')
if option == 'ímpar' or option == 'Ímpar' or option == 'impar' or option == 'Impar':
    print('Ok, você escolheu ímpar')
    n = int(input('Agora digite um número: '))
    if n % 2 == 0 and x % 2 == 0:
        print('VOCÊ PERDEU')
    if n % 2 != 0 and x % 2 != 0:
        print('VOCÊ PERDEU')
    if n % 2 == 0 and x % 2 != 0:
        print('VOCÊ VENCEU!')
    if n % 2 != 0 and x % 2 == 0:
        print('VOCÊ VENCEU!')