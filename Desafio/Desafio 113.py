def leiaint(msg):
    
    while True:
    
        try:
            inteiro = int(input(msg))
        except (ValueError,TypeError):
            print('Por favor digite um numero inteiro válido!')
        except KeyboardInterrupt:
            print('O usuario preferiu nao informar os dados!')
        else:
            break
    return inteiro

def leiafloat(msg):
    
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print('Por favor digite um numero REAL válido!')
        except KeyboardInterrupt:
            print('O usuario preferiu nao informar os dados!')
        else:
            break
    return real
    

n = leiaint('Digite um numero INTEIRO: ')
k = leiafloat('Digite um numero REAL: ')

print(f'inteiro: {n} real: {k}')

