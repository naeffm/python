import random

jogador = 's'
computador = random.randint(0,10)

while jogador != computador:
    jogador = int(input('Tente adivinha que numero o computador pensou: '))
    print('O computador pensou no {} e você no {}'.format(computador, jogador))


print('Paraboins você pegou ele!')