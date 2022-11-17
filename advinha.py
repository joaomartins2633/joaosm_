import random

print('Você tem 3 chances para acertar o número que o computador escolheu!')
print('Vamos lá?')
prim = print('Primeira chance!')
num1 = int(input('Digite o número que você acha que o computador escolheu: '))
x = random.randint(1, 10)

if num1 == x:
    print('Computador também escolheu {}'.format(x))
    print('Você acertou!')
else:
    print('Você errou, tente novamente!')
    seg = print('Segunda chance!')
    num2 = int(input('Digite o número que você acha que o computador escolheu: '))

    if num2 == x:
        print('Computador também escolheu {}'.format(x))
        print('Você acertou!')
    else:
        print('Você errou, tente novamente!')
        ter = print('Terceira chance!')
        num3 = int(input('Digite o número que você acha que o computador escolheu: '))

        if num3 == x:
            print('Computador também escolheu {}'.format(x))
            print('Você acertou!')
        else:
            print('Computador escolheu {}'.format(x))
            print('Você perdeu, sinto muito!')