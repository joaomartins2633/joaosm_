print('PEDRA, PAPEL E TESOURA')
numero = input('Escolha uma opção(pedra, papel ou tesoura): ')
import random

x = random.randint(1, 3)
if x == 1:
    print('Computador escolheu: pedra')
if x == 2:
    print('Computador escolheu: papel')
if x == 3:
    print('Computador escolheu: tesoura')
if numero == 'pedra':
    print('Você escolheu: {}'.format(numero))
if numero == 'papel':
    print('Você escolheu: {}'.format(numero))
if numero == 'tesoura':
    print('Você escolheu: {}'.format(numero))
if x == 1:
    if numero == 'pedra':
        print('EMPATE')
    else:
        if numero == 'papel':
            print('VOCÊ VENCEU!')
        else:
            print('VOCÊ PERDEU')
if x == 2:
    if numero == 'pedra':
        print('VOCÊ PERDEU')
    else:
        if numero == 'papel':
            print('EMPATE')
        else:
            print('VOCÊ VENCEU!')
if x == 3:
    if numero == 'pedra':
        print('VOCÊ VENCEU!')
    else:
        if numero == 'papel':
            print('VOCÊ PERDEU')
        else:
            print('EMPATE')