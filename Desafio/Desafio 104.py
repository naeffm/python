def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
            break
        else:
            print('ERRO! DIGITA UM NUMERO VALIDO.')

    return valor

n = leiaint('Digite um numero: ')
print(f'{n}')