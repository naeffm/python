def leiaint(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError,TypeError):
            print('Por favor digite um numero inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('O usuario preferiu nao informar os dados!')
            return 0
        else:
            return inteiro

def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def alo(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc