exp = str(input('Digite sua expressão: '))

    if exp.count('(') == exp.count(')') and exp.index('(') < exp.index(')'):
        print('Expressão válida')
    elif exp.index('(') > exp.index(')'):
        print('Expressão inválida')
    else:
        print('Expressão inválida')