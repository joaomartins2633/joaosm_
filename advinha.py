import random

print('Você tem 3 chances para acertar o número que o computador escolheu!')
print('Vamos lá?')
prim = print('Primeira chance!')
num1 = int(input('Digite o número que você acha que o computador escolheu: '))
x = random.randint(1, 10)

if num1 == 1 and x == 1 or num1 == 2 and x == 2 or num1 == 3 and x == 3 or num1 == 4 and x == 4 or num1 == 5 and x == 5 or num1 == 6 and x == 6 or num1 == 7 and x == 7 or num1 == 8 and x == 8 or num1 == 9 and x == 9 or num1 == 10 and x == 10:
    print('Computador também escolheu {}'.format(x))
    print('Você acertou!')
else:
    print('Você errou, tente novamente!')
    seg = print('Segunda chance!')
    num2 = int(input('Digite o número que você acha que o computador escolheu: '))

    if num2 == 1 and x == 1 or num2 == 2 and x == 2 or num2 == 3 and x == 3 or num2 == 4 and x == 4 or num2 == 5 and x == 5 or num2 == 6 and x == 6 or num2 == 7 and x == 7 or num2 == 8 and x == 8 or num2 == 9 and x == 9 or num2 == 10 and x == 10:
        print('Computador também escolheu {}'.format(x))
        print('Você acertou!')
    else:
        print('Você errou, tente novamente!')
        ter = print('Terceira chance!')
        num3 = int(input('Digite o número que você acha que o computador escolheu: '))

        if num3 == 1 and x == 1 or num3 == 2 and x == 2 or num3 == 3 and x == 3 or num3 == 4 and x == 4 or num3 == 5 and x == 5 or num3 == 6 and x == 6 or num3 == 7 and x == 7 or num3 == 8 and x == 8 or num3 == 9 and x == 9 or num3 == 10 and x == 10:
            print('Computador também escolheu {}'.format(x))
            print('Você acertou!')
        else:
            print('Computador escolheu {}'.format(x))
            print('Você errou, sinto muito!')