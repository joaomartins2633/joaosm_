import random

def program():
    try:
        print('Você tem 3 chances para acertar o número que o computador escolheu!\nVamos lá?\n\n1° chance:')
        num = int(input('Digite seu número: '))
        x = random.randint(1, 10)

        for i in range(2):
            if num == x:
                print('Você acertou!')
                print('Computador também escolheu {}'.format(x))
                exit()
            else:
                print("Você errou!\n{}° chance:".format(i + 2))
                num = int(input("Digite seu número: "))
    except:
        print('Entrada inválida!')

program()