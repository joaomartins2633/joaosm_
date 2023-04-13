import random

def program():
    try:
        print('PEDRA, PAPEL E TESOURA')
        n = input('Escolha uma opção(pedra, papel ou tesoura): ')

        x = random.randint(1, 3)

        if n == 'pedra':
            print('Você escolheu: {}\n'.format(n))
            format = 1
        else:
            if n == 'papel':
                print('Você escolheu: {}\n'.format(n))
                format = 2
            else:
                if n == 'tesoura':
                    print('Você escolheu: {}\n'.format(n))
                    format = 3

        if x == 1:
            if format == 1:
                print('EMPATE')
                print('Computador também escolheu pedra')
            else:
                if format == 2:
                    print('VOCÊ VENCEU')
                    print('Computador escolheu pedra')
                else:
                    print('VOCÊ PERDEU')
                    print('Computador escolheu pedra')
        if x == 2:
            if format == 1:
                print('VOCÊ PERDEU')
                print('Computador escolheu papel')
            else:
                if format == 2:
                    print('EMPATE')
                    print('Computador também escolheu papel')
                else:
                    print('VOCÊ VENCEU')
                    print('Computador escolheu papel')
        if x == 3:
            if format == 1:
                print('VOCÊ VENCEU')
                print('Computador escolheu tesoura')
            else:
                if format == 2:
                    print('VOCÊ PERDEU')
                    print('Computador escolheu tesoura')
                else:
                    print('EMPATE')
                    print('Computador também escolheu tesoura')
    except:
        print('Entrada inválida!')

program()