m = 0
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('DIgite o segundo numero: '))

while m != 5 :

    print("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] novos numeros
[ 5 ] Sair do programa""")

    m = int(input('Digite a opção: '))

    if m == 1:
        print(n1 + n2)

    elif m == 2:
        print(n1 * n2)

    elif m == 3:
         if n1 > n2:
            print('{} é maior'.format(n1))
         else:
            print('{} é maior'.format(n2))
    elif m == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))





print('Que o programa tenha te ajudado!')

