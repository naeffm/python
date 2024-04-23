def quebra():
    print('-'*25)

def ajuda():
    while True:
        print('\033[0;30;46m-\033[m'*20)
        print('\033[0;30;46mSISTEMA DE AJUDA PYHELP\033[m')
        print('\033[0;30;46m-\033[m'*20)
        print()

        msg = str(input('Função ou biblioteca > ')).lower()

        if msg == 'fim':
            break
        else:
            print('\033[0;30;41m-\033[m'*30)
            print(f'\033[0;30;41mACESSANDO O MANUEL DE {msg}\033[m')
            print('\033[0;30;41m-\033[m'*30)
            help(msg)
        

ajuda()
