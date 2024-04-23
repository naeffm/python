import random
import time

computador = 0
pontos = 0

jogador = str(input('ESCOLHA [ PAR / IMPAR ] = ')).upper()

while True:
    if jogador == 'par' or jogador == 'PAR':
        jogadorj = int(input('ESCOLHA O SEU NUMERO: '))
        computador = random.randint(1,10)
        soma = jogadorj + computador
        time.sleep(1)
        print('--------------------------------------')
        print(f'COMPUTADOR = {computador}')
        print(f'VOCÊ = {jogadorj}')
        print('--------------------------------------')
        time.sleep(1)
        print(f'{jogadorj} + {computador} = {soma}')
        if soma % 2 == 0:
            print(f'{soma} é par!')
            pontos += 1
            time.sleep(1)
            print('PARABENS VOCÊ FEZ 1 PONTO')
            print('--------------------------------------')
        else:
            print(f'{soma} é impar!')
            break
            time.sleep(1)
    elif jogador == 'impar' or jogador == 'IMPAR':
        jogadorj = int(input('ESCOLHA O SEU NUMERO: '))
        computador = random.randint(1, 10)
        soma = jogadorj + computador
        time.sleep(1)
        print('--------------------------------------')
        print(f'COMPUTADOR = {computador}')
        print(f'VOCÊ = {jogadorj}')
        print('--------------------------------------')
        time.sleep(1)
        print(f'{jogadorj} + {computador} = {soma}')
        print('--------------------------------------')
        if soma % 2 == 0:
            time.sleep(1)
            print(f'{soma} é par!')
            print('--------------------------------------')
            break

        else:
            print(f'{soma} é impar!')
            pontos += 1
            print('PARABENS VOCÊ FEZ 1 PONTO')
            print('--------------------------------------')

print(f'PERDEU DOIDÃO FEZ SÓ {pontos} PONTOS, BOTA OUTRA FICHA')