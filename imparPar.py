import random

def program():
    try:
        x = random.randint(1, 2)
        option = input('Par ou ímpar? ')

        if option == 'par' or option == 'Par':
            print('Ok, você escolheu par')
            n = int(input('Agora digite um número: '))
            if n % 2 == 0 and x % 2 != 0:
                print('VOCÊ PERDEU')
                print('O computador escolheu o número: {}'.format(x))
            else:
                if n % 2 != 0 and x % 2 == 0:
                    print('VOCÊ PERDEU')
                else:
                    if n % 2 == 0 and x % 2 == 0:
                        print('VOCÊ VENCEU!')
                    else:
                        print('VOCÊ VENCEU!')
        else:
            if option == 'ímpar' or option == 'Ímpar' or option == 'impar' or option == 'Impar':
                print('Ok, você escolheu ímpar')
                n = int(input('Agora digite um número: '))
                if n % 2 == 0 and x % 2 == 0:
                    print('VOCÊ PERDEU')
                else:
                    if n % 2 != 0 and x % 2 != 0:
                        print('VOCÊ PERDEU')
                    else:
                        if n % 2 == 0 and x % 2 != 0:
                            print('VOCÊ VENCEU!')
                        else:
                            print('VOCÊ VENCEU!')
            else:
                print('Entrada inválida!')
    except:
        print('Entrada inválida!')

program()